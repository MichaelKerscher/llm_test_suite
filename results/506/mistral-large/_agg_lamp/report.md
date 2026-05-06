# Aggregation Report (506/mistral-large) [lamp]
- judge_version filter: **judge_v1_1**
- Tests (latest runs): **270**
- Incidents with any deltas: **30**

## Mean scores by context level (snapshot)
### L0 (n=30)
- mean runtime: 7.4324666666666666
- mean R/H/S/D/K: 3.6/3.8333333333333335/3.533333333333333/4.133333333333334/2.5
- mean overall (avg R/H/S/D/K): 3.52
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.00, hallucination_suspected=0.10
### L2 (n=30)
- mean runtime: 9.7965
- mean R/H/S/D/K: 4.866666666666666/4.8/4.766666666666667/4.866666666666666/4.333333333333333
- mean overall (avg R/H/S/D/K): 4.7266666666666675
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.03, hallucination_suspected=0.00
### L2B (n=30)
- mean runtime: 10.9371
- mean R/H/S/D/K: 4.933333333333334/4.933333333333334/4.8/4.966666666666667/5.0
- mean overall (avg R/H/S/D/K): 4.926666666666667
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.60, hallucination_suspected=0.00
### unknown (n=180)
- mean runtime: 9.382227777777777
- mean R/H/S/D/K: 4.8/4.805555555555555/4.783333333333333/4.916666666666667/4.777777777777778
- mean overall (avg R/H/S/D/K): 4.816666666666666
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.40, hallucination_suspected=0.00

## Mean scores by strategy (snapshot)
### S0 (n=30)
- mean runtime: 7.4324666666666666
- mean R/H/S/D/K: 3.6/3.8333333333333335/3.533333333333333/4.133333333333334/2.5
- mean overall (avg R/H/S/D/K): 3.52
### S0_RAW (n=30)
- mean runtime: 9.408066666666667
- mean R/H/S/D/K: 4.833333333333333/4.833333333333333/4.733333333333333/4.933333333333334/4.666666666666667
- mean overall (avg R/H/S/D/K): 4.8
### S0_UNSTRUCTURED (n=30)
- mean runtime: 10.1927
- mean R/H/S/D/K: 4.566666666666666/4.566666666666666/4.6/4.766666666666667/4.133333333333334
- mean overall (avg R/H/S/D/K): 4.526666666666667
### S1 (n=30)
- mean runtime: 9.7965
- mean R/H/S/D/K: 4.866666666666666/4.8/4.766666666666667/4.866666666666666/4.333333333333333
- mean overall (avg R/H/S/D/K): 4.7266666666666675
### S2 (n=30)
- mean runtime: 10.9371
- mean R/H/S/D/K: 4.933333333333334/4.933333333333334/4.8/4.966666666666667/5.0
- mean overall (avg R/H/S/D/K): 4.926666666666667
### S2_ABL_NOASSET (n=30)
- mean runtime: 9.7382
- mean R/H/S/D/K: 4.866666666666666/4.9/4.866666666666666/4.933333333333334/4.966666666666667
- mean overall (avg R/H/S/D/K): 4.906666666666666
### S2_ABL_NODEV (n=30)
- mean runtime: 9.3244
- mean R/H/S/D/K: 4.966666666666667/4.933333333333334/4.866666666666666/5.0/4.966666666666667
- mean overall (avg R/H/S/D/K): 4.946666666666667
### S2_ABL_NOENV (n=30)
- mean runtime: 8.850366666666668
- mean R/H/S/D/K: 4.833333333333333/4.766666666666667/4.7/4.9/4.933333333333334
- mean overall (avg R/H/S/D/K): 4.826666666666667
### S2_ABL_NOINC (n=30)
- mean runtime: 8.779633333333333
- mean R/H/S/D/K: 4.733333333333333/4.833333333333333/4.933333333333334/4.966666666666667/5.0
- mean overall (avg R/H/S/D/K): 4.8933333333333335

## Top missing elements (max 20)
- offline_workflow: 2
- Kontextnutzung minimal (nur Asset-ID): 2
- Kein expliziter Offline-Workflow trotz spotty connectivity: 2
- Offline-Workflow explizit (spotty connectivity + low_power_mode): 2
- Offline-Workflow explizit (spotty connectivity): 2
- Offline-Workflow nicht explizit erwähnt (spotty connectivity vorhanden): 2
- Kontextnutzung minimal (nur Asset-ID vorhanden): 2
- Keine Nutzung der Asset-ID im Kontext: 2
- Offline-Workflow nicht explizit (spotty connectivity vorhanden): 2
- Keine Nutzung des Kontexts (nur Asset-ID vorhanden): 2
- Offline-Workflow explizit: 2
- Offline-Workflow nicht erwähnt trotz connectivity=spotty: 2
- Klare Stop-Condition für Beobachtungsphase fehlt: 1
- Offline-Workflow nicht explizit erwähnt: 1
- Offline-Workflow nicht explizit (trotz offline-Signal): 1
- Keine Nutzung der Asset-ID im Text: 1
- Keine Erwähnung von Foto-Workflow (obwohl nicht im Context): 1
- Keine spezifische Erwähnung intermittierender Fehler: 1
- Explizite Erwähnung der Asset-ID (n4427359783) in Dokumentation: 1
- Keine Offline-Workflow-Erwähnung (aber auch nicht erwartbar bei minimalem Context): 1
