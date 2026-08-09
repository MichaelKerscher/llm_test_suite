"""
scripts/verify_offline_flag.py

Checks the judge's offline_workflow_mentioned flag against the response
texts themselves.

Why
---
The flag carries a substantial part of the evaluation's argument, and it
is set by the judge rather than counted from the text. Re-judging the
ablation responses against the full context moved the flag from 0.000 to
0.400 on identical response texts, which shows the flag responds to the
judge's expectation as well as to the response. A lexical count is not a
better measure of the construct, but it is independent of the judge, and
where the two agree the finding no longer rests on the judge alone.

Two tiers are counted separately, because they are not the same claim:

  MENTION   the response refers to connectivity or device state at all
            ("Ihr Gerät ist offline", "keine Verbindung")

  WORKFLOW  the response prescribes an offline-capable procedure:
            storing locally and synchronising later

The distinction matters. A response that merely notes the device is
offline has acknowledged the state; it has not adapted the workflow.

Usage
-----
    python scripts/verify_offline_flag.py \
        --results-dir results_single/506 \
        --client gemini-2.5-flash \
        --testfile tests/lamp_testcases_v05.csv \
        --domain lamp --incident-filter regular

    # inspect the cases where judge and text disagree
    python scripts/verify_offline_flag.py ... --show-disagreements 10
"""

import argparse
import csv
import json
import re
import sys
from collections import defaultdict
from pathlib import Path

# --------------------------------------------------------------------------
# Lexical patterns
# --------------------------------------------------------------------------

# Tier 1: any reference to connectivity or device state.
MENTION_PATTERNS = [
    r"\boffline\b",
    r"\bkeine?\s+(?:Netz|Verbindung|Konnektivit(?:ä|ae)t|Internetverbindung)",
    r"\bohne\s+(?:Netz|Verbindung|Internet)",
    r"\bKonnektivit(?:ä|ae)t\b",
    r"\bspotty\b",
    r"\binstabile[rn]?\s+Verbindung",
    r"\blow[_\s]?battery\b",
    r"\bschwache[rn]?\s+(?:Akku|Batterie)",
]

# Tier 2: a prescribed offline-capable procedure. Requires a storage verb
# and a later-transfer verb, or an explicit offline-workflow phrase.
LOCAL_STORE_PATTERNS = [
    r"\blokal\w*\s+(?:speicher|dokumentier|erfass|ablegen|sicher|notier)",
    r"\b(?:speicher|dokumentier|erfass|notier)\w*\s+(?:\w+\s+){0,3}lokal",
    r"\boffline[-\s]?(?:f(?:ä|ae)hig|Modus|Workflow|Dokumentation|Erfassung)",
    r"\bauf\s+dem\s+Ger(?:ä|ae)t\s+(?:speicher|sicher|ablegen)",
    r"\b(?:handschriftlich|auf\s+Papier)\s+(?:notier|dokumentier|festhalten)",
]

LATER_SYNC_PATTERNS = [
    r"\bsynchronisier",
    r"\bsp(?:ä|ae)ter\s+(?:(?:\w+\s+){0,3})?(?:(?:ü|ue)bertrag|hochlad|(?:ü|ue)bermittel|einpfleg|nachtrag)",
    r"\bnachtr(?:ä|ae)glich\s+(?:(?:ü|ue)bertrag|hochlad|(?:ü|ue)bermittel|einpfleg)",
    r"\bsobald\s+(?:wieder\s+)?(?:eine\s+)?(?:Verbindung|Netz|Konnektivit(?:ä|ae)t|online)",
    r"\bbei\s+(?:wieder\s+)?(?:hergestellter|verf(?:ü|ue)gbarer)\s+Verbindung",
]

EXPLICIT_WORKFLOW_PATTERNS = [
    r"\boffline[-\s]?Workflow",
    r"\boffline[-\s]?f(?:ä|ae)hige[rn]?\s+(?:Dokumentation|Workflow|Erfassung)",
]

_MENTION = [re.compile(p, re.IGNORECASE) for p in MENTION_PATTERNS]
_STORE = [re.compile(p, re.IGNORECASE) for p in LOCAL_STORE_PATTERNS]
_SYNC = [re.compile(p, re.IGNORECASE) for p in LATER_SYNC_PATTERNS]
_EXPLICIT = [re.compile(p, re.IGNORECASE) for p in EXPLICIT_WORKFLOW_PATTERNS]


def has_any(text: str, patterns) -> bool:
    return any(p.search(text) for p in patterns)


def classify(text: str) -> tuple[bool, bool]:
    """Returns (mention, workflow)."""
    if not isinstance(text, str) or not text:
        return False, False
    mention = has_any(text, _MENTION)
    workflow = has_any(text, _EXPLICIT) or (
        has_any(text, _STORE) and has_any(text, _SYNC)
    )
    return mention, workflow


# --------------------------------------------------------------------------
# Corpus: which incidents actually carry degraded connectivity
# --------------------------------------------------------------------------

