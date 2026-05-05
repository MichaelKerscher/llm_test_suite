# Aggregation Report (506/gemini-2.5-flash) [lamp]
- judge_version filter: **judge_v1_1**
- Tests (latest runs): **270**
- Incidents with any deltas: **30**

## Mean scores by context level (snapshot)
### L0 (n=30)
- mean runtime: 8.518133333333333
- mean R/H/S/D/K: 3.6666666666666665/3.8333333333333335/3.9/4.066666666666666/2.566666666666667
- mean overall (avg R/H/S/D/K): 3.606666666666667
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.00, hallucination_suspected=0.03
### L2 (n=30)
- mean runtime: 11.061366666666666
- mean R/H/S/D/K: 4.833333333333333/4.8/4.733333333333333/4.9/4.5
- mean overall (avg R/H/S/D/K): 4.753333333333333
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.17, hallucination_suspected=0.00
### L2B (n=30)
- mean runtime: 11.313633333333334
- mean R/H/S/D/K: 5.0/5.0/4.866666666666666/5.0/5.0
- mean overall (avg R/H/S/D/K): 4.973333333333333
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.60, hallucination_suspected=0.00
### unknown (n=180)
- mean runtime: 9.81023888888889
- mean R/H/S/D/K: 4.711111111111111/4.711111111111111/4.772222222222222/4.85/4.688888888888889
- mean overall (avg R/H/S/D/K): 4.746666666666666
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.40, hallucination_suspected=0.01

## Mean scores by strategy (snapshot)
### S0 (n=30)
- mean runtime: 8.518133333333333
- mean R/H/S/D/K: 3.6666666666666665/3.8333333333333335/3.9/4.066666666666666/2.566666666666667
- mean overall (avg R/H/S/D/K): 3.606666666666667
### S0_RAW (n=30)
- mean runtime: 10.829133333333335
- mean R/H/S/D/K: 4.6/4.6/4.733333333333333/4.833333333333333/4.533333333333333
- mean overall (avg R/H/S/D/K): 4.66
### S0_UNSTRUCTURED (n=30)
- mean runtime: 10.760033333333332
- mean R/H/S/D/K: 4.2/4.266666666666667/4.533333333333333/4.466666666666667/3.7333333333333334
- mean overall (avg R/H/S/D/K): 4.24
### S1 (n=30)
- mean runtime: 11.061366666666666
- mean R/H/S/D/K: 4.833333333333333/4.8/4.733333333333333/4.9/4.5
- mean overall (avg R/H/S/D/K): 4.753333333333333
### S2 (n=30)
- mean runtime: 11.313633333333334
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
- Offline-Workflow bei spotty connectivity: 5
- Offline-Workflow explizit (spotty connectivity vorhanden): 3
- offline_workflow: 3
- Offline-Workflow (nicht erwartbar, da CONTEXT kein connectivity-Signal enthält): 2
- Offline-Workflow (spotty connectivity im CONTEXT, aber nicht explizit adressiert): 2
- Offline-Workflow (spotty connectivity): 2
- Offline-Workflow nicht explizit: 2
- Keine Nutzung des Kontexts (nur Asset-ID vorhanden): 2
- Keine Nutzung der Asset-ID im Kontext: 2
- Offline-Workflow (nicht erwartbar, da connectivity nicht im CONTEXT): 2
- offline_workflow_explicit: 2
- Gerätezustand (nicht erwartbar): 1
- Offline-Workflow explizit (Signal vorhanden, aber nicht adressiert): 1
- Offline-Workflow explizit (Signal vorhanden, aber nicht klar adressiert): 1
- Kontext-Nutzung minimal: 1
- Keine Erwähnung von Umgebungsbedingungen: 1
- Unstrukturierter Kontext erschwert Parsing: 1
- Offline-Workflow (nicht erwartbar, da connectivity nicht offline): 1
- Offline-Workflow (spotty connectivity vorhanden, aber nicht explizit adressiert): 1
- Explizite Ticket-ID-Erfassung: 1
