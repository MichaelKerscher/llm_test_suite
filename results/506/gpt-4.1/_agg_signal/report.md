# Aggregation Report (506/gpt-4.1) [signal]
- judge_version filter: **judge_v1_1**
- Tests (latest runs): **150**
- Incidents with any deltas: **30**

## Mean scores by context level (snapshot)
### L0 (n=30)
- mean runtime: 7.157733333333334
- mean R/H/S/D/K: 3.8333333333333335/4.0/3.9/4.1/2.6333333333333333
- mean overall (avg R/H/S/D/K): 3.6933333333333334
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.00, hallucination_suspected=0.03
### L2 (n=30)
- mean runtime: 9.875200000000001
- mean R/H/S/D/K: 4.866666666666666/4.833333333333333/4.8/4.966666666666667/4.566666666666666
- mean overall (avg R/H/S/D/K): 4.806666666666667
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.10, hallucination_suspected=0.00
### L2B (n=30)
- mean runtime: 9.784500000000001
- mean R/H/S/D/K: 4.9/4.9/4.9/4.9/4.966666666666667
- mean overall (avg R/H/S/D/K): 4.913333333333333
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.60, hallucination_suspected=0.00
### unknown (n=60)
- mean runtime: 10.694133333333333
- mean R/H/S/D/K: 4.966666666666667/4.966666666666667/4.983333333333333/4.983333333333333/4.933333333333334
- mean overall (avg R/H/S/D/K): 4.966666666666667
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.38, hallucination_suspected=0.00

## Mean scores by strategy (snapshot)
### S0 (n=30)
- mean runtime: 7.157733333333334
- mean R/H/S/D/K: 3.8333333333333335/4.0/3.9/4.1/2.6333333333333333
- mean overall (avg R/H/S/D/K): 3.6933333333333334
### S0_RAW (n=30)
- mean runtime: 10.949633333333333
- mean R/H/S/D/K: 5.0/5.0/4.966666666666667/4.966666666666667/4.966666666666667
- mean overall (avg R/H/S/D/K): 4.98
### S0_UNSTRUCTURED (n=30)
- mean runtime: 10.438633333333334
- mean R/H/S/D/K: 4.933333333333334/4.933333333333334/5.0/5.0/4.9
- mean overall (avg R/H/S/D/K): 4.953333333333333
### S1 (n=30)
- mean runtime: 9.875200000000001
- mean R/H/S/D/K: 4.866666666666666/4.833333333333333/4.8/4.966666666666667/4.566666666666666
- mean overall (avg R/H/S/D/K): 4.806666666666667
### S2 (n=30)
- mean runtime: 9.784500000000001
- mean R/H/S/D/K: 4.9/4.9/4.9/4.9/4.966666666666667
- mean overall (avg R/H/S/D/K): 4.913333333333333

## Top missing elements (max 20)
- Kontextnutzung minimal (nur Asset-ID): 3
- Offline-Workflow bei spotty connectivity: 3
- Offline-Workflow (nicht erwartbar bei L0_minimal): 2
- Offline-Workflow explizit (device.connectivity=offline vorhanden, aber nicht als 'lokale Dokumentation, spätere Sync' formuliert): 2
- Explizite Erwähnung severity=high: 2
- Offline-Workflow bei spotty connectivity nicht explizit erwähnt: 2
- Offline-Workflow (device.connectivity=offline nicht explizit adressiert): 1
- Offline-Workflow (Dokumentation lokal, spätere Sync): 1
- Severity-Einschätzung fehlt (nur aus Asset-ID ableitbar): 1
- Keine Erwähnung von Wetter/Sicht (nicht im Context): 1
- Keine Nutzung von Kontext-Signalen (rush_hour, high traffic): 1
- Keine Erwähnung von Verkehrsleitstelle bei medium severity + high traffic: 1
- Regen als Sicherheitsfaktor: 1
- Severity-Einschätzung fehlt (nur Asset-ID vorhanden): 1
- Keine Priorisierung nach Dringlichkeit erkennbar: 1
- Offline-Workflow (nicht erwartbar, da kein Signal im Kontext): 1
- Keine Nutzung der Richtungsinfo 'backward': 1
- Keine Erwähnung von Timing-Vergleich mit Soll-Zeiten: 1
- Keine Priorisierung nach Verkehrslage/Severity: 1
- Keine Nutzung des Kontexts (nur Asset-ID vorhanden): 1
