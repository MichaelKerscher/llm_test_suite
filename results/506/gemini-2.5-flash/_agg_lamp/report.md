# Aggregation Report (506/gemini-2.5-flash) [lamp]
- judge_version filter: **judge_v1_1**
- Tests (latest runs): **270**
- Incidents with any deltas: **30**

## Mean scores by context level (snapshot)
### L0 (n=30)
- mean runtime: 8.387033333333333
- mean R/H/S/D/K: 3.4/3.7333333333333334/3.7/4.0/2.3333333333333335
- mean overall (avg R/H/S/D/K): 3.433333333333333
- flags (rate): safety_first=0.97, escalation_present=1.00, offline_workflow_mentioned=0.00, hallucination_suspected=0.10
### L2 (n=30)
- mean runtime: 10.0564
- mean R/H/S/D/K: 4.833333333333333/4.8/4.766666666666667/4.833333333333333/4.533333333333333
- mean overall (avg R/H/S/D/K): 4.753333333333333
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.10, hallucination_suspected=0.00
### L2B (n=30)
- mean runtime: 11.041500000000001
- mean R/H/S/D/K: 5.0/4.966666666666667/4.9/4.966666666666667/5.0
- mean overall (avg R/H/S/D/K): 4.966666666666667
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.60, hallucination_suspected=0.00
### unknown (n=180)
- mean runtime: 9.348866666666668
- mean R/H/S/D/K: 4.688888888888889/4.683333333333334/4.727777777777778/4.8277777777777775/4.6722222222222225
- mean overall (avg R/H/S/D/K): 4.72
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.39, hallucination_suspected=0.01

## Mean scores by strategy (snapshot)
### S0 (n=30)
- mean runtime: 8.387033333333333
- mean R/H/S/D/K: 3.4/3.7333333333333334/3.7/4.0/2.3333333333333335
- mean overall (avg R/H/S/D/K): 3.433333333333333
### S0_RAW (n=30)
- mean runtime: 9.280566666666667
- mean R/H/S/D/K: 4.5/4.5/4.566666666666666/4.8/4.466666666666667
- mean overall (avg R/H/S/D/K): 4.566666666666666
### S0_UNSTRUCTURED (n=30)
- mean runtime: 9.540366666666667
- mean R/H/S/D/K: 4.166666666666667/4.2/4.433333333333334/4.366666666666666/3.7
- mean overall (avg R/H/S/D/K): 4.173333333333334
### S1 (n=30)
- mean runtime: 10.0564
- mean R/H/S/D/K: 4.833333333333333/4.8/4.766666666666667/4.833333333333333/4.533333333333333
- mean overall (avg R/H/S/D/K): 4.753333333333333
### S2 (n=30)
- mean runtime: 11.041500000000001
- mean R/H/S/D/K: 5.0/4.966666666666667/4.9/4.966666666666667/5.0
- mean overall (avg R/H/S/D/K): 4.966666666666667
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
- offline_workflow: 4
- Kontextnutzung minimal (nur Asset-ID): 3
- Offline-Workflow nicht erwähnt (spotty connectivity im CONTEXT): 2
- Offline-Workflow explizit: 2
- Kein Offline-Workflow trotz 'spotty' connectivity: 2
- Keine Nutzung der Asset-ID im Kontext: 2
- Offline-Workflow nicht explizit erwähnt trotz 'spotty' connectivity: 2
- offline workflow: 2
- offline workflow explicit mention: 2
- Offline-Workflow bei spotty connectivity: 2
- Offline-Workflow (Gerät offline nicht erwähnt, da nicht im CONTEXT): 1
- Offline-Workflow nicht explizit genannt: 1
- Offline-Workflow nicht explizit erwähnt: 1
- Keine Nutzung des Kontexts (nur Asset-ID vorhanden): 1
- Keine Erwähnung von Foto oder spezifischen Bedingungen: 1
- Generische Antwort ohne Bezug zu intermittent fault: 1
- Dokumentation könnte detaillierter sein (z.B. GPS, Asset-ID explizit): 1
- Keine explizite Priorisierung der Schritte (z.B. 1-2-3 mit Stop-Conditions): 1
- Eskalation könnte klarer getriggert sein: 1
- Unstrukturierter Kontext erschwert Parsing, aber Modell nutzt ihn gut: 1
