"""
scripts/rejudge_ablation.py

Re-judges existing ablation responses against the FULL four-dimensional
context of the corresponding incident, rather than against the ablated
context the generator received.

Rationale
---------
In single-testcase mode the judge is supplied with the context the model
was given. For an ablation variant that context is missing one dimension,
and the judge's non-speculation rule forbids it from recording as absent
anything the context does not contain. Removing a dimension therefore
removes the information and the expectation at the same time, and the
measured cost of the removal collapses towards zero.

An ablation asks what the absence of X costs. Answering that requires a
reference frame that contains X. This script supplies one: the generated
responses are left untouched, and only the judging is repeated with the
unablated context of the same incident as reference.

Usage
-----
    python scripts/rejudge_ablation.py \
        --results-dir results_single/506 \
        --client gemini-2.5-flash \
        --testfile tests/lamp_testcases_v05.csv \
        --out-root results_single_ablfull

Writes one run file per source run into
    <out-root>/<client>/<test_id>/run_XX.json
preserving the run index, so that aggregate_results.py can be pointed at
the new tree unchanged.
"""

import argparse
import csv
import json
import os
import sys
import time
from pathlib import Path

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from lib.clients import CLIENTS
from lib.test_runner import (
    _safe_json_dumps,
    _score_block_to_expected_schema,
    _try_parse_judge_object,
    _is_client_error_answer,
)

JUDGE_VERSION = os.getenv("REJUDGE_VERSION", "judge_v1_1_single_fullref")


def load_full_contexts(testfile: str) -> dict[str, dict]:
    """
    incident_id -> full four-dimensional context.

    Taken from the S1 row of each incident, which carries the unmodified
    L2_full context object.
    """
    contexts: dict[str, dict] = {}
    with open(testfile, "r", encoding="utf-8-sig", newline="") as f:
        for row in csv.DictReader(f):
            if (row.get("strategy") or "").strip().upper() != "S1":
                continue
            incident_id = (row.get("incident_id") or "").strip()
            raw = row.get("context_json") or ""
            if not incident_id or not raw.strip():
                continue
            try:
                contexts[incident_id] = json.loads(raw)
            except json.JSONDecodeError:
                print(f"[WARN] {incident_id}: context_json is not valid JSON, skipped.")
    return contexts


def base_incident_of(test_id: str) -> str | None:
    """INC-LAMP-0006-ABL-NODEV -> INC-LAMP-0006"""
    if "-ABL" not in test_id:
        return None
    return test_id.split("-ABL")[0]


