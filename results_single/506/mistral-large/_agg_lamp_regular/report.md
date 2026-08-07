# Aggregation Report (mistral-large) [lamp]
- judge_version filter: **judge_v1_1_single**
- incident filter: **regular**
- Tests (latest runs): **150**
- Incidents with any deltas: **30**

## Mean scores by context level (snapshot)
### L0 (n=30)
- mean runtime: 8.2622
- mean R/H/S/D/K: 4.633333333333334/4.866666666666666/4.9/4.966666666666667/3.6
- mean overall (avg R/H/S/D/K): 4.593333333333334
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.00, hallucination_suspected=0.03
### L2 (n=30)
- mean runtime: 10.5048
- mean R/H/S/D/K: 4.966666666666667/4.9/5.0/5.0/4.8
- mean overall (avg R/H/S/D/K): 4.933333333333334
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.53, hallucination_suspected=0.00
### L2B (n=30)
- mean runtime: 12.218766666666665
- mean R/H/S/D/K: 4.966666666666667/4.966666666666667/5.0/4.866666666666666/4.966666666666667
- mean overall (avg R/H/S/D/K): 4.953333333333333
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.63, hallucination_suspected=0.00
### unknown (n=60)
- mean runtime: 10.625366666666668
- mean R/H/S/D/K: 4.95/4.916666666666667/4.95/5.0/4.966666666666667
- mean overall (avg R/H/S/D/K): 4.956666666666666
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.45, hallucination_suspected=0.00

## Mean scores by strategy (snapshot)
### S0 (n=30)
- mean runtime: 8.2622
- mean R/H/S/D/K: 4.633333333333334/4.866666666666666/4.9/4.966666666666667/3.6
- mean overall (avg R/H/S/D/K): 4.593333333333334
### S0_RAW (n=30)
- mean runtime: 10.2743
- mean R/H/S/D/K: 4.966666666666667/4.966666666666667/4.933333333333334/5.0/5.0
- mean overall (avg R/H/S/D/K): 4.973333333333333
### S0_UNSTRUCTURED (n=30)
- mean runtime: 10.976433333333334
- mean R/H/S/D/K: 4.933333333333334/4.866666666666666/4.966666666666667/5.0/4.933333333333334
- mean overall (avg R/H/S/D/K): 4.9399999999999995
### S1 (n=30)
- mean runtime: 10.5048
- mean R/H/S/D/K: 4.966666666666667/4.9/5.0/5.0/4.8
- mean overall (avg R/H/S/D/K): 4.933333333333334
### S2 (n=30)
- mean runtime: 12.218766666666665
- mean R/H/S/D/K: 4.966666666666667/4.966666666666667/5.0/4.866666666666666/4.966666666666667
- mean overall (avg R/H/S/D/K): 4.953333333333333

## Top missing elements (max 20)
- Keine Nutzung der Asset-ID zur Kontextabfrage: 1
- Keine Nachfrage nach fehlendem Kontext (Lampentyp, Standort): 1
- Konkrete Stop-Conditions für Abbruch der Diagnose: 1
- Asset-Typ unbekannt, aber Modell spekuliert stark (Ampel/Straßenlampe): 1
- Keine Nachfrage nach Asset-Typ oder Domain: 1
- Kontext enthält nur OSM-ID, keine weiteren Infos: 1
- Asset-ID (n4427359783) nicht explizit dokumentiert: 1
- Keine Nutzung des CONTEXT (asset_osm wird nur wiederholt, nicht genutzt): 1
- Keine Nachfrage nach fehlenden Kontextinformationen (Severity, Traffic, Connectivity): 1
- Asset-ID/OSM-Referenz in Dokumentation: 1
- Keine explizite Nutzung der Asset-ID aus CONTEXT für spezifische Abfragen: 1
- Asset-ID/OSM-Referenz explizit im Ticket: 1
- Asset-Typ aus OSM-Daten ermitteln: 1
- Spezifische Prüfschritte je nach Asset-Typ: 1
- Explizite Priorisierung auf intermittent-spezifische Diagnose: 1
- Hinweis auf Beobachtungsdauer bei zeitweisen Fehlern: 1
- Offline-Workflow nicht erwähnt (aber auch nicht erwartbar aus Context): 1
- Keine explizite Stop-Condition für Abbruch der Diagnose: 1
- Explizite Erwähnung des Offline-Workflows bei spotty connectivity: 1
- Kontext-Nutzung: Keine Informationen zu Ort/GPS, Verkehrslage oder Konnektivität aus CONTEXT abgeleitet: 1
