# Aggregation Report (506/mistral-large) [lamp]
- judge_version filter: **judge_v1_1**
- Tests (latest runs): **270**
- Incidents with any deltas: **30**

## Mean scores by context level (snapshot)
### L0 (n=30)
- mean runtime: 7.856566666666667
- mean R/H/S/D/K: 3.566666666666667/3.8/3.7333333333333334/4.066666666666666/2.566666666666667
- mean overall (avg R/H/S/D/K): 3.546666666666667
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.00, hallucination_suspected=0.10
### L2 (n=30)
- mean runtime: 10.188433333333334
- mean R/H/S/D/K: 4.9/4.866666666666666/4.8/4.9/4.5
- mean overall (avg R/H/S/D/K): 4.793333333333334
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.17, hallucination_suspected=0.00
### L2B (n=30)
- mean runtime: 10.8303
- mean R/H/S/D/K: 5.0/5.0/4.833333333333333/5.0/5.0
- mean overall (avg R/H/S/D/K): 4.966666666666667
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.60, hallucination_suspected=0.00
### unknown (n=180)
- mean runtime: 9.298833333333333
- mean R/H/S/D/K: 4.75/4.761111111111111/4.761111111111111/4.9/4.666666666666667
- mean overall (avg R/H/S/D/K): 4.767777777777778
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.40, hallucination_suspected=0.02

## Mean scores by strategy (snapshot)
### S0 (n=30)
- mean runtime: 7.856566666666667
- mean R/H/S/D/K: 3.566666666666667/3.8/3.7333333333333334/4.066666666666666/2.566666666666667
- mean overall (avg R/H/S/D/K): 3.546666666666667
### S0_RAW (n=30)
- mean runtime: 9.225033333333332
- mean R/H/S/D/K: 4.8/4.7/4.733333333333333/4.9/4.566666666666666
- mean overall (avg R/H/S/D/K): 4.739999999999999
### S0_UNSTRUCTURED (n=30)
- mean runtime: 9.875366666666668
- mean R/H/S/D/K: 4.3/4.433333333333334/4.466666666666667/4.7/3.566666666666667
- mean overall (avg R/H/S/D/K): 4.293333333333334
### S1 (n=30)
- mean runtime: 10.188433333333334
- mean R/H/S/D/K: 4.9/4.866666666666666/4.8/4.9/4.5
- mean overall (avg R/H/S/D/K): 4.793333333333334
### S2 (n=30)
- mean runtime: 10.8303
- mean R/H/S/D/K: 5.0/5.0/4.833333333333333/5.0/5.0
- mean overall (avg R/H/S/D/K): 4.966666666666667
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
- Kontextnutzung minimal (nur Asset-ID): 3
- Offline-Workflow (nicht erwartbar, da connectivity nicht im CONTEXT): 2
- Keine Nutzung des Kontexts (nur Asset-ID vorhanden): 2
- Offline-Workflow (spotty connectivity): 2
- Keine Kontextnutzung (nur Asset-ID vorhanden): 2
- Keine Offline-Workflow-Erwähnung (nicht erwartbar): 2
- Offline-Workflow nicht explizit erwähnt (spotty connectivity im Context): 2
- Kontext-Nutzung minimal (nur Asset-ID): 2
- Klare Stop-Condition für Beobachtungsphase fehlt: 1
- Kontextnutzung minimal (nur Asset-ID verwendet): 1
- Offline-Workflow nicht erwähnt (trotz connectivity=offline im CONTEXT): 1
- Kontextnutzung teilweise, aber device.* nicht explizit adressiert: 1
- Offline-Workflow nicht explizit erwähnt (trotz offline/low_battery im CONTEXT): 1
- Keine Anpassung an Umgebung/Wetter: 1
- Generische Schritte ohne Bezug zu 'intermittent': 1
- Unstrukturierter Kontext erschwert Parsing, aber gut verarbeitet: 1
- Explizite Erwähnung der Asset-ID (n4427359783) in Dokumentation: 1
- Halluzinationen: UVV, StVO, Netzbetreiber, Schaltuhr, Dämmerungsschalter ohne Kontext-Basis: 1
- Offline-Workflow nicht erwartbar, aber Gerätezustand ignoriert: 1
