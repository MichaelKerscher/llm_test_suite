# Aggregation Report (506/gemini-2.5-flash) [lamp]
- judge_version filter: **judge_v1_1**
- Tests (latest runs): **270**
- Incidents with any deltas: **30**

## Mean scores by context level (snapshot)
### L0 (n=30)
- mean runtime: 5.5879
- mean R/H/S/D/K: 3.466666666666667/3.8333333333333335/3.9/4.033333333333333/2.8333333333333335
- mean overall (avg R/H/S/D/K): 3.6133333333333337
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.00, hallucination_suspected=0.03
### L2 (n=30)
- mean runtime: 8.964233333333334
- mean R/H/S/D/K: 4.733333333333333/4.6/4.633333333333334/4.9/3.7333333333333334
- mean overall (avg R/H/S/D/K): 4.52
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.03, hallucination_suspected=0.10
### L2B (n=30)
- mean runtime: 9.6204
- mean R/H/S/D/K: 4.833333333333333/4.833333333333333/4.8/5.0/4.966666666666667
- mean overall (avg R/H/S/D/K): 4.886666666666667
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.60, hallucination_suspected=0.00
### unknown (n=180)
- mean runtime: 9.470216666666666
- mean R/H/S/D/K: 4.872222222222222/4.861111111111111/4.877777777777778/4.955555555555556/4.95
- mean overall (avg R/H/S/D/K): 4.903333333333333
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.46, hallucination_suspected=0.00

## Mean scores by strategy (snapshot)
### S0 (n=30)
- mean runtime: 5.5879
- mean R/H/S/D/K: 3.466666666666667/3.8333333333333335/3.9/4.033333333333333/2.8333333333333335
- mean overall (avg R/H/S/D/K): 3.6133333333333337
### S0_RAW (n=30)
- mean runtime: 9.605733333333331
- mean R/H/S/D/K: 4.966666666666667/4.933333333333334/4.966666666666667/4.966666666666667/4.966666666666667
- mean overall (avg R/H/S/D/K): 4.96
### S0_UNSTRUCTURED (n=30)
- mean runtime: 9.943299999999999
- mean R/H/S/D/K: 4.8/4.833333333333333/4.933333333333334/4.966666666666667/4.866666666666666
- mean overall (avg R/H/S/D/K): 4.88
### S1 (n=30)
- mean runtime: 8.964233333333334
- mean R/H/S/D/K: 4.733333333333333/4.6/4.633333333333334/4.9/3.7333333333333334
- mean overall (avg R/H/S/D/K): 4.52
### S2 (n=30)
- mean runtime: 9.6204
- mean R/H/S/D/K: 4.833333333333333/4.833333333333333/4.8/5.0/4.966666666666667
- mean overall (avg R/H/S/D/K): 4.886666666666667
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
- Kontextnutzung minimal (nur Asset-ID): 3
- Offline-Workflow fehlt trotz connectivity=offline: 2
- Keine Anpassung an Offline-Bedingungen erkennbar: 1
- Generische Schritte ohne Priorisierung nach Severity: 1
- Offline-Workflow nicht explizit erwähnt trotz connectivity=offline: 1
- Device-Status erwähnt, aber nicht als Workflow-Constraint genutzt: 1
- Kontextnutzung (nur Asset-ID vorhanden, keine Umwelt-/Geräte-Infos genutzt): 1
- Spezifische Priorisierung bei intermittent fault: 1
- Beobachtungsdauer/Trigger für intermittierenden Fehler: 1
- Klarstellung device_state vs. Asset-Fehler: 1
- Offline-Workflow explizit (spotty connectivity): 1
- Explizite Ticket-ID-Erfassung: 1
- Zeitstempel-Dokumentation: 1
- Explizite Stop-Conditions für Abbruch: 1
- Offline-Workflow (connectivity=offline, device_state=low_battery): 1
- Keine Offline-Workflow-Erwähnung (aber nicht erwartbar bei minimalem Kontext): 1
- Offline-Workflow bei spotty connectivity nicht explizit erwähnt: 1
- Offline-Workflow (connectivity=offline): 1
- Klare Priorisierung Offline-Dokumentation: 1
