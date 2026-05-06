# Aggregation Report (506/gpt-4.1) [signal]
- judge_version filter: **judge_v1_1**
- Tests (latest runs): **150**
- Incidents with any deltas: **30**

## Mean scores by context level (snapshot)
### L0 (n=30)
- mean runtime: 8.559500000000002
- mean R/H/S/D/K: 3.8666666666666667/3.9/3.8333333333333335/4.233333333333333/2.5
- mean overall (avg R/H/S/D/K): 3.6666666666666665
- flags (rate): safety_first=0.97, escalation_present=1.00, offline_workflow_mentioned=0.00, hallucination_suspected=0.43
### L2 (n=30)
- mean runtime: 10.457333333333334
- mean R/H/S/D/K: 4.833333333333333/4.8/4.866666666666666/4.9/4.533333333333333
- mean overall (avg R/H/S/D/K): 4.786666666666666
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.13, hallucination_suspected=0.00
### L2B (n=30)
- mean runtime: 9.395233333333332
- mean R/H/S/D/K: 4.933333333333334/4.933333333333334/4.9/4.966666666666667/4.966666666666667
- mean overall (avg R/H/S/D/K): 4.9399999999999995
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.53, hallucination_suspected=0.00
### unknown (n=60)
- mean runtime: 10.106833333333332
- mean R/H/S/D/K: 4.633333333333334/4.633333333333334/4.766666666666667/4.75/4.366666666666666
- mean overall (avg R/H/S/D/K): 4.63
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.27, hallucination_suspected=0.00

## Mean scores by strategy (snapshot)
### S0 (n=30)
- mean runtime: 8.559500000000002
- mean R/H/S/D/K: 3.8666666666666667/3.9/3.8333333333333335/4.233333333333333/2.5
- mean overall (avg R/H/S/D/K): 3.6666666666666665
### S0_RAW (n=30)
- mean runtime: 9.902933333333333
- mean R/H/S/D/K: 4.866666666666666/4.833333333333333/4.866666666666666/4.933333333333334/4.733333333333333
- mean overall (avg R/H/S/D/K): 4.846666666666667
### S0_UNSTRUCTURED (n=30)
- mean runtime: 10.310733333333333
- mean R/H/S/D/K: 4.4/4.433333333333334/4.666666666666667/4.566666666666666/4.0
- mean overall (avg R/H/S/D/K): 4.413333333333333
### S1 (n=30)
- mean runtime: 10.457333333333334
- mean R/H/S/D/K: 4.833333333333333/4.8/4.866666666666666/4.9/4.533333333333333
- mean overall (avg R/H/S/D/K): 4.786666666666666
### S2 (n=30)
- mean runtime: 9.395233333333332
- mean R/H/S/D/K: 4.933333333333334/4.933333333333334/4.9/4.966666666666667/4.966666666666667
- mean overall (avg R/H/S/D/K): 4.9399999999999995

## Top missing elements (max 20)
- offline_workflow: 5
- offline_workflow_explicit: 2
- Offline-Workflow (nicht erwartbar, da connectivity nicht im CONTEXT): 2
- Keine Kontextnutzung erkennbar (nur Asset-ID vorhanden): 2
- Kontext-Nutzung minimal (nur Asset-ID): 2
- Offline-Workflow (spotty connectivity im Context, aber nicht explizit adressiert): 2
- Offline-Workflow (spotty connectivity im CONTEXT, aber nicht explizit adressiert): 2
- Offline-Workflow (spotty connectivity): 2
- explicit_offline_workflow: 2
- Offline-Workflow (spotty connectivity nicht explizit adressiert): 2
- Offline-Workflow nicht explizit erwähnt: 1
- context_utilization: 1
- Keine GPS-Koordinaten genutzt (waren nicht im Context): 1
- Spekuliert über Reset/Schaltkasten-Details ohne Basis: 1
- Unstrukturierter Context erschwert Parsing, aber Antwort nutzt Infos gut: 1
- Keine klare Priorisierung bei intermittierendem Fehler: 1
- Keine Erwähnung von Verkehrsregelung trotz Hauptverkehrszeit: 1
- Keine explizite Erwähnung von Verkehrsregelung bei Ausfall: 1
- Kontext nur teilweise genutzt (unstrukturiert): 1
- Spezifische Kontextnutzung fehlt (nur Asset-ID vorhanden): 1
