# Aggregation Report (506/gemini-2.5-flash) [signal]
- judge_version filter: **judge_v1_1**
- Tests (latest runs): **150**
- Incidents with any deltas: **30**

## Mean scores by context level (snapshot)
### L0 (n=30)
- mean runtime: 8.354033333333334
- mean R/H/S/D/K: 3.933333333333333/3.933333333333333/4.233333333333333/4.3/2.6
- mean overall (avg R/H/S/D/K): 3.8
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.00, hallucination_suspected=0.30
### L2 (n=30)
- mean runtime: 10.923399999999999
- mean R/H/S/D/K: 4.9/4.866666666666666/4.833333333333333/4.966666666666667/4.633333333333334
- mean overall (avg R/H/S/D/K): 4.84
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.13, hallucination_suspected=0.00
### L2B (n=30)
- mean runtime: 9.738866666666667
- mean R/H/S/D/K: 4.966666666666667/4.933333333333334/4.933333333333334/4.966666666666667/5.0
- mean overall (avg R/H/S/D/K): 4.96
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.60, hallucination_suspected=0.00
### unknown (n=60)
- mean runtime: 10.596666666666666
- mean R/H/S/D/K: 4.616666666666666/4.6/4.766666666666667/4.783333333333333/4.283333333333333
- mean overall (avg R/H/S/D/K): 4.61
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.27, hallucination_suspected=0.00

## Mean scores by strategy (snapshot)
### S0 (n=30)
- mean runtime: 8.354033333333334
- mean R/H/S/D/K: 3.933333333333333/3.933333333333333/4.233333333333333/4.3/2.6
- mean overall (avg R/H/S/D/K): 3.8
### S0_RAW (n=30)
- mean runtime: 10.151333333333334
- mean R/H/S/D/K: 4.833333333333333/4.8/4.833333333333333/4.966666666666667/4.633333333333334
- mean overall (avg R/H/S/D/K): 4.8133333333333335
### S0_UNSTRUCTURED (n=30)
- mean runtime: 11.042
- mean R/H/S/D/K: 4.4/4.4/4.7/4.6/3.933333333333333
- mean overall (avg R/H/S/D/K): 4.406666666666666
### S1 (n=30)
- mean runtime: 10.923399999999999
- mean R/H/S/D/K: 4.9/4.866666666666666/4.833333333333333/4.966666666666667/4.633333333333334
- mean overall (avg R/H/S/D/K): 4.84
### S2 (n=30)
- mean runtime: 9.738866666666667
- mean R/H/S/D/K: 4.966666666666667/4.933333333333334/4.933333333333334/4.966666666666667/5.0
- mean overall (avg R/H/S/D/K): 4.96

## Top missing elements (max 20)
- Offline-Workflow (nicht erwartbar aus CONTEXT): 2
- Kontext-Nutzung minimal (nur Asset-ID): 2
- Kontextnutzung minimal (nur Asset-ID vorhanden): 2
- Keine Nutzung der Asset-ID im Kontext: 2
- Kontextnutzung minimal (nur Asset-ID): 2
- Offline-Workflow nicht explizit erwähnt (spotty connectivity im Kontext): 2
- Offline-Workflow bei spotty connectivity: 2
- offline workflow explicit: 2
- offline_workflow_explicit: 2
- Kein Offline-Workflow (aber connectivity=online, daher nicht erwartbar): 2
- Offline-Workflow (nicht erwartbar, da connectivity=online): 2
- Spekulation über Marderbiss ohne Basis: 1
- Multimeter-Prüfung ohne Schulungshinweis im CONTEXT: 1
- Keine wesentlichen Lücken: 1
- Offline-Workflow nicht explizit erwähnt (trotz offline im CONTEXT): 1
- Offline-Workflow explizit: 1
- Offline-Workflow explizit erwähnen: 1
- Halluzinationen: Schaltkasten-Details ohne Kontext-Basis: 1
- Spekulation über Qualifikation/Sicherheit ohne Signal: 1
- Rückfrage am Ende ist gut, aber nicht zwingend nötig: 1
