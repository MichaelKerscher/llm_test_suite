#!/usr/bin/env python3
"""
scripts/sample_blind_review.py

Draws a reproducible stratified sample for the blind re-evaluation of the
LLM-as-judge and emits three artefacts:

  blind_pack.md       response texts + judge-visible context, WITHOUT scores
  sealed_judge.json   judge scores/flags, keyed by blind id  -- open in step 4
  sample_manifest.csv blind id -> test_id/model/strategy      -- open in step 4

Pre-registered sampling criterion
---------------------------------
Full factorial over domain x model x strategy (2 x 3 x 5 = 30 cells).
Per cell, one incident is drawn with random.Random(42) from the sorted list of
incident_ids available in that cell, and then one run is drawn from the
repetitions of that testcase (generation temperature is 0.2, so the
repetitions differ and picking run_01 would be a silent choice).
Both draws use the same generator, in that order.

Incident drawing is without replacement within a domain, so no incident
appears twice in the pack; this keeps the strategy of a case from being
reconstructable by comparing two responses to the same task.
Reading order is shuffled with the same generator.

Usage
-----
  python scripts/sample_blind_review.py \
      --results results_single \
      --corpus corpus/lamp_testcases_v0X.csv \
      --corpus corpus/signal_testcases_v04.csv \
      --out review/

Only records with run_mode == "testcase", status == "success" and a judge
block are eligible. Each testcase directory holds several run_XX.json files;
all of them are eligible and the run index is recorded in the manifest.
"""

from __future__ import annotations

import argparse
import csv
import json
import random
import sys
from collections import defaultdict
from pathlib import Path

SEED = 42
DOMAINS = ["LAMP", "SIGNAL"]
STRATEGIES = ["S0", "S0_RAW", "S0_UNSTRUCTURED", "S1", "S2"]

# Judge artefacts written alongside the records; not evaluation records.
SKIP_NAMES = {"judge_raw.json"}
SKIP_SUFFIXES = ("__judge.json",)


def domain_of(test_id: str) -> str | None:
    for d in DOMAINS:
        if f"-{d}-" in test_id.upper():
            return d
    return None


def load_records(root: Path) -> tuple[list[dict], list[str]]:
    records: list[dict] = []
    problems: list[str] = []

    for path in sorted(root.rglob("*.json")):
        if path.name in SKIP_NAMES or path.name.endswith(SKIP_SUFFIXES):
            continue
        try:
            rec = json.loads(path.read_text(encoding="utf-8"))
        except Exception as exc:
            problems.append(f"unreadable: {path} ({exc})")
            continue
        if not isinstance(rec, dict) or "request_params" not in rec:
            continue

        rp = rec.get("request_params") or {}
        if rp.get("run_mode") != "testcase":
            continue
        if (rec.get("meta") or {}).get("status") != "success":
            continue
        if not rec.get("judge"):
            continue

        rec["_path"] = str(path)
        stem = path.stem  # run_07 -> 7; anything else sorts last
        rec["_run"] = int(stem[4:]) if stem.startswith("run_") and stem[4:].isdigit() else 999
        records.append(rec)

    return records, problems


def load_corpus(paths: list[Path]) -> dict[str, dict]:
    """
    Returns testcase_id -> context_json as it stands in the corpus.

    For S0_RAW and S0_UNSTRUCTURED this is the flattened representation
    ({"_raw_text": ...} / {"_unstructured_text": ...}), which is what
    run_testcase() copies into original_context and hands to the judge. The
    structured L2_full context is NOT what those two variants are judged
    against, despite the comment in _build_judge_prompt_single.
    """
    contexts: dict[str, dict] = {}
    for p in paths:
        with p.open(encoding="utf-8-sig", newline="") as fh:
            for row in csv.DictReader(fh):
                tid = (row.get("testcase_id") or "").strip()
                if not tid or tid in contexts:
                    continue
                try:
                    contexts[tid] = json.loads(row.get("context_json") or "{}")
                except Exception:
                    contexts[tid] = {}
    return contexts


def judge_context_for(rec: dict, corpus: dict[str, dict]) -> dict:
    """Reproduces the CONTEXT block the judge saw, per test_runner logic."""
    strat = ((rec.get("request_params") or {}).get("context_strategy") or "").upper()
    if strat in ("S0_RAW", "S0_UNSTRUCTURED"):
        # context_for_model is None for these, so the log carries {}; the
        # judge saw original_context, i.e. the corpus row itself.
        return corpus.get(rec.get("test_id") or "", {})
    return rec.get("input", {}).get("context") or {}


def build_cells(records: list[dict]) -> dict[tuple[str, str, str], dict[str, list[dict]]]:
    cells: dict[tuple[str, str, str], dict[str, list[dict]]] = defaultdict(
        lambda: defaultdict(list)
    )
    for rec in records:
        test_id = rec.get("test_id") or ""
        dom = domain_of(test_id)
        if dom is None:
            continue
        rp = rec.get("request_params") or {}
        strat = (rp.get("context_strategy") or "").upper()
        if strat not in STRATEGIES:
            continue
        inc = rp.get("incident_id") or ""
        if not inc:
            continue
        cells[(dom, rec.get("model") or "", strat)][inc].append(rec)
    return cells


