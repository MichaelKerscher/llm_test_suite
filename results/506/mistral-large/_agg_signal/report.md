# Aggregation Report (506/mistral-large) [signal]
- judge_version filter: **judge_v1_1**
- Tests (latest runs): **150**
- Incidents with any deltas: **30**

## Mean scores by context level (snapshot)
### L0 (n=30)
- mean runtime: 9.244866666666667
- mean R/H/S/D/K: 3.933333333333333/3.933333333333333/4.133333333333334/4.2/2.566666666666667
- mean overall (avg R/H/S/D/K): 3.753333333333333
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.00, hallucination_suspected=0.37
### L2 (n=30)
- mean runtime: 12.760700000000002
- mean R/H/S/D/K: 4.9/4.9/4.933333333333334/4.933333333333334/4.633333333333334
- mean overall (avg R/H/S/D/K): 4.86
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.20, hallucination_suspected=0.00
### L2B (n=30)
- mean runtime: 11.3567
- mean R/H/S/D/K: 4.966666666666667/4.966666666666667/4.966666666666667/5.0/5.0
- mean overall (avg R/H/S/D/K): 4.98
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.53, hallucination_suspected=0.00
### unknown (n=60)
- mean runtime: 11.411033333333334
- mean R/H/S/D/K: 4.583333333333333/4.616666666666666/4.75/4.716666666666667/4.3
- mean overall (avg R/H/S/D/K): 4.593333333333334
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.22, hallucination_suspected=0.00

## Mean scores by strategy (snapshot)
### S0 (n=30)
- mean runtime: 9.244866666666667
- mean R/H/S/D/K: 3.933333333333333/3.933333333333333/4.133333333333334/4.2/2.566666666666667
- mean overall (avg R/H/S/D/K): 3.753333333333333
### S0_RAW (n=30)
- mean runtime: 11.795533333333333
- mean R/H/S/D/K: 4.9/4.933333333333334/4.933333333333334/5.0/4.766666666666667
- mean overall (avg R/H/S/D/K): 4.906666666666666
### S0_UNSTRUCTURED (n=30)
- mean runtime: 11.026533333333333
- mean R/H/S/D/K: 4.266666666666667/4.3/4.566666666666666/4.433333333333334/3.8333333333333335
- mean overall (avg R/H/S/D/K): 4.28
### S1 (n=30)
- mean runtime: 12.760700000000002
- mean R/H/S/D/K: 4.9/4.9/4.933333333333334/4.933333333333334/4.633333333333334
- mean overall (avg R/H/S/D/K): 4.86
### S2 (n=30)
- mean runtime: 11.3567
- mean R/H/S/D/K: 4.966666666666667/4.966666666666667/4.966666666666667/5.0/5.0
- mean overall (avg R/H/S/D/K): 4.98

## Top missing elements (max 20)
- offline_workflow: 4
- offline_workflow_explicit: 4
- Offline-Workflow nicht explizit erwähnt: 2
- Kontextnutzung minimal: 2
- Offline-Workflow (nicht erwartbar, da connectivity nicht im CONTEXT): 2
- Offline-Workflow (nicht erwartbar, da connectivity nicht im Context): 2
- Offline-Workflow (nicht erwartbar, da CONTEXT kein offline-Signal enthält): 2
- Keine GPS-Koordinaten erwähnt (nicht im CONTEXT vorhanden, daher kein Fehler): 1
- Keine explizite Erwähnung von Stoßzeit/rush_hour (nicht im CONTEXT, daher kein Fehler): 1
- Keine explizite Erwähnung von 'signal_stuck' als Fehlertyp (im CONTEXT vorhanden, aber nicht zwingend zu nennen): 1
- Keine Offline-Workflow-Erwähnung (aber nicht erwartbar bei minimalem Context): 1
- Keine explizite Priorisierung bei mehreren Signalgebern: 1
- Keine explizite Erwähnung des low_battery-Status des Geräts: 1
- Spekulation über Komponenten ohne Basis: 1
- GPS-Koordinaten nicht explizit dokumentiert: 1
- Spezifische Kontextnutzung (nur Asset-ID vorhanden): 1
- Offline-Workflow (spotty connectivity im CONTEXT, aber nicht explizit adressiert): 1
- Keine Nutzung der Asset-ID im Kontext (nur minimal vorhanden): 1
- Keine Erwähnung von GPS/Koordinaten (nicht im CONTEXT): 1
- Keine explizite Erwähnung von Foto-Dokumentation trotz Foto-Hinweis im User message: 1
