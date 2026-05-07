# Aggregation Report (506/mistral-large) [signal]
- judge_version filter: **judge_v1_1**
- Tests (latest runs): **150**
- Incidents with any deltas: **30**

## Mean scores by context level (snapshot)
### L0 (n=30)
- mean runtime: 8.754366666666668
- mean R/H/S/D/K: 3.8666666666666667/3.933333333333333/4.133333333333334/4.133333333333334/2.533333333333333
- mean overall (avg R/H/S/D/K): 3.7199999999999998
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.00, hallucination_suspected=0.23
### L2 (n=30)
- mean runtime: 11.3852
- mean R/H/S/D/K: 4.866666666666666/4.833333333333333/4.833333333333333/4.9/4.6
- mean overall (avg R/H/S/D/K): 4.806666666666667
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.17, hallucination_suspected=0.00
### L2B (n=30)
- mean runtime: 10.342933333333333
- mean R/H/S/D/K: 4.933333333333334/4.933333333333334/4.9/4.933333333333334/4.966666666666667
- mean overall (avg R/H/S/D/K): 4.933333333333334
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.53, hallucination_suspected=0.00
### unknown (n=60)
- mean runtime: 11.093716666666667
- mean R/H/S/D/K: 4.55/4.566666666666666/4.716666666666667/4.683333333333334/4.166666666666667
- mean overall (avg R/H/S/D/K): 4.536666666666666
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.18, hallucination_suspected=0.00

## Mean scores by strategy (snapshot)
### S0 (n=30)
- mean runtime: 8.754366666666668
- mean R/H/S/D/K: 3.8666666666666667/3.933333333333333/4.133333333333334/4.133333333333334/2.533333333333333
- mean overall (avg R/H/S/D/K): 3.7199999999999998
### S0_RAW (n=30)
- mean runtime: 11.335866666666668
- mean R/H/S/D/K: 4.8/4.8/4.833333333333333/4.866666666666666/4.566666666666666
- mean overall (avg R/H/S/D/K): 4.7733333333333325
### S0_UNSTRUCTURED (n=30)
- mean runtime: 10.851566666666667
- mean R/H/S/D/K: 4.3/4.333333333333333/4.6/4.5/3.7666666666666666
- mean overall (avg R/H/S/D/K): 4.3
### S1 (n=30)
- mean runtime: 11.3852
- mean R/H/S/D/K: 4.866666666666666/4.833333333333333/4.833333333333333/4.9/4.6
- mean overall (avg R/H/S/D/K): 4.806666666666667
### S2 (n=30)
- mean runtime: 10.342933333333333
- mean R/H/S/D/K: 4.933333333333334/4.933333333333334/4.9/4.933333333333334/4.966666666666667
- mean overall (avg R/H/S/D/K): 4.933333333333334

## Top missing elements (max 20)
- offline_workflow_explicit: 4
- Offline-Workflow (nicht erwartbar, da connectivity nicht im CONTEXT): 3
- Keine Nutzung der Asset-ID im Kontext: 2
- Kontext-Nutzung minimal (nur Asset-ID): 2
- Offline-Workflow (erwartbar bei connectivity=spotty): 2
- Offline-Workflow bei spotty connectivity: 2
- Offline-Workflow nicht erwähnt, obwohl nicht im CONTEXT signalisiert: 1
- Offline-Workflow (nicht erwartbar aus minimalem Context): 1
- Halluzination: Steuerungseinheit, Statusleuchten, Wetterbedingungen nicht im Context: 1
- Offline-Workflow nicht explizit (aber offline im Context): 1
- Offline-Workflow nicht explizit erwähnt (aber offline im Context): 1
- Keine Kontextnutzung (nur Asset-ID vorhanden): 1
- Keine Erwähnung von Umgebungsbedingungen (nicht im Context): 1
- Keine explizite Erwähnung von Schnee/poor_visibility aus unstrukturiertem Context: 1
- Keine Erwähnung von Verkehrsaufkommen/Rush-Hour aus User message: 1
- Keine explizite Nutzung der Koordinaten oder OSM-ID aus unstructured context: 1
- Spekulation über Asset-Typ (Straßenlampe/Ampel) ohne Basis: 1
- GPS-Koordinaten nicht explizit in Doku-Checkliste: 1
- GPS-Koordinaten nicht explizit in Dokumentation erwähnt: 1
- Offline-Workflow nicht explizit (spotty connectivity im CONTEXT): 1
