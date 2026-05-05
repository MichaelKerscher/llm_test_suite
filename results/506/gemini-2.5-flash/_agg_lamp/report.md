# Aggregation Report (506/gemini-2.5-flash) [lamp]
- judge_version filter: **judge_v1_1**
- Tests (latest runs): **270**
- Incidents with any deltas: **30**

## Mean scores by context level (snapshot)
### L0 (n=30)
- mean runtime: 8.451766666666666
- mean R/H/S/D/K: 3.533333333333333/3.8/3.8/4.033333333333333/2.6333333333333333
- mean overall (avg R/H/S/D/K): 3.56
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.00, hallucination_suspected=0.07
### L2 (n=30)
- mean runtime: 12.154599999999999
- mean R/H/S/D/K: 4.866666666666666/4.866666666666666/4.833333333333333/4.9/4.566666666666666
- mean overall (avg R/H/S/D/K): 4.806666666666667
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.07, hallucination_suspected=0.03
### L2B (n=30)
- mean runtime: 11.198166666666667
- mean R/H/S/D/K: 5.0/5.0/4.933333333333334/5.0/5.0
- mean overall (avg R/H/S/D/K): 4.986666666666666
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.60, hallucination_suspected=0.00
### unknown (n=180)
- mean runtime: 10.029583333333333
- mean R/H/S/D/K: 4.722222222222222/4.716666666666667/4.777777777777778/4.866666666666666/4.677777777777778
- mean overall (avg R/H/S/D/K): 4.752222222222222
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.39, hallucination_suspected=0.01

## Mean scores by strategy (snapshot)
### S0 (n=30)
- mean runtime: 8.451766666666666
- mean R/H/S/D/K: 3.533333333333333/3.8/3.8/4.033333333333333/2.6333333333333333
- mean overall (avg R/H/S/D/K): 3.56
### S0_RAW (n=30)
- mean runtime: 11.079233333333333
- mean R/H/S/D/K: 4.6/4.6/4.766666666666667/4.866666666666666/4.433333333333334
- mean overall (avg R/H/S/D/K): 4.653333333333333
### S0_UNSTRUCTURED (n=30)
- mean runtime: 11.825999999999999
- mean R/H/S/D/K: 4.266666666666667/4.3/4.533333333333333/4.533333333333333/3.7666666666666666
- mean overall (avg R/H/S/D/K): 4.28
### S1 (n=30)
- mean runtime: 12.154599999999999
- mean R/H/S/D/K: 4.866666666666666/4.866666666666666/4.833333333333333/4.9/4.566666666666666
- mean overall (avg R/H/S/D/K): 4.806666666666667
### S2 (n=30)
- mean runtime: 11.198166666666667
- mean R/H/S/D/K: 5.0/5.0/4.933333333333334/5.0/5.0
- mean overall (avg R/H/S/D/K): 4.986666666666666
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
- Offline-Workflow (nicht erwartbar, da connectivity nicht im CONTEXT): 6
- offline_workflow: 6
- Kontextnutzung minimal (nur Asset-ID): 4
- Offline-Workflow explizit: 3
- offline_workflow_explicit: 3
- Offline-Workflow (spotty connectivity im CONTEXT, aber nicht explizit adressiert): 2
- Offline-Workflow nicht erwähnt (connectivity=spotty im Kontext): 2
- Offline-Workflow nicht erwähnt trotz 'spotty' connectivity im CONTEXT: 2
- Keine Nutzung der Asset-ID im Kontext (nur minimal vorhanden): 2
- Keine Nutzung des Kontexts (nur Asset-ID vorhanden): 2
- Keine explizite Erwähnung von low_power_mode als Handlungseinschränkung: 2
- Expliziter Offline-Workflow (spotty connectivity im CONTEXT): 2
- Offline-Workflow nicht explizit (aber low_battery/offline im CONTEXT vorhanden): 1
- Keine Erwähnung von Umgebungsbedingungen: 1
- Unstrukturierter Kontext erschwert Parsing: 1
- Kontextnutzung (nur Asset-ID vorhanden, keine Umgebungs-/Device-Infos genutzt): 1
- Offline-Workflow nicht erwähnt (aber auch nicht erwartbar, da connectivity nicht im Context): 1
- Offline-Workflow nicht explizit erwähnt trotz spotty connectivity: 1
- Offline-Workflow nicht explizit erwähnt trotz 'instabil' connectivity: 1
- Device-Zustand (low_battery, spotty) nur am Rand erwähnt, nicht in Handlungsempfehlungen integriert: 1
