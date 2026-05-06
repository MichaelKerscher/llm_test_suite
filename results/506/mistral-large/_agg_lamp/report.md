# Aggregation Report (506/mistral-large) [lamp]
- judge_version filter: **judge_v1_1**
- Tests (latest runs): **270**
- Incidents with any deltas: **30**

## Mean scores by context level (snapshot)
### L0 (n=30)
- mean runtime: 7.0653999999999995
- mean R/H/S/D/K: 3.533333333333333/3.7333333333333334/3.7666666666666666/4.233333333333333/2.466666666666667
- mean overall (avg R/H/S/D/K): 3.546666666666667
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.00, hallucination_suspected=0.07
### L2 (n=30)
- mean runtime: 11.092233333333333
- mean R/H/S/D/K: 4.833333333333333/4.766666666666667/4.866666666666666/4.8/4.366666666666666
- mean overall (avg R/H/S/D/K): 4.7266666666666675
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.03, hallucination_suspected=0.00
### L2B (n=30)
- mean runtime: 10.2266
- mean R/H/S/D/K: 4.933333333333334/4.9/4.866666666666666/4.933333333333334/4.9
- mean overall (avg R/H/S/D/K): 4.906666666666666
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.60, hallucination_suspected=0.03
### unknown (n=180)
- mean runtime: 9.284
- mean R/H/S/D/K: 4.733333333333333/4.716666666666667/4.772222222222222/4.877777777777778/4.722222222222222
- mean overall (avg R/H/S/D/K): 4.764444444444445
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.41, hallucination_suspected=0.01

## Mean scores by strategy (snapshot)
### S0 (n=30)
- mean runtime: 7.0653999999999995
- mean R/H/S/D/K: 3.533333333333333/3.7333333333333334/3.7666666666666666/4.233333333333333/2.466666666666667
- mean overall (avg R/H/S/D/K): 3.546666666666667
### S0_RAW (n=30)
- mean runtime: 9.500866666666667
- mean R/H/S/D/K: 4.6/4.533333333333333/4.7/4.866666666666666/4.633333333333334
- mean overall (avg R/H/S/D/K): 4.666666666666667
### S0_UNSTRUCTURED (n=30)
- mean runtime: 9.510533333333333
- mean R/H/S/D/K: 4.4/4.333333333333333/4.566666666666666/4.6/3.8333333333333335
- mean overall (avg R/H/S/D/K): 4.346666666666667
### S1 (n=30)
- mean runtime: 11.092233333333333
- mean R/H/S/D/K: 4.833333333333333/4.766666666666667/4.866666666666666/4.8/4.366666666666666
- mean overall (avg R/H/S/D/K): 4.7266666666666675
### S2 (n=30)
- mean runtime: 10.2266
- mean R/H/S/D/K: 4.933333333333334/4.9/4.866666666666666/4.933333333333334/4.9
- mean overall (avg R/H/S/D/K): 4.906666666666666
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
- offline_workflow: 6
- Offline-Workflow (spotty connectivity): 3
- Kontextnutzung minimal (nur Asset-ID): 3
- Keine Nutzung des Kontexts (nur Asset-ID vorhanden): 2
- Offline-Workflow nicht erwähnt (spotty connectivity vorhanden): 2
- Low_battery nicht adressiert: 2
- Offline-Workflow nicht erwähnt (spotty connectivity im CONTEXT): 2
- Offline-Workflow (nicht erwartbar, da connectivity nicht im CONTEXT): 2
- Offline-Workflow (erwartbar wegen spotty connectivity, aber nicht explizit erwähnt): 2
- Offline-Workflow (spotty connectivity im CONTEXT, aber nicht erwähnt): 2
- Klare Stop-Condition für Beobachtungsphase fehlt: 1
- Offline-Workflow (Kontext zeigt nur asset_osm, keine Offline-Signale): 1
- Kontextnutzung minimal (nur Asset-ID erwähnt): 1
- Halluzinationen: RSA, PSA, Vorschaltgerät, Zeitschaltuhr ohne Kontext-Basis: 1
- Offline-Workflow nicht explizit erwähnt (trotz offline/low_battery): 1
- Offline-Workflow nicht explizit (trotz offline/low_battery im Kontext): 1
- Hinweis auf low_battery/offline etwas vage interpretiert: 1
- Keine Erwähnung von Foto oder spezifischen Beobachtungen: 1
- Generische Antwort ohne Bezug zu 'zeitweisem Ausfall': 1
- Explizite Erwähnung der Asset-ID (n4427359783) in Dokumentation: 1
