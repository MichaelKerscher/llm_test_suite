# Aggregation Report (506/mistral-large) [signal]
- judge_version filter: **judge_v1_1**
- Tests (latest runs): **150**
- Incidents with any deltas: **30**

## Mean scores by context level (snapshot)
### L0 (n=30)
- mean runtime: 9.6699
- mean R/H/S/D/K: 3.9/3.966666666666667/4.0/4.166666666666667/2.566666666666667
- mean overall (avg R/H/S/D/K): 3.7199999999999998
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.00, hallucination_suspected=0.33
### L2 (n=30)
- mean runtime: 11.287866666666668
- mean R/H/S/D/K: 5.0/4.9/4.9/4.933333333333334/4.6
- mean overall (avg R/H/S/D/K): 4.866666666666666
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.17, hallucination_suspected=0.00
### L2B (n=30)
- mean runtime: 11.074333333333334
- mean R/H/S/D/K: 4.966666666666667/4.966666666666667/4.966666666666667/4.933333333333334/4.966666666666667
- mean overall (avg R/H/S/D/K): 4.96
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.53, hallucination_suspected=0.00
### unknown (n=60)
- mean runtime: 11.318333333333333
- mean R/H/S/D/K: 4.683333333333334/4.666666666666667/4.75/4.783333333333333/4.2
- mean overall (avg R/H/S/D/K): 4.616666666666666
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.20, hallucination_suspected=0.00

## Mean scores by strategy (snapshot)
### S0 (n=30)
- mean runtime: 9.6699
- mean R/H/S/D/K: 3.9/3.966666666666667/4.0/4.166666666666667/2.566666666666667
- mean overall (avg R/H/S/D/K): 3.7199999999999998
### S0_RAW (n=30)
- mean runtime: 11.242266666666666
- mean R/H/S/D/K: 4.833333333333333/4.8/4.866666666666666/4.9/4.5
- mean overall (avg R/H/S/D/K): 4.78
### S0_UNSTRUCTURED (n=30)
- mean runtime: 11.3944
- mean R/H/S/D/K: 4.533333333333333/4.533333333333333/4.633333333333334/4.666666666666667/3.9
- mean overall (avg R/H/S/D/K): 4.453333333333333
### S1 (n=30)
- mean runtime: 11.287866666666668
- mean R/H/S/D/K: 5.0/4.9/4.9/4.933333333333334/4.6
- mean overall (avg R/H/S/D/K): 4.866666666666666
### S2 (n=30)
- mean runtime: 11.074333333333334
- mean R/H/S/D/K: 4.966666666666667/4.966666666666667/4.966666666666667/4.933333333333334/4.966666666666667
- mean overall (avg R/H/S/D/K): 4.96

## Top missing elements (max 20)
- offline_workflow_explicit: 7
- offline_workflow: 5
- Kontextnutzung minimal (nur Asset-ID): 4
- Keine Kontextnutzung (nur Asset-ID vorhanden): 2
- Keine Anpassung an Umgebungsbedingungen: 2
- Keine Nutzung der Asset-ID im Kontext: 2
- Offline-Workflow (connectivity=spotty → erwartbar, aber nicht erwähnt): 2
- Offline-Workflow explizit genannt: 1
- Offline-Workflow explizit erwähnt: 1
- Keine explizite Erwähnung poor_visibility/Schnee in Safety-Maßnahmen: 1
- Keine klare Priorisierung der Beobachtung während Hauptverkehrszeit: 1
- Intermittierender Fehler nicht explizit als Diagnose-Schwerpunkt hervorgehoben: 1
- Intermittierender Fehler könnte stärker als Diagnose-Schwerpunkt betont werden: 1
- Annahme 'Straßenlampe/Ampel' nicht im Context begründet: 1
- Offline-Workflow (spotty connectivity erwähnt, aber kein Workflow): 1
- Offline-Workflow (instabile Konnektivität erwähnt, aber kein Workflow): 1
- Kein expliziter Hinweis auf lokale Speicherung: 1
- Offline-Workflow (spotty connectivity im Context): 1
- Kontextnutzung teilweise generisch (unstructured schwer lesbar): 1
- Keine Offline-Workflow-Erwähnung nötig (online): 1
