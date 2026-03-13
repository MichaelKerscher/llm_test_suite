# Aggregation Report (506/mistral-large)
- judge_version filter: **judge_v1_1**
- Tests (latest runs): **90**
- Incidents with any deltas: **30**

## Mean scores by context level (snapshot)
### L0 (n=30)
- mean runtime: 5.4493
- mean R/H/S/D/K: 3.6333333333333333/3.9/3.7333333333333334/4.033333333333333/2.8666666666666667
- mean overall (avg R/H/S/D/K): 3.6333333333333333
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.00, hallucination_suspected=0.03
### L2 (n=30)
- mean runtime: 8.452233333333334
- mean R/H/S/D/K: 4.866666666666666/4.7/4.633333333333334/5.0/3.8333333333333335
- mean overall (avg R/H/S/D/K): 4.6066666666666665
- flags (rate): safety_first=0.97, escalation_present=1.00, offline_workflow_mentioned=0.07, hallucination_suspected=0.10
### L2B (n=30)
- mean runtime: 8.805733333333334
- mean R/H/S/D/K: 5.0/4.966666666666667/4.9/5.0/5.0
- mean overall (avg R/H/S/D/K): 4.973333333333333
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.60, hallucination_suspected=0.00

## Mean scores by strategy (snapshot)
### S0 (n=30)
- mean runtime: 5.4493
- mean R/H/S/D/K: 3.6333333333333333/3.9/3.7333333333333334/4.033333333333333/2.8666666666666667
- mean overall (avg R/H/S/D/K): 3.6333333333333333
### S1 (n=30)
- mean runtime: 8.452233333333334
- mean R/H/S/D/K: 4.866666666666666/4.7/4.633333333333334/5.0/3.8333333333333335
- mean overall (avg R/H/S/D/K): 4.6066666666666665
### S2 (n=30)
- mean runtime: 8.805733333333334
- mean R/H/S/D/K: 5.0/4.966666666666667/4.9/5.0/5.0
- mean overall (avg R/H/S/D/K): 4.973333333333333

## Top missing elements (max 20)
- Offline-Workflow bei spotty connectivity: 3
- Kontextnutzung minimal (nur Asset-ID vorhanden): 2
- Kontextnutzung minimal (nur Asset-ID): 2
- Offline-Workflow bei spotty connectivity nicht erwähnt: 2
- Offline-Workflow nicht erwähnt (aber auch nicht erwartbar aus minimalem Kontext): 1
- Offline-Workflow fehlt trotz connectivity=offline im Kontext: 1
- Keine Erwähnung von Akku-Ladung/Synchronisation später: 1
- Keine Nutzung der Asset-ID im Text: 1
- Keine Erwähnung von GPS/Koordinaten (nicht im Context vorhanden): 1
- Offline-Workflow bei spotty connectivity nicht explizit erwähnt: 1
- Offline-Workflow (device.connectivity=offline): 1
- Offline-Workflow (connectivity=offline): 1
- Keine Online-Schritte erlaubt: 1
- Keine Kontextnutzung (nur Asset-ID vorhanden): 1
- Keine Priorisierung bei unbekanntem severity: 1
- Offline-Workflow fehlt (connectivity=spotty, device_state=low_power_mode): 1
- Missverständnis: device.* als Asset-Problem interpretiert: 1
- Offline-Workflow nicht explizit beschrieben: 1
- Offline-Workflow (spotty connectivity): 1
- Keine Nutzung der Asset-ID im Kontext (nur minimal vorhanden): 1
