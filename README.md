# LLM Test Suite
 
Evaluation pipeline for the master's thesis *Development and Evaluation of a
Context-Aware Mobile Support App for LLM-Assisted Field Support*
(FH Upper Austria, Hagenberg).
 
The suite compares five prompt strategies across three language model backends
and two municipal asset classes, and scores the generated responses with a
separate model against a five-dimensional rubric. It is one of the two
artifacts described in the thesis; the other is the Flutter application in
`support_app`.
 
---
 
## What it does
 
Each **test case** is one incident under one prompt strategy. The pipeline
loads it from a CSV corpus, builds the prompt the strategy calls for, sends it
to a generator backend, then sends the response to a judge model together with
the rubric, and writes both interactions to disk as a structured record.
 
The five strategies differ in what reaches the model and in what form:
 
| Strategy | Context in the prompt |
|---|---|
| `S0` | asset identifier only |
| `S0_UNSTRUCTURED` | all values, no field names, order shuffled |
| `S0_RAW` | the same values as German prose |
| `S1` | the full four-dimensional context as JSON |
| `S2` | the same fields, selected, ordered and annotated by the context policy |
 
`S1` and `S2` receive byte-identical input; the difference between them is
produced by the context policy at prompt construction time. That difference is
the subject of the thesis.
 
---
 
## Setup
 
Python 3.13.2.
 
```bash
python -m venv .venv
.venv\Scripts\activate          # Windows
source .venv/bin/activate       # Linux, macOS
pip install -r requirements.txt
cp .env.example .env            # then fill in the credentials
```
 
`.env` holds the platform credentials and the run configuration. It is not in
the repository; `.env.example` lists every variable the suite reads.
 
The four that change between runs:
 
| Variable | Meaning |
|---|---|
| `TESTSUITE_RUN_MODE` | `testcase` (one response per judge request) or `incident` (all five variants of an incident judged together) |
| `TESTSUITE_RESULTS_ROOT` | where the run records are written; keeps the two protocols in separate trees |
| `TESTSUITE_DEFAULT_MODEL` | generator backend for this run |
| `TESTSUITE_ENABLE_JUDGE` | set to `false` to generate without judging |
 
---
 
## Running an evaluation
 
```bash
# one full corpus, current settings from .env
python scripts/run_test.py tests/lamp_testcases_v05.csv
 
# a single incident, all five strategies
python scripts/run_test.py tests/lamp_testcases_v05.csv --incident INC-LAMP-0006
 
# a single test case
python scripts/run_test.py tests/lamp_testcases_v05.csv --case INC-LAMP-0006-TC5
 
# generate without judging
python scripts/run_test.py tests/signal_testcases_v04.csv --no-judge
 
# override the run mode for this call
python scripts/run_test.py tests/lamp_testcases_v05.csv --mode incident
```
 
Records accumulate rather than overwrite: each call writes
`run_NN.json` with the next free index, so repeated runs of the same corpus
build up the run history the aggregation reads.
 
Note that `run_test.py` falls back to `incident` mode when
`TESTSUITE_RUN_MODE` is unset, while `.env.example` sets `testcase`. The mode
in force is printed at the start of every run.

Note that `--client` means different things: in `aggregate_results.py` it is
the platform (`506`) and `--results-dir` is the tree above it; in
`verify_offline_flag.py` and `rejudge_ablation.py` it is the backend
(`gpt-4.1`) and the platform folder is part of `--results-dir`.
 
---
 
## Aggregating
 
```bash
# per-strategy means over all runs, LAMP only
python scripts/aggregate_results.py \
    --results-dir results_single --domain lamp --all-runs
 
# the ablation, judged against the full context
python scripts/aggregate_results.py \
    --results-dir results_single_ablfull --domain lamp \
    --incident-filter ablation --all-runs
```
 
| Option | Effect |
|---|---|
| `--results-dir` | which result tree to read |
| `--domain` | `lamp` or `signal`; omit for both |
| `--incident-filter` | `ablation` (ids ending in `-ABL`) or `regular` |
| `--judge-version` | restrict to records carrying a given judge version |
| `--all-runs` | also write `runs_by_index` and `runs_overall`, the per-run history the thesis reports dispersion from |
 
Output goes to `<results-dir>/<client>/_agg` unless `--out` says otherwise.
 
---
 
## Result trees
 
| Directory | Judging protocol | Reported in |
|---|---|---|
| `results_single/` | single-testcase (primary analysis) | Ch. 6, §6.4.1–6.4.5 |
| `results_incident/` | incident-group (sensitivity analysis) | Ch. 6, §6.4.6 |
| `results_single_ablfull/` | single-testcase, ablation re-judged against the full four-dimensional context | Ch. 6, §6.4.3 |
| `results_superseded_pre_fix/` | incident-group, produced before the payload correction of 2026-07-26 — **not reported, not comparable** | — |
 
