"""
context_formatters.py
Transforms a structured L2_full context dict into two unstructured formats:
  - format_raw(ctx, domain):          readable German prose
  - format_unstructured(ctx, domain): shuffled value dump, no keys/structure
"""
import json
import random

# ------------------------------------------------------------------
# Value label maps for readable prose
# ------------------------------------------------------------------
FAULT_TYPE_DE = {
    # LAMP
    "intermittent":    "sporadischer Ausfall",
    "open_housing":    "geöffnetes Gehäuse",
    "cable_damage":    "Kabelschaden",
    "bulb_failure":    "Leuchtmittelausfall",
    "controller_fault":"Steuerungsdefekt",
    "vandalism":       "Vandalismus",
    # SIGNAL
    "signal_dark":     "Signalausfall (dunkel)",
    "signal_stuck":    "feststehendes Signal",
    "button_failure":  "Tasterausfall",
    "timing_issue":    "Schaltzeitproblem",
    "physical_damage": "physischer Schaden",
}

SEVERITY_DE = {"low": "niedrig", "medium": "mittel", "high": "hoch"}
CONNECTIVITY_DE = {"offline": "offline", "online": "online", "spotty": "instabil"}
DEVICE_STATE_DE = {
    "ok": "in Ordnung",
    "low_battery": "schwache Batterie",
    "low_power_mode": "Stromsparmodus",
}
WEATHER_DE = {
    "clear": "klar", "rain": "Regen", "snow": "Schnee",
    "storm": "Sturm", "fog": "Nebel",
}
TIME_DE = {
    "day": "tagsüber", "night": "nachts",
    "rush_hour": "Stoßzeit", "evening": "abends",
}
TRAFFIC_DE = {"low": "gering", "medium": "mittel", "high": "hoch"}
REPORTER_DE = {
    "citizen": "Bürger", "dispatch": "Leitstelle",
    "patrol": "Streife", "internal": "intern",
}


def _v(mapping, key, fallback=None):
    return mapping.get(str(key) if key else "", fallback or str(key or ""))


def format_raw(ctx: dict, domain: str = "lamp") -> str:
    """
    Converts L2_full context dict to readable German prose.
    Domain: 'lamp' or 'signal'
    """
    parts = []
    asset = ctx.get("asset") or {}
    inc = ctx.get("incident") or {}
    env = ctx.get("environment") or {}
    dev = ctx.get("device") or {}

    # Asset
    if domain == "lamp":
        name = asset.get("name", "")
        osm = asset.get("asset_osm", "")
        lat = asset.get("latitude", "")
        lon = asset.get("longitude", "")
        parts.append(
            f"Die Straßenlampe befindet sich am Standort {name} "
            f"(OSM-ID: {osm}, Koordinaten: {lat}, {lon})."
        )
    else:  # signal
        osm = asset.get("asset_osm", "")
        lat = asset.get("latitude", "")
        lon = asset.get("longitude", "")
        direction = asset.get("traffic_signals:direction", "")
        btn = asset.get("button_operated")
        btn_str = "mit Anforderungstaster" if btn else "ohne Anforderungstaster"
        parts.append(
            f"Die Lichtsignalanlage (OSM-ID: {osm}, Koordinaten: {lat}, {lon}, "
            f"Richtung: {direction}) ist {btn_str}."
        )

    # Incident
    fault = _v(FAULT_TYPE_DE, inc.get("fault_type"), inc.get("fault_type", ""))
    sev = _v(SEVERITY_DE, inc.get("severity"))
    reported = inc.get("reported_at", "")
    reporter = _v(REPORTER_DE, inc.get("reporter"))
    photo = inc.get("photo_available", False)
    photo_desc = inc.get("photo_description", "")

    parts.append(
        f"Gemeldeter Fehler: {fault}, Schweregrad {sev}. "
        f"Gemeldet am {reported} von {reporter}."
    )
    if photo and photo_desc:
        parts.append(f"Foto vorhanden. Bildbeschreibung: {photo_desc}")
    elif photo:
        parts.append("Foto vorhanden.")
    else:
        parts.append("Kein Foto verfügbar.")

    # Environment
    time_str = _v(TIME_DE, env.get("time_of_day"))
    weather_str = _v(WEATHER_DE, env.get("weather"))
    traffic_str = _v(TRAFFIC_DE, env.get("traffic_exposure"))

    if domain == "lamp":
        lighting = env.get("lighting_condition", "")
        parts.append(
            f"Umgebung: {time_str}, Wetter {weather_str}, "
            f"Lichtverhältnisse {lighting}, Verkehrsaufkommen {traffic_str}."
        )
    else:
        visibility = env.get("visibility", "")
        parts.append(
            f"Umgebung: {time_str}, Wetter {weather_str}, "
            f"Sichtweite {visibility}, Verkehrsaufkommen {traffic_str}."
        )

    # Device
    conn = _v(CONNECTIVITY_DE, dev.get("connectivity"))
    state = _v(DEVICE_STATE_DE, dev.get("device_state"))
    parts.append(
        f"Technikgerät des Außendienstmitarbeiters: Konnektivität {conn}, "
        f"Gerätezustand {state}."
    )

    return " ".join(parts)


def _extract_leaf_values(obj, keys_to_skip=None) -> list:
    """Recursively extract all leaf values from a dict."""
    keys_to_skip = keys_to_skip or []
    values = []
    if isinstance(obj, dict):
        for k, v in obj.items():
            if k in keys_to_skip:
                continue
            if isinstance(v, (dict, list)):
                values.extend(_extract_leaf_values(v, keys_to_skip))
            elif v is not None and str(v).strip():
                values.append(str(v))
    elif isinstance(obj, list):
        for item in obj:
            values.extend(_extract_leaf_values(item, keys_to_skip))
    return values


def format_unstructured(ctx: dict, domain: str = "lamp", seed: int = 42) -> str:
    """
    Dumps all leaf values from L2_full context in shuffled order.
    No keys, no structure, no labels – just a blob of values.
    """
    values = _extract_leaf_values(ctx, keys_to_skip=["crs"])
    rng = random.Random(seed)
    rng.shuffle(values)
    return " | ".join(values)


if __name__ == "__main__":
    # Quick test
    import json
    sample_lamp = {
        "asset": {"asset_osm": "n5718630492", "longitude": 12.119, "latitude": 47.851,
                  "crs": "EPSG:4326", "lit": "yes", "name": "Rosenheim, Bahnhof"},
        "incident": {"fault_type": "intermittent", "severity": "low",
                     "reported_at": "2026-01-21T09:11:43+01:00", "reporter": "citizen",
                     "photo_available": True,
                     "photo_description": "Leuchtmittel optisch intakt, Mastfuß ohne Schäden."},
        "environment": {"time_of_day": "day", "weather": "clear",
                        "lighting_condition": "normal_visibility",
                        "traffic_exposure": "high", "noise_level": "medium"},
        "device": {"device_state": "low_battery", "connectivity": "offline"},
    }
    print("=== S0_raw (LAMP) ===")
    print(format_raw(sample_lamp, "lamp"))
    print()
    print("=== S0_unstructured (LAMP) ===")
    print(format_unstructured(sample_lamp, "lamp"))
