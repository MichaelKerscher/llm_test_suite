# Aggregation Report (506/mistral-large) [lamp]
- judge_version filter: **judge_v1_1**
- Tests (latest runs): **270**
- Incidents with any deltas: **30**

## Mean scores by context level (snapshot)
### L0 (n=30)
- mean runtime: 7.453366666666667
- mean R/H/S/D/K: 3.5/3.7/3.7/4.1/2.466666666666667
- mean overall (avg R/H/S/D/K): 3.493333333333333
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.00, hallucination_suspected=0.07
### L2 (n=30)
- mean runtime: 9.9827
- mean R/H/S/D/K: 4.866666666666666/4.766666666666667/4.733333333333333/4.9/4.5
- mean overall (avg R/H/S/D/K): 4.753333333333333
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.10, hallucination_suspected=0.03
### L2B (n=30)
- mean runtime: 11.036966666666666
- mean R/H/S/D/K: 5.0/5.0/4.933333333333334/5.0/5.0
- mean overall (avg R/H/S/D/K): 4.986666666666666
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.60, hallucination_suspected=0.00
### unknown (n=180)
- mean runtime: 9.178688888888889
- mean R/H/S/D/K: 4.738888888888889/4.727777777777778/4.7444444444444445/4.872222222222222/4.688888888888889
- mean overall (avg R/H/S/D/K): 4.754444444444444
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.40, hallucination_suspected=0.01

## Mean scores by strategy (snapshot)
### S0 (n=30)
- mean runtime: 7.453366666666667
- mean R/H/S/D/K: 3.5/3.7/3.7/4.1/2.466666666666667
- mean overall (avg R/H/S/D/K): 3.493333333333333
### S0_RAW (n=30)
- mean runtime: 9.078766666666667
- mean R/H/S/D/K: 4.666666666666667/4.6/4.7/4.833333333333333/4.533333333333333
- mean overall (avg R/H/S/D/K): 4.666666666666667
### S0_UNSTRUCTURED (n=30)
- mean runtime: 9.300766666666668
- mean R/H/S/D/K: 4.366666666666666/4.333333333333333/4.4/4.6/3.7333333333333334
- mean overall (avg R/H/S/D/K): 4.286666666666666
### S1 (n=30)
- mean runtime: 9.9827
- mean R/H/S/D/K: 4.866666666666666/4.766666666666667/4.733333333333333/4.9/4.5
- mean overall (avg R/H/S/D/K): 4.753333333333333
### S2 (n=30)
- mean runtime: 11.036966666666666
- mean R/H/S/D/K: 5.0/5.0/4.933333333333334/5.0/5.0
- mean overall (avg R/H/S/D/K): 4.986666666666666
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
- offline_workflow: 4
- offline_workflow_explicit: 3
- Keine Nutzung der Asset-ID im Kontext: 3
- Offline-Workflow nicht erwähnt trotz spotty connectivity: 2
- Offline-Workflow nicht explizit erwähnt trotz connectivity=offline: 2
- Offline-Workflow nicht explizit trotz spotty connectivity: 2
- Offline-Workflow nicht explizit erwähnt: 2
- Klare Stop-Condition für Beobachtungsphase fehlt: 1
- Offline-Workflow (Kontext zeigt nur asset_osm, kein device.connectivity): 1
- Kontextnutzung minimal (nur Asset-ID erwähnt, keine Umgebung/Foto/Severity): 1
- Offline-Workflow nicht explizit (trotz device.connectivity=offline): 1
- Kontext-Hinweis auf Offline-Workflow vorhanden, aber nicht umgesetzt: 1
- Priorisierung/Stop-Conditions könnten klarer sein: 1
- Offline-Workflow nicht explizit (trotz offline/low_battery im Kontext): 1
- Unstrukturierter Kontext erschwert Nutzung, aber Modell extrahiert gut: 1
- Kein Bezug zu intermittent fault_type: 1
- Keine Nutzung der Asset-ID im Text: 1
- Generisch, keine Kontextanpassung: 1
- Explizite Erwähnung der Asset-ID (n4427359783) in Dokumentation: 1
- Offline-Workflow fehlt trotz spotty connectivity: 1
