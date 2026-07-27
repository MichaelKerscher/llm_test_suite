# lib/context_policy_signal.py
# Context Selection Policy for the SIGNAL (traffic light) domain.
#
# Parallel to context_policy_s2.py (LAMP domain): the two modules share the
# same five-stage pipeline and the same selection-metadata contract, and
# differ only in what is domain-specific -- trigger conditions, tier
# assignments, and guardrail texts.
#
#   selector_version:   signal-s2-v2
#   guardrails_version: signal-guard-v1
#
# Changes over signal-s2-v1:
#   * selection metadata uses the same key names as the LAMP policy
#     (trigger_signals, path, prio), so that the logger and the aggregation
#     scripts read both domains through one code path
#   * fields absent from the input are no longer reported as dropped;
#     dropped_fields now contains budget exclusions only
#   * an explicit dimension ordering stage was added, mirroring
#     stable_serialize_context() in the LAMP policy

from __future__ import annotations

import json
from dataclasses import dataclass


# ---------------------------------------------------------------------------
# Budget Policy
# ---------------------------------------------------------------------------
@dataclass
class BudgetPolicy:
    max_chars: int = 3500

    def fits(self, used: int) -> bool:
        return used <= self.max_chars


# ---------------------------------------------------------------------------
# Stage 2 -- Trigger extraction
# ---------------------------------------------------------------------------
def extract_triggers(ctx: dict) -> dict:
    inc = ctx.get("incident") or {}
    dev = ctx.get("device") or {}
    env = ctx.get("environment") or {}

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
# Stages 3 and 4 -- Guardrail injection and deterministic selection plan
# ---------------------------------------------------------------------------
def deterministic_selection_plan(ctx: dict, triggers: dict) -> dict:
    """
    Returns a plan with p1/p2/p3 field lists and the guardrail notes.

    Priority logic for the SIGNAL domain:
      P1 -- must-have for this fault and situation
      P2 -- highly useful
      P3 -- nice-to-have, first to be dropped under budget pressure
    """
    p1, p2, p3 = [], [], []
    guardrail_notes = []

    inc = ctx.get("incident") or {}
    dev = ctx.get("device") or {}

    # --- ASSET ---
    # Location is P2 for signals: dispatch and escalation need it, but the
    # operational context of the fault determines urgency more than identity.
    p2.append({"field": "asset.asset_osm", "reason": "asset-id"})
    p2.append({"field": "asset.longitude", "reason": "gps"})
    p2.append({"field": "asset.latitude",  "reason": "gps"})

    # --- INCIDENT ---
    p1.append({"field": "incident.fault_type",  "reason": "fault-classification"})
    p1.append({"field": "incident.severity",    "reason": "severity-routing"})
    p1.append({"field": "incident.reported_at", "reason": "timestamp"})
    p1.append({"field": "incident.reporter",    "reason": "source-context"})

    if triggers["photo_description"]:
        p1.append({"field": "incident.photo_description", "reason": "photo-evidence"})
    else:
        p2.append({"field": "incident.photo_available", "reason": "photo-flag"})

    # --- ENVIRONMENT ---
    # Visibility and time of day are decisive for signal faults.
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
        p1.append({"field": "device.connectivity", "reason": "offline-workflow"})
        p1.append({"field": "device.device_state", "reason": "device-constraint"})
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

    # --- SAFETY-CRITICAL escalation ---
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
# Field access helpers (dotted paths)
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
# Stage 5b -- Stable dimension ordering
# ---------------------------------------------------------------------------
def stable_serialize_context(context_partial: dict) -> dict:
    """
    Emits the dimensions in a fixed order, mirroring the corresponding stage
    of the LAMP policy. Without this the ordering would depend on the order
    in which fields happen to be added, which is an implementation detail
    rather than a design decision.
    """
    ordered: dict = {}
    for k in ("incident", "asset", "device", "environment", "_guardrail_notes"):
        if k in context_partial:
            ordered[k] = context_partial[k]
    for k in sorted(set(context_partial.keys()) - set(ordered.keys())):
        ordered[k] = context_partial[k]
    return ordered


# ---------------------------------------------------------------------------
# Public: Build L2B
# ---------------------------------------------------------------------------
SELECTOR_VERSION = "signal-s2-v2"
GUARDRAILS_VERSION = "signal-guard-v1"


def build_l2b(ctx: dict, budget: BudgetPolicy | None = None) -> dict:
    if budget is None:
        budget = BudgetPolicy()

    triggers = extract_triggers(ctx)
    plan = deterministic_selection_plan(ctx, triggers)

    selected_ctx: dict = {}
    selected_fields: list[dict] = []
    dropped_fields: list[dict] = []
    compressed_fields: list[dict] = []

    def _try_add(field_entry: dict, prio: str) -> str:
        """
        Returns 'added', 'absent', or 'budget_exceeded'. The distinction
        matters: a field that is not present in the input was never a
        candidate, whereas a field excluded by the budget was.
        """
        fp = field_entry["field"]
        val = _get_nested(ctx, fp)
        if val is None:
            return "absent"

        candidate = dict(selected_ctx)
        _set_nested(candidate, fp, val)
        if not budget.fits(len(json.dumps(candidate, ensure_ascii=False))):
            return "budget_exceeded"

        _set_nested(selected_ctx, fp, val)
        selected_fields.append({
            "path": fp,
            "prio": prio,
            "reason": field_entry.get("reason", ""),
        })
        return "added"

    for prio_key, prio in (("p1", "P1"), ("p2", "P2"), ("p3", "P3")):
        for fe in plan[prio_key]:
            if _try_add(fe, prio) == "budget_exceeded":
                dropped_fields.append({
                    "path": fe["field"],
                    "reason": "budget_exceeded",
                    "prio": prio,
                })

    # Guardrails are emitted as a top-level key rather than under extras,
    # reflecting that they carry escalation guidance rather than annotation.
    if plan["guardrail_notes"]:
        selected_ctx["_guardrail_notes"] = plan["guardrail_notes"]

    selected_ctx = stable_serialize_context(selected_ctx)
    used_chars = len(json.dumps(selected_ctx, ensure_ascii=False))

    selection_meta = {
        "selector_version": SELECTOR_VERSION,
        "guardrails_version": GUARDRAILS_VERSION,
        "trigger_signals": triggers,
        "budget_policy": {"metric": "chars", "max": budget.max_chars, "used": used_chars},
        "selected_fields": selected_fields,
        "dropped_fields": dropped_fields,
        "compressed_fields": compressed_fields,
    }

    return {"context": selected_ctx, "selection_meta": selection_meta}