# Aggregation Report (506/mistral-large) [signal]
- judge_version filter: **judge_v1_1**
- Tests (latest runs): **150**
- Incidents with any deltas: **30**

## Mean scores by context level (snapshot)
### L0 (n=30)
- mean runtime: 9.019266666666665
- mean R/H/S/D/K: 3.8666666666666667/3.966666666666667/4.266666666666667/4.166666666666667/2.7333333333333334
- mean overall (avg R/H/S/D/K): 3.8
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.00, hallucination_suspected=0.10
### L2 (n=30)
- mean runtime: 11.921899999999999
- mean R/H/S/D/K: 4.966666666666667/4.933333333333334/4.933333333333334/5.0/4.766666666666667
- mean overall (avg R/H/S/D/K): 4.92
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.13, hallucination_suspected=0.00
### L2B (n=30)
- mean runtime: 10.866533333333333
- mean R/H/S/D/K: 5.0/4.966666666666667/4.933333333333334/4.933333333333334/5.0
- mean overall (avg R/H/S/D/K): 4.966666666666667
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.57, hallucination_suspected=0.00
### unknown (n=60)
- mean runtime: 11.7054
- mean R/H/S/D/K: 4.683333333333334/4.666666666666667/4.833333333333333/4.833333333333333/4.45
- mean overall (avg R/H/S/D/K): 4.693333333333333
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.27, hallucination_suspected=0.00

## Mean scores by strategy (snapshot)
### S0 (n=30)
- mean runtime: 9.019266666666665
- mean R/H/S/D/K: 3.8666666666666667/3.966666666666667/4.266666666666667/4.166666666666667/2.7333333333333334
- mean overall (avg R/H/S/D/K): 3.8
### S0_RAW (n=30)
- mean runtime: 11.582566666666667
- mean R/H/S/D/K: 4.866666666666666/4.866666666666666/4.933333333333334/4.966666666666667/4.766666666666667
- mean overall (avg R/H/S/D/K): 4.88
### S0_UNSTRUCTURED (n=30)
- mean runtime: 11.828233333333333
- mean R/H/S/D/K: 4.5/4.466666666666667/4.733333333333333/4.7/4.133333333333334
- mean overall (avg R/H/S/D/K): 4.506666666666666
### S1 (n=30)
- mean runtime: 11.921899999999999
- mean R/H/S/D/K: 4.966666666666667/4.933333333333334/4.933333333333334/5.0/4.766666666666667
- mean overall (avg R/H/S/D/K): 4.92
### S2 (n=30)
- mean runtime: 10.866533333333333
- mean R/H/S/D/K: 5.0/4.966666666666667/4.933333333333334/4.933333333333334/5.0
- mean overall (avg R/H/S/D/K): 4.966666666666667

## Top missing elements (max 20)
- offline_workflow_explicit: 8
- offline_workflow: 6
- Keine Nutzung der Asset-ID im Kontext: 4
- Offline-Workflow (nicht erwartbar, da connectivity nicht im CONTEXT): 3
- Kontextnutzung minimal (nur Asset-ID vorhanden): 2
- Offline-Workflow (spotty connectivity im CONTEXT, aber nicht explizit erwähnt): 2
- device_constraints: 1
- Keine Nutzung der Asset-ID im Kontext erkennbar: 1
- Keine Erwähnung von Fehlerspeicher/Logs bei intermittent fault: 1
- Unstrukturierter Kontext erschwert Nachvollziehbarkeit der Kontextnutzung: 1
- Kontextnutzung minimal (nur Asset-ID): 1
- Offline-Workflow (spotty connectivity vorhanden, aber nicht explizit als Workflow-Anpassung formuliert): 1
- Offline-Workflow (spotty connectivity im CONTEXT, aber nicht explizit adressiert): 1
- Kontext-Nutzung minimal (nur Asset-ID vorhanden): 1
- Keine Erwähnung von Foto-Dokumentation aus CONTEXT: 1
- Offline-Workflow explizit (spotty connectivity vorhanden): 1
- Keine Erwähnung der Koordinaten (nicht verfügbar im Context): 1
- Könnte Guardrail-Hinweis expliziter aufgreifen: 1
- Keine Erwähnung von Wetter/Sicht (nicht im Context): 1
- Spekuliert über Stromausfall ohne Basis: 1
