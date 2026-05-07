# Aggregation Report (506/gemini-2.5-flash) [signal]
- judge_version filter: **judge_v1_1**
- Tests (latest runs): **150**
- Incidents with any deltas: **30**

## Mean scores by context level (snapshot)
### L0 (n=30)
- mean runtime: 8.0966
- mean R/H/S/D/K: 3.8666666666666667/3.933333333333333/4.0/4.2/2.5
- mean overall (avg R/H/S/D/K): 3.7
- flags (rate): safety_first=0.97, escalation_present=1.00, offline_workflow_mentioned=0.00, hallucination_suspected=0.23
### L2 (n=30)
- mean runtime: 11.396899999999999
- mean R/H/S/D/K: 4.933333333333334/4.833333333333333/4.866666666666666/4.933333333333334/4.633333333333334
- mean overall (avg R/H/S/D/K): 4.84
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.10, hallucination_suspected=0.00
### L2B (n=30)
- mean runtime: 9.7398
- mean R/H/S/D/K: 5.0/4.966666666666667/4.9/5.0/5.0
- mean overall (avg R/H/S/D/K): 4.973333333333333
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.60, hallucination_suspected=0.00
### unknown (n=60)
- mean runtime: 10.4529
- mean R/H/S/D/K: 4.6/4.616666666666666/4.75/4.75/4.366666666666666
- mean overall (avg R/H/S/D/K): 4.616666666666666
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.30, hallucination_suspected=0.00

## Mean scores by strategy (snapshot)
### S0 (n=30)
- mean runtime: 8.0966
- mean R/H/S/D/K: 3.8666666666666667/3.933333333333333/4.0/4.2/2.5
- mean overall (avg R/H/S/D/K): 3.7
### S0_RAW (n=30)
- mean runtime: 10.622633333333333
- mean R/H/S/D/K: 4.9/4.866666666666666/4.866666666666666/4.966666666666667/4.733333333333333
- mean overall (avg R/H/S/D/K): 4.866666666666666
### S0_UNSTRUCTURED (n=30)
- mean runtime: 10.283166666666666
- mean R/H/S/D/K: 4.3/4.366666666666666/4.633333333333334/4.533333333333333/4.0
- mean overall (avg R/H/S/D/K): 4.366666666666666
### S1 (n=30)
- mean runtime: 11.396899999999999
- mean R/H/S/D/K: 4.933333333333334/4.833333333333333/4.866666666666666/4.933333333333334/4.633333333333334
- mean overall (avg R/H/S/D/K): 4.84
### S2 (n=30)
- mean runtime: 9.7398
- mean R/H/S/D/K: 5.0/4.966666666666667/4.9/5.0/5.0
- mean overall (avg R/H/S/D/K): 4.973333333333333

## Top missing elements (max 20)
- Kontext-Nutzung minimal (nur Asset-ID): 4
- offline_workflow: 3
- Offline-Workflow nicht explizit erwähnt trotz spotty connectivity: 2
- Offline-Workflow (nicht erwartbar, da connectivity nicht im CONTEXT): 2
- Keine Nutzung der Asset-ID im Kontext: 2
- offline_workflow_explicit: 2
- Offline-Workflow explizit: 1
- Offline-Workflow (nicht erwartbar aus minimalem Context): 1
- Explizite Kreuzungsregelung wie unbeschrankt: 1
- Offline-Workflow nicht explizit adressiert: 1
- Offline-Workflow nicht explizit erwähnt: 1
- Kreuzung wie unbeschrankt behandeln: 1
- Spekuliert über Ursachen ohne Basis: 1
- Erfindet Details (Detektoren, Steuerung): 1
- Unstrukturierter Kontext erschwert Nutzung: 1
- Kontextnutzung minimal (nur Asset-ID): 1
- Keine Anpassung an Umgebungsbedingungen: 1
- Keine Offline-Workflow-Hinweise: 1
- Kein expliziter Offline-Workflow trotz 'spotty': 1
- asset_osm explizit in Doku: 1
