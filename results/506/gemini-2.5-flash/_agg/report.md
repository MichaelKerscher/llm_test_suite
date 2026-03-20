# Aggregation Report (506\gemini-2.5-flash) [combined]
- judge_version filter: **judge_v1_1**
- Tests (latest runs): **300**
- Incidents with any deltas: **60**

## Mean scores by context level (snapshot)
### L0 (n=60)
- mean runtime: 5.78465
- mean R/H/S/D/K: 3.6666666666666665/3.9/3.9166666666666665/4.116666666666666/2.85
- mean overall (avg R/H/S/D/K): 3.69
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.00, hallucination_suspected=0.03
### L2 (n=60)
- mean runtime: 8.95935
- mean R/H/S/D/K: 4.8/4.7/4.75/4.916666666666667/4.033333333333333
- mean overall (avg R/H/S/D/K): 4.64
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.10, hallucination_suspected=0.05
### L2B (n=60)
- mean runtime: 9.180033333333334
- mean R/H/S/D/K: 4.883333333333334/4.9/4.85/4.95/4.933333333333334
- mean overall (avg R/H/S/D/K): 4.903333333333333
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.62, hallucination_suspected=0.02
### unknown (n=120)
- mean runtime: 9.318066666666665
- mean R/H/S/D/K: 4.866666666666666/4.85/4.841666666666667/4.95/4.966666666666667
- mean overall (avg R/H/S/D/K): 4.895
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.47, hallucination_suspected=0.00

## Mean scores by strategy (snapshot)
### S0 (n=60)
- mean runtime: 5.78465
- mean R/H/S/D/K: 3.6666666666666665/3.9/3.9166666666666665/4.116666666666666/2.85
- mean overall (avg R/H/S/D/K): 3.69
### S1 (n=60)
- mean runtime: 8.95935
- mean R/H/S/D/K: 4.8/4.7/4.75/4.916666666666667/4.033333333333333
- mean overall (avg R/H/S/D/K): 4.64
### S2 (n=60)
- mean runtime: 9.180033333333334
- mean R/H/S/D/K: 4.883333333333334/4.9/4.85/4.95/4.933333333333334
- mean overall (avg R/H/S/D/K): 4.903333333333333
### S2_ABL_NOASSET (n=30)
- mean runtime: 9.480966666666665
- mean R/H/S/D/K: 4.9/4.933333333333334/4.866666666666666/4.966666666666667/5.0
- mean overall (avg R/H/S/D/K): 4.933333333333334
### S2_ABL_NODEV (n=30)
- mean runtime: 8.9771
- mean R/H/S/D/K: 4.933333333333334/4.866666666666666/4.866666666666666/5.0/5.0
- mean overall (avg R/H/S/D/K): 4.933333333333334
### S2_ABL_NOENV (n=30)
- mean runtime: 9.661033333333334
- mean R/H/S/D/K: 4.866666666666666/4.766666666666667/4.766666666666667/4.9/4.933333333333334
- mean overall (avg R/H/S/D/K): 4.846666666666667
### S2_ABL_NOINC (n=30)
- mean runtime: 9.153166666666667
- mean R/H/S/D/K: 4.766666666666667/4.833333333333333/4.866666666666666/4.933333333333334/4.933333333333334
- mean overall (avg R/H/S/D/K): 4.866666666666666

## Top missing elements (max 20)
- Offline-Workflow bei spotty connectivity: 7
- Kontextnutzung minimal (nur Asset-ID): 5
- Offline-Workflow bei spotty connectivity nicht explizit erwähnt: 3
- Offline-Workflow (spotty connectivity): 3
- Keine Priorisierung nach Severity (nicht im Context): 2
- Offline-Workflow fehlt trotz connectivity=offline: 2
- Kontextnutzung minimal (nur Asset-ID vorhanden): 2
- Keine Anpassung an Offline-Bedingungen erkennbar: 1
- Generische Schritte ohne Priorisierung nach Severity: 1
- Offline-Workflow nicht explizit erwähnt trotz connectivity=offline: 1
- Device-Status erwähnt, aber nicht als Workflow-Constraint genutzt: 1
- Kontextnutzung (nur Asset-ID vorhanden, keine Umwelt-/Geräte-Infos genutzt): 1
- Spezifische Priorisierung bei intermittent fault: 1
- Beobachtungsdauer/Trigger für intermittierenden Fehler: 1
- Klarstellung device_state vs. Asset-Fehler: 1
- Explizite Ticket-ID-Erfassung: 1
- Zeitstempel-Dokumentation: 1
- Explizite Stop-Conditions für Abbruch: 1
- Offline-Workflow (connectivity=offline, device_state=low_battery): 1
- Keine Offline-Workflow-Erwähnung (aber nicht erwartbar bei minimalem Kontext): 1
