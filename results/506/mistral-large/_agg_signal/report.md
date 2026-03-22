# Aggregation Report (506\mistral-large) [signal]
- judge_version filter: **judge_v1_1**
- Tests (latest runs): **90**
- Incidents with any deltas: **30**

## Mean scores by context level (snapshot)
### L0 (n=30)
- mean runtime: 6.022
- mean R/H/S/D/K: 3.8666666666666667/3.966666666666667/4.033333333333333/4.133333333333334/2.7666666666666666
- mean overall (avg R/H/S/D/K): 3.753333333333333
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.00, hallucination_suspected=0.10
### L2 (n=30)
- mean runtime: 7.8635
- mean R/H/S/D/K: 4.933333333333334/4.8/4.8/5.0/4.5
- mean overall (avg R/H/S/D/K): 4.806666666666667
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.17, hallucination_suspected=0.00
### L2B (n=30)
- mean runtime: 8.392566666666665
- mean R/H/S/D/K: 4.966666666666667/4.9/4.933333333333334/4.9/4.966666666666667
- mean overall (avg R/H/S/D/K): 4.933333333333334
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.57, hallucination_suspected=0.00

## Mean scores by strategy (snapshot)
### S0 (n=30)
- mean runtime: 6.022
- mean R/H/S/D/K: 3.8666666666666667/3.966666666666667/4.033333333333333/4.133333333333334/2.7666666666666666
- mean overall (avg R/H/S/D/K): 3.753333333333333
### S1 (n=30)
- mean runtime: 7.8635
- mean R/H/S/D/K: 4.933333333333334/4.8/4.8/5.0/4.5
- mean overall (avg R/H/S/D/K): 4.806666666666667
### S2 (n=30)
- mean runtime: 8.392566666666665
- mean R/H/S/D/K: 4.966666666666667/4.9/4.933333333333334/4.9/4.966666666666667
- mean overall (avg R/H/S/D/K): 4.933333333333334

## Top missing elements (max 20)
- Kontextnutzung minimal (nur Asset-ID vorhanden): 3
- Offline-Workflow (nicht erwartbar bei L0): 2
- Wetter-/Sichtbedingungen (nicht im Context): 2
- Offline-Workflow (nicht erwartbar bei L0_minimal): 2
- Spekuliert leicht über Ampel/Straßenlampe (asset_type=unknown): 2
- Offline-Workflow bei spotty connectivity nicht explizit erwähnt: 2
- Expliziter Offline-Workflow (connectivity=offline im Context, aber nicht als separater Workflow-Schritt hervorgehoben): 1
- Severity-Einschätzung fehlt (nur Asset-ID gegeben): 1
- Keine Priorisierung bei Eskalation erkennbar: 1
- GPS-Koordinaten nicht explizit in Doku erwähnt: 1
- GPS-Koordinaten nicht genutzt (nicht im Context): 1
- Keine Priorisierung nach severity/traffic: 1
- Kontextnutzung minimal (nur Asset-ID): 1
- Halluzinationen: Ampel/Licht/Steuerung ohne Basis: 1
- Offline-Workflow nicht erwartbar (kein Signal): 1
- Offline-Workflow nicht erwähnt (spotty connectivity): 1
- Widerspruch device_state/connectivity nur angemerkt, nicht gelöst: 1
- Offline-Workflow (spotty connectivity + low_power_mode): 1
- Explizite Erwähnung 'Kreuzung wie unbeschrankt behandeln': 1
- Offline-Workflow (spotty connectivity + low battery): 1
