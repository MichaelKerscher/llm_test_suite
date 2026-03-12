# Aggregation Report (506)
- judge_version filter: **judge_v1_1**
- Tests (latest runs): **90**
- Incidents with any deltas: **30**

## Mean scores by context level (snapshot)
### L0 (n=30)
- mean runtime: 3.6285666666666665
- mean R/H/S/D/K: 3.5/3.533333333333333/3.2/3.7333333333333334/2.8333333333333335
- mean overall (avg R/H/S/D/K): 3.36
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.00, hallucination_suspected=0.03
### L2 (n=30)
- mean runtime: 4.073033333333333
- mean R/H/S/D/K: 4.6/4.366666666666666/4.2/4.4/4.033333333333333
- mean overall (avg R/H/S/D/K): 4.319999999999999
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.20, hallucination_suspected=0.00
### L2B (n=30)
- mean runtime: 4.267833333333333
- mean R/H/S/D/K: 4.866666666666666/4.833333333333333/4.5/4.833333333333333/4.933333333333334
- mean overall (avg R/H/S/D/K): 4.793333333333334
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.63, hallucination_suspected=0.00

## Mean scores by strategy (snapshot)
### S0 (n=30)
- mean runtime: 3.6285666666666665
- mean R/H/S/D/K: 3.5/3.533333333333333/3.2/3.7333333333333334/2.8333333333333335
- mean overall (avg R/H/S/D/K): 3.36
### S1 (n=30)
- mean runtime: 4.073033333333333
- mean R/H/S/D/K: 4.6/4.366666666666666/4.2/4.4/4.033333333333333
- mean overall (avg R/H/S/D/K): 4.319999999999999
### S2 (n=30)
- mean runtime: 4.267833333333333
- mean R/H/S/D/K: 4.866666666666666/4.833333333333333/4.5/4.833333333333333/4.933333333333334
- mean overall (avg R/H/S/D/K): 4.793333333333334

## Top missing elements (max 20)
- Kontextnutzung minimal (nur Asset-ID): 2
- Offline-Workflow nicht erwartbar (kein Signal im Kontext): 2
- Keine Nutzung des minimalen Kontexts (nur asset_osm vorhanden): 2
- Keine Nutzung der Asset-ID im Kontext: 2
- Keine explizite Erwähnung von 'intermittent' als Fehlertyp: 2
- Offline-Workflow (lokal dokumentieren/Foto lokal speichern): 1
- Keine Nutzung von Kontext (nur Asset-ID vorhanden): 1
- Keine spezifische Anpassung an intermittent fault_type: 1
- Offline-Workflow nicht erwartbar (kein Signal): 1
- GPS-Koordinaten nicht explizit dokumentiert: 1
- Offline-Workflow bei spotty connectivity: 1
- Severity/Traffic-Kontext fehlt (minimal context): 1
- Offline-Workflow (connectivity=offline, device_state=low_battery): 1
- Explizite Erwähnung 'lokal speichern/später synchronisieren': 1
- Offline-Workflow (kein Signal im Kontext, daher nicht erwartbar): 1
- Wetter-/Verkehrskontext (nicht vorhanden): 1
- Foto-Workflow (nicht vorhanden): 1
- Offline-Workflow explizit (connectivity=offline, aber nicht klar als Workflow-Schritt formuliert): 1
- Keine Anpassung an fehlende Umgebungs-/Severity-Infos: 1
- Kein expliziter Offline-Workflow trotz spotty connectivity: 1
