#!/usr/bin/env python3
"""Compare the judge scores against the independent second assessment.

Reproduces the figures reported in the thesis, Chapter 6, Section 6.5
(Judge Reliability) from the two score files in this directory. Reads
only recorded data; no model is involved and no run is repeated.

Usage:
    python review/compare.py
    python review/compare.py --csv review/agreement.csv
"""

from __future__ import annotations

import argparse
import csv
import json
import sys
from pathlib import Path

DIMENSIONS = ("R", "H", "S", "D", "K")
SATURATION_THRESHOLD = 4.85  # pre-registered, see report.md

HERE = Path(__file__).resolve().parent


def load_pairs(sealed_path: Path, independent_path: Path):
    """Return [(case_id, judge_case, second_case), ...] sorted by case id."""
    sealed = json.loads(sealed_path.read_text(encoding="utf-8"))
    independent = json.loads(independent_path.read_text(encoding="utf-8"))
    cases = independent["cases"]

    missing = sorted(set(sealed) ^ set(cases))
    if missing:
        sys.exit(f"case ids do not match between the two files: {missing}")

    return [(c, sealed[c], cases[c]) for c in sorted(sealed)]


def mean(values):
    return sum(values) / len(values) if values else float("nan")


def spearman(xs, ys):
    """Rank correlation with midranks for ties. Returns None if a series is constant."""
    def rank(values):
        order = sorted(range(len(values)), key=lambda i: values[i])
        ranks = [0.0] * len(values)
        i = 0
        while i < len(order):
            j = i
            while j + 1 < len(order) and values[order[j + 1]] == values[order[i]]:
                j += 1
            midrank = (i + j) / 2 + 1
            for k in range(i, j + 1):
                ranks[order[k]] = midrank
            i = j + 1
        return ranks

    rx, ry = rank(xs), rank(ys)
    mx, my = mean(rx), mean(ry)
    num = sum((a - mx) * (b - my) for a, b in zip(rx, ry))
    dx = sum((a - mx) ** 2 for a in rx)
    dy = sum((b - my) ** 2 for b in ry)
    if dx == 0 or dy == 0:
        return None
    return num / (dx * dy) ** 0.5


def per_dimension(pairs):
    """One stats dict per rubric dimension."""
    out = []
    for dim in DIMENSIONS:
        judge = [p[1]["scores"][dim] for p in pairs]
        second = [p[2]["scores"][dim] for p in pairs]
        diffs = [s - j for j, s in zip(judge, second)]
        out.append({
            "dimension": dim,
            "n": len(pairs),
            "exact": sum(1 for d in diffs if d == 0),
            "within_one": sum(1 for d in diffs if abs(d) <= 1),
            "judge_mean": mean(judge),
            "second_mean": mean(second),
            "mean_diff": mean(diffs),
            "rho": spearman(judge, second),
        })
    return out


def behavioural(pairs):
    """Agreement on the two behavioural judgements recorded separately.

    The judge sets one flag, offline_workflow_mentioned. The second pass
    records two: whether the response mentions the constraint, and whether
    it adapts the procedure. Comparing the flag against both is what shows
    which of the two it actually tracks.
    """
    rows = []
    for case_id, judge, second in pairs:
        flag = judge["flags"]["offline_workflow_mentioned"]
        rows.append((case_id, flag, second["mention"], second["adapt"]))

    return {
        "n": len(rows),
        "flag_set": sum(1 for r in rows if r[1]),
        "mention": sum(1 for r in rows if r[2]),
        "adapt": sum(1 for r in rows if r[3]),
        "flag_eq_mention": sum(1 for r in rows if r[1] == r[2]),
        "flag_eq_adapt": sum(1 for r in rows if r[1] == r[3]),
        "flag_set_without_adapt": sum(1 for r in rows if r[1] and not r[3]),
    }


def hallucination(pairs):
    """Cases the second pass flags as fabrication and the judge does not.

    The judge role prompt caps K at 2 where a fabrication is suspected, so a
    case flagged here with a high K is a cap that did not engage.
    """
    out = []
    for case_id, judge, second in pairs:
        if second.get("hallucination_suspected") and not judge["flags"]["hallucination_suspected"]:
            out.append((case_id, judge["scores"]["K"], second.get("note", "")))
    return out


