# Aggregation Report (gpt-4.1) [lamp]
- judge_version filter: **judge_v1_1_single**
- incident filter: **regular**
- Tests (latest runs): **150**
- Incidents with any deltas: **30**

## Mean scores by context level (snapshot)
### L0 (n=30)
- mean runtime: 7.8777333333333335
- mean R/H/S/D/K: 4.6/4.766666666666667/4.833333333333333/4.9/3.533333333333333
- mean overall (avg R/H/S/D/K): 4.526666666666667
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.00, hallucination_suspected=0.07
### L2 (n=30)
- mean runtime: 9.484833333333334
- mean R/H/S/D/K: 5.0/4.933333333333334/4.933333333333334/5.0/4.9
- mean overall (avg R/H/S/D/K): 4.953333333333333
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.50, hallucination_suspected=0.00
### L2B (n=30)
- mean runtime: 11.0511
- mean R/H/S/D/K: 4.966666666666667/4.966666666666667/5.0/4.966666666666667/4.966666666666667
- mean overall (avg R/H/S/D/K): 4.973333333333333
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.63, hallucination_suspected=0.00
### unknown (n=60)
- mean runtime: 9.566633333333334
- mean R/H/S/D/K: 4.966666666666667/4.933333333333334/4.983333333333333/4.983333333333333/4.9
- mean overall (avg R/H/S/D/K): 4.953333333333333
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.42, hallucination_suspected=0.00

## Mean scores by strategy (snapshot)
### S0 (n=30)
- mean runtime: 7.8777333333333335
- mean R/H/S/D/K: 4.6/4.766666666666667/4.833333333333333/4.9/3.533333333333333
- mean overall (avg R/H/S/D/K): 4.526666666666667
### S0_RAW (n=30)
- mean runtime: 9.387066666666668
- mean R/H/S/D/K: 5.0/4.966666666666667/5.0/4.966666666666667/4.933333333333334
- mean overall (avg R/H/S/D/K): 4.973333333333333
### S0_UNSTRUCTURED (n=30)
- mean runtime: 9.7462
- mean R/H/S/D/K: 4.933333333333334/4.9/4.966666666666667/5.0/4.866666666666666
- mean overall (avg R/H/S/D/K): 4.933333333333334
### S1 (n=30)
- mean runtime: 9.484833333333334
- mean R/H/S/D/K: 5.0/4.933333333333334/4.933333333333334/5.0/4.9
- mean overall (avg R/H/S/D/K): 4.953333333333333
### S2 (n=30)
- mean runtime: 11.0511
- mean R/H/S/D/K: 4.966666666666667/4.966666666666667/5.0/4.966666666666667/4.966666666666667
- mean overall (avg R/H/S/D/K): 4.973333333333333

## Top missing elements (max 20)
- Konkrete Stop-Conditions zwischen Schritten: 2
- Keine GPS/Standortdaten dokumentiert: 1
- Keine explizite Stop-Condition für Beobachtungszeitraum: 1
- Offline-Workflow für device_state=offline explizit erwähnen: 1
- Offline-Workflow nicht erwähnt (device.connectivity=offline im CONTEXT): 1
- Domänen-/Asset-Typ-Identifikation fehlt: 1
- Spezifische Prüfpunkte ohne Kenntnis des Asset-Typs spekulativ: 1
- Asset-ID (n4427359783) nicht explizit in Dokumentation erwähnt: 1
- Explizite Ticket-ID oder Asset-ID Nennung: 1
- GPS-Koordinaten in Dokumentation: 1
- Explizite Nutzung der Asset-ID im Workflow: 1
- Asset-Typ aus CONTEXT ermitteln: 1
- Keine Spekulation über Straßenlampe/Ampel ohne Kontext-Basis: 1
- Offline-Workflow für spotty connectivity nicht explizit erwähnt: 1
- Explizite Nutzung der GPS-Koordinaten aus CONTEXT: 1
- Erwähnung der Dämmerung/poor_visibility für Absicherung: 1
- Asset-ID (n4939032525) nicht explizit in Dokumentation erwähnt: 1
- Explizite Erwähnung der OSM-ID n4939032525 in Dokumentation: 1
- Hinweis auf Schweregrad 'mittel' aus Context: 1
- Severity-Einschätzung fehlt: 1
