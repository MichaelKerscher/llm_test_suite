# Aggregation Report (506/mistral-large)
- judge_version filter: **judge_v1_1**
- Tests (latest runs): **90**
- Incidents with any deltas: **30**

## Mean scores by context level (snapshot)
### L0 (n=30)
- mean runtime: 5.3031
- mean R/H/S/D/K: 3.566666666666667/3.8666666666666667/3.566666666666667/4.1/2.8666666666666667
- mean overall (avg R/H/S/D/K): 3.5933333333333333
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.00, hallucination_suspected=0.07
### L2 (n=30)
- mean runtime: 8.2994
- mean R/H/S/D/K: 4.733333333333333/4.6/4.566666666666666/4.866666666666666/3.8
- mean overall (avg R/H/S/D/K): 4.513333333333334
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.07, hallucination_suspected=0.13
### L2B (n=30)
- mean runtime: 8.408533333333333
- mean R/H/S/D/K: 4.966666666666667/4.966666666666667/4.766666666666667/5.0/4.966666666666667
- mean overall (avg R/H/S/D/K): 4.933333333333334
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.60, hallucination_suspected=0.00

## Mean scores by strategy (snapshot)
### S0 (n=30)
- mean runtime: 5.3031
- mean R/H/S/D/K: 3.566666666666667/3.8666666666666667/3.566666666666667/4.1/2.8666666666666667
- mean overall (avg R/H/S/D/K): 3.5933333333333333
### S1 (n=30)
- mean runtime: 8.2994
- mean R/H/S/D/K: 4.733333333333333/4.6/4.566666666666666/4.866666666666666/3.8
- mean overall (avg R/H/S/D/K): 4.513333333333334
### S2 (n=30)
- mean runtime: 8.408533333333333
- mean R/H/S/D/K: 4.966666666666667/4.966666666666667/4.766666666666667/5.0/4.966666666666667
- mean overall (avg R/H/S/D/K): 4.933333333333334

## Top missing elements (max 20)
- Offline-Workflow bei spotty connectivity: 5
- Kontextnutzung minimal (nur Asset-ID): 3
- Offline-Workflow (nicht erwartbar, da kein Signal im Kontext): 2
- Offline-Workflow (spotty connectivity): 2
- Offline-Workflow (connectivity=offline): 2
- Kontextnutzung minimal (nur Asset-ID vorhanden): 1
- Offline-Workflow fehlt (device.connectivity=offline → MUSS erwähnt werden): 1
- Low-battery-Hinweis für Techniker-Gerät fehlt: 1
- Offline-Workflow explizit (spotty connectivity): 1
- Offline-Workflow nicht erwähnt (aber auch nicht erwartbar bei minimalem Kontext): 1
- Offline-Workflow (lokal dokumentieren/später sync): 1
- Klarstellung: device.* = Techniker-Gerät, nicht Asset: 1
- Offline-Workflow (nicht erwartbar bei L0_minimal): 1
- Halluzinationen: Ampel, Schaltkasten, IR-Thermometer, Verkehrsbehörde: 1
- Gerätestatus korrekt interpretiert: 1
- Keine Anpassung an Umgebungsbedingungen: 1
- Kontext-Nutzung (nur Asset-ID vorhanden, keine weiteren Signale): 1
- Offline-Workflow nicht erwartbar (kein Signal im Context): 1
- Offline-Workflow (spotty connectivity erwähnt, aber kein expliziter Offline-Workflow beschrieben): 1
- Keine Nutzung der Asset-ID im Kontext: 1
