# Aggregation Report (gemini-2.5-flash) [lamp]
- judge_version filter: **judge_v1_1_single**
- incident filter: **regular**
- Tests (latest runs): **150**
- Incidents with any deltas: **30**

## Mean scores by context level (snapshot)
### L0 (n=30)
- mean runtime: 6.853933333333333
- mean R/H/S/D/K: 4.533333333333333/4.7/4.7/4.966666666666667/3.433333333333333
- mean overall (avg R/H/S/D/K): 4.466666666666667
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.00, hallucination_suspected=0.03
### L2 (n=30)
- mean runtime: 9.404033333333333
- mean R/H/S/D/K: 5.0/4.933333333333334/4.933333333333334/5.0/4.9
- mean overall (avg R/H/S/D/K): 4.953333333333333
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.47, hallucination_suspected=0.00
### L2B (n=30)
- mean runtime: 10.552666666666665
- mean R/H/S/D/K: 4.933333333333334/4.933333333333334/4.966666666666667/4.933333333333334/4.933333333333334
- mean overall (avg R/H/S/D/K): 4.9399999999999995
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.60, hallucination_suspected=0.00
### unknown (n=60)
- mean runtime: 9.161883333333332
- mean R/H/S/D/K: 4.933333333333334/4.916666666666667/4.916666666666667/4.966666666666667/4.966666666666667
- mean overall (avg R/H/S/D/K): 4.9399999999999995
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.43, hallucination_suspected=0.00

## Mean scores by strategy (snapshot)
### S0 (n=30)
- mean runtime: 6.853933333333333
- mean R/H/S/D/K: 4.533333333333333/4.7/4.7/4.966666666666667/3.433333333333333
- mean overall (avg R/H/S/D/K): 4.466666666666667
### S0_RAW (n=30)
- mean runtime: 8.571666666666665
- mean R/H/S/D/K: 4.966666666666667/4.966666666666667/4.966666666666667/4.966666666666667/4.966666666666667
- mean overall (avg R/H/S/D/K): 4.966666666666667
### S0_UNSTRUCTURED (n=30)
- mean runtime: 9.7521
- mean R/H/S/D/K: 4.9/4.866666666666666/4.866666666666666/4.966666666666667/4.966666666666667
- mean overall (avg R/H/S/D/K): 4.913333333333333
### S1 (n=30)
- mean runtime: 9.404033333333333
- mean R/H/S/D/K: 5.0/4.933333333333334/4.933333333333334/5.0/4.9
- mean overall (avg R/H/S/D/K): 4.953333333333333
### S2 (n=30)
- mean runtime: 10.552666666666665
- mean R/H/S/D/K: 4.933333333333334/4.933333333333334/4.966666666666667/4.933333333333334/4.933333333333334
- mean overall (avg R/H/S/D/K): 4.9399999999999995

## Top missing elements (max 20)
- Offline-Workflow für spotty connectivity: 3
- Severity-Einschätzung für sporadischen Fehler: 1
- Konkrete Eskalations-Trigger definieren: 1
- Klare Stop-Condition für Beobachtungszeitraum fehlt: 1
- Priorisierung zwischen Beobachtung und sofortiger Eskalation könnte schärfer sein: 1
- Kontext-Nutzung minimal (nur Asset-ID übernommen): 1
- Keine Nachfrage zu Asset-Typ oder Standort: 1
- Keine Kontextinformationen zu Verkehr/Wetter/Tageszeit genutzt: 1
- Offline-Workflow nicht erwähnt (aber auch nicht erwartbar aus CONTEXT): 1
- Asset-ID/OSM-ID explizit im Protokoll: 1
- Kontext-Nutzung: Asset-OSM-ID wird nicht weiter genutzt (z.B. für Standortabfrage): 1
- Keine Nachfrage nach fehlenden Infos (Anzahl Leuchten, Verkehrslage, Tageszeit): 1
- Offline-Workflow explizit (bei spotty connectivity): 1
- Asset-ID (n7230270217) nicht explizit im Protokoll erwähnt: 1
- Kontextnutzung: Asset-ID wird genannt, aber OSM-Kontext nicht aktiv genutzt: 1
- Keine Nachfrage zu fehlenden Infos (Verkehrslage, Tageszeit, Wetter): 1
- Severity-Einschätzung (Stadtmitte könnte hohe Verkehrsdichte bedeuten): 1
- Explizite Prüfung ob Offline-Workflow nötig (Kontext gibt keine Connectivity-Info): 1
- Asset-Typ nicht identifiziert (Ampel/Lampe unklar): 1
- Keine Priorisierung bei zeitweisem Fehler: 1
