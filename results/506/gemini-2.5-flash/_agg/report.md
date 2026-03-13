# Aggregation Report (506/gemini-2.5-flash)
- judge_version filter: **judge_v1_1**
- Tests (latest runs): **90**
- Incidents with any deltas: **30**

## Mean scores by context level (snapshot)
### L0 (n=30)
- mean runtime: 5.374066666666667
- mean R/H/S/D/K: 3.533333333333333/3.933333333333333/3.9/4.066666666666666/2.8333333333333335
- mean overall (avg R/H/S/D/K): 3.6533333333333333
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.00, hallucination_suspected=0.03
### L2 (n=30)
- mean runtime: 9.3343
- mean R/H/S/D/K: 4.766666666666667/4.7/4.633333333333334/4.9/3.9
- mean overall (avg R/H/S/D/K): 4.58
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.07, hallucination_suspected=0.00
### L2B (n=30)
- mean runtime: 8.5933
- mean R/H/S/D/K: 4.9/4.866666666666666/4.766666666666667/5.0/5.0
- mean overall (avg R/H/S/D/K): 4.906666666666666
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.63, hallucination_suspected=0.00

## Mean scores by strategy (snapshot)
### S0 (n=30)
- mean runtime: 5.374066666666667
- mean R/H/S/D/K: 3.533333333333333/3.933333333333333/3.9/4.066666666666666/2.8333333333333335
- mean overall (avg R/H/S/D/K): 3.6533333333333333
### S1 (n=30)
- mean runtime: 9.3343
- mean R/H/S/D/K: 4.766666666666667/4.7/4.633333333333334/4.9/3.9
- mean overall (avg R/H/S/D/K): 4.58
### S2 (n=30)
- mean runtime: 8.5933
- mean R/H/S/D/K: 4.9/4.866666666666666/4.766666666666667/5.0/5.0
- mean overall (avg R/H/S/D/K): 4.906666666666666

## Top missing elements (max 20)
- Offline-Workflow bei spotty connectivity: 7
- Kontextnutzung minimal (nur Asset-ID): 3
- Keine Nutzung des minimalen Kontexts (nur asset_osm vorhanden): 2
- Offline-Workflow (nicht erwartbar bei L0): 2
- Offline-Workflow bei spotty connectivity nicht erwähnt: 2
- Keine Nutzung der Asset-ID im Kontext: 2
- Generische Antwort ohne Bezug zu intermittent-Fehler: 1
- Keine Erwähnung von Foto oder spezifischen Beobachtungen: 1
- Offline-Workflow fehlt (device.connectivity=offline): 1
- Keine Erwähnung lokaler Speicherung/Sync: 1
- Offline-Workflow (connectivity=offline): 1
- Keine Anpassung an tatsächliche Umgebungsbedingungen: 1
- Offline-Workflow nicht erwähnt trotz connectivity=offline: 1
- Kontext-Nutzung minimal (nur Asset-ID): 1
- Spekuliert über Ampelanlage (nicht im Kontext): 1
- Überhitzung/Geräusche ohne Basis erwähnt: 1
- Keine Erwähnung von Severity/Priorisierung: 1
- Offline-Workflow explizit (spotty connectivity): 1
- Keine Priorisierung nach Severity/Umgebung: 1
- Generische Antwort ohne Bezug zu verfügbaren Kontext-Signalen: 1
