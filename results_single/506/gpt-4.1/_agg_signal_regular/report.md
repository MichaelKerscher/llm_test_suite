# Aggregation Report (gpt-4.1) [signal]
- judge_version filter: **judge_v1_1_single**
- incident filter: **regular**
- Tests (latest runs): **150**
- Incidents with any deltas: **30**

## Mean scores by context level (snapshot)
### L0 (n=30)
- mean runtime: 7.763066666666666
- mean R/H/S/D/K: 4.633333333333334/4.766666666666667/4.833333333333333/5.0/3.6333333333333333
- mean overall (avg R/H/S/D/K): 4.573333333333333
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.00, hallucination_suspected=0.10
### L2 (n=30)
- mean runtime: 9.369366666666668
- mean R/H/S/D/K: 4.966666666666667/4.933333333333334/5.0/4.966666666666667/4.866666666666666
- mean overall (avg R/H/S/D/K): 4.946666666666667
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.43, hallucination_suspected=0.00
### L2B (n=30)
- mean runtime: 9.829766666666666
- mean R/H/S/D/K: 4.966666666666667/4.933333333333334/4.966666666666667/4.933333333333334/5.0
- mean overall (avg R/H/S/D/K): 4.96
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.57, hallucination_suspected=0.00
### unknown (n=60)
- mean runtime: 9.352333333333332
- mean R/H/S/D/K: 4.95/4.95/4.966666666666667/5.0/4.966666666666667
- mean overall (avg R/H/S/D/K): 4.966666666666667
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.33, hallucination_suspected=0.00

## Mean scores by strategy (snapshot)
### S0 (n=30)
- mean runtime: 7.763066666666666
- mean R/H/S/D/K: 4.633333333333334/4.766666666666667/4.833333333333333/5.0/3.6333333333333333
- mean overall (avg R/H/S/D/K): 4.573333333333333
### S0_RAW (n=30)
- mean runtime: 9.256666666666666
- mean R/H/S/D/K: 5.0/5.0/4.966666666666667/5.0/4.966666666666667
- mean overall (avg R/H/S/D/K): 4.986666666666666
### S0_UNSTRUCTURED (n=30)
- mean runtime: 9.448
- mean R/H/S/D/K: 4.9/4.9/4.966666666666667/5.0/4.966666666666667
- mean overall (avg R/H/S/D/K): 4.946666666666667
### S1 (n=30)
- mean runtime: 9.369366666666668
- mean R/H/S/D/K: 4.966666666666667/4.933333333333334/5.0/4.966666666666667/4.866666666666666
- mean overall (avg R/H/S/D/K): 4.946666666666667
### S2 (n=30)
- mean runtime: 9.829766666666666
- mean R/H/S/D/K: 4.966666666666667/4.933333333333334/4.966666666666667/4.933333333333334/5.0
- mean overall (avg R/H/S/D/K): 4.96

## Top missing elements (max 20)
- Asset-ID/OSM-Referenz explizit erwähnen: 2
- Keine Offline-Workflow-Erwähnung (aber nicht erwartbar aus CONTEXT): 1
- Asset-ID im Text falsch (n6896979934 statt n6896979334): 1
- Explizite Offline-Workflow-Anweisung könnte deutlicher sein: 1
- Asset-ID (n6887356469) nicht explizit im Protokoll erwähnt: 1
- GPS-Koordinaten nicht dokumentiert: 1
- Konkrete Asset-Typ-Identifikation (Ampel vs. Straßenlampe unklar): 1
- Spezifische Priorisierung für sporadische Fehler: 1
- GPS-Koordinaten für Dokumentation: 1
- Keine Kontextnutzung erkennbar (nur Asset-ID verwendet): 1
- Keine Nachfrage zu fehlenden Infos (z.B. Konnektivität, Wetter): 1
- Spezifische Asset-Typ-Identifikation (Lampe/Ampel unklar): 1
- Keine Nutzung des CONTEXT (nur Asset-ID wiederholt): 1
- Keine Nachfrage zu fehlenden Infos (Verkehrslage, Tageszeit, Wetter): 1
- Klärung 'backward' bleibt spekulativ: 1
- Kein Hinweis auf Offline-Workflow (aber nicht erwartbar): 1
- Kontext-Nutzung: asset_osm wird nicht interpretiert: 1
- Spekulation über Asset-Typ (Ampel/Lampe) ohne Basis im Context: 1
- GPS-Koordinaten in Dokumentation: 1
- Offline-Workflow bei spotty connectivity nicht explizit erwähnt: 1
