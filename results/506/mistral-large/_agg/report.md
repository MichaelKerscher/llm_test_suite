# Aggregation Report (506/mistral-large)
- judge_version filter: **judge_v1_1**
- Tests (latest runs): **210**
- Incidents with any deltas: **30**

## Mean scores by context level (snapshot)
### L0 (n=30)
- mean runtime: 5.444566666666666
- mean R/H/S/D/K: 3.533333333333333/3.6666666666666665/3.6/4.0/2.9
- mean overall (avg R/H/S/D/K): 3.54
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.00, hallucination_suspected=0.10
### L2 (n=30)
- mean runtime: 8.620433333333333
- mean R/H/S/D/K: 4.8/4.6/4.733333333333333/4.833333333333333/3.8666666666666667
- mean overall (avg R/H/S/D/K): 4.566666666666666
- flags (rate): safety_first=0.97, escalation_present=1.00, offline_workflow_mentioned=0.10, hallucination_suspected=0.17
### L2B (n=30)
- mean runtime: 9.108633333333334
- mean R/H/S/D/K: 4.933333333333334/4.866666666666666/4.833333333333333/4.966666666666667/5.0
- mean overall (avg R/H/S/D/K): 4.92
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.60, hallucination_suspected=0.00
### unknown (n=120)
- mean runtime: 9.020058333333333
- mean R/H/S/D/K: 4.925/4.85/4.866666666666666/4.966666666666667/4.983333333333333
- mean overall (avg R/H/S/D/K): 4.918333333333334
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.45, hallucination_suspected=0.00

## Mean scores by strategy (snapshot)
### S0 (n=30)
- mean runtime: 5.444566666666666
- mean R/H/S/D/K: 3.533333333333333/3.6666666666666665/3.6/4.0/2.9
- mean overall (avg R/H/S/D/K): 3.54
### S1 (n=30)
- mean runtime: 8.620433333333333
- mean R/H/S/D/K: 4.8/4.6/4.733333333333333/4.833333333333333/3.8666666666666667
- mean overall (avg R/H/S/D/K): 4.566666666666666
### S2 (n=30)
- mean runtime: 9.108633333333334
- mean R/H/S/D/K: 4.933333333333334/4.866666666666666/4.833333333333333/4.966666666666667/5.0
- mean overall (avg R/H/S/D/K): 4.92
### S2_ABL_NOASSET (n=30)
- mean runtime: 9.652566666666667
- mean R/H/S/D/K: 4.933333333333334/4.933333333333334/4.9/5.0/5.0
- mean overall (avg R/H/S/D/K): 4.953333333333333
### S2_ABL_NODEV (n=30)
- mean runtime: 8.844166666666666
- mean R/H/S/D/K: 4.933333333333334/4.766666666666667/4.8/4.933333333333334/4.966666666666667
- mean overall (avg R/H/S/D/K): 4.88
### S2_ABL_NOENV (n=30)
- mean runtime: 8.653699999999999
- mean R/H/S/D/K: 4.9/4.733333333333333/4.8/4.933333333333334/4.966666666666667
- mean overall (avg R/H/S/D/K): 4.866666666666666
### S2_ABL_NOINC (n=30)
- mean runtime: 8.9298
- mean R/H/S/D/K: 4.933333333333334/4.966666666666667/4.966666666666667/5.0/5.0
- mean overall (avg R/H/S/D/K): 4.973333333333333

## Top missing elements (max 20)
- Offline-Workflow bei spotty connectivity: 5
- Offline-Workflow bei spotty connectivity nicht explizit erwähnt: 3
- Keine Nutzung der Asset-ID im Kontext: 3
- Kontextnutzung minimal (nur Asset-ID): 2
- Keine Priorisierung nach Severity (nicht im Context): 2
- Offline-Workflow fehlt trotz connectivity=offline: 1
- Verwechslung device.* mit Asset-Fehlerursache: 1
- Keine Nutzung von Umgebungs-/Foto-Kontext (nicht vorhanden): 1
- Keine spezifische Priorisierung bei intermittent fault: 1
- Keine Anpassung an Umgebung/Zeit/Konnektivität: 1
- Offline-Workflow nicht erwähnt trotz spotty connectivity: 1
- Annahme zu low_battery spekulativ formuliert: 1
- Explizite Stop-Conditions vor Eskalation: 1
- Offline-Workflow (connectivity=offline, device_state=low_battery): 1
- Offline-Workflow (connectivity=offline → lokal dokumentieren/später sync): 1
- Annahme 'Straßenleuchte' ohne Basis: 1
- Spekulation über Ampel/Bewuchs ohne Signal: 1
- Offline-Workflow bei spotty connectivity nicht erwähnt: 1
- Offline-Workflow nicht klar priorisiert: 1
- Widerspruch 'offline vs. ok' ist Fehlinterpretation: 1
