# Aggregation Report (506/gemini-2.5-flash) [lamp]
- judge_version filter: **judge_v1_1**
- Tests (latest runs): **270**
- Incidents with any deltas: **30**

## Mean scores by context level (snapshot)
### L0 (n=30)
- mean runtime: 7.071333333333333
- mean R/H/S/D/K: 3.5/3.8/3.7333333333333334/4.033333333333333/2.433333333333333
- mean overall (avg R/H/S/D/K): 3.5
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.00, hallucination_suspected=0.10
### L2 (n=30)
- mean runtime: 10.342866666666668
- mean R/H/S/D/K: 4.866666666666666/4.8/4.833333333333333/4.9/4.466666666666667
- mean overall (avg R/H/S/D/K): 4.7733333333333325
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.07, hallucination_suspected=0.00
### L2B (n=30)
- mean runtime: 10.019433333333334
- mean R/H/S/D/K: 5.0/5.0/4.866666666666666/5.0/5.0
- mean overall (avg R/H/S/D/K): 4.973333333333333
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.60, hallucination_suspected=0.00
### unknown (n=180)
- mean runtime: 9.467666666666666
- mean R/H/S/D/K: 4.761111111111111/4.7444444444444445/4.761111111111111/4.877777777777778/4.722222222222222
- mean overall (avg R/H/S/D/K): 4.773333333333333
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.39, hallucination_suspected=0.01

## Mean scores by strategy (snapshot)
### S0 (n=30)
- mean runtime: 7.071333333333333
- mean R/H/S/D/K: 3.5/3.8/3.7333333333333334/4.033333333333333/2.433333333333333
- mean overall (avg R/H/S/D/K): 3.5
### S0_RAW (n=30)
- mean runtime: 9.794066666666668
- mean R/H/S/D/K: 4.7/4.633333333333334/4.666666666666667/4.833333333333333/4.533333333333333
- mean overall (avg R/H/S/D/K): 4.673333333333333
### S0_UNSTRUCTURED (n=30)
- mean runtime: 9.739666666666666
- mean R/H/S/D/K: 4.4/4.433333333333334/4.533333333333333/4.633333333333334/3.933333333333333
- mean overall (avg R/H/S/D/K): 4.386666666666667
### S1 (n=30)
- mean runtime: 10.342866666666668
- mean R/H/S/D/K: 4.866666666666666/4.8/4.833333333333333/4.9/4.466666666666667
- mean overall (avg R/H/S/D/K): 4.7733333333333325
### S2 (n=30)
- mean runtime: 10.019433333333334
- mean R/H/S/D/K: 5.0/5.0/4.866666666666666/5.0/5.0
- mean overall (avg R/H/S/D/K): 4.973333333333333
### S2_ABL_NOASSET (n=30)
- mean runtime: 9.480966666666665
- mean R/H/S/D/K: 4.9/4.933333333333334/4.866666666666666/4.966666666666667/5.0
- mean overall (avg R/H/S/D/K): 4.933333333333334
### S2_ABL_NODEV (n=30)
- mean runtime: 8.9771
- mean R/H/S/D/K: 4.933333333333334/4.866666666666666/4.866666666666666/5.0/5.0
- mean overall (avg R/H/S/D/K): 4.933333333333334
### S2_ABL_NOENV (n=30)
- mean runtime: 9.661033333333334
- mean R/H/S/D/K: 4.866666666666666/4.766666666666667/4.766666666666667/4.9/4.933333333333334
- mean overall (avg R/H/S/D/K): 4.846666666666667
### S2_ABL_NOINC (n=30)
- mean runtime: 9.153166666666667
- mean R/H/S/D/K: 4.766666666666667/4.833333333333333/4.866666666666666/4.933333333333334/4.933333333333334
- mean overall (avg R/H/S/D/K): 4.866666666666666

## Top missing elements (max 20)
- offline_workflow: 5
- Keine Nutzung des Kontexts (nur Asset-ID vorhanden): 4
- Offline-Workflow (spotty connectivity): 3
- Offline-Workflow explizit (offline-Signal vorhanden, aber nicht klar adressiert): 2
- Offline-Workflow nicht explizit erwähnt trotz spotty connectivity: 2
- Keine Anpassung an Umgebungsbedingungen (nicht im Context): 2
- Keine Nutzung der Asset-ID im Kontext: 2
- Kontextnutzung minimal (nur Asset-ID vorhanden): 2
- Offline-Workflow nicht erwähnt trotz 'spotty' connectivity: 2
- Offline-Workflow explizit: 2
- Kontextnutzung minimal (nur Asset-ID): 2
- Offline-Workflow nicht explizit erwähnt trotz connectivity=offline: 2
- Offline-Workflow nicht explizit erwähnt (trotz offline/low_battery im Kontext): 1
- Expliziter Offline-Workflow: 1
- Offline-Workflow trotz spotty connectivity: 1
- Korrekte Interpretation von low_battery (Gerät, nicht Asset): 1
- Keine Anpassung an Umgebungsbedingungen (Nebel/Nacht nicht erwähnt, da nicht im Kontext): 1
- Keine Erwähnung von Offline-Workflow (nicht erwartbar, da connectivity nicht im Kontext): 1
- Offline-Workflow nicht explizit (spotty connectivity im Kontext, aber nur indirekt angesprochen): 1
- Offline-Workflow nicht explizit erwähnt (instabile Konnektivität im Kontext, aber nur kurz angesprochen): 1
