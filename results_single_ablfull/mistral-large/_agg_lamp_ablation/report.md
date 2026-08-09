# Aggregation Report (mistral-large) [lamp]
- judge_version filter: **judge_v1_1_single_fullref**
- incident filter: **ablation**
- Tests (latest runs): **120**
- Incidents with any deltas: **0**

## Mean scores by context level (snapshot)
### unknown (n=120)
- mean runtime: 10.413658333333332
- mean R/H/S/D/K: 4.916666666666667/4.85/4.95/4.958333333333333/4.916666666666667
- mean overall (avg R/H/S/D/K): 4.918333333333334
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.57, hallucination_suspected=0.00

## Mean scores by strategy (snapshot)
### S2_ABL_NOASSET (n=30)
- mean runtime: 10.448033333333333
- mean R/H/S/D/K: 4.966666666666667/4.9/4.966666666666667/4.933333333333334/4.933333333333334
- mean overall (avg R/H/S/D/K): 4.9399999999999995
### S2_ABL_NODEV (n=30)
- mean runtime: 10.108133333333335
- mean R/H/S/D/K: 4.866666666666666/4.833333333333333/4.933333333333334/5.0/4.833333333333333
- mean overall (avg R/H/S/D/K): 4.8933333333333335
### S2_ABL_NOENV (n=30)
- mean runtime: 11.139666666666667
- mean R/H/S/D/K: 4.9/4.833333333333333/4.933333333333334/4.966666666666667/4.933333333333334
- mean overall (avg R/H/S/D/K): 4.913333333333333
### S2_ABL_NOINC (n=30)
- mean runtime: 9.9588
- mean R/H/S/D/K: 4.933333333333334/4.833333333333333/4.966666666666667/4.933333333333334/4.966666666666667
- mean overall (avg R/H/S/D/K): 4.926666666666667

## Top missing elements (max 20)
- Offline-Workflow für device_state=offline nicht erwähnt: 1
- Batteriestatus des Geräts nicht berücksichtigt: 1
- Explizite Erwähnung severity=medium: 1
- GPS-Koordinaten für Ticket: 1
- Offline-Workflow bei spotty connectivity nicht explizit erwähnt: 1
- Asset-ID (n4484173276) nicht explizit dokumentiert: 1
- Offline-Workflow explizit (bei spotty connectivity): 1
- Asset-ID/OSM-Referenz in Doku: 1
- Explizite Erwähnung der Korrosion/lockeren Bodenplatte aus Foto: 1
- Explizite Erwähnung Asset-ID/OSM-ID für Ticket: 1
- Stop-Conditions für Sichtprüfung könnten expliziter sein: 1
- Asset-ID (n4446442023) nicht explizit dokumentiert: 1
- GPS-Koordinaten nicht in Dokumentation erwähnt: 1
- Ticket-ID/Asset-ID explizit erwähnen: 1
- Explizite Berücksichtigung von Nebel/schlechter Sicht bei Absicherung: 1
- Wasserschaden-Hinweis aus photo_description nicht explizit adressiert: 1
- Schaltbox-Dichtung aus Foto nicht erwähnt: 1
- Explizite Erwähnung des Offline-Modus für Dokumentation: 1
