# Analysis Protocol

Fixed on 2026-08-09, before the results of the single-testcase runs
were known. Recorded here so that the choice of primary analysis can be
verified as independent of its outcome.

## Judging protocols

The evaluation exists under two judging protocols. Both use the same
corpus, the same generator configuration, the same rubric, and the same
judge model.

**Incident-group judging** submits all strategy variants of one
incident in a single judge request. It holds the application of the
rubric constant within an incident, but the assessment of a response is
not independent of the others present in the same prompt: a
minimal-context answer is scored alongside four context-bearing ones,
the strategy order in the prompt is fixed, and the experimental design
is legible from the prompt itself.

**Single-testcase judging** submits one response per request. The
assessment is independent, at the cost of possible drift in rubric
application between invocations.

## Decision

Single-testcase judging is the **primary analysis**. Incident-group
judging is reported as a **sensitivity analysis**.

Reasoning: drift between invocations is undirected and averages out
over thirty incidents and ten runs. Contrast and position effects are
directed, act along the axis under investigation, and do not average
out. For a study whose entire purpose is the comparison of conditions,
directed error is the more damaging of the two.

This decision holds regardless of which protocol produces the larger
effects.

## Exception: ablation study

The ablation is judged against the **full four-dimensional context** of
the incident, not against the ablated context the generator received.

Reasoning: under single-testcase judging the judge is supplied with the
context the model was given, and its non-speculation rule forbids
recording as absent anything that context does not contain. Removing a
dimension therefore removes the information and the expectation
together. An ablation asks what the absence of a dimension costs, which
requires a reference frame that contains it.

The generated responses are unchanged; only the judging is repeated.
Records carry `judge_version=judge_v1_1_single_fullref` and
`judge_reference_context=full_l2`.

## Result trees

| Tree | Protocol | Role |
|---|---|---|
| `results/` | incident-group | sensitivity analysis |
| `results_single/` | single-testcase | primary analysis |
| `results_single_ablfull/` | single-testcase, full-context reference | ablation |

## Known limitation, recorded at the same time

The judge role prompt defines a scoring heuristic based on a
per-incident list of expected response elements. That list is not
transmitted: the corpus loader does not populate the field, and the
judge receives an empty block. All conditions are affected identically,
so comparisons between conditions remain valid; absolute score levels
should be read as relative rather than calibrated.