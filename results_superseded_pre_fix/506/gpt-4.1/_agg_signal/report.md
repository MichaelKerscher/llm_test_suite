# Aggregation Report (506/gpt-4.1) [signal]
- judge_version filter: **judge_v1_1**
- Tests (latest runs): **150**
- Incidents with any deltas: **30**

## Mean scores by context level (snapshot)
### L0 (n=30)
- mean runtime: 8.708266666666667
- mean R/H/S/D/K: 3.933333333333333/4.033333333333333/4.033333333333333/4.233333333333333/2.566666666666667
- mean overall (avg R/H/S/D/K): 3.76
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.00, hallucination_suspected=0.33
### L2 (n=30)
- mean runtime: 11.006766666666666
- mean R/H/S/D/K: 4.866666666666666/4.866666666666666/4.9/4.933333333333334/4.7
- mean overall (avg R/H/S/D/K): 4.8533333333333335
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.17, hallucination_suspected=0.00
### L2B (n=30)
- mean runtime: 10.2169
- mean R/H/S/D/K: 4.966666666666667/4.966666666666667/4.933333333333334/5.0/5.0
- mean overall (avg R/H/S/D/K): 4.973333333333333
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.53, hallucination_suspected=0.00
### unknown (n=60)
- mean runtime: 11.2594
- mean R/H/S/D/K: 4.633333333333334/4.633333333333334/4.8/4.716666666666667/4.3
- mean overall (avg R/H/S/D/K): 4.616666666666666
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.20, hallucination_suspected=0.00

## Mean scores by strategy (snapshot)
### S0 (n=30)
- mean runtime: 8.708266666666667
- mean R/H/S/D/K: 3.933333333333333/4.033333333333333/4.033333333333333/4.233333333333333/2.566666666666667
- mean overall (avg R/H/S/D/K): 3.76
### S0_RAW (n=30)
- mean runtime: 11.305466666666666
- mean R/H/S/D/K: 4.866666666666666/4.866666666666666/4.9/4.933333333333334/4.666666666666667
- mean overall (avg R/H/S/D/K): 4.846666666666667
### S0_UNSTRUCTURED (n=30)
- mean runtime: 11.213333333333333
- mean R/H/S/D/K: 4.4/4.4/4.7/4.5/3.933333333333333
- mean overall (avg R/H/S/D/K): 4.386666666666667
### S1 (n=30)
- mean runtime: 11.006766666666666
- mean R/H/S/D/K: 4.866666666666666/4.866666666666666/4.9/4.933333333333334/4.7
- mean overall (avg R/H/S/D/K): 4.8533333333333335
### S2 (n=30)
- mean runtime: 10.2169
- mean R/H/S/D/K: 4.966666666666667/4.966666666666667/4.933333333333334/5.0/5.0
- mean overall (avg R/H/S/D/K): 4.973333333333333

## Top missing elements (max 20)
- offline_workflow: 3
- Offline-Workflow nicht explizit erwähnt: 3
- Offline-Workflow nicht erwähnt (aber auch nicht im Context signalisiert): 2
- Offline-Workflow nicht explizit erwähnt (trotz offline im Context): 2
- Keine Kontextnutzung (nur Asset-ID vorhanden): 2
- Keine Nutzung der Asset-ID aus Context: 2
- Offline-Workflow bei spotty connectivity: 2
- Keine explizite Erwähnung 'Kreuzung wie unbeschrankt behandeln': 2
- Kontextnutzung minimal (nur Asset-ID): 2
- Kontext-Nutzung minimal (nur Asset-ID): 2
- Offline-Workflow (nicht erwartbar, da connectivity nicht im CONTEXT): 2
- Keine Nutzung der Asset-ID im Kontext: 2
- Offline-Workflow (connectivity=spotty im CONTEXT, aber nicht explizit als Workflow-Anpassung erwähnt): 2
- Offline-Workflow nicht explizit erwähnt (spotty connectivity im Kontext vorhanden): 2
- Offline-Workflow nicht explizit (trotz offline/low_battery im Context): 1
- Offline-Workflow (nicht erwartbar, da connectivity nicht im Context): 1
- GPS-Koordinaten (nicht im Context vorhanden): 1
- Offline-Workflow nicht explizit adressiert (connectivity=offline im Context): 1
- Explizite Offline-Workflow-Erwähnung (offline im Context, aber nicht prominent adressiert): 1
- Keine Erwähnung von Wetter/Sicht/Verkehr (nicht im Context): 1
