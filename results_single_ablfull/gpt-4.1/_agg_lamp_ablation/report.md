# Aggregation Report (gpt-4.1) [lamp]
- judge_version filter: **judge_v1_1_single_fullref**
- incident filter: **ablation**
- Tests (latest runs): **120**
- Incidents with any deltas: **0**

## Mean scores by context level (snapshot)
### unknown (n=120)
- mean runtime: 10.138708333333334
- mean R/H/S/D/K: 4.9/4.9/4.958333333333333/4.983333333333333/4.933333333333334
- mean overall (avg R/H/S/D/K): 4.9350000000000005
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.57, hallucination_suspected=0.00

## Mean scores by strategy (snapshot)
### S2_ABL_NOASSET (n=30)
- mean runtime: 10.225933333333334
- mean R/H/S/D/K: 4.9/4.933333333333334/4.933333333333334/4.966666666666667/4.933333333333334
- mean overall (avg R/H/S/D/K): 4.933333333333334
### S2_ABL_NODEV (n=30)
- mean runtime: 9.696033333333334
- mean R/H/S/D/K: 4.966666666666667/4.9/4.966666666666667/5.0/4.966666666666667
- mean overall (avg R/H/S/D/K): 4.96
### S2_ABL_NOENV (n=30)
- mean runtime: 10.978
- mean R/H/S/D/K: 4.8/4.833333333333333/4.933333333333334/4.966666666666667/4.833333333333333
- mean overall (avg R/H/S/D/K): 4.873333333333333
### S2_ABL_NOINC (n=30)
- mean runtime: 9.654866666666667
- mean R/H/S/D/K: 4.933333333333334/4.933333333333334/5.0/5.0/5.0
- mean overall (avg R/H/S/D/K): 4.973333333333333

## Top missing elements (max 20)
- Expliziter Offline-Workflow für device_state=offline: 1
- Asset-ID/OSM-ID explizit erwähnen: 1
- Explizite Erwähnung der Nebel-Bedingungen (fog/poor_visibility) bei Sicherheitsmaßnahmen: 1
- Offline-Workflow für spotty connectivity: 1
- Explizite Nutzung der GPS-Koordinaten aus CONTEXT: 1
- Erwähnung des severity=medium für Priorisierung: 1
- Priorisierung bei severity=medium könnte expliziter sein: 1
- Explizite Erwähnung severity=medium und fault_type=outage aus Context: 1
- Nutzung der konkreten Asset-ID (n4446442023) für Dokumentation: 1
- Explizite Erwähnung severity=medium und traffic_exposure=low: 1
- Nutzung photo_available=true als Vorab-Info: 1
- Regen/poor_visibility als Safety-Faktor: 1
- Nebel/schlechte Sicht explizit in Sicherheitsmaßnahmen erwähnt: 1
