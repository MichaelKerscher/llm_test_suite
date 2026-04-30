# Aggregation Report (506/gpt-4.1) [lamp]
- judge_version filter: **judge_v1_1**
- Tests (latest runs): **270**
- Incidents with any deltas: **30**

## Mean scores by context level (snapshot)
### L0 (n=30)
- mean runtime: 3.797433333333333
- mean R/H/S/D/K: 3.433333333333333/3.5/3.1/3.8/2.6333333333333333
- mean overall (avg R/H/S/D/K): 3.2933333333333334
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.00, hallucination_suspected=0.07
### L2 (n=30)
- mean runtime: 4.447533333333333
- mean R/H/S/D/K: 4.633333333333334/4.366666666666666/4.2/4.4/3.566666666666667
- mean overall (avg R/H/S/D/K): 4.233333333333333
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.07, hallucination_suspected=0.10
### L2B (n=30)
- mean runtime: 4.139466666666666
- mean R/H/S/D/K: 4.833333333333333/4.766666666666667/4.366666666666666/4.8/4.966666666666667
- mean overall (avg R/H/S/D/K): 4.746666666666667
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.70, hallucination_suspected=0.00
### unknown (n=180)
- mean runtime: 10.881655555555556
- mean R/H/S/D/K: 4.894444444444445/4.855555555555555/4.861111111111111/4.944444444444445/4.966666666666667
- mean overall (avg R/H/S/D/K): 4.904444444444445
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.44, hallucination_suspected=0.00

## Mean scores by strategy (snapshot)
### S0 (n=30)
- mean runtime: 3.797433333333333
- mean R/H/S/D/K: 3.433333333333333/3.5/3.1/3.8/2.6333333333333333
- mean overall (avg R/H/S/D/K): 3.2933333333333334
### S0_RAW (n=30)
- mean runtime: 10.051799999999998
- mean R/H/S/D/K: 4.966666666666667/4.933333333333334/4.933333333333334/4.966666666666667/5.0
- mean overall (avg R/H/S/D/K): 4.96
### S0_UNSTRUCTURED (n=30)
- mean runtime: 10.5152
- mean R/H/S/D/K: 4.933333333333334/4.9/4.933333333333334/4.966666666666667/4.933333333333334
- mean overall (avg R/H/S/D/K): 4.933333333333334
### S1 (n=30)
- mean runtime: 4.447533333333333
- mean R/H/S/D/K: 4.633333333333334/4.366666666666666/4.2/4.4/3.566666666666667
- mean overall (avg R/H/S/D/K): 4.233333333333333
### S2 (n=30)
- mean runtime: 4.139466666666666
- mean R/H/S/D/K: 4.833333333333333/4.766666666666667/4.366666666666666/4.8/4.966666666666667
- mean overall (avg R/H/S/D/K): 4.746666666666667
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
- Spezifische Stop-Conditions für Beobachtungsphase: 3
- Offline-Workflow bei spotty connectivity: 3
- Kein expliziter Offline-Workflow trotz connectivity=spotty: 2
- Keine Nutzung der Asset-ID im Kontext: 2
- Kontextnutzung minimal (nur Asset-ID): 2
- Klare Stop-Condition für Beobachtungsphase: 1
- Konkrete Zeitangabe für Wiederholungsprüfung: 1
- Explizite Stop-Condition für Beobachtungsphase: 1
- Offline-Workflow (Gerät offline): 1
- Klarstellung: device_state betrifft Techniker-Gerät, nicht Asset: 1
- Konkrete Stop-Condition für Langzeitbeobachtung fehlt: 1
- Keine Nutzung der Asset-ID im Workflow: 1
- Keine Berücksichtigung des intermittent-Charakters: 1
- Generische Ampel-Erwähnung ohne Kontext-Signal: 1
- Keine explizite Stop-Condition bei Gefahr: 1
- Asset-ID/Mast-Nummer explizit erwähnen: 1
- Ticket-ID/Asset-ID explizit in Dokumentation: 1
- Asset-ID/OSM-ID explizit im Protokoll erwähnen: 1
- GPS-Koordinaten für Dokumentation nennen: 1
- Kontext-Nutzung minimal (nur Asset-ID verwendet): 1
