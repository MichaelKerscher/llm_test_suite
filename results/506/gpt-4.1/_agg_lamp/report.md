# Aggregation Report (506/gpt-4.1) [lamp]
- judge_version filter: **judge_v1_1**
- Tests (latest runs): **270**
- Incidents with any deltas: **30**

## Mean scores by context level (snapshot)
### L0 (n=30)
- mean runtime: 8.339966666666667
- mean R/H/S/D/K: 3.566666666666667/3.7666666666666666/3.7666666666666666/4.033333333333333/2.533333333333333
- mean overall (avg R/H/S/D/K): 3.533333333333333
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.00, hallucination_suspected=0.03
### L2 (n=30)
- mean runtime: 11.633766666666666
- mean R/H/S/D/K: 4.933333333333334/4.9/4.933333333333334/5.0/4.466666666666667
- mean overall (avg R/H/S/D/K): 4.846666666666667
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.17, hallucination_suspected=0.00
### L2B (n=30)
- mean runtime: 11.266133333333332
- mean R/H/S/D/K: 4.966666666666667/4.966666666666667/4.966666666666667/4.966666666666667/5.0
- mean overall (avg R/H/S/D/K): 4.973333333333333
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.60, hallucination_suspected=0.00
### unknown (n=180)
- mean runtime: 11.184427777777778
- mean R/H/S/D/K: 4.7444444444444445/4.711111111111111/4.772222222222222/4.861111111111111/4.733333333333333
- mean overall (avg R/H/S/D/K): 4.764444444444445
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.39, hallucination_suspected=0.00

## Mean scores by strategy (snapshot)
### S0 (n=30)
- mean runtime: 8.339966666666667
- mean R/H/S/D/K: 3.566666666666667/3.7666666666666666/3.7666666666666666/4.033333333333333/2.533333333333333
- mean overall (avg R/H/S/D/K): 3.533333333333333
### S0_RAW (n=30)
- mean runtime: 11.277566666666667
- mean R/H/S/D/K: 4.6/4.566666666666666/4.733333333333333/4.866666666666666/4.533333333333333
- mean overall (avg R/H/S/D/K): 4.66
### S0_UNSTRUCTURED (n=30)
- mean runtime: 11.106066666666667
- mean R/H/S/D/K: 4.4/4.4/4.6/4.566666666666666/4.0
- mean overall (avg R/H/S/D/K): 4.3933333333333335
### S1 (n=30)
- mean runtime: 11.633766666666666
- mean R/H/S/D/K: 4.933333333333334/4.9/4.933333333333334/5.0/4.466666666666667
- mean overall (avg R/H/S/D/K): 4.846666666666667
### S2 (n=30)
- mean runtime: 11.266133333333332
- mean R/H/S/D/K: 4.966666666666667/4.966666666666667/4.966666666666667/4.966666666666667/5.0
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
- offline_workflow: 11
- Offline-Workflow (nicht erwartbar, da connectivity nicht im CONTEXT): 3
- Kontextnutzung minimal (nur Asset-ID): 3
- offline_workflow_explicit: 2
- Spezifische Stop-Conditions für Beobachtungsphase: 2
- Offline-Workflow (spotty connectivity im CONTEXT, aber nicht explizit erwähnt): 2
- Klare Stop-Condition für Beobachtungsphase: 1
- Konkrete Zeitangabe für Wiederholungsprüfung: 1
- Explizite Stop-Condition für Beobachtungsphase: 1
- Feuchtigkeitsflecken nicht erwähnt: 1
- Nebel/poor_visibility nicht berücksichtigt: 1
- Foto-Workflow nicht integriert: 1
- Offline-Workflow nicht nötig (online): 1
- Asset-ID/Mast-Nummer explizit erwähnen: 1
- Ticket-ID/Asset-ID explizit in Dokumentation: 1
- Asset-ID/OSM-ID explizit im Protokoll erwähnen: 1
- GPS-Koordinaten für Dokumentation nennen: 1
- Expliziter Offline-Workflow bei spotty connectivity: 1
- Offline-Workflow bei spotty connectivity: 1
- Explizite Stop-Conditions für Eskalation: 1