def load_connectivity(testfile: str) -> dict[str, str]:
    """incident_id -> device.connectivity, read from the S1 rows."""
    out: dict[str, str] = {}
    with open(testfile, "r", encoding="utf-8-sig", newline="") as f:
        for row in csv.DictReader(f):
            if (row.get("strategy") or "").strip().upper() != "S1":
                continue
            inc = (row.get("incident_id") or "").strip()
            try:
                ctx = json.loads(row.get("context_json") or "{}")
            except json.JSONDecodeError:
                continue
            conn = ((ctx.get("device") or {}).get("connectivity") or "").strip().lower()
            if inc:
                out[inc] = conn
    return out


def base_incident(test_id: str, incident_id: str | None) -> str:
    if incident_id:
        return incident_id.split("-ABL")[0]
    return test_id.split("-ABL")[0].split("-TC")[0]


# --------------------------------------------------------------------------

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--results-dir", required=True)
    ap.add_argument("--client", required=True)
    ap.add_argument("--testfile", required=True)
    ap.add_argument("--domain", choices=["lamp", "signal"], default=None)
    ap.add_argument("--incident-filter", choices=["regular", "ablation"], default=None)
    ap.add_argument("--show-disagreements", type=int, default=0,
                    help="print up to N cases where judge and text disagree")
    args = ap.parse_args()

    base = Path(args.results_dir) / args.client
    if not base.exists():
        raise SystemExit(f"[ERROR] Not found: {base}")

    connectivity = load_connectivity(args.testfile)
    degraded = {"offline", "spotty", "poor", "unstable"}

    prefix = {"lamp": "INC-LAMP-", "signal": "INC-SIGNAL-"}.get(args.domain)

    def passes_filter(name: str) -> bool:
        if prefix and not name.startswith(prefix):
            return False
        if args.incident_filter is None:
            return True
        is_abl = "-ABL" in name
        return is_abl if args.incident_filter == "ablation" else not is_abl

    stats = defaultdict(lambda: {
        "n": 0, "n_expected": 0,
        "judge": 0, "mention": 0, "workflow": 0,
        "judge_expected": 0, "mention_expected": 0, "workflow_expected": 0,
        "judge_yes_wf_no": 0, "judge_no_wf_yes": 0,
    })
    disagreements = []

    for td in sorted(p for p in base.iterdir() if p.is_dir() and not p.name.startswith("_agg")):
        if not passes_filter(td.name):
            continue
        for rf in sorted(td.glob("run_*.json")):
            try:
                obj = json.loads(rf.read_text(encoding="utf-8"))
            except Exception:
                continue
            if (obj.get("meta") or {}).get("status") != "success":
                continue

            rp = obj.get("request_params") or {}
            strategy = (rp.get("context_strategy") or "UNKNOWN").upper()
            text = ((obj.get("response") or {}).get("text") or "")
            judge = obj.get("judge")
            if not isinstance(judge, dict):
                continue
            flag = bool((judge.get("flags") or {}).get("offline_workflow_mentioned"))

            inc = base_incident(obj.get("test_id", td.name), rp.get("incident_id"))
            expected = connectivity.get(inc, "") in degraded

            mention, workflow = classify(text)

            s = stats[strategy]
            s["n"] += 1
            s["judge"] += int(flag)
            s["mention"] += int(mention)
            s["workflow"] += int(workflow)
            if expected:
                s["n_expected"] += 1
                s["judge_expected"] += int(flag)
                s["mention_expected"] += int(mention)
                s["workflow_expected"] += int(workflow)
            if flag and not workflow:
                s["judge_yes_wf_no"] += 1
                disagreements.append((strategy, "judge=1 text=0", obj.get("test_id"), rf.name, text))
            if workflow and not flag:
                s["judge_no_wf_yes"] += 1
                disagreements.append((strategy, "judge=0 text=1", obj.get("test_id"), rf.name, text))

    def rate(a, b):
        return f"{a / b:.3f}" if b else "  -  "

    print(f"\n{args.client} | domain={args.domain} | filter={args.incident_filter}\n")
    print("All responses")
    print(f"{'Strategy':<20}{'n':>6}{'judge':>9}{'mention':>9}{'workflow':>10}")
    for strat in sorted(stats):
        s = stats[strat]
        print(f"{strat:<20}{s['n']:>6}{rate(s['judge'], s['n']):>9}"
              f"{rate(s['mention'], s['n']):>9}{rate(s['workflow'], s['n']):>10}")

    print("\nIncidents with degraded connectivity in the corpus")
    print(f"{'Strategy':<20}{'n':>6}{'judge':>9}{'mention':>9}{'workflow':>10}")
    for strat in sorted(stats):
        s = stats[strat]
        print(f"{strat:<20}{s['n_expected']:>6}{rate(s['judge_expected'], s['n_expected']):>9}"
              f"{rate(s['mention_expected'], s['n_expected']):>9}"
              f"{rate(s['workflow_expected'], s['n_expected']):>10}")

    print("\nDisagreement between judge flag and text")
    print(f"{'Strategy':<20}{'judge=1 text=0':>16}{'judge=0 text=1':>16}")
    for strat in sorted(stats):
        s = stats[strat]
        print(f"{strat:<20}{s['judge_yes_wf_no']:>16}{s['judge_no_wf_yes']:>16}")

    if args.show_disagreements:
        print("\n" + "=" * 70)
        for strat, kind, tid, run, text in disagreements[:args.show_disagreements]:
            print(f"\n--- {strat} | {kind} | {tid} | {run} ---")
            print(text[:1200].strip())
            print("...")


if __name__ == "__main__":
    main()