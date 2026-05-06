# Aggregation Report (506/gemini-2.5-flash) [lamp]
- judge_version filter: **judge_v1_1**
- Tests (latest runs): **270**
- Incidents with any deltas: **30**

## Mean scores by context level (snapshot)
### L0 (n=30)
- mean runtime: 6.818700000000001
- mean R/H/S/D/K: 3.4/3.7/3.6/4.1/2.3666666666666667
- mean overall (avg R/H/S/D/K): 3.433333333333333
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.00, hallucination_suspected=0.13
### L2 (n=30)
- mean runtime: 9.7739
- mean R/H/S/D/K: 4.8/4.766666666666667/4.833333333333333/4.9/4.433333333333334
- mean overall (avg R/H/S/D/K): 4.746666666666667
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.03, hallucination_suspected=0.00
### L2B (n=30)
- mean runtime: 10.9912
- mean R/H/S/D/K: 4.933333333333334/4.933333333333334/4.833333333333333/4.966666666666667/5.0
- mean overall (avg R/H/S/D/K): 4.933333333333334
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.60, hallucination_suspected=0.00
### unknown (n=180)
- mean runtime: 9.370427777777778
- mean R/H/S/D/K: 4.716666666666667/4.711111111111111/4.722222222222222/4.905555555555556/4.688888888888889
- mean overall (avg R/H/S/D/K): 4.748888888888889
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.39, hallucination_suspected=0.01

## Mean scores by strategy (snapshot)
### S0 (n=30)
- mean runtime: 6.818700000000001
- mean R/H/S/D/K: 3.4/3.7/3.6/4.1/2.3666666666666667
- mean overall (avg R/H/S/D/K): 3.433333333333333
### S0_RAW (n=30)
- mean runtime: 9.180666666666667
- mean R/H/S/D/K: 4.566666666666666/4.533333333333333/4.533333333333333/4.9/4.566666666666666
- mean overall (avg R/H/S/D/K): 4.62
### S0_UNSTRUCTURED (n=30)
- mean runtime: 9.769633333333333
- mean R/H/S/D/K: 4.266666666666667/4.333333333333333/4.433333333333334/4.733333333333333/3.7
- mean overall (avg R/H/S/D/K): 4.293333333333334
### S1 (n=30)
- mean runtime: 9.7739
- mean R/H/S/D/K: 4.8/4.766666666666667/4.833333333333333/4.9/4.433333333333334
- mean overall (avg R/H/S/D/K): 4.746666666666667
### S2 (n=30)
- mean runtime: 10.9912
- mean R/H/S/D/K: 4.933333333333334/4.933333333333334/4.833333333333333/4.966666666666667/5.0
- mean overall (avg R/H/S/D/K): 4.933333333333334
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
- Keine Nutzung der Asset-ID im Kontext: 4
- Keine Nutzung des Kontexts (nur Asset-ID vorhanden): 3
- Klare Stop-Conditions für Beobachtung: 2
- Kontextnutzung minimal (nur Asset-ID): 2
- Offline-Workflow nicht erwähnt (spotty connectivity im Kontext): 2
- Offline-Workflow nicht explizit erwähnt (connectivity=spotty im Context): 2
- Offline-Workflow (Kontext zeigt nur asset_osm, keine connectivity-Info): 2
- Offline-Workflow nicht explizit trotz 'spotty' connectivity: 2
- Offline-Workflow (spotty connectivity + low_power_mode): 2
- Kein expliziter Offline-Workflow trotz spotty connectivity: 2
- Offline-Workflow nicht explizit erwähnt trotz 'spotty' connectivity: 2
- Offline-Workflow (spotty connectivity im Kontext): 2
- Offline-Workflow (nicht erwartbar, da CONTEXT kein connectivity-Signal enthält): 1
- Konkrete Priorisierung der Schritte (z.B. 'erst X, dann Y'): 1
- Stop-Conditions für Beobachtung: 1
- Offline-Workflow (erwartbar, da connectivity=offline): 1
- Priorisierung innerhalb Diagnose-Schritt: 1
- Offline-Workflow (erwartbar, da connectivity=offline im CONTEXT): 1
- Klare Stop-Conditions: 1