def draw(cells, models, warnings) -> list[tuple[str, dict]]:
    rng = random.Random(SEED)
    used: dict[str, set[str]] = defaultdict(set)
    picked: list[dict] = []

    for domain in DOMAINS:
        for model in models:
            for strat in STRATEGIES:
                pool = cells.get((domain, model, strat), {})
                if not pool:
                    warnings.append(f"empty cell: {domain} / {model} / {strat}")
                    continue
                cands = sorted(i for i in pool if i not in used[domain])
                if not cands:
                    cands = sorted(pool)
                    warnings.append(
                        f"pool exhausted, drawing with replacement: "
                        f"{domain} / {model} / {strat}"
                    )
                inc = rng.choice(cands)
                used[domain].add(inc)
                runs = sorted(pool[inc], key=lambda r: (r["_run"], r["_path"]))
                picked.append(rng.choice(runs))

    rng.shuffle(picked)
    return [(f"C{i:02d}", rec) for i, rec in enumerate(picked, start=1)]


def write_outputs(sample, corpus, out_dir: Path) -> None:
    out_dir.mkdir(parents=True, exist_ok=True)

    pack = [
        "# Blind Pack -- Nachbewertung LLM-as-judge",
        "",
        f"Seed {SEED}. Reihenfolge gemischt. Strategie und Modell sind nicht "
        "aufgefuehrt; der CONTEXT-Block ist derselbe, den der Judge gesehen hat.",
        "",
    ]
    sealed: dict[str, dict] = {}
    manifest_rows = []

    for blind_id, rec in sample:
        rp = rec.get("request_params") or {}
        inc = rp.get("incident_id") or ""
        test_id = rec.get("test_id") or ""
        strat = (rp.get("context_strategy") or "").upper()
        ctx = judge_context_for(rec, corpus)

        pack += [
            f"## {blind_id}",
            "",
            f"- Domaene: {domain_of(test_id)}",
            "",
            "### USER MESSAGE",
            "",
            "```",
            str(rp.get("user_message") or "").strip(),
            "```",
            "",
            "### CONTEXT (wie vom Judge gesehen)",
            "",
            "```json",
            json.dumps(ctx, ensure_ascii=False, indent=2),
            "```",
            "",
            "### EXPECTED ELEMENTS",
            "",
            "```",
            "(leer -- test_loader schreibt keinen Schluessel "
            "expected_elements_short in input.meta, der Judge erhielt hier "
            "keinen Inhalt)",
            "```",
            "",
            "### MODEL ANSWER",
            "",
            str((rec.get("response") or {}).get("text") or "").strip(),
            "",
            "---",
            "",
        ]

        judge = rec.get("judge") or {}
        sealed[blind_id] = {
            "test_id": test_id,
            "domain": domain_of(test_id),
            "model": rec.get("model"),
            "strategy": strat,
            "incident_id": inc,
            "run_index": rec.get("_run"),
            "scores": judge.get("scores"),
            "flags": judge.get("flags"),
            "missing_elements": judge.get("missing_elements"),
            "short_justification": judge.get("short_justification"),
            "source_path": rec.get("_path"),
        }
        manifest_rows.append(
            [blind_id, test_id, domain_of(test_id), rec.get("model"), strat, inc,
             rec.get("_run")]
        )

    (out_dir / "blind_pack.md").write_text("\n".join(pack), encoding="utf-8")
    (out_dir / "sealed_judge.json").write_text(
        json.dumps(sealed, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    with (out_dir / "sample_manifest.csv").open("w", encoding="utf-8", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["blind_id", "test_id", "domain", "model", "strategy",
                    "incident_id", "run_index"])
        w.writerows(manifest_rows)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--results", required=True, type=Path,
                    help="root of the primary single-testcase run")
    ap.add_argument("--corpus", action="append", default=[], type=Path,
                    help="testcase corpus CSV; repeat per domain")
    ap.add_argument("--out", default=Path("review"), type=Path)
    args = ap.parse_args()

    records, problems = load_records(args.results)
    for p in problems:
        print("[WARN] " + p, file=sys.stderr)

    if not records:
        print("ABORT: no eligible records found.", file=sys.stderr)
        return 2

    corpus = load_corpus(args.corpus)
    if not corpus:
        print("[WARN] corpus empty; the two unstructured variants will show "
              "an empty CONTEXT block.", file=sys.stderr)

    cells = build_cells(records)
    models = sorted({m for (_, m, _) in cells})
    print(f"[INFO] models found: {models}")

    warnings: list[str] = []
    sample = draw(cells, models, warnings)
    for w in warnings:
        print("[WARN] " + w, file=sys.stderr)

    write_outputs(sample, corpus, args.out)
    print(f"[INFO] {len(sample)} cases written to {args.out}")
    print("[INFO] do not open sealed_judge.json or sample_manifest.csv "
          "before the blind pass is complete.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
