# Aggregation Report (506/gpt-4.1) [lamp]
- judge_version filter: **judge_v1_1**
- Tests (latest runs): **270**
- Incidents with any deltas: **30**

## Mean scores by context level (snapshot)
### L0 (n=30)
- mean runtime: 8.4004
- mean R/H/S/D/K: 3.5/3.6666666666666665/3.7/3.933333333333333/2.433333333333333
- mean overall (avg R/H/S/D/K): 3.4466666666666668
- flags (rate): safety_first=0.97, escalation_present=1.00, offline_workflow_mentioned=0.00, hallucination_suspected=0.10
### L2 (n=30)
- mean runtime: 10.797866666666666
- mean R/H/S/D/K: 4.9/4.8/4.9/4.866666666666666/4.366666666666666
- mean overall (avg R/H/S/D/K): 4.766666666666667
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.03, hallucination_suspected=0.00
### L2B (n=30)
- mean runtime: 11.681266666666666
- mean R/H/S/D/K: 5.0/4.966666666666667/4.966666666666667/5.0/5.0
- mean overall (avg R/H/S/D/K): 4.986666666666666
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.60, hallucination_suspected=0.00
### unknown (n=180)
- mean runtime: 11.16755
- mean R/H/S/D/K: 4.722222222222222/4.705555555555556/4.727777777777778/4.816666666666666/4.655555555555556
- mean overall (avg R/H/S/D/K): 4.725555555555555
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.39, hallucination_suspected=0.01

## Mean scores by strategy (snapshot)
### S0 (n=30)
- mean runtime: 8.4004
- mean R/H/S/D/K: 3.5/3.6666666666666665/3.7/3.933333333333333/2.433333333333333
- mean overall (avg R/H/S/D/K): 3.4466666666666668
### S0_RAW (n=30)
- mean runtime: 10.3806
- mean R/H/S/D/K: 4.5/4.5/4.533333333333333/4.666666666666667/4.4
- mean overall (avg R/H/S/D/K): 4.52
### S0_UNSTRUCTURED (n=30)
- mean runtime: 11.901766666666667
- mean R/H/S/D/K: 4.366666666666666/4.433333333333334/4.533333333333333/4.5/3.6666666666666665
- mean overall (avg R/H/S/D/K): 4.3
### S1 (n=30)
- mean runtime: 10.797866666666666
- mean R/H/S/D/K: 4.9/4.8/4.9/4.866666666666666/4.366666666666666
- mean overall (avg R/H/S/D/K): 4.766666666666667
### S2 (n=30)
- mean runtime: 11.681266666666666
- mean R/H/S/D/K: 5.0/4.966666666666667/4.966666666666667/5.0/5.0
- mean overall (avg R/H/S/D/K): 4.986666666666666
### S2_ABL_NOASSET (n=30)
- mean runtime: 10.9962
- mean R/H/S/D/K: 4.9/4.933333333333334/4.933333333333334/4.9/4.966666666666667
- mean overall (avg R/H/S/D/K): 4.926666666666667
### S2_ABL_NODEV (n=30)
- mean runtime: 10.410633333333333
- mean R/H/S/D/K: 4.933333333333334/4.8/4.766666666666667/4.933333333333334/4.966666666666667
- mean overall (avg R/H/S/D/K): 4.88
### S2_ABL_NOENV (n=30)
- mean runtime: 11.9838
- mean R/H/S/D/K: 4.8/4.666666666666667/4.7/4.9/4.966666666666667
- mean overall (avg R/H/S/D/K): 4.806666666666667
### S2_ABL_NOINC (n=30)
- mean runtime: 11.3323
- mean R/H/S/D/K: 4.833333333333333/4.9/4.9/5.0/4.966666666666667
- mean overall (avg R/H/S/D/K): 4.92

## Top missing elements (max 20)
- offline_workflow: 5
- Offline-Workflow nicht explizit genannt: 2
- Offline-Workflow nicht explizit erwähnt: 2
- Offline-Workflow bei spotty connectivity nicht explizit erwähnt: 2
- Offline-Workflow nicht explizit (spotty connectivity im Kontext): 2
- Spezifische Stop-Conditions für Beobachtungsphase: 2
- Offline-Workflow nicht explizit trotz spotty connectivity: 2
- Offline-Workflow nicht erwähnt trotz 'spotty connectivity' im Kontext: 2
- Keine Nutzung von Kontext (nur Asset-ID vorhanden): 2
- Klare Stop-Condition für Beobachtungsphase: 1
- Konkrete Zeitangabe für Wiederholungsprüfung: 1
- Explizite Stop-Condition für Beobachtungsphase: 1
- Offline-Workflow (nicht erwartbar, da kein Signal im CONTEXT): 1
- Kontextnutzung minimal (nur asset_osm): 1
- Offline-Workflow nicht explizit (trotz offline-Signal): 1
- Offline-Workflow nicht explizit (trotz offline-Signal im CONTEXT): 1
- Keine Nutzung der Asset-ID im Text: 1
- Keine Erwähnung von Foto-Workflow (obwohl nicht im Context): 1
- Generische Schritte ohne spezifische Kontextanpassung: 1
- Unstructured-Format erschwert Parsing, aber Modell extrahiert gut: 1
