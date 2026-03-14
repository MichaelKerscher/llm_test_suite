# Aggregation Report (506/mistral-large)
- judge_version filter: **judge_v1_1**
- Tests (latest runs): **90**
- Incidents with any deltas: **30**

## Mean scores by context level (snapshot)
### L0 (n=30)
- mean runtime: 5.0133
- mean R/H/S/D/K: 3.533333333333333/3.8666666666666667/3.7666666666666666/3.966666666666667/2.8333333333333335
- mean overall (avg R/H/S/D/K): 3.5933333333333333
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.00, hallucination_suspected=0.07
### L2 (n=30)
- mean runtime: 7.721466666666667
- mean R/H/S/D/K: 4.9/4.666666666666667/4.8/4.933333333333334/3.933333333333333
- mean overall (avg R/H/S/D/K): 4.6466666666666665
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.07, hallucination_suspected=0.10
### L2B (n=30)
- mean runtime: 8.2623
- mean R/H/S/D/K: 4.933333333333334/4.9/4.866666666666666/5.0/4.966666666666667
- mean overall (avg R/H/S/D/K): 4.933333333333334
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.60, hallucination_suspected=0.00

## Mean scores by strategy (snapshot)
### S0 (n=30)
- mean runtime: 5.0133
- mean R/H/S/D/K: 3.533333333333333/3.8666666666666667/3.7666666666666666/3.966666666666667/2.8333333333333335
- mean overall (avg R/H/S/D/K): 3.5933333333333333
### S1 (n=30)
- mean runtime: 7.721466666666667
- mean R/H/S/D/K: 4.9/4.666666666666667/4.8/4.933333333333334/3.933333333333333
- mean overall (avg R/H/S/D/K): 4.6466666666666665
### S2 (n=30)
- mean runtime: 8.2623
- mean R/H/S/D/K: 4.933333333333334/4.9/4.866666666666666/5.0/4.966666666666667
- mean overall (avg R/H/S/D/K): 4.933333333333334

## Top missing elements (max 20)
- Offline-Workflow bei spotty connectivity: 4
- Offline-Workflow bei spotty connectivity nicht explizit erwähnt: 3
- Offline-Workflow (connectivity=offline): 2
- Offline-Workflow (lokal dokumentieren/synchronisieren): 1
- Klarstellung: device.* = Techniker-Gerät, nicht Asset-Fehlerursache: 1
- Kein Bezug zu intermittent fault_type: 1
- Keine Nutzung von Foto-Hinweisen (nicht im Context): 1
- Offline-Workflow (spotty connectivity): 1
- Klare Unterscheidung device vs. asset: 1
- Offline-Workflow explizit (connectivity=spotty): 1
- Offline-Workflow (connectivity=offline, device_state=low_battery): 1
- Offline-Workflow explizit erwähnen: 1
- Severity-Bewusstsein fehlt (high severity nicht erkennbar): 1
- Keine Priorisierung bei Eskalation: 1
- Asset-ID falsch wiedergegeben (n44277955479 statt n4427955479): 1
- Keine Nutzung von Kontext (nur Asset-ID vorhanden): 1
- Keine Erwähnung intermittierender Natur des Fehlers: 1
- Keine Nutzung der GPS-Koordinaten (im CONTEXT vorhanden): 1
- Keine Erwähnung der Tageszeit/Umgebungsbedingungen: 1
- Keine Nutzung der Asset-ID im Kontext: 1
