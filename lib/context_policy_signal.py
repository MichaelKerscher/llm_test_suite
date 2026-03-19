# lib/context_policy_signal.py
# Context Selection Policy for Signal (traffic light) domain
# Parallel to context_policy_s2.py (LAMP domain)
# selector_version: signal-s2-v1
# guardrails_version: signal-guard-v1

from __future__ import annotations
import json
from dataclasses import dataclass, field


# ---------------------------------------------------------------------------
# Budget Policy
# ---------------------------------------------------------------------------
@dataclass
class BudgetPolicy:
    max_chars: int = 3500

    def fits(self, used: int) -> bool:
        return used <= self.max_chars


# ---------------------------------------------------------------------------
# Trigger extraction
# ---------------------------------------------------------------------------
def extract_triggers(ctx: dict) -> dict:
    inc = ctx.get("incident") or {}
    dev = ctx.get("device") or {}
    env = ctx.get("environment") or {}
    asset = ctx.get("asset") or {}

    fault = inc.get("fault_type", "")
    severity = inc.get("severity", "")
    connectivity = dev.get("connectivity", "")
    device_state = dev.get("device_state", "")
    visibility = env.get("visibility", "")
    time_of_day = env.get("time_of_day", "")
    weather = env.get("weather", "")
    traffic = env.get("traffic_exposure", "")

    return {
        # Incident triggers
        "safety_critical": fault in ("signal_dark", "physical_damage") or severity == "high",
        "timing_issue":    fault == "timing_issue",
        "button_failure":  fault == "button_failure",
        "signal_stuck":    fault == "signal_stuck",
        "intermittent":    fault == "intermittent",
        "high_severity":   severity == "high",
        "photo_description": bool(inc.get("photo_description")),

        # Device triggers
        "offline":         connectivity == "offline",
        "spotty":          connectivity == "spotty",
        "low_battery":     device_state in ("low_battery", "low_power_mode"),

        # Environment triggers
        "poor_visibility": visibility == "poor_visibility",
        "rush_hour":       time_of_day == "rush_hour",
        "night":           time_of_day == "night",
        "bad_weather":     weather in ("rain", "snow", "storm", "fog"),
        "high_traffic":    traffic == "high",
    }


# ---------------------------------------------------------------------------
# Priority field definitions
# ---------------------------------------------------------------------------
P1_FIELDS = []   # filled by deterministic_selection_plan
P2_FIELDS = []
P3_FIELDS = []


def deterministic_selection_plan(ctx: dict, triggers: dict) -> dict:
    """
    Returns a plan dict with p1/p2/p3 field lists and guardrail_notes.
    Priority logic for Signal domain:
      P1 – must-have for this fault/context
      P2 – highly useful
      P3 – nice-to-have / compressible
    """
    p1, p2, p3 = [], [], []
    guardrail_notes = []

    inc  = ctx.get("incident") or {}
    dev  = ctx.get("device") or {}
    env  = ctx.get("environment") or {}
    asset = ctx.get("asset") or {}

    # --- ASSET ---
    # GPS always P2 for signal (location needed for dispatch/escalation)
    p2.append({"field": "asset.asset_osm",   "reason": "asset-id"})
    p2.append({"field": "asset.longitude",   "reason": "gps"})
    p2.append({"field": "asset.latitude",    "reason": "gps"})

    # --- INCIDENT (P1 core) ---
    p1.append({"field": "incident.fault_type",  "reason": "fault-classification"})
    p1.append({"field": "incident.severity",    "reason": "severity-routing"})
    p1.append({"field": "incident.reported_at", "reason": "timestamp"})
    p1.append({"field": "incident.reporter",    "reason": "source-context"})

    if triggers["photo_description"]:
        p1.append({"field": "incident.photo_description", "reason": "photo-evidence"})
    else:
        p2.append({"field": "incident.photo_available", "reason": "photo-flag"})

    # --- ENVIRONMENT ---
    # Visibility and time_of_day are critical for signal faults
    p1.append({"field": "environment.visibility",       "reason": "safety-visibility"})
    p1.append({"field": "environment.time_of_day",      "reason": "operational-context"})
    p1.append({"field": "environment.traffic_exposure", "reason": "safety-traffic"})

    if triggers["bad_weather"]:
        p1.append({"field": "environment.weather", "reason": "weather-safety"})
    else:
        p3.append({"field": "environment.weather", "reason": "context-weather"})

    if triggers["high_traffic"] or triggers["rush_hour"]:
        p1.append({"field": "environment.noise_level", "reason": "high-traffic-env"})
    else:
        p3.append({"field": "environment.noise_level", "reason": "env-context"})

    # --- DEVICE ---
    if triggers["offline"] or triggers["spotty"] or triggers["low_battery"]:
        p1.append({"field": "device.connectivity",  "reason": "offline-workflow"})
        p1.append({"field": "device.device_state",  "reason": "device-constraint"})
        guardrail_notes.append(
            "HINWEIS: device.connectivity="
            + str(dev.get("connectivity", ""))
            + " und device.device_state="
            + str(dev.get("device_state", ""))
            + " beziehen sich auf das Technikgerät (Smartphone/Tablet), "
            "NICHT auf die Ampelanlage selbst. "
            "Offline-Workflow anpassen: Dokumentation lokal, spätere Synchronisation."
        )
    else:
        p2.append({"field": "device.connectivity", "reason": "device-status"})
        p2.append({"field": "device.device_state", "reason": "device-status"})

    # --- SAFETY-CRITICAL escalation hint ---
    if triggers["safety_critical"]:
        guardrail_notes.append(
            "SICHERHEITSHINWEIS: fault_type="
            + str(inc.get("fault_type", ""))
            + " / severity="
            + str(inc.get("severity", ""))
            + " → Sofortige Absicherung der Kreuzung erforderlich. "
            "Bei signal_dark: Kreuzung wie unbeschrankt behandeln. "
            "Eskalation an Leitstelle priorisieren."
        )

    return {
        "p1": p1,
        "p2": p2,
        "p3": p3,
        "guardrail_notes": guardrail_notes,
    }


