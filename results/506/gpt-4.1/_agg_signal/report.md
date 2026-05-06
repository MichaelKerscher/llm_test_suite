# Aggregation Report (506/gpt-4.1) [signal]
- judge_version filter: **judge_v1_1**
- Tests (latest runs): **150**
- Incidents with any deltas: **30**

## Mean scores by context level (snapshot)
### L0 (n=30)
- mean runtime: 8.2502
- mean R/H/S/D/K: 3.8333333333333335/3.9/4.166666666666667/4.333333333333333/2.5
- mean overall (avg R/H/S/D/K): 3.746666666666667
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.00, hallucination_suspected=0.30
### L2 (n=30)
- mean runtime: 9.975433333333333
- mean R/H/S/D/K: 4.933333333333334/4.9/4.9/4.966666666666667/4.633333333333334
- mean overall (avg R/H/S/D/K): 4.866666666666666
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.13, hallucination_suspected=0.00
### L2B (n=30)
- mean runtime: 10.028166666666667
- mean R/H/S/D/K: 4.966666666666667/4.966666666666667/4.966666666666667/4.966666666666667/4.966666666666667
- mean overall (avg R/H/S/D/K): 4.966666666666667
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.53, hallucination_suspected=0.00
### unknown (n=60)
- mean runtime: 10.266916666666667
- mean R/H/S/D/K: 4.65/4.65/4.816666666666666/4.75/4.45
- mean overall (avg R/H/S/D/K): 4.663333333333333
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.22, hallucination_suspected=0.00

## Mean scores by strategy (snapshot)
### S0 (n=30)
- mean runtime: 8.2502
- mean R/H/S/D/K: 3.8333333333333335/3.9/4.166666666666667/4.333333333333333/2.5
- mean overall (avg R/H/S/D/K): 3.746666666666667
### S0_RAW (n=30)
- mean runtime: 9.963133333333333
- mean R/H/S/D/K: 4.866666666666666/4.866666666666666/4.9/4.966666666666667/4.833333333333333
- mean overall (avg R/H/S/D/K): 4.886666666666667
### S0_UNSTRUCTURED (n=30)
- mean runtime: 10.570699999999999
- mean R/H/S/D/K: 4.433333333333334/4.433333333333334/4.733333333333333/4.533333333333333/4.066666666666666
- mean overall (avg R/H/S/D/K): 4.4399999999999995
### S1 (n=30)
- mean runtime: 9.975433333333333
- mean R/H/S/D/K: 4.933333333333334/4.9/4.9/4.966666666666667/4.633333333333334
- mean overall (avg R/H/S/D/K): 4.866666666666666
### S2 (n=30)
- mean runtime: 10.028166666666667
- mean R/H/S/D/K: 4.966666666666667/4.966666666666667/4.966666666666667/4.966666666666667/4.966666666666667
- mean overall (avg R/H/S/D/K): 4.966666666666667

## Top missing elements (max 20)
- offline_workflow: 6
- Keine Nutzung der Asset-ID im Kontext: 3
- Offline-Workflow nicht explizit adressiert: 2
- Kontext-Nutzung minimal (nur Asset-ID): 2
- Offline-Workflow nicht explizit erwähnt (spotty connectivity vorhanden): 2
- Offline-Workflow (spotty connectivity): 2
- Offline-Workflow nicht explizit erwähnt (spotty connectivity im Kontext): 2
- Offline-Workflow (nicht erwartbar aus Kontext): 2
- Offline-Workflow (nicht erwartbar, da CONTEXT minimal): 1
- Wetter/Sicht-Bezug (nicht im CONTEXT): 1
- Offline-Workflow nicht explizit erwähnt: 1
- Keine Nutzung der Asset-ID aus Context: 1
- Spekuliert über Stromversorgung/Steuergerät ohne Context-Basis: 1
- Keine GPS-Koordinaten erwähnt (nicht im Context): 1
- Asset-ID nicht prominent in Dokumentation: 1
- Keine Erwähnung von Hauptverkehrszeit/hohem Verkehr aus User message: 1
- Keine Priorisierung auf intermittierenden Fehler: 1
- Unstrukturierter Kontext nur teilweise interpretiert: 1
- Keine explizite Erwähnung von OSM-ID oder Koordinaten: 1
- Offline-Workflow (spotty connectivity erwähnt, aber nicht explizit adressiert): 1