def build_judge_prompt(user_message: str, full_context: dict, answer: str) -> str:
    return f"""TESTCASE (User message):
<<<
{user_message}
>>>

CONTEXT (JSON):
<<<
{_safe_json_dumps(full_context)}
>>>

MODEL ANSWER:
<<<
{answer}
>>>

RUBRIC:
• R Relevanz (1-5)
• H Handlungsfähigkeit/Struktur (1-5)
• S Sicherheit/Eskalation (1-5)
• D Dokumentation/Nachvollziehbarkeit (1-5)
• K Kontextnutzung/Robustheit (1-5)

EXPECTED ELEMENTS (Fault-Type: unknown, Domain: lamp):
<<<

>>>

Bitte gib nur JSON im definierten Schema zurück.
WICHTIG: Gib gültiges JSON aus. In String-Feldern (z.B. short_justification) benutze keine doppelten Anführungszeichen ".
Wenn nötig, ersetze sie durch einfache Anführungszeichen ' oder escape als \\\".
"""


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--results-dir", required=True,
                    help="e.g. results_single/506")
    ap.add_argument("--client", required=True,
                    help="model slug directory, e.g. gemini-2.5-flash")
    ap.add_argument("--testfile", required=True,
                    help="corpus CSV holding the full contexts")
    ap.add_argument("--out-root", default="results_single_ablfull")
    ap.add_argument("--dry-run", action="store_true",
                    help="report what would be re-judged, issue no API calls")
    args = ap.parse_args()

    src = Path(args.results_dir) / args.client
    if not src.exists():
        raise SystemExit(f"[ERROR] Source dir not found: {src}")

    full_contexts = load_full_contexts(args.testfile)
    if not full_contexts:
        raise SystemExit("[ERROR] No full contexts loaded from the corpus.")
    print(f"[INFO] Loaded {len(full_contexts)} full contexts.")

    client = CLIENTS["506"]
    judge_model = os.getenv("TESTSUITE_JUDGE_MODEL", "claude-sonnet-4.5")
    judge_temp = float(os.getenv("TESTSUITE_JUDGE_TEMPERATURE", "0.0"))
    judge_mode = os.getenv("TESTSUITE_JUDGE_MODE", "BASIC")

    test_dirs = sorted(
        p for p in src.iterdir()
        if p.is_dir() and not p.name.startswith("_agg") and "-ABL" in p.name
    )
    if not test_dirs:
        raise SystemExit(f"[ERROR] No ablation directories under {src}")

    n_total = n_done = n_skipped = n_failed = 0

    for td in test_dirs:
        incident_id = base_incident_of(td.name)
        full_context = full_contexts.get(incident_id) if incident_id else None
        if full_context is None:
            print(f"[WARN] {td.name}: no full context for '{incident_id}', skipped.")
            continue

        for run_file in sorted(td.glob("run_*.json")):
            n_total += 1

            try:
                run_obj = json.loads(run_file.read_text(encoding="utf-8"))
            except Exception as e:
                print(f"[WARN] {run_file}: unreadable ({e}), skipped.")
                n_skipped += 1
                continue

            if (run_obj.get("meta") or {}).get("status") != "success":
                n_skipped += 1
                continue

            answer = ((run_obj.get("response") or {}).get("text") or "").strip()
            user_message = (run_obj.get("request_params") or {}).get("user_message") or ""
            if not answer or not user_message:
                print(f"[WARN] {run_file}: answer or user message missing, skipped.")
                n_skipped += 1
                continue

            out_dir = Path(args.out_root) / args.client / td.name
            out_path = out_dir / run_file.name
            if out_path.exists():
                n_skipped += 1
                continue

            if args.dry_run:
                n_done += 1
                continue

            prompt = build_judge_prompt(user_message, full_context, answer)
            judge_raw = client.judge(
                prompt=prompt,
                model=judge_model,
                temperature=judge_temp,
                selected_mode=judge_mode,
                internal_system_prompt=False,
            )

            if _is_client_error_answer(judge_raw):
                print(f"[ERROR] {run_file.name} ({td.name}): judge call failed.")
                n_failed += 1
                continue

            parsed = _try_parse_judge_object(judge_raw)
            if parsed is None:
                print(f"[WARN] {run_file.name} ({td.name}): judge output unparseable.")
                block = _score_block_to_expected_schema({
                    "test_id": run_obj.get("test_id"),
                    "missing_elements": ["judge_parse_failed"],
                    "short_justification": "Judge-Ausgabe nicht parsebar; Fallback gesetzt.",
                })
                n_failed += 1
            else:
                parsed.setdefault("test_id", run_obj.get("test_id"))
                block = _score_block_to_expected_schema(parsed)
                n_done += 1

            out_obj = dict(run_obj)
            out_obj["judge"] = block
            rp = dict(out_obj.get("request_params") or {})
            rp["judge_version"] = JUDGE_VERSION
            rp["judge_reference_context"] = "full_l2"
            out_obj["request_params"] = rp

            out_dir.mkdir(parents=True, exist_ok=True)
            out_dir.joinpath("judge_raw.json").write_text(
                judge_raw if isinstance(judge_raw, str)
                else json.dumps(judge_raw, ensure_ascii=False, indent=2),
                encoding="utf-8",
            )
            out_path.write_text(
                json.dumps(out_obj, ensure_ascii=False, indent=2), encoding="utf-8"
            )

            if n_done % 25 == 0:
                print(f"[INFO] {n_done} re-judged ...")
            time.sleep(0.2)

    print(f"\n[OK] seen={n_total} rejudged={n_done} skipped={n_skipped} failed={n_failed}")
    print(f"[OK] Output under: {Path(args.out_root) / args.client}")


if __name__ == "__main__":
    main()