# ---------------------------------------------------------------------------
# Field extractor (nested dot-notation)
# ---------------------------------------------------------------------------
def _get_nested(ctx: dict, field_path: str):
    parts = field_path.split(".")
    val = ctx
    for p in parts:
        if not isinstance(val, dict):
            return None
        val = val.get(p)
    return val


def _set_nested(target: dict, field_path: str, value):
    parts = field_path.split(".")
    d = target
    for p in parts[:-1]:
        d = d.setdefault(p, {})
    d[parts[-1]] = value


# ---------------------------------------------------------------------------
# Build L2B
# ---------------------------------------------------------------------------
def build_l2b(ctx: dict, budget: BudgetPolicy | None = None) -> dict:
    if budget is None:
        budget = BudgetPolicy()

    triggers = extract_triggers(ctx)
    plan = deterministic_selection_plan(ctx, triggers)

    selected_ctx: dict = {}
    selected_fields = []
    dropped_fields = []
    compressed_fields = []

    def _try_add(field_entry: dict, priority: str) -> bool:
        fp = field_entry["field"]
        val = _get_nested(ctx, fp)
        if val is None:
            return False
        candidate = dict(selected_ctx)
        _set_nested(candidate, fp, val)
        used = len(json.dumps(candidate, ensure_ascii=False))
        if budget.fits(used):
            _set_nested(selected_ctx, fp, val)
            selected_fields.append({"field": fp, "priority": priority,
                                     "reason": field_entry.get("reason", "")})
            return True
        return False

    # P1 always included
    for fe in plan["p1"]:
        if not _try_add(fe, "P1"):
            dropped_fields.append(fe["field"])

    # P2 if budget allows
    for fe in plan["p2"]:
        if not _try_add(fe, "P2"):
            dropped_fields.append(fe["field"])

    # P3 if budget allows
    for fe in plan["p3"]:
        if not _try_add(fe, "P3"):
            dropped_fields.append(fe["field"])

    # Guardrail notes as top-level key
    if plan["guardrail_notes"]:
        selected_ctx["_guardrail_notes"] = plan["guardrail_notes"]

    used_chars = len(json.dumps(selected_ctx, ensure_ascii=False))

    selection_meta = {
        "selector_version": "signal-s2-v1",
        "guardrails_version": "signal-guard-v1",
        "triggers": triggers,
        "budget_policy": {"max": budget.max_chars, "used": used_chars},
        "selected_fields": selected_fields,
        "dropped_fields": dropped_fields,
        "compressed_fields": compressed_fields,
    }

    return {"context": selected_ctx, "selection_meta": selection_meta}
