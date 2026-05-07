# Aggregation Report (506/gpt-4.1) [signal]
- judge_version filter: **judge_v1_1**
- Tests (latest runs): **150**
- Incidents with any deltas: **30**

## Mean scores by context level (snapshot)
### L0 (n=30)
- mean runtime: 8.469533333333334
- mean R/H/S/D/K: 3.8333333333333335/3.966666666666667/4.0/4.133333333333334/2.6333333333333333
- mean overall (avg R/H/S/D/K): 3.7133333333333334
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.00, hallucination_suspected=0.13
### L2 (n=30)
- mean runtime: 11.704066666666668
- mean R/H/S/D/K: 4.933333333333334/4.933333333333334/4.833333333333333/4.966666666666667/4.633333333333334
- mean overall (avg R/H/S/D/K): 4.86
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.20, hallucination_suspected=0.03
### L2B (n=30)
- mean runtime: 9.725533333333335
- mean R/H/S/D/K: 5.0/5.0/4.866666666666666/4.933333333333334/5.0
- mean overall (avg R/H/S/D/K): 4.96
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.53, hallucination_suspected=0.00
### unknown (n=60)
- mean runtime: 11.238783333333334
- mean R/H/S/D/K: 4.666666666666667/4.716666666666667/4.766666666666667/4.766666666666667/4.416666666666667
- mean overall (avg R/H/S/D/K): 4.666666666666667
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.25, hallucination_suspected=0.00

## Mean scores by strategy (snapshot)
### S0 (n=30)
- mean runtime: 8.469533333333334
- mean R/H/S/D/K: 3.8333333333333335/3.966666666666667/4.0/4.133333333333334/2.6333333333333333
- mean overall (avg R/H/S/D/K): 3.7133333333333334
### S0_RAW (n=30)
- mean runtime: 10.9467
- mean R/H/S/D/K: 4.9/4.9/4.833333333333333/4.966666666666667/4.8
- mean overall (avg R/H/S/D/K): 4.88
### S0_UNSTRUCTURED (n=30)
- mean runtime: 11.530866666666666
- mean R/H/S/D/K: 4.433333333333334/4.533333333333333/4.7/4.566666666666666/4.033333333333333
- mean overall (avg R/H/S/D/K): 4.453333333333333
### S1 (n=30)
- mean runtime: 11.704066666666668
- mean R/H/S/D/K: 4.933333333333334/4.933333333333334/4.833333333333333/4.966666666666667/4.633333333333334
- mean overall (avg R/H/S/D/K): 4.86
### S2 (n=30)
- mean runtime: 9.725533333333335
- mean R/H/S/D/K: 5.0/5.0/4.866666666666666/4.933333333333334/5.0
- mean overall (avg R/H/S/D/K): 4.96

## Top missing elements (max 20)
- Offline-Workflow nicht explizit erwähnt: 2
- Offline-Workflow (nicht erwartbar, da CONTEXT minimal): 2
- Offline-Workflow nicht explizit (spotty connectivity vorhanden): 2
- Offline-Workflow (nicht erwartbar, da connectivity nicht im Context): 2
- Offline-Workflow nicht explizit erwähnt (obwohl offline im Context): 2
- Explizite Erwähnung Offline-Workflow bei spotty connectivity: 2
- Offline-Workflow nicht adressiert: 1
- Fehlinterpretation device-Status: 1
- Offline-Workflow (nicht erwartbar, da CONTEXT kein connectivity-Signal enthält): 1
- GPS-Koordinaten (nicht im CONTEXT vorhanden, daher kein Fehler): 1
- Offline-Workflow nicht explizit (connectivity=offline im CONTEXT): 1
- Offline-Workflow nicht explizit erwähnt (aber offline im CONTEXT): 1
- Keine Nutzung der Asset-ID im Kontext (nur minimal vorhanden): 1
- Keine Erwähnung intermittierender Fehler-Muster: 1
- Keine Priorisierung auf Stoßzeit-Beobachtung: 1
- Unstrukturierter Kontext erschwert Nachvollziehbarkeit: 1
- Offline-Workflow (nicht erwartbar, da connectivity nicht im CONTEXT): 1
- Kontext-Nutzung minimal: 1
- Explizite Offline-Sync-Anweisung könnte klarer sein: 1
- Offline-Workflow nicht explizit (spotty im CONTEXT, aber nicht klar adressiert): 1
