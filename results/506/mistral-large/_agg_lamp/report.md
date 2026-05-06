# Aggregation Report (506/mistral-large) [lamp]
- judge_version filter: **judge_v1_1**
- Tests (latest runs): **270**
- Incidents with any deltas: **30**

## Mean scores by context level (snapshot)
### L0 (n=30)
- mean runtime: 7.498966666666666
- mean R/H/S/D/K: 3.5/3.7666666666666666/3.7333333333333334/4.1/2.433333333333333
- mean overall (avg R/H/S/D/K): 3.506666666666667
- flags (rate): safety_first=0.97, escalation_present=1.00, offline_workflow_mentioned=0.00, hallucination_suspected=0.23
### L2 (n=30)
- mean runtime: 10.274933333333333
- mean R/H/S/D/K: 4.866666666666666/4.866666666666666/4.866666666666666/5.0/4.466666666666667
- mean overall (avg R/H/S/D/K): 4.8133333333333335
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.07, hallucination_suspected=0.00
### L2B (n=30)
- mean runtime: 10.645433333333333
- mean R/H/S/D/K: 4.9/4.866666666666666/4.833333333333333/4.9/4.966666666666667
- mean overall (avg R/H/S/D/K): 4.8933333333333335
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.60, hallucination_suspected=0.00
### unknown (n=180)
- mean runtime: 9.192105555555555
- mean R/H/S/D/K: 4.727777777777778/4.733333333333333/4.761111111111111/4.872222222222222/4.722222222222222
- mean overall (avg R/H/S/D/K): 4.763333333333334
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.41, hallucination_suspected=0.00

## Mean scores by strategy (snapshot)
### S0 (n=30)
- mean runtime: 7.498966666666666
- mean R/H/S/D/K: 3.5/3.7666666666666666/3.7333333333333334/4.1/2.433333333333333
- mean overall (avg R/H/S/D/K): 3.506666666666667
### S0_RAW (n=30)
- mean runtime: 9.243333333333334
- mean R/H/S/D/K: 4.666666666666667/4.633333333333334/4.733333333333333/4.866666666666666/4.7
- mean overall (avg R/H/S/D/K): 4.72
### S0_UNSTRUCTURED (n=30)
- mean runtime: 9.2167
- mean R/H/S/D/K: 4.3/4.333333333333333/4.466666666666667/4.566666666666666/3.7666666666666666
- mean overall (avg R/H/S/D/K): 4.286666666666666
### S1 (n=30)
- mean runtime: 10.274933333333333
- mean R/H/S/D/K: 4.866666666666666/4.866666666666666/4.866666666666666/5.0/4.466666666666667
- mean overall (avg R/H/S/D/K): 4.8133333333333335
### S2 (n=30)
- mean runtime: 10.645433333333333
- mean R/H/S/D/K: 4.9/4.866666666666666/4.833333333333333/4.9/4.966666666666667
- mean overall (avg R/H/S/D/K): 4.8933333333333335
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
- offline_workflow: 8
- offline_workflow_explicit: 3
- Kontextnutzung minimal (nur Asset-ID): 2
- Offline-Workflow trotz spotty connectivity: 2
- Offline-Workflow fehlt (spotty connectivity im Context): 2
- Klare Stop-Condition für Beobachtungsphase fehlt: 1
- Offline-Workflow nicht erwähnt (kein Signal im CONTEXT): 1
- Keine Priorisierung bei sporadischem Fehler: 1
- Offline-Workflow nicht explizit erwähnt trotz offline/low_battery: 1
- Offline-Workflow nicht explizit erwähnt trotz offline/low_battery im CONTEXT: 1
- Keine Nutzung der Asset-ID im Text: 1
- Keine Erwähnung von Koordinaten/Standort (nur ID gegeben): 1
- Keine spezifische Anpassung an Kontext (generisch): 1
- Etwas weniger detailliert bei Dokumentation als TC2/TC4: 1
- Unstrukturierter Kontext erschwert Parsing, aber gut verarbeitet: 1
- Explizite Erwähnung der Asset-ID (n4427359783) in Dokumentation: 1
- Offline-Workflow nicht erwartbar (connectivity nicht im Context): 1
- Offline-Workflow nicht erwähnt trotz 'spotty' connectivity: 1
- Offline-Workflow nicht erwähnt trotz 'Konnektivität instabil' im Context: 1
- Offline-Workflow nicht erwähnt trotz 'spotty' connectivity im Context: 1
