# Aggregation Report (506/gemini-2.5-flash) [signal]
- judge_version filter: **judge_v1_1**
- Tests (latest runs): **150**
- Incidents with any deltas: **30**

## Mean scores by context level (snapshot)
### L0 (n=30)
- mean runtime: 8.373966666666666
- mean R/H/S/D/K: 3.8/3.8333333333333335/3.933333333333333/4.166666666666667/2.466666666666667
- mean overall (avg R/H/S/D/K): 3.64
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.00, hallucination_suspected=0.27
### L2 (n=30)
- mean runtime: 11.116166666666667
- mean R/H/S/D/K: 4.933333333333334/4.933333333333334/4.933333333333334/4.933333333333334/4.566666666666666
- mean overall (avg R/H/S/D/K): 4.86
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.07, hallucination_suspected=0.00
### L2B (n=30)
- mean runtime: 10.478933333333334
- mean R/H/S/D/K: 5.0/5.0/4.966666666666667/5.0/5.0
- mean overall (avg R/H/S/D/K): 4.993333333333334
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.60, hallucination_suspected=0.00
### unknown (n=60)
- mean runtime: 10.576383333333332
- mean R/H/S/D/K: 4.533333333333333/4.55/4.783333333333333/4.65/4.233333333333333
- mean overall (avg R/H/S/D/K): 4.55
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.20, hallucination_suspected=0.02

## Mean scores by strategy (snapshot)
### S0 (n=30)
- mean runtime: 8.373966666666666
- mean R/H/S/D/K: 3.8/3.8333333333333335/3.933333333333333/4.166666666666667/2.466666666666667
- mean overall (avg R/H/S/D/K): 3.64
### S0_RAW (n=30)
- mean runtime: 10.849933333333333
- mean R/H/S/D/K: 4.833333333333333/4.833333333333333/4.9/4.9/4.733333333333333
- mean overall (avg R/H/S/D/K): 4.84
### S0_UNSTRUCTURED (n=30)
- mean runtime: 10.302833333333332
- mean R/H/S/D/K: 4.233333333333333/4.266666666666667/4.666666666666667/4.4/3.7333333333333334
- mean overall (avg R/H/S/D/K): 4.26
### S1 (n=30)
- mean runtime: 11.116166666666667
- mean R/H/S/D/K: 4.933333333333334/4.933333333333334/4.933333333333334/4.933333333333334/4.566666666666666
- mean overall (avg R/H/S/D/K): 4.86
### S2 (n=30)
- mean runtime: 10.478933333333334
- mean R/H/S/D/K: 5.0/5.0/4.966666666666667/5.0/5.0
- mean overall (avg R/H/S/D/K): 4.993333333333334

## Top missing elements (max 20)
- Offline-Workflow nicht explizit erwähnt: 3
- Offline-Workflow (nicht erwartbar, da connectivity nicht im CONTEXT): 3
- Kontextnutzung minimal: 2
- Kein expliziter Offline-Workflow trotz 'spotty' Konnektivität: 2
- Offline-Workflow (spotty connectivity im CONTEXT, aber nicht explizit adressiert): 2
- Offline-Workflow bei spotty connectivity nicht explizit erwähnt: 2
- Offline-Workflow (nicht erwartbar aus CONTEXT): 2
- Offline-Workflow nicht explizit trotz offline/low_battery: 1
- Offline-Workflow nicht explizit erwähnt trotz offline/low_battery im Kontext: 1
- Offline-Workflow nicht explizit adressiert: 1
- Halluzinationen (Reset-Versuch, Steuergerät-Details ohne Kontext): 1
- Kontextnutzung minimal (nur Asset-ID vorhanden): 1
- Keine Erwähnung von Wetter/Sicht (nicht im Context): 1
- Unstrukturierter Context erschwert Parsing, aber Modell nutzt Infos gut: 1
- Keine Nutzung der Asset-ID im Kontext: 1
- Spekuliert über Asset-Typ (Ampel/Lampe) ohne Basis: 1
- Keine Anpassung an minimalen Kontext: 1
- Spekuliert leicht über Beleuchtungsanlage statt neutral zu bleiben: 1
- Offline-Workflow trotz spotty connectivity: 1
- Halluzination: 'hohes Sicherheitsrisiko' und 'Priorität hoch' widersprechen severity=medium: 1
