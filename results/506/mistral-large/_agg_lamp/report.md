# Aggregation Report (506/mistral-large) [lamp]
- judge_version filter: **judge_v1_1**
- Tests (latest runs): **270**
- Incidents with any deltas: **30**

## Mean scores by context level (snapshot)
### L0 (n=30)
- mean runtime: 7.5906666666666665
- mean R/H/S/D/K: 3.5/3.8/3.7666666666666666/4.033333333333333/2.433333333333333
- mean overall (avg R/H/S/D/K): 3.506666666666667
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.00, hallucination_suspected=0.03
### L2 (n=30)
- mean runtime: 10.399266666666668
- mean R/H/S/D/K: 4.8/4.733333333333333/4.7/4.766666666666667/4.266666666666667
- mean overall (avg R/H/S/D/K): 4.653333333333333
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.10, hallucination_suspected=0.00
### L2B (n=30)
- mean runtime: 11.019633333333333
- mean R/H/S/D/K: 5.0/4.966666666666667/4.9/5.0/5.0
- mean overall (avg R/H/S/D/K): 4.973333333333333
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.60, hallucination_suspected=0.00
### unknown (n=180)
- mean runtime: 9.350116666666667
- mean R/H/S/D/K: 4.711111111111111/4.733333333333333/4.727777777777778/4.866666666666666/4.727777777777778
- mean overall (avg R/H/S/D/K): 4.753333333333334
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.42, hallucination_suspected=0.00

## Mean scores by strategy (snapshot)
### S0 (n=30)
- mean runtime: 7.5906666666666665
- mean R/H/S/D/K: 3.5/3.8/3.7666666666666666/4.033333333333333/2.433333333333333
- mean overall (avg R/H/S/D/K): 3.506666666666667
### S0_RAW (n=30)
- mean runtime: 9.408999999999999
- mean R/H/S/D/K: 4.6/4.633333333333334/4.6/4.9/4.633333333333334
- mean overall (avg R/H/S/D/K): 4.673333333333333
### S0_UNSTRUCTURED (n=30)
- mean runtime: 9.9991
- mean R/H/S/D/K: 4.266666666666667/4.333333333333333/4.4/4.5/3.8666666666666667
- mean overall (avg R/H/S/D/K): 4.2733333333333325
### S1 (n=30)
- mean runtime: 10.399266666666668
- mean R/H/S/D/K: 4.8/4.733333333333333/4.7/4.766666666666667/4.266666666666667
- mean overall (avg R/H/S/D/K): 4.653333333333333
### S2 (n=30)
- mean runtime: 11.019633333333333
- mean R/H/S/D/K: 5.0/4.966666666666667/4.9/5.0/5.0
- mean overall (avg R/H/S/D/K): 4.973333333333333
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
- Keine Nutzung der Asset-ID im Kontext: 6
- offline_workflow: 5
- Offline-Workflow (nicht erwartbar, da connectivity nicht im CONTEXT): 3
- Offline-Workflow nicht explizit trotz spotty connectivity: 2
- offline_workflow_explicit: 2
- Kein expliziter Offline-Workflow trotz 'spotty' Konnektivität: 2
- Expliziter Offline-Workflow (offline/low_battery im Context): 2
- Offline-Workflow nicht explizit erwähnt (spotty connectivity im CONTEXT): 2
- Offline-Workflow bei spotty connectivity: 2
- Offline-Workflow (spotty connectivity + low_battery im Kontext): 2
- Klare Stop-Condition für Beobachtungsphase fehlt: 1
- Kein Bezug zu Feuchtigkeitsflecken (nicht im CONTEXT): 1
- Keine Nutzung von Koordinaten/Name (nicht im CONTEXT): 1
- Keine Erwähnung von Nebel/poor_visibility (nicht im CONTEXT): 1
- Explizite Erwähnung der Asset-ID (n4427359783) in Dokumentation: 1
- Offline-Workflow nicht erwartbar (connectivity nicht im CONTEXT): 1
- Kontext minimal genutzt (nur Asset-ID): 1
- Offline-Workflow nicht explizit erwähnt trotz 'spotty' im CONTEXT: 1
- Keine Anpassung an tatsächlich verfügbare Kontextdaten: 1
- Generische Antwort ohne Bezug zu minimalen Kontextinformationen: 1
