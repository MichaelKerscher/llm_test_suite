# Aggregation Report (506/gemini-2.5-flash)
- judge_version filter: **judge_v1_1**
- Tests (latest runs): **90**
- Incidents with any deltas: **30**

## Mean scores by context level (snapshot)
### L0 (n=30)
- mean runtime: 6.547700000000001
- mean R/H/S/D/K: 3.6/3.8666666666666667/3.8666666666666667/4.066666666666666/2.966666666666667
- mean overall (avg R/H/S/D/K): 3.6733333333333333
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.00, hallucination_suspected=0.00
### L2 (n=30)
- mean runtime: 9.253133333333333
- mean R/H/S/D/K: 4.733333333333333/4.5/4.633333333333334/4.833333333333333/3.8333333333333335
- mean overall (avg R/H/S/D/K): 4.506666666666666
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.07, hallucination_suspected=0.10
### L2B (n=30)
- mean runtime: 9.903699999999999
- mean R/H/S/D/K: 4.933333333333334/4.833333333333333/4.8/5.0/4.966666666666667
- mean overall (avg R/H/S/D/K): 4.906666666666666
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.63, hallucination_suspected=0.00

## Mean scores by strategy (snapshot)
### S0 (n=30)
- mean runtime: 6.547700000000001
- mean R/H/S/D/K: 3.6/3.8666666666666667/3.8666666666666667/4.066666666666666/2.966666666666667
- mean overall (avg R/H/S/D/K): 3.6733333333333333
### S1 (n=30)
- mean runtime: 9.253133333333333
- mean R/H/S/D/K: 4.733333333333333/4.5/4.633333333333334/4.833333333333333/3.8333333333333335
- mean overall (avg R/H/S/D/K): 4.506666666666666
### S2 (n=30)
- mean runtime: 9.903699999999999
- mean R/H/S/D/K: 4.933333333333334/4.833333333333333/4.8/5.0/4.966666666666667
- mean overall (avg R/H/S/D/K): 4.906666666666666

## Top missing elements (max 20)
- Offline-Workflow bei spotty connectivity: 6
- Offline-Workflow (connectivity=offline): 3
- Offline-Workflow fehlt trotz connectivity=offline: 2
- Kontextnutzung minimal (nur Asset-ID vorhanden): 2
- Keine Offline-Workflow-Erwähnung (aber nicht erwartbar bei L0_minimal): 2
- Offline-Workflow nicht erwähnt (aber auch nicht erwartbar bei minimalem Context): 1
- Keine Nutzung des vorhandenen Fotos aus photo_available: 1
- Keine Anweisung zu lokaler Speicherung/Synchronisation: 1
- Keine Nutzung des minimalen Kontexts (nur asset_osm vorhanden): 1
- Generische Antwort ohne Bezug auf fehlende Umgebungs-/Incident-Daten: 1
- Offline-Workflow (nicht erwartbar, da connectivity nicht im CONTEXT): 1
- Keine Offline-Workflow-Erwähnung (aber auch nicht erwartbar bei L0): 1
- Offline-Workflow nicht erwähnt trotz spotty connectivity: 1
- Low battery des Geräts nicht als Handlungsconstraint adressiert: 1
- Keine explizite Priorisierung nach severity (nicht im Context): 1
- Offline-Workflow nicht explizit genannt (connectivity=offline im Context): 1
- Offline-Workflow (spotty connectivity): 1
- Keine Spekulation über device_state als Asset-Problem: 1
- Keine Nutzung des Kontexts (nur Asset-ID vorhanden): 1
- Keine Erwähnung intermittierender Fehlercharakteristik: 1
