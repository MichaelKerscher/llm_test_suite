# Aggregation Report (506/gpt-4.1) [lamp]
- judge_version filter: **judge_v1_1**
- Tests (latest runs): **270**
- Incidents with any deltas: **30**

## Mean scores by context level (snapshot)
### L0 (n=30)
- mean runtime: 9.2704
- mean R/H/S/D/K: 3.5/3.8/3.7666666666666666/3.933333333333333/2.433333333333333
- mean overall (avg R/H/S/D/K): 3.4866666666666664
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.00, hallucination_suspected=0.17
### L2 (n=30)
- mean runtime: 11.3176
- mean R/H/S/D/K: 4.866666666666666/4.833333333333333/4.833333333333333/4.933333333333334/4.533333333333333
- mean overall (avg R/H/S/D/K): 4.8
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.10, hallucination_suspected=0.00
### L2B (n=30)
- mean runtime: 11.486066666666666
- mean R/H/S/D/K: 4.966666666666667/4.966666666666667/4.933333333333334/5.0/5.0
- mean overall (avg R/H/S/D/K): 4.973333333333333
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.60, hallucination_suspected=0.00
### unknown (n=180)
- mean runtime: 11.505133333333333
- mean R/H/S/D/K: 4.722222222222222/4.694444444444445/4.772222222222222/4.8277777777777775/4.694444444444445
- mean overall (avg R/H/S/D/K): 4.742222222222223
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.39, hallucination_suspected=0.01

## Mean scores by strategy (snapshot)
### S0 (n=30)
- mean runtime: 9.2704
- mean R/H/S/D/K: 3.5/3.8/3.7666666666666666/3.933333333333333/2.433333333333333
- mean overall (avg R/H/S/D/K): 3.4866666666666664
### S0_RAW (n=30)
- mean runtime: 11.413933333333334
- mean R/H/S/D/K: 4.533333333333333/4.5/4.666666666666667/4.7/4.4
- mean overall (avg R/H/S/D/K): 4.5600000000000005
### S0_UNSTRUCTURED (n=30)
- mean runtime: 12.893933333333333
- mean R/H/S/D/K: 4.333333333333333/4.366666666666666/4.666666666666667/4.533333333333333/3.9
- mean overall (avg R/H/S/D/K): 4.36
### S1 (n=30)
- mean runtime: 11.3176
- mean R/H/S/D/K: 4.866666666666666/4.833333333333333/4.833333333333333/4.933333333333334/4.533333333333333
- mean overall (avg R/H/S/D/K): 4.8
### S2 (n=30)
- mean runtime: 11.486066666666666
- mean R/H/S/D/K: 4.966666666666667/4.966666666666667/4.933333333333334/5.0/5.0
- mean overall (avg R/H/S/D/K): 4.973333333333333
### S2_ABL_NOASSET (n=30)
- mean runtime: 10.9962
- mean R/H/S/D/K: 4.9/4.933333333333334/4.933333333333334/4.9/4.966666666666667
- mean overall (avg R/H/S/D/K): 4.926666666666667
### S2_ABL_NODEV (n=30)
- mean runtime: 10.410633333333333
- mean R/H/S/D/K: 4.933333333333334/4.8/4.766666666666667/4.933333333333334/4.966666666666667
- mean overall (avg R/H/S/D/K): 4.88
### S2_ABL_NOENV (n=30)
- mean runtime: 11.9838
- mean R/H/S/D/K: 4.8/4.666666666666667/4.7/4.9/4.966666666666667
- mean overall (avg R/H/S/D/K): 4.806666666666667
### S2_ABL_NOINC (n=30)
- mean runtime: 11.3323
- mean R/H/S/D/K: 4.833333333333333/4.9/4.9/5.0/4.966666666666667
- mean overall (avg R/H/S/D/K): 4.92

## Top missing elements (max 20)
- offline_workflow: 4
- Kontextnutzung minimal (nur Asset-ID): 3
- Offline-Workflow (nicht erwartbar, da connectivity nicht im CONTEXT): 3
- Offline-Workflow (spotty connectivity erwähnt, aber kein expliziter Offline-Workflow): 3
- Offline-Workflow nicht explizit erwähnt: 2
- Keine Nutzung des Kontexts (nur Asset-ID vorhanden): 2
- Offline-Workflow (erwartbar bei connectivity=spotty, aber nicht explizit erwähnt): 2
- offline_workflow_explicit: 2
- Spezifische Stop-Conditions für Beobachtungsphase: 2
- Offline-Workflow bei spotty connectivity: 2
- Offline-Workflow nicht explizit erwähnt (spotty connectivity im CONTEXT): 2
- Klare Stop-Condition für Beobachtungsphase: 1
- Konkrete Zeitangabe für Wiederholungsprüfung: 1
- Explizite Stop-Condition für Beobachtungsphase: 1
- Offline-Workflow (Gerät offline nicht erwähnt im CONTEXT): 1
- Offline-Workflow nicht explizit erwähnt trotz 'offline' im CONTEXT: 1
- Keine Anpassung an Umgebung/Wetter/Verkehr: 1
- Keine Erwähnung intermittierender Fehler: 1
- Hinweis auf Zeitinkonsistenz (14:56 Uhr vs. 'night') ist spekulativ: 1
- Asset-ID/Mast-Nummer explizit erwähnen: 1
