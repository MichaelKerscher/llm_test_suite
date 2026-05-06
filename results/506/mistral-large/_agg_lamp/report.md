# Aggregation Report (506/mistral-large) [lamp]
- judge_version filter: **judge_v1_1**
- Tests (latest runs): **270**
- Incidents with any deltas: **30**

## Mean scores by context level (snapshot)
### L0 (n=30)
- mean runtime: 6.6658
- mean R/H/S/D/K: 3.5/3.7666666666666666/3.6333333333333333/4.033333333333333/2.433333333333333
- mean overall (avg R/H/S/D/K): 3.4733333333333336
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.00, hallucination_suspected=0.03
### L2 (n=30)
- mean runtime: 9.658999999999999
- mean R/H/S/D/K: 4.866666666666666/4.8/4.8/4.866666666666666/4.4
- mean overall (avg R/H/S/D/K): 4.746666666666667
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.03, hallucination_suspected=0.00
### L2B (n=30)
- mean runtime: 10.204533333333334
- mean R/H/S/D/K: 4.966666666666667/4.966666666666667/4.866666666666666/4.966666666666667/5.0
- mean overall (avg R/H/S/D/K): 4.953333333333333
- flags (rate): safety_first=0.97, escalation_present=1.00, offline_workflow_mentioned=0.60, hallucination_suspected=0.00
### unknown (n=180)
- mean runtime: 9.25848888888889
- mean R/H/S/D/K: 4.75/4.75/4.75/4.888888888888889/4.738888888888889
- mean overall (avg R/H/S/D/K): 4.775555555555556
- flags (rate): safety_first=0.99, escalation_present=1.00, offline_workflow_mentioned=0.40, hallucination_suspected=0.00

## Mean scores by strategy (snapshot)
### S0 (n=30)
- mean runtime: 6.6658
- mean R/H/S/D/K: 3.5/3.7666666666666666/3.6333333333333333/4.033333333333333/2.433333333333333
- mean overall (avg R/H/S/D/K): 3.4733333333333336
### S0_RAW (n=30)
- mean runtime: 8.958533333333332
- mean R/H/S/D/K: 4.666666666666667/4.633333333333334/4.633333333333334/4.9/4.533333333333333
- mean overall (avg R/H/S/D/K): 4.673333333333333
### S0_UNSTRUCTURED (n=30)
- mean runtime: 9.8998
- mean R/H/S/D/K: 4.433333333333334/4.433333333333334/4.5/4.633333333333334/4.033333333333333
- mean overall (avg R/H/S/D/K): 4.406666666666666
### S1 (n=30)
- mean runtime: 9.658999999999999
- mean R/H/S/D/K: 4.866666666666666/4.8/4.8/4.866666666666666/4.4
- mean overall (avg R/H/S/D/K): 4.746666666666667
### S2 (n=30)
- mean runtime: 10.204533333333334
- mean R/H/S/D/K: 4.966666666666667/4.966666666666667/4.866666666666666/4.966666666666667/5.0
- mean overall (avg R/H/S/D/K): 4.953333333333333
### S2_ABL_NOASSET (n=30)
- mean runtime: 9.7382
- mean R/H/S/D/K: 4.866666666666666/4.9/4.866666666666666/4.933333333333334/4.966666666666667
- mean overall (avg R/H/S/D/K): 4.906666666666666
### S2_ABL_NODEV (n=30)
- mean runtime: 9.3244
- mean R/H/S/D/K: 4.966666666666667/4.933333333333334/4.866666666666666/5.0/4.966666666666667
- mean overall (avg R/H/S/D/K): 4.946666666666667
### S2_ABL_NOENV (n=30)
- mean runtime: 8.850366666666668
- mean R/H/S/D/K: 4.833333333333333/4.766666666666667/4.7/4.9/4.933333333333334
- mean overall (avg R/H/S/D/K): 4.826666666666667
### S2_ABL_NOINC (n=30)
- mean runtime: 8.779633333333333
- mean R/H/S/D/K: 4.733333333333333/4.833333333333333/4.933333333333334/4.966666666666667/5.0
- mean overall (avg R/H/S/D/K): 4.8933333333333335

## Top missing elements (max 20)
- Keine Nutzung des Kontexts (nur Asset-ID vorhanden): 4
- Kontextnutzung minimal (nur Asset-ID): 3
- offline_workflow: 3
- Offline-Workflow nicht explizit trotz 'spotty' connectivity: 2
- Keine Erwähnung von Offline-Workflow trotz fehlender Konnektivitätsinfo: 2
- Kein Offline-Workflow trotz 'spotty' Konnektivität: 2
- Keine Erwähnung der schwachen Batterie im Handlungskontext: 2
- Offline-Workflow (nicht erwartbar, da connectivity nicht im CONTEXT): 2
- Keine Nutzung der Asset-ID im Kontext: 2
- Klare Stop-Condition für Beobachtungsphase fehlt: 1
- Offline-Workflow nicht erwähnt, obwohl nicht im Kontext gefordert: 1
- Offline-Workflow nicht explizit trotz offline/low_battery im Kontext: 1
- Safety-first nicht als Schritt 1 erkennbar: 1
- Offline-Workflow nicht explizit erwähnt trotz offline-Signal: 1
- Keine Anpassung an tatsächliche Umgebungsbedingungen: 1
- Generische Checkliste ohne Fallbezug: 1
- Keine explizite Priorisierung der Feuchtigkeitsflecken-Untersuchung als ersten Diagnoseschritt: 1
- Explizite Erwähnung der Asset-ID (n4427359783) in Dokumentation: 1
- Keine Anpassung an Umgebungsbedingungen: 1
- Keine Offline-Workflow-Erwähnung trotz fehlendem Kontext: 1
