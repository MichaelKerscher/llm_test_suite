# Aggregation Report (506/gemini-2.5-flash) [signal]
- judge_version filter: **judge_v1_1**
- Tests (latest runs): **150**
- Incidents with any deltas: **30**

## Mean scores by context level (snapshot)
### L0 (n=30)
- mean runtime: 8.396666666666667
- mean R/H/S/D/K: 3.933333333333333/3.933333333333333/4.1/4.133333333333334/2.6
- mean overall (avg R/H/S/D/K): 3.74
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.00, hallucination_suspected=0.33
### L2 (n=30)
- mean runtime: 12.243666666666666
- mean R/H/S/D/K: 4.933333333333334/4.9/4.866666666666666/4.966666666666667/4.833333333333333
- mean overall (avg R/H/S/D/K): 4.9
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.13, hallucination_suspected=0.00
### L2B (n=30)
- mean runtime: 10.063433333333334
- mean R/H/S/D/K: 4.966666666666667/4.966666666666667/4.966666666666667/4.966666666666667/5.0
- mean overall (avg R/H/S/D/K): 4.973333333333333
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.50, hallucination_suspected=0.00
### unknown (n=60)
- mean runtime: 10.880650000000001
- mean R/H/S/D/K: 4.666666666666667/4.65/4.8/4.783333333333333/4.35
- mean overall (avg R/H/S/D/K): 4.65
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.25, hallucination_suspected=0.00

## Mean scores by strategy (snapshot)
### S0 (n=30)
- mean runtime: 8.396666666666667
- mean R/H/S/D/K: 3.933333333333333/3.933333333333333/4.1/4.133333333333334/2.6
- mean overall (avg R/H/S/D/K): 3.74
### S0_RAW (n=30)
- mean runtime: 10.204566666666667
- mean R/H/S/D/K: 4.9/4.9/4.866666666666666/4.933333333333334/4.7
- mean overall (avg R/H/S/D/K): 4.86
### S0_UNSTRUCTURED (n=30)
- mean runtime: 11.556733333333334
- mean R/H/S/D/K: 4.433333333333334/4.4/4.733333333333333/4.633333333333334/4.0
- mean overall (avg R/H/S/D/K): 4.4399999999999995
### S1 (n=30)
- mean runtime: 12.243666666666666
- mean R/H/S/D/K: 4.933333333333334/4.9/4.866666666666666/4.966666666666667/4.833333333333333
- mean overall (avg R/H/S/D/K): 4.9
### S2 (n=30)
- mean runtime: 10.063433333333334
- mean R/H/S/D/K: 4.966666666666667/4.966666666666667/4.966666666666667/4.966666666666667/5.0
- mean overall (avg R/H/S/D/K): 4.973333333333333

## Top missing elements (max 20)
- offline_workflow: 6
- offline_workflow_explicit: 3
- Keine explizite Erwähnung der Behandlung als unbeschrankte Kreuzung: 2
- Offline-Workflow (nicht erwartbar, da connectivity nicht im CONTEXT): 2
- Offline-Workflow (spotty connectivity im _unstructured_text, aber nicht explizit adressiert): 2
- Kontext-Nutzung minimal (nur Asset-ID): 2
- Unstrukturierter Kontext erschwert Nutzung: 2
- Offline-Workflow (nicht erwartbar bei L0_minimal): 1
- Severity-basierte Priorisierung unklar: 1
- Offline-Workflow nicht explizit (trotz device.connectivity=offline): 1
- Offline-Workflow nicht explizit erwähnt (trotz 'offline' im Kontext): 1
- GPS-Koordinaten: 1
- Foto-Hinweis: 1
- Schweregrad-Kontext: 1
- Kontext-Nutzung (nur Asset-ID vorhanden, keine Umwelt-/Severity-Infos): 1
- Spekulative Details (Polizei, Schaltkasten, Qualifikation) ohne Kontext-Basis: 1
- Keine klare Priorisierung bei Schritt 3 (Diagnose vor Eskalation): 1
- Eskalation könnte früher/klarer als Trigger formuliert sein: 1
- Unstrukturierter Kontext erschwert Nachvollziehbarkeit, aber Modell nutzt ihn gut: 1
- Offline-Workflow explizit erwähnt: 1
