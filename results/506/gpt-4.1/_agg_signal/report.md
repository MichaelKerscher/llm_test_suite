# Aggregation Report (506/gpt-4.1) [signal]
- judge_version filter: **judge_v1_1**
- Tests (latest runs): **150**
- Incidents with any deltas: **30**

## Mean scores by context level (snapshot)
### L0 (n=30)
- mean runtime: 8.068133333333334
- mean R/H/S/D/K: 3.8666666666666667/3.8666666666666667/4.166666666666667/4.233333333333333/2.6666666666666665
- mean overall (avg R/H/S/D/K): 3.76
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.00, hallucination_suspected=0.20
### L2 (n=30)
- mean runtime: 10.2897
- mean R/H/S/D/K: 4.933333333333334/4.9/4.933333333333334/4.966666666666667/4.566666666666666
- mean overall (avg R/H/S/D/K): 4.86
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.13, hallucination_suspected=0.00
### L2B (n=30)
- mean runtime: 10.094833333333334
- mean R/H/S/D/K: 4.933333333333334/4.933333333333334/4.9/4.9/4.966666666666667
- mean overall (avg R/H/S/D/K): 4.926666666666667
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.60, hallucination_suspected=0.00
### unknown (n=60)
- mean runtime: 9.967566666666666
- mean R/H/S/D/K: 4.516666666666667/4.5/4.716666666666667/4.65/4.216666666666667
- mean overall (avg R/H/S/D/K): 4.52
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.23, hallucination_suspected=0.00

## Mean scores by strategy (snapshot)
### S0 (n=30)
- mean runtime: 8.068133333333334
- mean R/H/S/D/K: 3.8666666666666667/3.8666666666666667/4.166666666666667/4.233333333333333/2.6666666666666665
- mean overall (avg R/H/S/D/K): 3.76
### S0_RAW (n=30)
- mean runtime: 10.038233333333332
- mean R/H/S/D/K: 4.833333333333333/4.833333333333333/4.833333333333333/4.933333333333334/4.633333333333334
- mean overall (avg R/H/S/D/K): 4.8133333333333335
### S0_UNSTRUCTURED (n=30)
- mean runtime: 9.896899999999999
- mean R/H/S/D/K: 4.2/4.166666666666667/4.6/4.366666666666666/3.8
- mean overall (avg R/H/S/D/K): 4.226666666666667
### S1 (n=30)
- mean runtime: 10.2897
- mean R/H/S/D/K: 4.933333333333334/4.9/4.933333333333334/4.966666666666667/4.566666666666666
- mean overall (avg R/H/S/D/K): 4.86
### S2 (n=30)
- mean runtime: 10.094833333333334
- mean R/H/S/D/K: 4.933333333333334/4.933333333333334/4.9/4.9/4.966666666666667
- mean overall (avg R/H/S/D/K): 4.926666666666667

## Top missing elements (max 20)
- offline_workflow: 5
- Offline-Workflow (spotty connectivity): 3
- Offline-Workflow (spotty connectivity im Kontext): 3
- Keine explizite Erwähnung von 'Kreuzung wie unbeschrankt behandeln': 2
- offline_workflow_explicit: 2
- Keine Nutzung der Asset-ID im Kontext: 2
- Keine explizite Priorisierung nach severity=low: 2
- Offline-Workflow (spotty connectivity im CONTEXT, aber nicht explizit erwähnt): 2
- Offline-Workflow nicht explizit erwähnt: 1
- Keine GPS-Koordinaten erwähnt (nicht im Context): 1
- Kontextnutzung minimal (nur Asset-ID): 1
- Erfindet Details (Wetter, Verkehr, Batterie) nicht im Context: 1
- Keine Anpassung an tatsächlich verfügbare Infos: 1
- Koordinaten nicht explizit dokumentiert: 1
- Offline-Workflow (spotty connectivity erkennbar im unstructured text): 1
- Kreuzung wie unbeschrankt behandeln (explizit): 1
- Gerätestatus erwähnen: 1
- Steuerschrank-Details: 1
- Spannungsprüfung: 1
- Kontextnutzung minimal: 1
