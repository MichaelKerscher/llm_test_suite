# Aggregation Report (506/gemini-2.5-flash) [lamp]
- Tests (latest runs): **150**
- Incidents with any deltas: **30**

## Mean scores by context level (snapshot)
### L0 (n=30)
- mean runtime: 7.412433333333333
- mean R/H/S/D/K: 3.466666666666667/3.7333333333333334/3.9/4.1/2.3666666666666667
- mean overall (avg R/H/S/D/K): 3.5133333333333336
- flags (rate): safety_first=0.97, escalation_present=1.00, offline_workflow_mentioned=0.00, hallucination_suspected=0.10
### L2 (n=30)
- mean runtime: 10.634333333333334
- mean R/H/S/D/K: 4.866666666666666/4.766666666666667/4.733333333333333/4.9/4.433333333333334
- mean overall (avg R/H/S/D/K): 4.739999999999999
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.10, hallucination_suspected=0.00
### L2B (n=30)
- mean runtime: 12.0863
- mean R/H/S/D/K: 5.0/5.0/4.966666666666667/5.0/5.0
- mean overall (avg R/H/S/D/K): 4.993333333333334
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.60, hallucination_suspected=0.00
### unknown (n=60)
- mean runtime: 10.161633333333333
- mean R/H/S/D/K: 4.583333333333333/4.566666666666666/4.633333333333334/4.783333333333333/4.066666666666666
- mean overall (avg R/H/S/D/K): 4.526666666666667
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.27, hallucination_suspected=0.03

## Mean scores by strategy (snapshot)
### S0 (n=30)
- mean runtime: 7.412433333333333
- mean R/H/S/D/K: 3.466666666666667/3.7333333333333334/3.9/4.1/2.3666666666666667
- mean overall (avg R/H/S/D/K): 3.5133333333333336
### S0_RAW (n=30)
- mean runtime: 9.583766666666666
- mean R/H/S/D/K: 4.733333333333333/4.666666666666667/4.7/4.9/4.333333333333333
- mean overall (avg R/H/S/D/K): 4.666666666666667
### S0_UNSTRUCTURED (n=30)
- mean runtime: 10.7395
- mean R/H/S/D/K: 4.433333333333334/4.466666666666667/4.566666666666666/4.666666666666667/3.8
- mean overall (avg R/H/S/D/K): 4.386666666666667
### S1 (n=30)
- mean runtime: 10.634333333333334
- mean R/H/S/D/K: 4.866666666666666/4.766666666666667/4.733333333333333/4.9/4.433333333333334
- mean overall (avg R/H/S/D/K): 4.739999999999999
### S2 (n=30)
- mean runtime: 12.0863
- mean R/H/S/D/K: 5.0/5.0/4.966666666666667/5.0/5.0
- mean overall (avg R/H/S/D/K): 4.993333333333334

## Top missing elements (max 20)
- Kontextnutzung minimal (nur Asset-ID): 4
- Keine Nutzung der Asset-ID im Kontext: 3
- offline_workflow: 3
- Offline-Workflow (connectivity=spotty, aber nicht explizit erwähnt): 2
- Offline-Workflow bei spotty connectivity: 2
- Keine Anpassung an tatsächliche Situation: 1
- Generische Empfehlungen ohne Fallbezug: 1
- Offline-Workflow nicht explizit trotz connectivity=offline: 1
- Offline-Workflow nicht erwähnt trotz 'offline' im Kontext: 1
- Halluzination: 'Dringlichkeit als hoch eingestuft' (severity=low im Kontext): 1
- Kontextnutzung (Asset-ID, Standort, Foto): 1
- Feuchtigkeitsflecken/Nebel-Hinweis: 1
- Intermittent-Fehler-Strategie: 1
- Kontextnutzung minimal (nur OSM-ID): 1
- Keine Anpassung an Umgebung/Gerätezustand: 1
- Offline-Workflow nicht erwähnt trotz 'spotty' connectivity: 1
- Gerätezustand nur am Rande integriert: 1
- Offline-Workflow nicht explizit erwähnt trotz 'spotty' connectivity: 1
- Gerätezustand (low_battery) nur am Rande erwähnt: 1
- Offline-Workflow nicht erwähnt (aber Kontext zeigt keine Offline-Situation): 1
