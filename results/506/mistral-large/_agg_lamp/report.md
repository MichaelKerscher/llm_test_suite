# Aggregation Report (506/mistral-large) [lamp]
- judge_version filter: **judge_v1_1**
- Tests (latest runs): **270**
- Incidents with any deltas: **30**

## Mean scores by context level (snapshot)
### L0 (n=30)
- mean runtime: 7.024966666666667
- mean R/H/S/D/K: 3.466666666666667/3.7333333333333334/3.7666666666666666/4.1/2.466666666666667
- mean overall (avg R/H/S/D/K): 3.506666666666667
- flags (rate): safety_first=0.93, escalation_present=1.00, offline_workflow_mentioned=0.00, hallucination_suspected=0.07
### L2 (n=30)
- mean runtime: 9.192966666666667
- mean R/H/S/D/K: 4.833333333333333/4.733333333333333/4.8/4.9/4.433333333333334
- mean overall (avg R/H/S/D/K): 4.739999999999999
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.17, hallucination_suspected=0.03
### L2B (n=30)
- mean runtime: 10.455033333333335
- mean R/H/S/D/K: 5.0/5.0/4.933333333333334/5.0/5.0
- mean overall (avg R/H/S/D/K): 4.986666666666666
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.60, hallucination_suspected=0.00
### unknown (n=180)
- mean runtime: 9.115744444444445
- mean R/H/S/D/K: 4.722222222222222/4.711111111111111/4.772222222222222/4.861111111111111/4.694444444444445
- mean overall (avg R/H/S/D/K): 4.752222222222222
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.41, hallucination_suspected=0.00

## Mean scores by strategy (snapshot)
### S0 (n=30)
- mean runtime: 7.024966666666667
- mean R/H/S/D/K: 3.466666666666667/3.7333333333333334/3.7666666666666666/4.1/2.466666666666667
- mean overall (avg R/H/S/D/K): 3.506666666666667
### S0_RAW (n=30)
- mean runtime: 8.7006
- mean R/H/S/D/K: 4.6/4.533333333333333/4.666666666666667/4.866666666666666/4.5
- mean overall (avg R/H/S/D/K): 4.633333333333334
### S0_UNSTRUCTURED (n=30)
- mean runtime: 9.301266666666667
- mean R/H/S/D/K: 4.333333333333333/4.3/4.6/4.5/3.8
- mean overall (avg R/H/S/D/K): 4.306666666666667
### S1 (n=30)
- mean runtime: 9.192966666666667
- mean R/H/S/D/K: 4.833333333333333/4.733333333333333/4.8/4.9/4.433333333333334
- mean overall (avg R/H/S/D/K): 4.739999999999999
### S2 (n=30)
- mean runtime: 10.455033333333335
- mean R/H/S/D/K: 5.0/5.0/4.933333333333334/5.0/5.0
- mean overall (avg R/H/S/D/K): 4.986666666666666
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
- offline_workflow: 5
- Keine Nutzung der Asset-ID im Kontext: 3
- Kontextnutzung minimal (nur Asset-ID): 3
- Keine explizite Erwähnung des Foto-Workflows: 2
- Offline-Workflow (nicht erwartbar, da connectivity nicht im CONTEXT): 2
- Kein expliziter Offline-Workflow trotz spotty connectivity: 2
- offline_workflow_explicit: 2
- Klare Stop-Condition für Beobachtungsphase fehlt: 1
- Offline-Workflow nicht erwähnt trotz offline im Kontext: 1
- Halluzination: 'Smart-Lighting-System' nicht im Kontext: 1
- Offline-Workflow nicht erwähnt trotz offline/low_battery im Kontext: 1
- Keine Priorisierung auf intermittent fault: 1
- Zu generisch für minimalen Kontext: 1
- Schweregrad 'mittel' könnte stärker priorisiert werden: 1
- Unstrukturierter Kontext erschwert Parsing: 1
- Explizite Erwähnung der Asset-ID (n4427359783) in Dokumentation: 1
- Keine Nutzung von Kontext-Signalen (nur Asset-ID vorhanden): 1
- Keine Anpassung an Umgebung/Gerätezustand (nicht erwartbar bei L0): 1
- Offline-Workflow nicht explizit (spotty connectivity + low_battery im Kontext): 1
- Offline-Workflow nicht explizit genannt (spotty connectivity + low_battery im Kontext): 1
