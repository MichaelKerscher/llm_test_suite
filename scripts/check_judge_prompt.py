#!/usr/bin/env python3
"""
scripts/check_judge_prompt.py

Rebuilds the judge prompt for a few testcases and prints it. Pure string
assembly -- no model is called and no results are written.

Purpose: establish on the record what the judge actually received, namely
  (a) whether the EXPECTED ELEMENTS block carried any content, and
  (b) which CONTEXT the two unstructured variants were judged against.

Usage (from the repository root):
  python scripts/check_judge_prompt.py corpus/<lamp>.csv
  python scripts/check_judge_prompt.py corpus/<lamp>.csv --incident INC-LAMP-0001
"""

from __future__ import annotations

import argparse
import os
import sys
from pathlib import Path

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from lib.test_loader import load_testcases            # noqa: E402
from lib.test_runner import _build_judge_prompt_single  # noqa: E402

PLACEHOLDER_ANSWER = "<MODEL ANSWER -- hier steht im Lauf die echte Antwort>"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("corpus", type=Path, help="testcase corpus CSV")
    ap.add_argument("--incident", default=None,
                    help="incident_id to inspect; default is the first one")
    args = ap.parse_args()

    testcases = load_testcases(str(args.corpus))
    if not testcases:
        print("ABORT: corpus empty.", file=sys.stderr)
        return 2

    target = args.incident or (testcases[0]["input"]["meta"] or {}).get("incident_id")
    group = [
        tc for tc in testcases
        if (tc["input"].get("meta") or {}).get("incident_id") == target
    ]
    if not group:
        print(f"ABORT: incident {target} not found.", file=sys.stderr)
        return 2

    group.sort(key=lambda t: t.get("test_id", ""))

    print(f"### incident: {target}")
    print(f"### meta keys written by test_loader: "
          f"{sorted((group[0]['input'].get('meta') or {}).keys())}")
    print()

    for tc in group:
        meta = tc["input"].get("meta") or {}
        expected = meta.get("expected_elements_short", "")
        # run_testcase() hands original_context to the judge for the two
        # unstructured variants; at this point original_context is still a
        # verbatim copy of the corpus row, so tc-level context is correct here.
        ctx = tc["input"].get("context") or {}

        print("=" * 78)
        print(f"test_id = {tc['test_id']}   strategy = {meta.get('strategy')}")
        print(f"expected_elements_short is empty: {expected == ''!r}")
        print("=" * 78)
        print(_build_judge_prompt_single(tc, PLACEHOLDER_ANSWER, expected,
                                         judge_context=ctx))
        print()

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
