# Aggregation Report (mistral-large) [lamp]
- judge_version filter: **judge_v1_1_single**
- incident filter: **ablation**
- Tests (latest runs): **120**
- Incidents with any deltas: **0**

## Mean scores by context level (snapshot)
### unknown (n=120)
- mean runtime: 10.413658333333332
- mean R/H/S/D/K: 4.908333333333333/4.891666666666667/4.966666666666667/4.958333333333333/4.916666666666667
- mean overall (avg R/H/S/D/K): 4.928333333333333
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.46, hallucination_suspected=0.00

## Mean scores by strategy (snapshot)
### S2_ABL_NOASSET (n=30)
- mean runtime: 10.448033333333333
- mean R/H/S/D/K: 4.966666666666667/4.933333333333334/5.0/4.933333333333334/4.866666666666666
- mean overall (avg R/H/S/D/K): 4.9399999999999995
### S2_ABL_NODEV (n=30)
- mean runtime: 10.108133333333335
- mean R/H/S/D/K: 4.9/4.833333333333333/4.966666666666667/4.966666666666667/4.933333333333334
- mean overall (avg R/H/S/D/K): 4.92
### S2_ABL_NOENV (n=30)
- mean runtime: 11.139666666666667
- mean R/H/S/D/K: 4.866666666666666/4.866666666666666/4.933333333333334/4.966666666666667/4.9
- mean overall (avg R/H/S/D/K): 4.906666666666666
### S2_ABL_NOINC (n=30)
- mean runtime: 9.9588
- mean R/H/S/D/K: 4.9/4.933333333333334/4.966666666666667/4.966666666666667/4.966666666666667
- mean overall (avg R/H/S/D/K): 4.946666666666667

## Top missing elements (max 20)
- Asset-ID (n13293341689) nicht explizit dokumentiert: 2
- Asset-ID/Mastnummer explizit als Pflichtfeld: 1
- GPS-Koordinaten nicht als Dokumentationspunkt erwähnt: 1
- Explizite Erwähnung des Low-Power-Modus als Constraint für Dokumentation: 1
- Ticket-ID oder Asset-ID in Dokumentations-Checkliste: 1
- Asset-ID (n4446442023) nicht dokumentiert: 1
- GPS-Koordinaten nicht erwähnt: 1
- Ticket-ID/Asset-ID explizit erwähnen: 1
- Low-Power-Mode des Geräts berücksichtigen: 1
- Explizite Erwähnung des low_battery Status als Handlungseinschränkung: 1
- Asset-ID/OSM-Referenz explizit erwähnen: 1
- GPS-Koordinaten in Dokumentation: 1
