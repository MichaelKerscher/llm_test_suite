# Aggregation Report (506\mistral-large) [combined]
- judge_version filter: **judge_v1_1**
- Tests (latest runs): **300**
- Incidents with any deltas: **60**

## Mean scores by context level (snapshot)
### L0 (n=60)
- mean runtime: 5.87725
- mean R/H/S/D/K: 3.716666666666667/3.816666666666667/3.783333333333333/4.083333333333333/2.9
- mean overall (avg R/H/S/D/K): 3.6599999999999997
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.00, hallucination_suspected=0.10
### L2 (n=60)
- mean runtime: 8.643
- mean R/H/S/D/K: 4.866666666666666/4.716666666666667/4.8/4.9/4.2
- mean overall (avg R/H/S/D/K): 4.696666666666667
- flags (rate): safety_first=0.98, escalation_present=1.00, offline_workflow_mentioned=0.15, hallucination_suspected=0.08
### L2B (n=60)
- mean runtime: 8.721566666666666
- mean R/H/S/D/K: 4.95/4.883333333333334/4.883333333333334/4.916666666666667/5.0
- mean overall (avg R/H/S/D/K): 4.926666666666667
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.60, hallucination_suspected=0.00
### unknown (n=120)
- mean runtime: 9.17315
- mean R/H/S/D/K: 4.85/4.858333333333333/4.841666666666667/4.95/4.966666666666667
- mean overall (avg R/H/S/D/K): 4.8933333333333335
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.47, hallucination_suspected=0.00

## Mean scores by strategy (snapshot)
### S0 (n=60)
- mean runtime: 5.87725
- mean R/H/S/D/K: 3.716666666666667/3.816666666666667/3.783333333333333/4.083333333333333/2.9
- mean overall (avg R/H/S/D/K): 3.6599999999999997
### S1 (n=60)
- mean runtime: 8.643
- mean R/H/S/D/K: 4.866666666666666/4.716666666666667/4.8/4.9/4.2
- mean overall (avg R/H/S/D/K): 4.696666666666667
### S2 (n=60)
- mean runtime: 8.721566666666666
- mean R/H/S/D/K: 4.95/4.883333333333334/4.883333333333334/4.916666666666667/5.0
- mean overall (avg R/H/S/D/K): 4.926666666666667
### S2_ABL_NOASSET (n=30)
- mean runtime: 9.7382
- mean R/H/S/D/K: 4.866666666666666/4.9/4.866666666666666/4.933333333333334/4.966666666666667
- mean overall (avg R/H/S/D/K): 4.906666666666666
### S2_ABL_NODEV (n=30)
- mean runtime: 9.3244
- mean R/H/S/D/K: 4.966666666666667/4.933333333333334/4.866666666666666/5.0/4.966666666666667
- mean overall (avg R/H/S/D/K): 4.946666666666667
### S2_ABL_NOENV (n=30)
- mean runtime: 8.850366666666668
- mean R/H/S/D/K: 4.833333333333333/4.766666666666667/4.7/4.9/4.933333333333334
- mean overall (avg R/H/S/D/K): 4.826666666666667
### S2_ABL_NOINC (n=30)
- mean runtime: 8.779633333333333
- mean R/H/S/D/K: 4.733333333333333/4.833333333333333/4.933333333333334/4.966666666666667/5.0
- mean overall (avg R/H/S/D/K): 4.8933333333333335

## Top missing elements (max 20)
- Offline-Workflow bei spotty connectivity: 6
- Kontextnutzung minimal (nur Asset-ID): 3
- Offline-Workflow bei spotty connectivity nicht explizit erwähnt: 3
- Keine Nutzung der Asset-ID im Kontext: 3
- Keine Priorisierung nach Severity (nicht im Context): 2
- Keine Kontextnutzung (nur Asset-ID vorhanden): 2
- Severity-basierte Priorisierung: 2
- Klare Stop-Condition für Beobachtungsphase fehlt: 1
- Offline-Workflow fehlt trotz connectivity=offline: 1
- Verwechslung device.* mit Asset-Fehlerursache: 1
- Keine Nutzung von Umgebungs-/Foto-Kontext (nicht vorhanden): 1
- Keine spezifische Priorisierung bei intermittent fault: 1
- Explizite Erwähnung der Asset-ID (n4427359783) in Dokumentation: 1
- Keine Anpassung an Umgebung/Zeit/Konnektivität: 1
- Offline-Workflow nicht erwähnt trotz spotty connectivity: 1
- Annahme zu low_battery spekulativ formuliert: 1
- Offline-Workflow (connectivity=offline, device_state=low_battery): 1
- Offline-Workflow (connectivity=offline → lokal dokumentieren/später sync): 1
- Annahme 'Straßenleuchte' ohne Basis: 1
- Spekulation über Ampel/Bewuchs ohne Signal: 1
