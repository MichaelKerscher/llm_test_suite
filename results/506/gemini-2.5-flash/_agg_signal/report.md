# Aggregation Report (506/gemini-2.5-flash) [signal]
- judge_version filter: **judge_v1_1**
- Tests (latest runs): **150**
- Incidents with any deltas: **30**

## Mean scores by context level (snapshot)
### L0 (n=30)
- mean runtime: 7.932966666666667
- mean R/H/S/D/K: 3.8333333333333335/3.933333333333333/3.966666666666667/4.066666666666666/2.6333333333333333
- mean overall (avg R/H/S/D/K): 3.6866666666666665
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.00, hallucination_suspected=0.13
### L2 (n=30)
- mean runtime: 10.543033333333334
- mean R/H/S/D/K: 4.9/4.9/4.933333333333334/4.966666666666667/4.5
- mean overall (avg R/H/S/D/K): 4.84
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.10, hallucination_suspected=0.00
### L2B (n=30)
- mean runtime: 9.448066666666668
- mean R/H/S/D/K: 5.0/5.0/4.966666666666667/5.0/5.0
- mean overall (avg R/H/S/D/K): 4.993333333333334
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.53, hallucination_suspected=0.00
### unknown (n=60)
- mean runtime: 10.624833333333333
- mean R/H/S/D/K: 4.55/4.6/4.75/4.75/4.316666666666666
- mean overall (avg R/H/S/D/K): 4.593333333333334
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.23, hallucination_suspected=0.00

## Mean scores by strategy (snapshot)
### S0 (n=30)
- mean runtime: 7.932966666666667
- mean R/H/S/D/K: 3.8333333333333335/3.933333333333333/3.966666666666667/4.066666666666666/2.6333333333333333
- mean overall (avg R/H/S/D/K): 3.6866666666666665
### S0_RAW (n=30)
- mean runtime: 10.7385
- mean R/H/S/D/K: 4.8/4.833333333333333/4.933333333333334/4.933333333333334/4.733333333333333
- mean overall (avg R/H/S/D/K): 4.846666666666667
### S0_UNSTRUCTURED (n=30)
- mean runtime: 10.511166666666666
- mean R/H/S/D/K: 4.3/4.366666666666666/4.566666666666666/4.566666666666666/3.9
- mean overall (avg R/H/S/D/K): 4.34
### S1 (n=30)
- mean runtime: 10.543033333333334
- mean R/H/S/D/K: 4.9/4.9/4.933333333333334/4.966666666666667/4.5
- mean overall (avg R/H/S/D/K): 4.84
### S2 (n=30)
- mean runtime: 9.448066666666668
- mean R/H/S/D/K: 5.0/5.0/4.966666666666667/5.0/5.0
- mean overall (avg R/H/S/D/K): 4.993333333333334

## Top missing elements (max 20)
- offline_workflow_explicit: 5
- offline_workflow: 3
- Offline-Workflow (spotty connectivity): 3
- Wetter/Sicht-Anpassungen (nicht im Kontext): 2
- Offline-Workflow nicht erwartbar (kein Signal im CONTEXT): 2
- Offline-Workflow (spotty connectivity im Kontext): 2
- Offline-Workflow (spotty connectivity) nicht explizit erwähnt: 2
- Offline-Workflow (nicht erwartbar, da CONTEXT kein connectivity-Signal enthält): 1
- Explizite Eskalations-Trigger (z.B. 'wenn Polizei nicht binnen X min eintrifft'): 1
- Offline-Workflow explizit (connectivity=offline im CONTEXT, aber keine klare Anpassung wie 'lokale Speicherung, spätere Sync'): 1
- Offline-Workflow explizit (offline-Signal im CONTEXT vorhanden, aber nicht klar als Workflow-Anpassung formuliert): 1
- Keine Offline-Workflow-Erwähnung nötig (online): 1
- Kontext minimal, aber korrekt genutzt: 1
- Severity-Bewusstsein (high nicht erkennbar im Kontext): 1
- Kontext minimal genutzt (nur Asset-ID): 1
- Offline-Workflow nicht erwähnt trotz 'spotty' connectivity: 1
- Offline-Workflow erwähnt, aber nicht als Schritt 1 priorisiert: 1
- Kontext unstrukturiert, aber teilweise genutzt (Nacht, Regen, schlechte Sicht): 1
- Offline-Workflow nicht erwähnt trotz 'spotty': 1
- Keine klare Stop-Condition für Verkehrsregelung: 1
