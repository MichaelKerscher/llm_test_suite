# Aggregation Report (gpt-4.1) [lamp]
- judge_version filter: **judge_v1_1_single**
- incident filter: **ablation**
- Tests (latest runs): **120**
- Incidents with any deltas: **0**

## Mean scores by context level (snapshot)
### unknown (n=120)
- mean runtime: 10.138708333333334
- mean R/H/S/D/K: 4.908333333333333/4.925/4.941666666666666/4.983333333333333/4.958333333333333
- mean overall (avg R/H/S/D/K): 4.943333333333333
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.46, hallucination_suspected=0.00

## Mean scores by strategy (snapshot)
### S2_ABL_NOASSET (n=30)
- mean runtime: 10.225933333333334
- mean R/H/S/D/K: 4.833333333333333/4.9/4.9/5.0/4.9
- mean overall (avg R/H/S/D/K): 4.906666666666666
### S2_ABL_NODEV (n=30)
- mean runtime: 9.696033333333334
- mean R/H/S/D/K: 5.0/4.933333333333334/4.933333333333334/5.0/5.0
- mean overall (avg R/H/S/D/K): 4.973333333333333
### S2_ABL_NOENV (n=30)
- mean runtime: 10.978
- mean R/H/S/D/K: 4.9/4.9/4.933333333333334/4.933333333333334/4.966666666666667
- mean overall (avg R/H/S/D/K): 4.926666666666667
### S2_ABL_NOINC (n=30)
- mean runtime: 9.654866666666667
- mean R/H/S/D/K: 4.9/4.966666666666667/5.0/5.0/4.966666666666667
- mean overall (avg R/H/S/D/K): 4.966666666666667

## Top missing elements (max 20)
- Asset-ID explizit in Dokumentation erwähnen: 1
- Explizite Stop-Conditions für Abbruch der Diagnose: 1
- Klarere Priorisierung der Diagnoseschritte: 1
- Explizite Erwähnung des vorhandenen Fotos aus der Meldung: 1
- Hinweis auf low_power_mode des Geräts (Akku-Management): 1
- Asset-ID (n12520351647) nicht explizit in Dokumentation erwähnt: 1
- Asset-ID (n4483691318) nicht explizit in Dokumentation erwähnt: 1
- Konkrete Stop-Bedingung für Abbruch bei Eigengefährdung: 1
- Asset-ID (n5718630490) nicht explizit in Dokumentation erwähnt: 1
- GPS-Koordinaten nicht als Dokumentationspunkt genannt: 1
