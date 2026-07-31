# Aggregation Report (506/mistral-large) [lamp]
- incident filter: **regular**
- Tests (latest runs): **150**
- Incidents with any deltas: **30**

## Mean scores by context level (snapshot)
### L0 (n=30)
- mean runtime: 8.846200000000001
- mean R/H/S/D/K: 3.466666666666667/3.7/3.9/4.2/2.2666666666666666
- mean overall (avg R/H/S/D/K): 3.506666666666667
- flags (rate): safety_first=0.97, escalation_present=1.00, offline_workflow_mentioned=0.00, hallucination_suspected=0.20
### L2 (n=30)
- mean runtime: 11.070233333333334
- mean R/H/S/D/K: 4.866666666666666/4.833333333333333/4.833333333333333/4.866666666666666/4.433333333333334
- mean overall (avg R/H/S/D/K): 4.766666666666667
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.13, hallucination_suspected=0.00
### L2B (n=30)
- mean runtime: 11.639266666666666
- mean R/H/S/D/K: 5.0/5.0/4.9/5.0/5.0
- mean overall (avg R/H/S/D/K): 4.98
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.60, hallucination_suspected=0.00
### unknown (n=60)
- mean runtime: 10.6399
- mean R/H/S/D/K: 4.483333333333333/4.466666666666667/4.55/4.716666666666667/4.133333333333334
- mean overall (avg R/H/S/D/K): 4.47
- flags (rate): safety_first=0.98, escalation_present=1.00, offline_workflow_mentioned=0.32, hallucination_suspected=0.03

## Mean scores by strategy (snapshot)
### S0 (n=30)
- mean runtime: 8.846200000000001
- mean R/H/S/D/K: 3.466666666666667/3.7/3.9/4.2/2.2666666666666666
- mean overall (avg R/H/S/D/K): 3.506666666666667
### S0_RAW (n=30)
- mean runtime: 10.463733333333332
- mean R/H/S/D/K: 4.633333333333334/4.633333333333334/4.6/4.9/4.433333333333334
- mean overall (avg R/H/S/D/K): 4.64
### S0_UNSTRUCTURED (n=30)
- mean runtime: 10.816066666666668
- mean R/H/S/D/K: 4.333333333333333/4.3/4.5/4.533333333333333/3.8333333333333335
- mean overall (avg R/H/S/D/K): 4.3
### S1 (n=30)
- mean runtime: 11.070233333333334
- mean R/H/S/D/K: 4.866666666666666/4.833333333333333/4.833333333333333/4.866666666666666/4.433333333333334
- mean overall (avg R/H/S/D/K): 4.766666666666667
### S2 (n=30)
- mean runtime: 11.639266666666666
- mean R/H/S/D/K: 5.0/5.0/4.9/5.0/5.0
- mean overall (avg R/H/S/D/K): 4.98

## Top missing elements (max 20)
- Expliziter Offline-Workflow: 3
- Offline-Workflow nicht explizit erwähnt trotz spotty connectivity: 2
- Keine Kontextnutzung erkennbar (nur Asset-ID vorhanden): 2
- Offline-Workflow: 2
- Keine Nutzung der Asset-ID im Kontext: 2
- Generische Antwort ohne Kontextbezug: 2
- offline_workflow: 2
- Kontextnutzung minimal (nur Asset-ID): 2
- Offline-Workflow nicht explizit erwähnt: 2
- Safety-first structure: 1
- Offline workflow (not expected here): 1
- Context utilization (minimal context given): 1
- Offline workflow explicit: 1
- Safety-first as step 1: 1
- Offline workflow explicit mention: 1
- Spotty connectivity nicht adressiert (kein Offline-Workflow): 1
- Offline-Workflow trotz spotty connectivity nicht erwähnt: 1
- Kontextnutzung minimal (nur Asset-ID verwendet): 1
- Keine Anpassung an Umgebungsbedingungen (Nebel/Nacht nicht erwähnt): 1
- Keine Berücksichtigung von Konnektivitätsproblemen: 1
