# Aggregation Report (506/gemini-2.5-flash) [signal]
- judge_version filter: **judge_v1_1**
- Tests (latest runs): **150**
- Incidents with any deltas: **30**

## Mean scores by context level (snapshot)
### L0 (n=30)
- mean runtime: 8.858066666666668
- mean R/H/S/D/K: 3.8333333333333335/3.933333333333333/4.066666666666666/4.166666666666667/2.466666666666667
- mean overall (avg R/H/S/D/K): 3.6933333333333334
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.00, hallucination_suspected=0.43
### L2 (n=30)
- mean runtime: 11.354000000000001
- mean R/H/S/D/K: 4.9/4.866666666666666/4.9/4.9/4.633333333333334
- mean overall (avg R/H/S/D/K): 4.84
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.10, hallucination_suspected=0.00
### L2B (n=30)
- mean runtime: 9.827633333333333
- mean R/H/S/D/K: 4.966666666666667/4.966666666666667/4.933333333333334/5.0/5.0
- mean overall (avg R/H/S/D/K): 4.973333333333333
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.53, hallucination_suspected=0.00
### unknown (n=60)
- mean runtime: 11.201216666666665
- mean R/H/S/D/K: 4.6/4.616666666666666/4.733333333333333/4.733333333333333/4.283333333333333
- mean overall (avg R/H/S/D/K): 4.593333333333334
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.25, hallucination_suspected=0.00

## Mean scores by strategy (snapshot)
### S0 (n=30)
- mean runtime: 8.858066666666668
- mean R/H/S/D/K: 3.8333333333333335/3.933333333333333/4.066666666666666/4.166666666666667/2.466666666666667
- mean overall (avg R/H/S/D/K): 3.6933333333333334
### S0_RAW (n=30)
- mean runtime: 11.064733333333333
- mean R/H/S/D/K: 4.866666666666666/4.866666666666666/4.866666666666666/5.0/4.7
- mean overall (avg R/H/S/D/K): 4.86
### S0_UNSTRUCTURED (n=30)
- mean runtime: 11.3377
- mean R/H/S/D/K: 4.333333333333333/4.366666666666666/4.6/4.466666666666667/3.8666666666666667
- mean overall (avg R/H/S/D/K): 4.326666666666667
### S1 (n=30)
- mean runtime: 11.354000000000001
- mean R/H/S/D/K: 4.9/4.866666666666666/4.9/4.9/4.633333333333334
- mean overall (avg R/H/S/D/K): 4.84
### S2 (n=30)
- mean runtime: 9.827633333333333
- mean R/H/S/D/K: 4.966666666666667/4.966666666666667/4.933333333333334/5.0/5.0
- mean overall (avg R/H/S/D/K): 4.973333333333333

## Top missing elements (max 20)
- Kontext-Nutzung minimal (nur Asset-ID): 4
- Offline-Workflow (nicht erwartbar, da connectivity nicht im CONTEXT): 3
- offline_workflow: 2
- offline_workflow_explicit: 2
- Offline-Workflow (spotty connectivity im CONTEXT, aber nicht explizit adressiert): 2
- Konkrete Eskalations-Trigger fehlen teilweise: 1
- Offline-Workflow nicht explizit (obwohl connectivity=offline): 1
- Offline-Workflow nicht explizit erwähnt (obwohl offline im CONTEXT): 1
- Offline-Workflow (nicht erwartbar, da CONTEXT kein connectivity-Signal enthält): 1
- Kontextnutzung minimal (nur Asset-ID vorhanden): 1
- Offline-Workflow nicht explizit erwähnt (connectivity=offline im CONTEXT): 1
- Offline-Workflow nicht explizit erwähnt (obwohl connectivity=offline im CONTEXT): 1
- Halluzinationen: 'Unfallstelle', 'Induktionsschleifen', 'Bauarbeiten' ohne Basis im Context: 1
- Keine Kontextnutzung bzgl. Wetter/Sicht (nicht im CONTEXT): 1
- Keine Erwähnung Gerätezustand (nicht im CONTEXT): 1
- Keine explizite Erwähnung low_battery als Constraint: 1
- Spekuliert über Fehlerprotokoll/Spannungsmessung ohne Basis: 1
- Keine Priorisierung auf intermittierenden Charakter: 1
- Unstrukturierter Kontext erschwert Parsing, aber gut genutzt: 1
- Kontextnutzung minimal: 1
