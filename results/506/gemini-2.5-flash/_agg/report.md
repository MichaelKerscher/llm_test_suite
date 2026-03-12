# Aggregation Report (506/gemini-2.5-flash)
- judge_version filter: **judge_v1_1**
- Tests (latest runs): **90**
- Incidents with any deltas: **30**

## Mean scores by context level (snapshot)
### L0 (n=30)
- mean runtime: 7.4347666666666665
- mean R/H/S/D/K: 3.6/3.933333333333333/3.7666666666666666/4.1/2.8666666666666667
- mean overall (avg R/H/S/D/K): 3.6533333333333333
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.00, hallucination_suspected=0.03
### L2 (n=30)
- mean runtime: 9.167200000000001
- mean R/H/S/D/K: 4.8/4.7/4.633333333333334/4.966666666666667/3.966666666666667
- mean overall (avg R/H/S/D/K): 4.613333333333333
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.07, hallucination_suspected=0.03
### L2B (n=30)
- mean runtime: 9.854433333333333
- mean R/H/S/D/K: 4.966666666666667/4.966666666666667/4.833333333333333/5.0/4.966666666666667
- mean overall (avg R/H/S/D/K): 4.946666666666667
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.60, hallucination_suspected=0.03

## Mean scores by strategy (snapshot)
### S0 (n=30)
- mean runtime: 7.4347666666666665
- mean R/H/S/D/K: 3.6/3.933333333333333/3.7666666666666666/4.1/2.8666666666666667
- mean overall (avg R/H/S/D/K): 3.6533333333333333
### S1 (n=30)
- mean runtime: 9.167200000000001
- mean R/H/S/D/K: 4.8/4.7/4.633333333333334/4.966666666666667/3.966666666666667
- mean overall (avg R/H/S/D/K): 4.613333333333333
### S2 (n=30)
- mean runtime: 9.854433333333333
- mean R/H/S/D/K: 4.966666666666667/4.966666666666667/4.833333333333333/5.0/4.966666666666667
- mean overall (avg R/H/S/D/K): 4.946666666666667

## Top missing elements (max 20)
- Offline-Workflow bei spotty connectivity: 3
- Offline-Workflow bei spotty connectivity nicht explizit erwähnt: 2
- Offline-Workflow (device.connectivity=offline): 1
- Klarstellung device_state=low_battery betrifft Techniker-Gerät, nicht Asset: 1
- Keine Nutzung von Kontext (nur Asset-ID vorhanden): 1
- Keine Erwähnung von Foto-Verfügbarkeit: 1
- Keine spezifische Anpassung an Umgebungsbedingungen: 1
- Offline-Workflow (spotty connectivity): 1
- Offline-Workflow (spotty connectivity + low_battery): 1
- Keine Offline-Workflow-Erwähnung (aber nicht erwartbar bei L0_minimal): 1
- Severity-Einschätzung fehlt (high nicht erkennbar aus Kontext): 1
- Keine klare Priorisierung bei Eskalation: 1
- Offline-Workflow fehlt (device.connectivity=offline, device_state=low_battery → erwartbar): 1
- Keine Erwähnung lokaler Speicherung/Synchronisation später: 1
- Offline-Workflow (connectivity=offline im Context): 1
- Kontextnutzung (nur Asset-ID vorhanden, keine weiteren Infos genutzt): 1
- Offline-Workflow nicht erwähnt (bei minimalem Kontext nicht zwingend erwartbar): 1
- Offline-Workflow (spotty connectivity → sollte erwähnt werden): 1
- Keine Nutzung der Asset-ID in Dokumentation: 1
- Keine GPS-Koordinaten erwähnt (nicht im Context): 1
