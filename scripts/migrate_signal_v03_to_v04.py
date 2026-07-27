#!/usr/bin/env python3
"""
scripts/migrate_signal_v03_to_v04.py

Regenerates the leading asset sentence of the S0_raw prose form in the SIGNAL
test corpus. Everything else -- including all other strategies and the whole
remainder of each _raw_text -- is copied through unchanged.

Background
----------
The v03 prose form rendered absent OSM attributes as positive assertions:

    ... Richtung: None) ist ohne Anforderungstaster.

`button_operated` is null in all 30 SIGNAL incidents, so every S0_raw prompt
asserted that the signal has no pedestrian button, which the data does not
state. For two incidents (0001, 0008) this also contradicted the user message.
`traffic_signals:direction` is null in nine incidents, rendering as the Python
literal `None` inside German prose.

The corrected form omits what is not known rather than asserting its absence.

Usage
-----
    python scripts/migrate_signal_v03_to_v04.py \
        data/signal_testcases_v03.csv data/signal_testcases_v04.csv
"""

import csv
import json
import re
import sys


# The v03 sentence, captured so that the remainder of the prose can be kept.
_LEAD = re.compile(
    r"^Die Lichtsignalanlage \(OSM-ID: [^)]*\) ist (?:mit|ohne) Anforderungstaster\.\s*"
)


def build_asset_sentence(asset: dict) -> str:
    """
    Renders the asset sentence from what the record actually contains.

    Absent attributes produce no clause: a missing value is not evidence that
    the property is absent.
    """
    osm = asset.get("asset_osm", "")
    lat = asset.get("latitude", "")
    lon = asset.get("longitude", "")
    direction = asset.get("traffic_signals:direction")
    button = asset.get("button_operated")

    head = f"Betroffene Lichtsignalanlage: OSM-ID {osm}, Koordinaten {lat}, {lon}"
    if direction:
        head += f", Richtung {direction}"
    head += "."

    if button is True:
        return head + " Anlage mit Anforderungstaster. "
    if button is False:
        return head + " Anlage ohne Anforderungstaster. "
    # button_operated is null: the OSM record makes no statement, so neither
    # does the prose form.
    return head + " "


def main(src: str, dst: str) -> None:
    with open(src, "r", encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames
        rows = list(reader)

    # Asset objects come from the S1 row of each incident: the full context.
    assets: dict[str, dict] = {}
    for r in rows:
        if (r.get("strategy") or "").strip().upper() == "S1":
            ctx = json.loads(r["context_json"])
            assets[r["incident_id"]] = ctx.get("asset") or {}

    rewritten = 0
    untouched = 0

    for r in rows:
        if (r.get("strategy") or "").strip().upper() != "S0_RAW":
            untouched += 1
            continue

        payload = json.loads(r["context_json"])
        old_text = payload.get("_raw_text", "")

        m = _LEAD.match(old_text)
        if not m:
            raise SystemExit(
                f"[ERROR] {r['testcase_id']}: leading sentence did not match the "
                f"expected v03 pattern. Aborting rather than guessing.\n"
                f"  {old_text[:120]}..."
            )

        tail = old_text[m.end():]
        asset = assets.get(r["incident_id"])
        if asset is None:
            raise SystemExit(f"[ERROR] {r['testcase_id']}: no S1 row for this incident.")

        payload["_raw_text"] = build_asset_sentence(asset) + tail
        r["context_json"] = json.dumps(payload, ensure_ascii=False)
        rewritten += 1

    with open(dst, "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    print(f"[OK] {dst}")
    print(f"     rewritten (S0_raw): {rewritten}")
    print(f"     copied unchanged:   {untouched}")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        raise SystemExit(__doc__)
    main(sys.argv[1], sys.argv[2])
