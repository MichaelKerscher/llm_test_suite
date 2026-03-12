# Aggregation Report (506/gemini-2.5-flash)
- judge_version filter: **judge_v1_1**
- Tests (latest runs): **90**
- Incidents with any deltas: **30**

## Mean scores by context level (snapshot)
### L0 (n=30)
- mean runtime: 6.270433333333333
- mean R/H/S/D/K: 3.533333333333333/3.933333333333333/3.8333333333333335/4.066666666666666/2.8666666666666667
- mean overall (avg R/H/S/D/K): 3.646666666666667
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.00, hallucination_suspected=0.03
### L2 (n=30)
- mean runtime: 9.752866666666668
- mean R/H/S/D/K: 4.8/4.633333333333334/4.7/4.866666666666666/3.7
- mean overall (avg R/H/S/D/K): 4.54
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.10, hallucination_suspected=0.20
### L2B (n=30)
- mean runtime: 10.068000000000001
- mean R/H/S/D/K: 4.933333333333334/4.866666666666666/4.833333333333333/4.9/4.966666666666667
- mean overall (avg R/H/S/D/K): 4.9
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.60, hallucination_suspected=0.00

## Mean scores by strategy (snapshot)
### S0 (n=30)
- mean runtime: 6.270433333333333
- mean R/H/S/D/K: 3.533333333333333/3.933333333333333/3.8333333333333335/4.066666666666666/2.8666666666666667
- mean overall (avg R/H/S/D/K): 3.646666666666667
### S1 (n=30)
- mean runtime: 9.752866666666668
- mean R/H/S/D/K: 4.8/4.633333333333334/4.7/4.866666666666666/3.7
- mean overall (avg R/H/S/D/K): 4.54
### S2 (n=30)
- mean runtime: 10.068000000000001
- mean R/H/S/D/K: 4.933333333333334/4.866666666666666/4.833333333333333/4.9/4.966666666666667
- mean overall (avg R/H/S/D/K): 4.9

## Top missing elements (max 20)
- Offline-Workflow bei spotty connectivity: 4
- Offline-Workflow (lokal dokumentieren/synchronisieren): 2
- Kontextnutzung minimal (nur Asset-ID): 2
- Offline-Workflow (lokal dokumentieren/später sync): 2
- Offline-Workflow bei spotty connectivity nicht explizit erwähnt: 2
- Klarstellung: device.* = Techniker-Gerät, nicht Asset-Fehlerursache: 1
- Keine Anpassung an Umgebung/Zeit/Wetter: 1
- Foto-Hinweis könnte expliziter sein: 1
- Offline-Workflow (spotty connectivity): 1
- Keine Kontextnutzung (nur Asset-ID vorhanden): 1
- Keine Anpassung an Umgebungsbedingungen: 1
- Offline-Workflow trotz spotty connectivity nicht erwähnt: 1
- Missverständnis: device_state als Asset-Problem interpretiert: 1
- Offline-Workflow (lokal dokumentieren/Foto lokal speichern): 1
- Offline-Workflow explizit (spotty connectivity): 1
- Klarstellung device_state bezieht sich auf Techniker-Gerät: 1
- Spekulation über Ampelanlagen ohne Basis: 1
- Keine Anpassung an unbekannten asset_type: 1
- Keine Nutzung von Kontext (nur Asset-ID vorhanden): 1
- Keine Priorisierung nach Severity/Umgebung (nicht im Context): 1
