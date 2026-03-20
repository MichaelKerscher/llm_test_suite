# Aggregation Report (506\gemini-2.5-flash) [combined]
- judge_version filter: **judge_v1_1**
- Tests (latest runs): **300**
- Incidents with any deltas: **60**

## Mean scores by context level (snapshot)
### L0 (n=60)
- mean runtime: 6.337133333333333
- mean R/H/S/D/K: 3.683333333333333/3.9/4.05/4.183333333333334/2.8333333333333335
- mean overall (avg R/H/S/D/K): 3.73
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.00, hallucination_suspected=0.02
### L2 (n=60)
- mean runtime: 8.942516666666668
- mean R/H/S/D/K: 4.8/4.716666666666667/4.716666666666667/4.916666666666667/4.166666666666667
- mean overall (avg R/H/S/D/K): 4.663333333333333
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.12, hallucination_suspected=0.05
### L2B (n=60)
- mean runtime: 9.505366666666667
- mean R/H/S/D/K: 4.9/4.883333333333334/4.866666666666666/4.95/4.95
- mean overall (avg R/H/S/D/K): 4.91
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.63, hallucination_suspected=0.00
### unknown (n=120)
- mean runtime: 9.318066666666665
- mean R/H/S/D/K: 4.866666666666666/4.85/4.841666666666667/4.95/4.966666666666667
- mean overall (avg R/H/S/D/K): 4.895
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.47, hallucination_suspected=0.00

## Mean scores by strategy (snapshot)
### S0 (n=60)
- mean runtime: 6.337133333333333
- mean R/H/S/D/K: 3.683333333333333/3.9/4.05/4.183333333333334/2.8333333333333335
- mean overall (avg R/H/S/D/K): 3.73
### S1 (n=60)
- mean runtime: 8.942516666666668
- mean R/H/S/D/K: 4.8/4.716666666666667/4.716666666666667/4.916666666666667/4.166666666666667
- mean overall (avg R/H/S/D/K): 4.663333333333333
### S2 (n=60)
- mean runtime: 9.505366666666667
- mean R/H/S/D/K: 4.9/4.883333333333334/4.866666666666666/4.95/4.95
- mean overall (avg R/H/S/D/K): 4.91
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
- Kontextnutzung minimal (nur Asset-ID): 4
- Offline-Workflow bei spotty connectivity nicht explizit erwähnt: 3
- Offline-Workflow (spotty connectivity): 2
- Offline-Workflow fehlt trotz connectivity=offline: 2
- Keine Priorisierung nach Severity/Traffic: 2
- Offline-Workflow (device.connectivity=offline nicht adressiert): 2
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
