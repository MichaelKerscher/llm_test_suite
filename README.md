## Result trees

| Tree | Protocol | Role |
|---|---|---|
| `results_single/` | single-testcase | primary analysis |
| `results_incident/` | incident-group | sensitivity analysis |
| `results_single_ablfull/` | single-testcase, full-context reference | ablation |
| `results_superseded_pre_fix/` | incident-group, pre-correction | not reported, not comparable |

`results_superseded_pre_fix/` predates a correction to the prompt
composition (commit of 2026-07-26): the context payload was serialised
with sorted keys, which alphabetised away the dimension ordering the S2
policy produces, and the selection metadata was transmitted to the
model instead of being retained as an audit artefact. Both affect S1
and S2 payloads. The full matrix was re-run after the fix.