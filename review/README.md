# Judge reliability study

Independent second assessment of a stratified sample of 30 responses
against the same rubric. Reported in the thesis, Chapter 6, Section 6.5.

| File | Contents |
|---|---|
| `sample_manifest.csv` | The sample: one incident per (domain × backend × strategy) cell, drawn with `Random(42)` over the sorted incident ids. Resolves blind ids C01–C30 to test case, backend, strategy and run. |
| `blind_pack.md` | The 30 responses as presented for assessment: user message, context as seen by the judge, and response text. Scores and flags withheld. |
| `sealed_judge.json` | The original judge scores, flags and justifications for the same 30 cases, withheld during the assessment and opened only for the comparison. |
| `independent_scores.json` | The second assessment. Its `meta` block records that the scores were fixed before unsealing and that blinding was partial. |
| `compare.py` | Reproduces the figures reported in Section 6.5 from the two score files. Reads recorded data only; no model is involved. |
| `agreement.csv` | Output of `compare.py --csv`: the per-dimension summary followed by all thirty case-level comparisons. |
| `report.md` | Procedure, pre-registered criteria, findings, limitations. |

Sampling script: `scripts/sample_blind_review.py`.

## Reproducing the reported figures

`python review/compare.py`
`python review/compare.py --csv review/agreement.csv`

Exact agreement per dimension: R 83.3 %, H 76.7 %, S 90.0 %, D 80.0 %,
K 43.3 %. The figure for K is the finding rather than a defect of the
sample: the judge rewards that context is taken up, the second pass
deducts where context is taken up incorrectly, and the two orderings of
the conditions on that dimension do not agree.

`compare.py` additionally reports two things the rubric scores alone do
not show. The judge sets a single flag for offline workflow; the second
pass records separately whether a response mentions the constraint and
whether it adapts the procedure, which is what shows which of the two
the flag tracks. And it lists the cases the second pass judged to
contain a fabrication while the judge did not — the role prompt caps
Context Utilisation at 2 in that case, so a high score there is a cap
that did not engage.

## Scope

The evaluation criteria were fixed before the assessment, because four
of five rubric dimensions sit between 4.85 and 5.00 in the aggregates
and an agreement figure is trivially high there. The study establishes
the reliability and operationalisability of the rubric; it does not
establish construct validity, since the second assessment was made by a
model of the same family as the judge, and blinding was partial because
the context block identifies the strategy in all five conditions.