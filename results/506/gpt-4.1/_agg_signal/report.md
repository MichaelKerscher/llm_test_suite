# Aggregation Report (506/gpt-4.1) [signal]
- judge_version filter: **judge_v1_1**
- Tests (latest runs): **150**
- Incidents with any deltas: **30**

## Mean scores by context level (snapshot)
### L0 (n=30)
- mean runtime: 8.361033333333333
- mean R/H/S/D/K: 3.8333333333333335/3.933333333333333/4.133333333333334/4.2/2.6666666666666665
- mean overall (avg R/H/S/D/K): 3.753333333333333
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.00, hallucination_suspected=0.13
### L2 (n=30)
- mean runtime: 10.640666666666668
- mean R/H/S/D/K: 4.8/4.766666666666667/4.9/4.866666666666666/4.6
- mean overall (avg R/H/S/D/K): 4.786666666666666
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.17, hallucination_suspected=0.00
### L2B (n=30)
- mean runtime: 10.987566666666668
- mean R/H/S/D/K: 4.966666666666667/4.966666666666667/4.933333333333334/5.0/5.0
- mean overall (avg R/H/S/D/K): 4.973333333333333
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.53, hallucination_suspected=0.00
### unknown (n=60)
- mean runtime: 11.068866666666668
- mean R/H/S/D/K: 4.583333333333333/4.65/4.783333333333333/4.833333333333333/4.366666666666666
- mean overall (avg R/H/S/D/K): 4.6433333333333335
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.28, hallucination_suspected=0.02

## Mean scores by strategy (snapshot)
### S0 (n=30)
- mean runtime: 8.361033333333333
- mean R/H/S/D/K: 3.8333333333333335/3.933333333333333/4.133333333333334/4.2/2.6666666666666665
- mean overall (avg R/H/S/D/K): 3.753333333333333
### S0_RAW (n=30)
- mean runtime: 10.861633333333334
- mean R/H/S/D/K: 4.833333333333333/4.833333333333333/4.933333333333334/4.966666666666667/4.7
- mean overall (avg R/H/S/D/K): 4.8533333333333335
### S0_UNSTRUCTURED (n=30)
- mean runtime: 11.276100000000001
- mean R/H/S/D/K: 4.333333333333333/4.466666666666667/4.633333333333334/4.7/4.033333333333333
- mean overall (avg R/H/S/D/K): 4.433333333333334
### S1 (n=30)
- mean runtime: 10.640666666666668
- mean R/H/S/D/K: 4.8/4.766666666666667/4.9/4.866666666666666/4.6
- mean overall (avg R/H/S/D/K): 4.786666666666666
### S2 (n=30)
- mean runtime: 10.987566666666668
- mean R/H/S/D/K: 4.966666666666667/4.966666666666667/4.933333333333334/5.0/5.0
- mean overall (avg R/H/S/D/K): 4.973333333333333

## Top missing elements (max 20)
- Offline-Workflow nicht explizit erwähnt: 3
- Offline-Workflow (spotty connectivity): 3
- Offline-Workflow nicht erwähnt (spotty connectivity im Kontext): 2
- Offline-Workflow explizit erwähnen: 1
- Offline-Workflow nicht explizit adressiert: 1
- Keine Nutzung der GPS-Koordinaten (nur Asset-ID erwähnt): 1
- Keine Erwähnung von Umweltbedingungen (nicht im Context): 1
- Keine explizite Erwähnung der GPS-Koordinaten in Dokumentation: 1
- Kontextnutzung schwach (nur Asset-ID vorhanden, keine Umgebungs-/Severity-Infos genutzt): 1
- Keine Priorisierung nach Severity/Traffic: 1
- Offline-Workflow (nicht erwartbar, da connectivity nicht im CONTEXT): 1
- Sporadizitäts-Muster (nur allgemein erwähnt): 1
- Halluzination: Annahme 'Straßenlampe/Ampelanlage' ohne Basis im CONTEXT: 1
- Offline-Workflow (spotty im CONTEXT, aber nicht explizit adressiert): 1
- Asset-Typ-Annahme (aber als Annahme deklariert, daher akzeptabel): 1
- Keine GPS-Koordinaten erwähnt (nur Asset-ID): 1
- Keine explizite 'Kreuzung wie unbeschrankt behandeln'-Anweisung: 1
- Unstrukturierter Kontext erschwert Parsing, aber Modell nutzt Infos gut: 1
- Offline-Workflow (spotty connectivity erwähnt, aber nicht explizit adressiert): 1
- Keine Nutzung der Asset-ID im Kontext: 1