def report(pairs):
    dims = per_dimension(pairs)
    n = len(pairs)

    print(f"Judge reliability: {n} cases\n")

    print(f"{'dim':<5}{'exact':>12}{'within 1':>12}{'judge':>9}{'second':>9}"
          f"{'diff':>9}{'rho':>8}")
    for d in dims:
        rho = "n/a" if d["rho"] is None else f"{d['rho']:+.2f}"
        print(f"{d['dimension']:<5}"
              f"{d['exact']:>4}/{n} {100*d['exact']/n:>5.1f}%"
              f"{d['within_one']:>4}/{n} {100*d['within_one']/n:>5.1f}%"
              f"{d['judge_mean']:>9.2f}{d['second_mean']:>9.2f}"
              f"{d['mean_diff']:>+9.2f}{rho:>8}")

    print(f"\nSaturation (mean at or above {SATURATION_THRESHOLD}):")
    for d in dims:
        j = "yes" if d["judge_mean"] >= SATURATION_THRESHOLD else "no"
        s = "yes" if d["second_mean"] >= SATURATION_THRESHOLD else "no"
        print(f"  {d['dimension']}: judge {j:<4} second pass {s}")

    b = behavioural(pairs)
    print(f"\nBehavioural judgements ({b['n']} cases):")
    print(f"  judge flag offline_workflow_mentioned set : {b['flag_set']}")
    print(f"  second pass, mentions the constraint      : {b['mention']}")
    print(f"  second pass, adapts the procedure         : {b['adapt']}")
    print(f"  flag agrees with 'mentions'               : {b['flag_eq_mention']}/{b['n']}")
    print(f"  flag agrees with 'adapts'                 : {b['flag_eq_adapt']}/{b['n']}")
    print(f"  flag set where the procedure is not adapted: {b['flag_set_without_adapt']}")

    h = hallucination(pairs)
    print(f"\nFabrications found by the second pass but not flagged by the judge: {len(h)}")
    for case_id, k, note in h:
        print(f"  {case_id}: judge K = {k} -- {note[:70]}")

    return dims


def write_csv(pairs, dims, path: Path):
    with path.open("w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh)
        w.writerow(["dimension", "n", "exact", "exact_pct", "within_one",
                    "judge_mean", "second_mean", "mean_diff", "spearman_rho"])
        for d in dims:
            w.writerow([d["dimension"], d["n"], d["exact"],
                        f"{100*d['exact']/d['n']:.1f}", d["within_one"],
                        f"{d['judge_mean']:.3f}", f"{d['second_mean']:.3f}",
                        f"{d['mean_diff']:.3f}",
                        "" if d["rho"] is None else f"{d['rho']:.3f}"])
        w.writerow([])
        w.writerow(["case_id"] + [f"judge_{d}" for d in DIMENSIONS]
                   + [f"second_{d}" for d in DIMENSIONS]
                   + ["judge_flag_offline", "second_mention", "second_adapt"])
        for case_id, judge, second in pairs:
            w.writerow([case_id]
                       + [judge["scores"][d] for d in DIMENSIONS]
                       + [second["scores"][d] for d in DIMENSIONS]
                       + [judge["flags"]["offline_workflow_mentioned"],
                          second["mention"], second["adapt"]])
    print(f"\nwritten: {path}")


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--sealed", type=Path, default=HERE / "sealed_judge.json")
    ap.add_argument("--independent", type=Path, default=HERE / "independent_scores.json")
    ap.add_argument("--csv", type=Path, help="also write the comparison to this file")
    args = ap.parse_args()

    for p in (args.sealed, args.independent):
        if not p.is_file():
            sys.exit(f"not found: {p}")

    pairs = load_pairs(args.sealed, args.independent)
    dims = report(pairs)
    if args.csv:
        write_csv(pairs, dims, args.csv)


if __name__ == "__main__":
    main()
