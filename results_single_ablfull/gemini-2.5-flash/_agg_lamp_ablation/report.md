# Aggregation Report (gemini-2.5-flash) [lamp]
- judge_version filter: **judge_v1_1_single_fullref**
- incident filter: **ablation**
- Tests (latest runs): **120**
- Incidents with any deltas: **0**

## Mean scores by context level (snapshot)
### unknown (n=120)
- mean runtime: 10.382225
- mean R/H/S/D/K: 4.933333333333334/4.866666666666666/4.925/4.958333333333333/4.891666666666667
- mean overall (avg R/H/S/D/K): 4.915
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.56, hallucination_suspected=0.00

## Mean scores by strategy (snapshot)
### S2_ABL_NOASSET (n=30)
- mean runtime: 10.933633333333335
- mean R/H/S/D/K: 4.933333333333334/4.833333333333333/4.9/4.966666666666667/4.933333333333334
- mean overall (avg R/H/S/D/K): 4.913333333333333
### S2_ABL_NODEV (n=30)
- mean runtime: 9.963966666666666
- mean R/H/S/D/K: 4.933333333333334/4.833333333333333/4.866666666666666/4.966666666666667/4.733333333333333
- mean overall (avg R/H/S/D/K): 4.866666666666666
### S2_ABL_NOENV (n=30)
- mean runtime: 10.491333333333333
- mean R/H/S/D/K: 4.9/4.866666666666666/4.933333333333334/4.933333333333334/4.933333333333334
- mean overall (avg R/H/S/D/K): 4.913333333333333
### S2_ABL_NOINC (n=30)
- mean runtime: 10.139966666666668
- mean R/H/S/D/K: 4.966666666666667/4.933333333333334/5.0/4.966666666666667/4.966666666666667
- mean overall (avg R/H/S/D/K): 4.966666666666667

## Top missing elements (max 20)
- Offline-Workflow für spotty connectivity: 2
- Offline-Workflow (device.connectivity=offline): 1
- Low-Battery-Hinweis (device_state=low_battery): 1
- Severity-angepasste Priorisierung (severity=low): 1
- Low-battery Hinweis für Gerät: 1
- Offline-Workflow (device.connectivity=offline nicht adressiert): 1
- Asset-ID/OSM-ID explizit im Protokoll: 1
- Asset-ID/OSM-Referenz explizit nennen: 1
- GPS-Koordinaten für Ticket: 1
- Explizite Erwähnung Asset-ID (n4939032525): 1
- GPS-Koordinaten in Dokumentation: 1
- Explizite Stop-Condition bei akuter Gefahr: 1
- Explizite Erwähnung der Nebel-/Sichtbedingungen bei Absicherung: 1
- Offline-Workflow explizit erwähnt: 1
- Explizite Stop-Conditions für Diagnose-Schritte: 1