The first three were produced from the same generated responses and differ only
in how those responses were judged. Which protocol carries the primary analysis
was fixed before the results were known; the reasoning is in
`docs/analysis_protocol.md`.
 
---
 
## Verification
 
Two measurements in the thesis do not go through the judge.
 
**Lexical verification.** The judge sets a flag for offline workflow, but the
flag turned out to record whether a response *mentions* connectivity rather
than whether it *adapts* the procedure. `verify_offline_flag.py` counts both
directly from the response texts, with no model involved:
 
```bash
python scripts/verify_offline_flag.py \
    --results-dir results_single/506 \
    --client gpt-4.1 \
    --testfile tests/lamp_testcases_v05.csv \
    --domain lamp
```
 
The behavioural claims of the thesis rest on this count, not on the flag.
 
**Judge reliability.** A stratified sample of thirty responses was assessed a
second time against the same rubric, independently and without sight of the
judge scores. See `review/README.md`; `review/compare.py` reproduces the
figures reported in Chapter 6, Section 6.5.
 
---
 
## Re-judging the ablation
 
The ablation removes one context dimension from the S2 payload and asks what
its absence costs. Judged against the ablated context, the judge cannot record
as missing what that context never contained — the information and the
expectation disappear together. `rejudge_ablation.py` therefore re-runs the
judging step against the full four-dimensional context, without invoking a
generator:
 
```bash
python scripts/rejudge_ablation.py \
    --results-dir results_single/506 \
    --client gemini-2.5-flash \
    --testfile tests/lamp_testcases_v05.csv \
    --out-root results_single_ablfull
```
 
Records carry `judge_version=judge_v1_1_single_fullref`. The full context is
read from the `S1` row of the corpus, which holds the unmodified context object
for each incident. The reasoning is in `docs/analysis_protocol.md`.
 
---
 
## Layout
 
```
lib/
  test_loader.py              CSV and JSON corpus parsing
  test_runner.py              runner, strategy hook, prompt builders
  context_formatters.py       prose and value-sequence renderings (S0_RAW, S0_UNSTRUCTURED)
  context_policy_s2.py        the context policy, LAMP domain
  context_policy_signal.py    the context policy, SIGNAL domain
  logger.py                   structured run records
  clients/
    companygpt_client.py      506.ai platform client
 
scripts/
  run_test.py                 entry point
  aggregate_results.py        summary statistics
  verify_offline_flag.py      lexical count over response texts
  rejudge_ablation.py         re-judging against the full context
  sample_blind_review.py      draws the reliability sample
  check_judge_prompt.py       rebuilds a judge prompt without calling a    model; shows that the expected-elements block was empty and which context each strategy was judged against
  get_models.py               lists the backends the platform exposes
 
tests/                         scenario corpora
docs/analysis_protocol.md     which analysis is primary, fixed in advance
review/                       judge reliability study
```
 
The two policy modules are held in separate files because their behaviour is
version-stamped: every run record carries the selector and guardrail versions
that produced its context, so any reported result can be traced back to the
policy that generated it.
 
---

## Adding a domain

The two policy modules share a structure. To add a third asset class:

1. Copy `lib/context_policy_signal.py` and adapt three things — the trigger
   conditions, the tier assignments, and the guardrail texts. Everything else
   (the selection-metadata contract, the packing, the ordering) stays.
2. Add a discriminating field to the Asset dimension so the dispatch can tell
   the domains apart, the way `traffic_signals:direction` distinguishes SIGNAL
   from LAMP.
3. Add one branch to the dispatch conditional in `lib/test_runner.py`.
4. Write a test case file following the column structure of the existing corpora.

Nothing in the runner, the prompt builder, the API client, the logger, the
aggregator, the rubric or the judge configuration changes. What the
architecture does not supply is the content: which signals matter for the new
asset class, and what a guardrail should say. Chapter 4, Section 4.4 of the
thesis works this through.

---

## Where the thesis describes what
 
| Thesis | Component |
|---|---|
| Ch. 4, §4.2 | the shared context schema and what each strategy makes of it |
| Ch. 4, §4.3 | the context policy: triggers, priority tiers, guardrails, budget |
| Ch. 4, §4.4 | domain dispatch, and what a further asset class would require |
| Ch. 5, §5.3 | this pipeline: module structure, judging protocols, log records |
| Ch. 5, §5.4 | the platform integration at request level |
| Ch. 5, §5.5 | what these choices imply for reproducibility |
| Ch. 6 | the evaluation itself |
 
---
 
## Scope
 
This is research code for a controlled experiment, not a production system.
The corpora are synthetic, the credentials belong to an academic access grant,
and the two assistant role prompts live in the platform configuration rather
than in this repository — they are reproduced verbatim in the appendices of the
thesis, which is the mitigation, not a substitute.
 
