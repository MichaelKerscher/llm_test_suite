# CSLI LLM Test Suite (506.ai / CompanyGPT) — README

> **Kurzfassung:** Diese Test-Suite führt reproduzierbare LLM-Experimente für Mobile-Support-Szenarien (Außendienst) aus und bewertet die Antworten automatisiert mit einem LLM-as-a-Judge.  
> **Fokus:** Context Engineering als kontrollierbare Variable (S0–S2).  
> **Pipeline:** Testcases (CSV/JSON) → Generator → Judge → Logs → Aggregation (Run-Reports + Run-Historie).

---

## 1) Projektziel

Diese Masterarbeits-Komponente operationalisiert **Context Engineering** als messbares Experiment:

- **S0 (Baseline):** Prompt-only / minimaler Kontext  
- **S1 (Fixed Schema):** vollständiger, strukturierter Kontext (deterministisches JSON)  
- **S2 (Prioritized & Budgeted):** deterministische Feldselektion + Budget + Audit-Meta (`_selection_meta`)

**Messziel:** Einfluss der Kontextkomposition auf Antwortqualität (Rubrik R/H/S/D/K), Stabilität über Runs und qualitative Fehlermuster (Flags, missing_elements).

---

## 2) Architektur (High-Level)

**LLM Test Suite** (lokal, Python)
- Runner lädt Testcases und steuert Run-Modus
- Strategy Hook wendet S0/S1/S2 an (S2 via deterministische Policy Engine)
- 506 API Client ruft:
  - **Generator Assistant** (Antwort erzeugen)
  - **Judge Assistant** (Antwort bewerten)
- Logger schreibt `run_XX.json` pro Testcase + `INC-...__judge.json` pro Incident
- Aggregation erzeugt Reports + Deltas + Run-Historie

---

## 3) Datenmodell: Testcases

### CSV (pro Zeile = 1 Testcase)
Pflichtfelder (empfohlen):
- `test_id` (z. B. `INC-LAMP-0001-TC1`)
- `incident_id`
- `user_message`
- `context_json` (JSON-String oder leer)
- `strategy` (`S0|S1|S2`)
- `expected_elements_short` (fault-type-spezifische Kurzliste für Judge)

Optional:
- `client`, `model`, `temperature`
- `image_path`, `audio_path`, `video_path` (wenn multimodal getestet wird)

> **Hinweis:** `photo_available` im Kontext ist **nur ein Workflow-Signal** („Foto vorhanden“), ersetzt aber **kein echtes Bild**. Für echte Bildtests muss ein Bild als File referenziert/übergeben werden.

---

## 4) Bewertung: Rubrik + Judge

### Rubrik (1–5)
- **R** Relevanz  
- **H** Handlungsfähigkeit/Struktur  
- **S** Sicherheit/Eskalation  
- **D** Dokumentation/Nachvollziehbarkeit  
- **K** Kontextnutzung/Robustheit (inkl. Halluzinationen)

### Konsistenzregeln (Caps)
- `severity=high` ohne erkennbare Absicherung/Eskalation ⇒ **S ≤ 2**
- erfundene Fakten ⇒ **K ≤ 2** + `hallucination_suspected=true`
- „Missing“ darf nur erwartet werden, wenn durch **User message oder Context** plausibel

### Judge Setup (empfohlen)
- eigenes Modell als Judge (z. B. **Claude Sonnet 4.5**)
- `temperature=0.0`
- versionierte Judge-Rolle (z. B. `judge_v1_1`) → wird geloggt

---

## 5) Repository-Struktur (typisch)

- `lib/`
  - `test_runner.py` — Run-Logik (testcase/incident), Strategy Hook, Judge-Prompts
  - `context_policy_s2.py` — deterministische Selektion + Budget + `_selection_meta`
  - `clients/` — 506.ai/CompanyGPT Client (generate + judge)
  - `logger.py` — schreibt `run_XX.json` Artefakte
- `scripts/`
  - `run_test.py` — CLI entrypoint für Suite-Runs
  - `aggregate_results.py` — Snapshot-Report + Run-Historie + runs_overall
- `tests/`
  - `lamp_testcases_v02.csv`, ...

- `results/`
  - `results/506/<TEST_ID>/run_01.json` …
  - `results/506/<INCIDENT_ID>__judge.json`
  - `results/506/_agg/` (Reports/JSONs)

---

## 6) Setup

### Python
- Python **3.10+** empfohlen

### Installation
```bash
pip install -r requirements.txt
```

