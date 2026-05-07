# Aggregation Report (506/mistral-large) [signal]
- judge_version filter: **judge_v1_1**
- Tests (latest runs): **150**
- Incidents with any deltas: **30**

## Mean scores by context level (snapshot)
### L0 (n=30)
- mean runtime: 8.319333333333333
- mean R/H/S/D/K: 3.9/3.966666666666667/4.2/4.2/2.6
- mean overall (avg R/H/S/D/K): 3.7733333333333334
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.00, hallucination_suspected=0.27
### L2 (n=30)
- mean runtime: 12.2521
- mean R/H/S/D/K: 4.966666666666667/4.933333333333334/4.933333333333334/4.933333333333334/4.533333333333333
- mean overall (avg R/H/S/D/K): 4.86
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.17, hallucination_suspected=0.03
### L2B (n=30)
- mean runtime: 10.477733333333333
- mean R/H/S/D/K: 5.0/5.0/4.966666666666667/5.0/5.0
- mean overall (avg R/H/S/D/K): 4.993333333333334
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.53, hallucination_suspected=0.00
### unknown (n=60)
- mean runtime: 11.869750000000002
- mean R/H/S/D/K: 4.7/4.733333333333333/4.833333333333333/4.85/4.433333333333334
- mean overall (avg R/H/S/D/K): 4.71
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.23, hallucination_suspected=0.02

## Mean scores by strategy (snapshot)
### S0 (n=30)
- mean runtime: 8.319333333333333
- mean R/H/S/D/K: 3.9/3.966666666666667/4.2/4.2/2.6
- mean overall (avg R/H/S/D/K): 3.7733333333333334
### S0_RAW (n=30)
- mean runtime: 11.453166666666668
- mean R/H/S/D/K: 4.933333333333334/4.933333333333334/4.933333333333334/4.966666666666667/4.866666666666666
- mean overall (avg R/H/S/D/K): 4.926666666666667
### S0_UNSTRUCTURED (n=30)
- mean runtime: 12.286333333333335
- mean R/H/S/D/K: 4.466666666666667/4.533333333333333/4.733333333333333/4.733333333333333/4.0
- mean overall (avg R/H/S/D/K): 4.493333333333334
### S1 (n=30)
- mean runtime: 12.2521
- mean R/H/S/D/K: 4.966666666666667/4.933333333333334/4.933333333333334/4.933333333333334/4.533333333333333
- mean overall (avg R/H/S/D/K): 4.86
### S2 (n=30)
- mean runtime: 10.477733333333333
- mean R/H/S/D/K: 5.0/5.0/4.966666666666667/5.0/5.0
- mean overall (avg R/H/S/D/K): 4.993333333333334

## Top missing elements (max 20)
- offline_workflow: 3
- offline_workflow_explicit: 3
- Offline-Workflow nicht erwartbar: 2
- Offline-Workflow (nicht erwartbar, da connectivity nicht im CONTEXT): 2
- Offline-Workflow (spotty connectivity im CONTEXT, aber nicht explizit erwähnt): 2
- Offline-Workflow (nicht erwartbar, da CONTEXT minimal): 1
- Batterie-Hinweis (nicht im CONTEXT): 1
- Offline-Workflow explizit (erkennbar aus CONTEXT, aber nicht klar adressiert): 1
- Offline-Workflow (nicht erwartbar, da CONTEXT kein connectivity-Signal enthält): 1
- Konkrete GPS-Koordinaten (nicht im CONTEXT vorhanden, daher kein Fehler): 1
- Offline-Workflow nicht explizit erwähnt (obwohl connectivity=offline im CONTEXT): 1
- Offline-Workflow nicht explizit erwähnt (obwohl 'offline' im _unstructured_text steht): 1
- Keine Kontextnutzung (nur Asset-ID vorhanden): 1
- Keine Erwähnung von Umgebungsbedingungen: 1
- Gerätebatterie-Hinweis könnte expliziter auf Workflow-Implikationen eingehen: 1
- Batterie-Hinweis könnte klarer auf Gerät vs. Anlage eingehen: 1
- Kontext-Nutzung (GPS, Koordinaten, Umgebung): 1
- Explizite GPS-Nutzung: 1
- Stoßzeit/Verkehr im Kontext weniger sichtbar: 1
- Keine explizite Erwähnung 'Kreuzung wie unbeschrankt behandeln': 1
