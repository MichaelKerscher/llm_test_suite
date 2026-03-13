# Aggregation Report (506/mistral-large)
- judge_version filter: **judge_v1_1**
- Tests (latest runs): **90**
- Incidents with any deltas: **30**

## Mean scores by context level (snapshot)
### L0 (n=30)
- mean runtime: 5.536133333333334
- mean R/H/S/D/K: 3.533333333333333/3.7/3.7333333333333334/4.066666666666666/2.8333333333333335
- mean overall (avg R/H/S/D/K): 3.5733333333333333
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.00, hallucination_suspected=0.00
### L2 (n=30)
- mean runtime: 9.266633333333335
- mean R/H/S/D/K: 4.7/4.633333333333334/4.633333333333334/4.833333333333333/3.9
- mean overall (avg R/H/S/D/K): 4.54
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.00, hallucination_suspected=0.13
### L2B (n=30)
- mean runtime: 9.222399999999999
- mean R/H/S/D/K: 4.966666666666667/4.9/4.866666666666666/4.966666666666667/5.0
- mean overall (avg R/H/S/D/K): 4.9399999999999995
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.63, hallucination_suspected=0.00

## Mean scores by strategy (snapshot)
### S0 (n=30)
- mean runtime: 5.536133333333334
- mean R/H/S/D/K: 3.533333333333333/3.7/3.7333333333333334/4.066666666666666/2.8333333333333335
- mean overall (avg R/H/S/D/K): 3.5733333333333333
### S1 (n=30)
- mean runtime: 9.266633333333335
- mean R/H/S/D/K: 4.7/4.633333333333334/4.633333333333334/4.833333333333333/3.9
- mean overall (avg R/H/S/D/K): 4.54
### S2 (n=30)
- mean runtime: 9.222399999999999
- mean R/H/S/D/K: 4.966666666666667/4.9/4.866666666666666/4.966666666666667/5.0
- mean overall (avg R/H/S/D/K): 4.9399999999999995

## Top missing elements (max 20)
- Offline-Workflow bei spotty connectivity: 5
- Offline-Workflow (device.connectivity=offline): 1
- Klarstellung device_state bezieht sich auf Techniker-Gerät: 1
- Offline-Workflow explizit (spotty connectivity): 1
- Keine Offline-Workflow-Erwähnung (aber nicht erwartbar bei minimalem Context): 1
- Severity/Traffic nicht explizit adressiert (nicht im Context): 1
- Offline-Workflow nicht explizit genannt (device.connectivity=offline im Context): 1
- Offline-Workflow (lokal dokumentieren/speichern): 1
- Keine Online-Schritte bei connectivity=offline: 1
- Keine Nutzung des minimalen Kontexts (nur asset_osm vorhanden): 1
- Keine Anpassung an fehlende Umgebungs-/Incident-Daten: 1
- Offline-Workflow bei spotty connectivity nicht erwähnt: 1
- Offline-Workflow (lokal dokumentieren/synchronisieren): 1
- Klarstellung device.* = Techniker-Gerät: 1
- Kontextnutzung minimal (nur Asset-ID): 1
- Keine Anpassung an Umweltbedingungen: 1
- Offline-Workflow bei spotty connectivity nicht explizit erwähnt: 1
- Keine Nutzung der GPS-Koordinaten (nur Asset-ID erwähnt): 1
- Keine Erwähnung von Foto-Dokumentation trotz minimaler Kontext: 1
- Keine Nutzung von Foto-Hinweis (nicht im Context): 1
