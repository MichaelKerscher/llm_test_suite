# Aggregation Report (506\gpt-4.1) [combined]
- judge_version filter: **judge_v1_1**
- Tests (latest runs): **300**
- Incidents with any deltas: **60**

## Mean scores by context level (snapshot)
### L0 (n=60)
- mean runtime: 5.361833333333333
- mean R/H/S/D/K: 3.65/3.7333333333333334/3.5166666666666666/4.0/2.683333333333333
- mean overall (avg R/H/S/D/K): 3.5166666666666666
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.00, hallucination_suspected=0.10
### L2 (n=60)
- mean runtime: 7.1508
- mean R/H/S/D/K: 4.8/4.633333333333334/4.533333333333333/4.7/4.116666666666666
- mean overall (avg R/H/S/D/K): 4.556666666666667
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.13, hallucination_suspected=0.05
### L2B (n=60)
- mean runtime: 6.752966666666667
- mean R/H/S/D/K: 4.9/4.866666666666666/4.633333333333334/4.866666666666666/4.966666666666667
- mean overall (avg R/H/S/D/K): 4.846666666666667
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.63, hallucination_suspected=0.00
### unknown (n=120)
- mean runtime: 11.180733333333334
- mean R/H/S/D/K: 4.866666666666666/4.825/4.825/4.933333333333334/4.966666666666667
- mean overall (avg R/H/S/D/K): 4.883333333333334
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.46, hallucination_suspected=0.00

## Mean scores by strategy (snapshot)
### S0 (n=60)
- mean runtime: 5.361833333333333
- mean R/H/S/D/K: 3.65/3.7333333333333334/3.5166666666666666/4.0/2.683333333333333
- mean overall (avg R/H/S/D/K): 3.5166666666666666
### S1 (n=60)
- mean runtime: 7.1508
- mean R/H/S/D/K: 4.8/4.633333333333334/4.533333333333333/4.7/4.116666666666666
- mean overall (avg R/H/S/D/K): 4.556666666666667
### S2 (n=60)
- mean runtime: 6.752966666666667
- mean R/H/S/D/K: 4.9/4.866666666666666/4.633333333333334/4.866666666666666/4.966666666666667
- mean overall (avg R/H/S/D/K): 4.846666666666667
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
- Kontextnutzung minimal (nur Asset-ID): 5
- Offline-Workflow bei spotty connectivity: 3
- Kein expliziter Offline-Workflow trotz connectivity=spotty: 2
- Keine Nutzung der Asset-ID im Kontext: 2
- Spezifische Stop-Conditions für Beobachtungsphase: 2
- Kontextnutzung minimal (nur Asset-ID vorhanden): 2
- Offline-Workflow bei spotty connectivity nicht explizit erwähnt: 2
- Klare Stop-Condition für Beobachtungsphase: 1
- Konkrete Zeitangabe für Wiederholungsprüfung: 1
- Explizite Stop-Condition für Beobachtungsphase: 1
- Offline-Workflow (Gerät offline): 1
- Klarstellung: device_state betrifft Techniker-Gerät, nicht Asset: 1
- Keine Nutzung der Asset-ID im Workflow: 1
- Keine Berücksichtigung des intermittent-Charakters: 1
- Generische Ampel-Erwähnung ohne Kontext-Signal: 1
- Keine explizite Stop-Condition bei Gefahr: 1
- Asset-ID/Mast-Nummer explizit erwähnen: 1
- Ticket-ID/Asset-ID explizit in Dokumentation: 1
- Asset-ID/OSM-ID explizit im Protokoll erwähnen: 1
- GPS-Koordinaten für Dokumentation nennen: 1
