# Aggregation Report (gemini-2.5-flash) [signal]
- judge_version filter: **judge_v1_1_single**
- incident filter: **regular**
- Tests (latest runs): **150**
- Incidents with any deltas: **30**

## Mean scores by context level (snapshot)
### L0 (n=30)
- mean runtime: 8.745466666666665
- mean R/H/S/D/K: 4.7/4.833333333333333/4.866666666666666/4.966666666666667/3.6333333333333333
- mean overall (avg R/H/S/D/K): 4.6
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.00, hallucination_suspected=0.07
### L2 (n=30)
- mean runtime: 10.681966666666666
- mean R/H/S/D/K: 4.9/4.9/4.966666666666667/4.966666666666667/4.966666666666667
- mean overall (avg R/H/S/D/K): 4.9399999999999995
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.47, hallucination_suspected=0.00
### L2B (n=30)
- mean runtime: 10.523166666666667
- mean R/H/S/D/K: 4.933333333333334/4.933333333333334/5.0/4.933333333333334/4.966666666666667
- mean overall (avg R/H/S/D/K): 4.953333333333333
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.57, hallucination_suspected=0.00
### unknown (n=60)
- mean runtime: 10.334133333333334
- mean R/H/S/D/K: 4.933333333333334/4.95/5.0/4.966666666666667/4.9
- mean overall (avg R/H/S/D/K): 4.95
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.33, hallucination_suspected=0.00

## Mean scores by strategy (snapshot)
### S0 (n=30)
- mean runtime: 8.745466666666665
- mean R/H/S/D/K: 4.7/4.833333333333333/4.866666666666666/4.966666666666667/3.6333333333333333
- mean overall (avg R/H/S/D/K): 4.6
### S0_RAW (n=30)
- mean runtime: 10.0191
- mean R/H/S/D/K: 5.0/5.0/5.0/4.933333333333334/4.966666666666667
- mean overall (avg R/H/S/D/K): 4.98
### S0_UNSTRUCTURED (n=30)
- mean runtime: 10.649166666666668
- mean R/H/S/D/K: 4.866666666666666/4.9/5.0/5.0/4.833333333333333
- mean overall (avg R/H/S/D/K): 4.92
### S1 (n=30)
- mean runtime: 10.681966666666666
- mean R/H/S/D/K: 4.9/4.9/4.966666666666667/4.966666666666667/4.966666666666667
- mean overall (avg R/H/S/D/K): 4.9399999999999995
### S2 (n=30)
- mean runtime: 10.523166666666667
- mean R/H/S/D/K: 4.933333333333334/4.933333333333334/5.0/4.933333333333334/4.966666666666667
- mean overall (avg R/H/S/D/K): 4.953333333333333

## Top missing elements (max 20)
- Keine explizite Priorisierung zwischen Sichtprüfung und Diagnose: 1
- Kein klarer Stop-Trigger bei drohendem Ausfall definiert: 1
- Spezifische Diagnose für sporadische Störungen (z.B. Wackelkontakt, thermische Probleme): 1
- Konkrete Messungen oder Tests zur Reproduktion: 1
- Offline-Workflow nicht erwähnt (bei spotty connectivity plausibel): 1
- Asset-ID/OSM-Referenz explizit erwähnen: 1
- GPS-Koordinaten in Dokumentation: 1
- Offline-Workflow (device.connectivity=offline nicht adressiert): 1
- Keine Nutzung des CONTEXT (nur Asset-ID übernommen): 1
- Keine gezielte Nachfrage nach fehlenden Infos: 1
- Konkrete Stop-Conditions für Langzeitbeobachtung: 1
- Spezifische Hinweise zur Intermittenz-Diagnose könnten detaillierter sein: 1
- GPS/Standort-Erfassung explizit erwähnen: 1
- Asset-ID (OSM n6887356444) nicht explizit in Dokumentation erwähnt: 1
- Severity-Einschätzung basierend auf Verkehrslage: 1
- Spezifische Offline-Workflow-Hinweise falls Konnektivität fehlt: 1
- OSM-ID n81364626 nicht explizit in Dokumentation erwähnt: 1
- Klärung was 'backward' bedeutet statt Spekulation: 1
- Konkrete Stop-Conditions für Eskalation: 1
- Asset-Typ aus Kontext ableiten oder erfragen: 1
