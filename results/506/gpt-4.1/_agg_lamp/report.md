# Aggregation Report (506/gpt-4.1) [lamp]
- judge_version filter: **judge_v1_1**
- Tests (latest runs): **270**
- Incidents with any deltas: **30**

## Mean scores by context level (snapshot)
### L0 (n=30)
- mean runtime: 8.8376
- mean R/H/S/D/K: 3.6/3.7666666666666666/3.7666666666666666/4.1/2.566666666666667
- mean overall (avg R/H/S/D/K): 3.56
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.00, hallucination_suspected=0.07
### L2 (n=30)
- mean runtime: 11.385133333333332
- mean R/H/S/D/K: 4.9/4.866666666666666/4.866666666666666/4.966666666666667/4.633333333333334
- mean overall (avg R/H/S/D/K): 4.846666666666667
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.17, hallucination_suspected=0.00
### L2B (n=30)
- mean runtime: 11.851066666666666
- mean R/H/S/D/K: 5.0/5.0/4.933333333333334/5.0/5.0
- mean overall (avg R/H/S/D/K): 4.986666666666666
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.63, hallucination_suspected=0.00
### unknown (n=180)
- mean runtime: 11.147133333333333
- mean R/H/S/D/K: 4.727777777777778/4.705555555555556/4.7555555555555555/4.855555555555555/4.666666666666667
- mean overall (avg R/H/S/D/K): 4.742222222222223
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.38, hallucination_suspected=0.01

## Mean scores by strategy (snapshot)
### S0 (n=30)
- mean runtime: 8.8376
- mean R/H/S/D/K: 3.6/3.7666666666666666/3.7666666666666666/4.1/2.566666666666667
- mean overall (avg R/H/S/D/K): 3.56
### S0_RAW (n=30)
- mean runtime: 10.6766
- mean R/H/S/D/K: 4.566666666666666/4.533333333333333/4.733333333333333/4.866666666666666/4.433333333333334
- mean overall (avg R/H/S/D/K): 4.626666666666667
### S0_UNSTRUCTURED (n=30)
- mean runtime: 11.483266666666667
- mean R/H/S/D/K: 4.333333333333333/4.4/4.5/4.533333333333333/3.7
- mean overall (avg R/H/S/D/K): 4.293333333333334
### S1 (n=30)
- mean runtime: 11.385133333333332
- mean R/H/S/D/K: 4.9/4.866666666666666/4.866666666666666/4.966666666666667/4.633333333333334
- mean overall (avg R/H/S/D/K): 4.846666666666667
### S2 (n=30)
- mean runtime: 11.851066666666666
- mean R/H/S/D/K: 5.0/5.0/4.933333333333334/5.0/5.0
- mean overall (avg R/H/S/D/K): 4.986666666666666
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
- offline_workflow: 8
- Offline-Workflow (Gerät offline nicht erwähnt): 2
- Offline-Workflow bei spotty connectivity: 2
- Spezifische Stop-Conditions für Beobachtungsphase: 2
- Keine Nutzung des Kontexts (nur Asset-ID vorhanden): 2
- Klare Stop-Condition für Beobachtungsphase: 1
- Konkrete Zeitangabe für Wiederholungsprüfung: 1
- Explizite Stop-Condition für Beobachtungsphase: 1
- Kontextnutzung schwach (nur Asset-ID genutzt): 1
- Offline-Workflow nicht explizit (trotz offline-Status): 1
- Kein Bezug zu Feuchtigkeitsflecken (nicht im Kontext): 1
- Keine Nutzung von Standort/Koordinaten (nicht im Kontext): 1
- Keine Erwähnung von Nebel/Sicht (nicht im Kontext): 1
- Unstrukturierter Kontext erschwert Parsing, aber gut genutzt: 1
- Asset-ID/Mast-Nummer explizit erwähnen: 1
- Ticket-ID/Asset-ID explizit in Dokumentation: 1
- Asset-ID/OSM-ID explizit im Protokoll erwähnen: 1
- GPS-Koordinaten für Dokumentation nennen: 1
- Offline-Workflow explizit (spotty+low_battery): 1
- Offline-Workflow explizit (spotty connectivity + low_battery): 1