### .env (Beispiel)
```dotenv
# 506.ai / CompanyGPT
COMPANYGPT_BASE_URL=https://companygpt.506.ai:3003
COMPANYGPT_ORG_ID=...
COMPANYGPT_API_KEY=...

# Assistants
COMPANYGPT_GENERATOR_ASSISTANT_ID=...
COMPANYGPT_JUDGE_ASSISTANT_ID=...

# Defaults
TESTSUITE_ENABLE_JUDGE=true
TESTSUITE_RUN_MODE=incident
TESTSUITE_DEFAULT_MODEL=gpt-4.1

# Judge
TESTSUITE_JUDGE_MODEL=claude-sonnet-4.5
TESTSUITE_JUDGE_TEMPERATURE=0.0
TESTSUITE_JUDGE_MODE=BASIC
TESTSUITE_JUDGE_VERSION=judge_v1_1

# S2 budget
S2_BUDGET_CHARS=3500
```

---

## 7) Ausführen

### A) Full Suite (Incident-Mode, empfohlen)
```powershell
$env:TESTSUITE_ENABLE_JUDGE="true"
python .\scripts\run_test.py .\tests\lamp_testcases_v01.csv --mode incident
```

### B) Einzelner Incident (Smoke-Test)
```powershell
$env:TESTSUITE_ENABLE_JUDGE="true"
python .\scripts\run_test.py .\tests\lamp_testcases_v01.csv --mode incident --incident INC-LAMP-0001
```

### C) Einzelner Testcase
```powershell
$env:TESTSUITE_ENABLE_JUDGE="true"
python .\scripts\run_test.py .\tests\lamp_testcases_v01.csv --mode testcase --case INC-LAMP-0001-TC1
```

---

## 8) Aggregation / Reports

### Snaphsot-Report (latest run je Testcase)
```powershell
$env:TESTSUITE_ENABLE_JUDGE="true"
python .\scripts\run_test.py .\tests\lamp_testcases_v01.csv --mode testcase --case INC-LAMP-0001-TC1
```

Outputs:  
- `results/506/_agg/report.md`
- `summary_by_strategy.json`, `summary_by_context_level.json`
- `deltas_by_incident.json`
- `missing_elements_top.json`
- `rows.jsonl`
  
### Run-Historie + run_overall (Mean-of-run-means)
```powershell
python .\scripts\aggregate_results.py --client 506 --judge-version judge_v1_1 --all-runs
```

Zusätzliche Outputs:  
- `results/506/_agg/runs_by_index.json` (pro RunIndex x Strategie)
- `results/506/_agg/runs_overall.json` (ungewichtet über Run-Mittelwerte, pro Strategie & Rubrik)
**Wichtig:** `--judge-version` nutzen, damit Runs mit unterschiedlichen Judge-Rollen nicht vermischt werden.

---

## 10) Troubleshooting

- **Judge-JSON kaputt / nicht parsebar**  
  → `test_runner.py` hat Sanitizer/Repair (Quotes/Kommas). Prüfe zusätzlich das Incident-Artifact `results/506/<INCIDENT_ID>__judge.json`.

- **Runs werden „vermengt“ (alte + neue Judge-Versionen)**  
  → In der Aggregation immer filtern:  
  `python .\scripts\aggregate_results.py --client 506 --judge-version judge_v1_1`  
  bzw. mit Historie:  
  `python .\scripts\aggregate_results.py --client 506 --judge-version judge_v1_1 --all-runs`

- **Judge bewertet „fehlende“ Dinge, die nicht im Kontext stehen sollten**  
  → Prüfe, ob du im Judge-Prompt wirklich nur die passenden `expected_elements_short` pro Fault-Type übergibst.  
  → Stelle sicher, dass die Judge-Rolle die Regel enthält: *nur erwartbar, wenn in Context oder User message plausibel*.

- **Incident-Mode: Judge-Blocks fehlen oder sind falsch zugeordnet**  
  → Prüfe, ob der Judge im Array pro Block `test_id` exakt übernimmt.  
  → Fallback-Mapping nach Position greift nur, wenn `len(judge_array) == len(generated)`

- **Viele 5.0-Scores / Ceiling-Effekt**  
  → Rubrik-Anker (1/3/5) schärfen, Expected Elements präzisieren, Judge-Text strenger machen.  
  → Wichtig: Änderungen am Judge als neue `TESTSUITE_JUDGE_VERSION` versionieren und Runs neu ausführen.

---

## 11) Citation / Kontext (Masterarbeit)

Diese Test-Suite dient als **experimentelles Instrument** für die Masterarbeit:
- kontrollierte Variation der Kontextkomposition (S0–S2)
- reproduzierbares Logging + Audit Trail
- rubric-basierte automatische Bewertung (LLM-as-a-Judge) + Run-Stabilität

---

## 12) Lizenz / Hinweise

Internes Forschungsartefakt im Rahmen einer Masterarbeit. Keine Garantie für Produktivbetrieb.