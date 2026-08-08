# Aggregation Report (mistral-large) [signal]
- judge_version filter: **judge_v1_1_single**
- incident filter: **regular**
- Tests (latest runs): **150**
- Incidents with any deltas: **30**

## Mean scores by context level (snapshot)
### L0 (n=30)
- mean runtime: 7.666033333333333
- mean R/H/S/D/K: 4.8/4.866666666666666/4.866666666666666/5.0/3.7
- mean overall (avg R/H/S/D/K): 4.6466666666666665
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.00, hallucination_suspected=0.03
### L2 (n=30)
- mean runtime: 9.786399999999999
- mean R/H/S/D/K: 4.933333333333334/4.866666666666666/4.9/4.966666666666667/4.933333333333334
- mean overall (avg R/H/S/D/K): 4.92
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.43, hallucination_suspected=0.00
### L2B (n=30)
- mean runtime: 10.099333333333334
- mean R/H/S/D/K: 4.833333333333333/4.8/4.866666666666666/4.866666666666666/4.866666666666666
- mean overall (avg R/H/S/D/K): 4.846666666666667
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.57, hallucination_suspected=0.07
### unknown (n=60)
- mean runtime: 9.469899999999999
- mean R/H/S/D/K: 4.933333333333334/4.933333333333334/4.983333333333333/4.983333333333333/4.9
- mean overall (avg R/H/S/D/K): 4.946666666666667
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.37, hallucination_suspected=0.02

## Mean scores by strategy (snapshot)
### S0 (n=30)
- mean runtime: 7.666033333333333
- mean R/H/S/D/K: 4.8/4.866666666666666/4.866666666666666/5.0/3.7
- mean overall (avg R/H/S/D/K): 4.6466666666666665
### S0_RAW (n=30)
- mean runtime: 9.410166666666667
- mean R/H/S/D/K: 5.0/5.0/5.0/5.0/4.966666666666667
- mean overall (avg R/H/S/D/K): 4.993333333333334
### S0_UNSTRUCTURED (n=30)
- mean runtime: 9.529633333333333
- mean R/H/S/D/K: 4.866666666666666/4.866666666666666/4.966666666666667/4.966666666666667/4.833333333333333
- mean overall (avg R/H/S/D/K): 4.9
### S1 (n=30)
- mean runtime: 9.786399999999999
- mean R/H/S/D/K: 4.933333333333334/4.866666666666666/4.9/4.966666666666667/4.933333333333334
- mean overall (avg R/H/S/D/K): 4.92
### S2 (n=30)
- mean runtime: 10.099333333333334
- mean R/H/S/D/K: 4.833333333333333/4.8/4.866666666666666/4.866666666666666/4.866666666666666
- mean overall (avg R/H/S/D/K): 4.846666666666667

## Top missing elements (max 20)
- Offline-Workflow (device.connectivity=offline): 2
- GPS-Koordinaten nicht in Dokumentation erwähnt: 2
- Low-Battery-Hinweis (device_state=low_battery): 1
- Explizite Nutzung von Asset-ID/GPS-Koordinaten aus Context: 1
- Offline-Workflow (device.connectivity=offline nicht adressiert): 1
- Korrekte Zeitstempel-Nutzung: 1
- Keine OSM-Daten im Context genutzt (nur Asset-ID übernommen): 1
- Keine Nachfrage zu fehlenden Kontextinformationen: 1
- Asset-Typ unklar (Straßenlampe vs. Ampel): 1
- Severity=low nicht berücksichtigt (zu umfangreich): 1
- Keine klare Stop-Condition für Beobachtungsphase: 1
- Ticket-ID/Asset-ID nicht explizit erwähnt: 1
- Explizite Erwähnung der OSM-ID n6887356470 im Protokoll: 1
- GPS-Koordinaten 47.8428337, 12.0803209 für Dokumentation: 1
- Keine Erwähnung von Asset-ID/OSM-Referenz in Dokumentation: 1
- Keine Kontextinformationen zu Verkehr/Wetter/Konnektivität genutzt: 1
- Kontext gibt keine Asset-Details - Annahme 'Straßenlampe/Ampel' ist Spekulation: 1
- Keine Offline-Workflow-Erwähnung (aber auch nicht erwartbar aus Context): 1
- Spezifische Hinweise zur intermittent-Natur aus Context könnten stärker betont werden: 1
- Priorisierung zwischen Sichtprüfung und Diagnose könnte klarer sein: 1
