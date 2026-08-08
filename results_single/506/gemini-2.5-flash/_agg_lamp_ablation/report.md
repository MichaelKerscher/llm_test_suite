# Aggregation Report (gemini-2.5-flash) [lamp]
- judge_version filter: **judge_v1_1_single**
- incident filter: **ablation**
- Tests (latest runs): **120**
- Incidents with any deltas: **0**

## Mean scores by context level (snapshot)
### unknown (n=120)
- mean runtime: 10.382225
- mean R/H/S/D/K: 4.9/4.891666666666667/4.966666666666667/4.983333333333333/4.95
- mean overall (avg R/H/S/D/K): 4.9383333333333335
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.47, hallucination_suspected=0.00

## Mean scores by strategy (snapshot)
### S2_ABL_NOASSET (n=30)
- mean runtime: 10.933633333333335
- mean R/H/S/D/K: 4.9/4.8/4.966666666666667/4.933333333333334/4.9
- mean overall (avg R/H/S/D/K): 4.9
### S2_ABL_NODEV (n=30)
- mean runtime: 9.963966666666666
- mean R/H/S/D/K: 4.933333333333334/4.933333333333334/4.9/5.0/4.966666666666667
- mean overall (avg R/H/S/D/K): 4.946666666666667
### S2_ABL_NOENV (n=30)
- mean runtime: 10.491333333333333
- mean R/H/S/D/K: 4.866666666666666/4.866666666666666/5.0/5.0/4.933333333333334
- mean overall (avg R/H/S/D/K): 4.933333333333334
### S2_ABL_NOINC (n=30)
- mean runtime: 10.139966666666668
- mean R/H/S/D/K: 4.9/4.966666666666667/5.0/5.0/5.0
- mean overall (avg R/H/S/D/K): 4.973333333333333

## Top missing elements (max 20)
- Spezifische Trigger für Eskalation bei intermittent faults: 1
- Zeitfenster für Beobachtung/Monitoring: 1
- Explizite Erwähnung severity=medium im Priorisierungskontext: 1
- Hinweis auf Ticket-ID/Asset-ID in Dokumentation: 1
- Keine explizite Priorisierung zwischen Einzelausfall vs. Netzausfall-Prüfung: 1
- Keine klare Stop-Condition für Vor-Ort-Diagnose: 1
- Spezifische Stop-Conditions für Beobachtungsphase: 1
- Priorisierung zwischen Diagnose-Schritten: 1
- Asset-ID/Standort-Koordinaten explizit erwähnen: 1
