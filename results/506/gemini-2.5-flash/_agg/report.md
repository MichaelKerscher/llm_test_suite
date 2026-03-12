# Aggregation Report (506/gemini-2.5-flash)
- judge_version filter: **judge_v1_1**
- Tests (latest runs): **90**
- Incidents with any deltas: **30**

## Mean scores by context level (snapshot)
### L0 (n=30)
- mean runtime: 6.7362
- mean R/H/S/D/K: 3.566666666666667/3.8666666666666667/3.933333333333333/4.033333333333333/2.966666666666667
- mean overall (avg R/H/S/D/K): 3.6733333333333333
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.00, hallucination_suspected=0.03
### L2 (n=30)
- mean runtime: 9.285300000000001
- mean R/H/S/D/K: 4.766666666666667/4.666666666666667/4.7/4.9/3.7333333333333334
- mean overall (avg R/H/S/D/K): 4.553333333333333
- flags (rate): safety_first=0.97, escalation_present=1.00, offline_workflow_mentioned=0.07, hallucination_suspected=0.10
### L2B (n=30)
- mean runtime: 9.551400000000001
- mean R/H/S/D/K: 4.966666666666667/4.966666666666667/4.833333333333333/4.966666666666667/5.0
- mean overall (avg R/H/S/D/K): 4.946666666666667
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.60, hallucination_suspected=0.00

## Mean scores by strategy (snapshot)
### S0 (n=30)
- mean runtime: 6.7362
- mean R/H/S/D/K: 3.566666666666667/3.8666666666666667/3.933333333333333/4.033333333333333/2.966666666666667
- mean overall (avg R/H/S/D/K): 3.6733333333333333
### S1 (n=30)
- mean runtime: 9.285300000000001
- mean R/H/S/D/K: 4.766666666666667/4.666666666666667/4.7/4.9/3.7333333333333334
- mean overall (avg R/H/S/D/K): 4.553333333333333
### S2 (n=30)
- mean runtime: 9.551400000000001
- mean R/H/S/D/K: 4.966666666666667/4.966666666666667/4.833333333333333/4.966666666666667/5.0
- mean overall (avg R/H/S/D/K): 4.946666666666667

## Top missing elements (max 20)
- Offline-Workflow bei spotty connectivity: 8
- Offline-Workflow (connectivity=offline): 1
- Keine Safety-first-Priorisierung trotz high traffic: 1
- Offline-Workflow (spotty connectivity + low_battery): 1
- Offline-Workflow (connectivity=offline, device_state=low_battery): 1
- Offline-Workflow (lokal dokumentieren/später sync): 1
- Offline-Workflow nicht erwähnt (aber auch nicht erwartbar bei L0_minimal): 1
- Offline-Workflow fehlt trotz connectivity=offline: 1
- Keine Erwähnung lokaler Speicherung/Synchronisation: 1
- Keine Nutzung von Kontext-Daten (nur Asset-ID vorhanden): 1
- Keine Priorisierung bei intermittierendem Fehler: 1
- Klare Priorisierung wegen severity=high: 1
- Keine Nutzung von Umgebungskontext (Zeit/Wetter/Verkehr): 1
- Keine Erwähnung der Geräte-Konnektivität: 1
- Offline-Workflow (connectivity=offline nicht adressiert): 1
- Offline-Workflow (lokal dokumentieren/Foto lokal speichern): 1
- Offline-Workflow (connectivity=offline → lokal dokumentieren/synchronisieren): 1
