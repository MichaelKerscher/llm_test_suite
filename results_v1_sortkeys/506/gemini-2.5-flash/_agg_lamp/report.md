# Aggregation Report (506/gemini-2.5-flash) [lamp]
- judge_version filter: **judge_v1_1**
- Tests (latest runs): **270**
- Incidents with any deltas: **30**

## Mean scores by context level (snapshot)
### L0 (n=30)
- mean runtime: 6.668666666666667
- mean R/H/S/D/K: 3.566666666666667/3.7666666666666666/3.7/4.1/2.5
- mean overall (avg R/H/S/D/K): 3.5266666666666664
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.00, hallucination_suspected=0.13
### L2 (n=30)
- mean runtime: 10.2672
- mean R/H/S/D/K: 4.866666666666666/4.866666666666666/4.9/4.966666666666667/4.4
- mean overall (avg R/H/S/D/K): 4.8
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.13, hallucination_suspected=0.03
### L2B (n=30)
- mean runtime: 9.587
- mean R/H/S/D/K: 5.0/5.0/4.933333333333334/5.0/5.0
- mean overall (avg R/H/S/D/K): 4.986666666666666
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.60, hallucination_suspected=0.00
### unknown (n=180)
- mean runtime: 9.417300000000001
- mean R/H/S/D/K: 4.7444444444444445/4.727777777777778/4.7555555555555555/4.883333333333334/4.722222222222222
- mean overall (avg R/H/S/D/K): 4.766666666666667
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.41, hallucination_suspected=0.02

## Mean scores by strategy (snapshot)
### S0 (n=30)
- mean runtime: 6.668666666666667
- mean R/H/S/D/K: 3.566666666666667/3.7666666666666666/3.7/4.1/2.5
- mean overall (avg R/H/S/D/K): 3.5266666666666664
### S0_RAW (n=30)
- mean runtime: 9.224833333333333
- mean R/H/S/D/K: 4.633333333333334/4.6/4.7/4.866666666666666/4.533333333333333
- mean overall (avg R/H/S/D/K): 4.666666666666667
### S0_UNSTRUCTURED (n=30)
- mean runtime: 10.0067
- mean R/H/S/D/K: 4.366666666666666/4.366666666666666/4.466666666666667/4.633333333333334/3.933333333333333
- mean overall (avg R/H/S/D/K): 4.3533333333333335
### S1 (n=30)
- mean runtime: 10.2672
- mean R/H/S/D/K: 4.866666666666666/4.866666666666666/4.9/4.966666666666667/4.4
- mean overall (avg R/H/S/D/K): 4.8
### S2 (n=30)
- mean runtime: 9.587
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
- Offline-Workflow fehlt trotz 'offline' im Kontext: 2
- Keine Nutzung der Asset-ID im Kontext: 2
- Kein expliziter Offline-Workflow trotz spotty connectivity: 2
- Kontextnutzung minimal (nur Asset-ID): 2
- Offline-Workflow nicht erwähnt (spotty connectivity im Context): 2
- Offline-Workflow nicht explizit erwähnt (connectivity=offline im Context): 2
- Offline-Workflow (spotty connectivity im Kontext): 2
- Offline-Workflow fehlt trotz 'offline' + 'low_battery': 1
- Gerätezustand wird als Lampenursache interpretiert: 1
- Gerätezustand wird falsch interpretiert (Lampe vs. Technikgerät): 1
- Fehlinterpretation 'low_battery' als Lampenproblem: 1
- Keine Nutzung der Asset-ID im Text: 1
- Keine Erwähnung intermittierender Fehler-Spezifika: 1
- Keine Kontextanpassung (generisch): 1
- Offline-Workflow explizit (spotty connectivity + low_battery): 1
- Offline-Workflow (spotty connectivity erkennbar): 1
- Kontextnutzung minimal (nur Asset-ID vorhanden): 1
- Keine Anpassung an Umgebungsbedingungen (Nebel/Nacht nicht bekannt): 1
- Keine Offline-Workflow-Erwähnung (Konnektivität unbekannt): 1
- Offline-Workflow nicht explizit erwähnt trotz spotty connectivity: 1
