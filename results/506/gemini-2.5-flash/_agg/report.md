# Aggregation Report (506/gemini-2.5-flash)
- judge_version filter: **judge_v1_1**
- Tests (latest runs): **90**
- Incidents with any deltas: **30**

## Mean scores by context level (snapshot)
### L0 (n=30)
- mean runtime: 10.602233333333334
- mean R/H/S/D/K: 3.533333333333333/3.7/3.6/4.0/2.8666666666666667
- mean overall (avg R/H/S/D/K): 3.54
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.00, hallucination_suspected=0.03
### L2 (n=30)
- mean runtime: 9.3012
- mean R/H/S/D/K: 4.7/4.566666666666666/4.566666666666666/4.8/3.7666666666666666
- mean overall (avg R/H/S/D/K): 4.48
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.07, hallucination_suspected=0.07
### L2B (n=30)
- mean runtime: 11.048300000000001
- mean R/H/S/D/K: 4.933333333333334/4.866666666666666/4.866666666666666/5.0/5.0
- mean overall (avg R/H/S/D/K): 4.933333333333334
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.63, hallucination_suspected=0.00

## Mean scores by strategy (snapshot)
### S0 (n=30)
- mean runtime: 10.602233333333334
- mean R/H/S/D/K: 3.533333333333333/3.7/3.6/4.0/2.8666666666666667
- mean overall (avg R/H/S/D/K): 3.54
### S1 (n=30)
- mean runtime: 9.3012
- mean R/H/S/D/K: 4.7/4.566666666666666/4.566666666666666/4.8/3.7666666666666666
- mean overall (avg R/H/S/D/K): 4.48
### S2 (n=30)
- mean runtime: 11.048300000000001
- mean R/H/S/D/K: 4.933333333333334/4.866666666666666/4.866666666666666/5.0/5.0
- mean overall (avg R/H/S/D/K): 4.933333333333334

## Top missing elements (max 20)
- Offline-Workflow (lokal dokumentieren/Foto lokal speichern): 4
- Kontextnutzung minimal (nur Asset-ID): 2
- Offline-Workflow bei spotty connectivity nicht explizit erwähnt: 2
- Keine Nutzung des minimalen Kontexts (nur asset_osm vorhanden): 2
- Offline-Workflow bei spotty connectivity: 2
- Keine Nutzung der Asset-ID im Kontext erkennbar: 1
- Keine spezifische Priorisierung bei intermittent fault: 1
- Offline-Workflow (spotty connectivity): 1
- Spekuliert über Sicherungskasten ohne Kontext-Signal: 1
- Erwähnt Bauarbeiten ohne Anhaltspunkt: 1
- Keine Anpassung an tatsächliche Umgebung: 1
- Offline-Workflow explizit (spotty connectivity): 1
- Offline-Workflow (lokal dokumentieren/später sync): 1
- Keine Kontextnutzung (nur Asset-ID vorhanden): 1
- Keine Priorisierung bei unbekanntem Umfang: 1
- Keine Nutzung der Asset-ID im Kontext: 1
- Keine Priorisierung nach Severity/Traffic: 1
- Keine Erwähnung von Offline-Workflow trotz minimalem Kontext: 1
- Kein expliziter Offline-Workflow trotz connectivity=spotty: 1
- Keine Anpassung an fehlende Umgebungsinformationen: 1
