# Aggregation Report (506/gpt-4.1)
- judge_version filter: **judge_v1_1**
- Tests (latest runs): **210**
- Incidents with any deltas: **30**

## Mean scores by context level (snapshot)
### L0 (n=30)
- mean runtime: 3.797433333333333
- mean R/H/S/D/K: 3.433333333333333/3.5/3.1/3.8/2.6333333333333333
- mean overall (avg R/H/S/D/K): 3.2933333333333334
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.00, hallucination_suspected=0.07
### L2 (n=30)
- mean runtime: 4.447533333333333
- mean R/H/S/D/K: 4.633333333333334/4.366666666666666/4.2/4.4/3.566666666666667
- mean overall (avg R/H/S/D/K): 4.233333333333333
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.07, hallucination_suspected=0.10
### L2B (n=30)
- mean runtime: 4.139466666666666
- mean R/H/S/D/K: 4.833333333333333/4.766666666666667/4.366666666666666/4.8/4.966666666666667
- mean overall (avg R/H/S/D/K): 4.746666666666667
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.70, hallucination_suspected=0.00
### unknown (n=120)
- mean runtime: 9.999625
- mean R/H/S/D/K: 4.883333333333334/4.833333333333333/4.858333333333333/4.958333333333333/4.966666666666667
- mean overall (avg R/H/S/D/K): 4.9
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.45, hallucination_suspected=0.00

## Mean scores by strategy (snapshot)
### S0 (n=30)
- mean runtime: 3.797433333333333
- mean R/H/S/D/K: 3.433333333333333/3.5/3.1/3.8/2.6333333333333333
- mean overall (avg R/H/S/D/K): 3.2933333333333334
### S1 (n=30)
- mean runtime: 4.447533333333333
- mean R/H/S/D/K: 4.633333333333334/4.366666666666666/4.2/4.4/3.566666666666667
- mean overall (avg R/H/S/D/K): 4.233333333333333
### S2 (n=30)
- mean runtime: 4.139466666666666
- mean R/H/S/D/K: 4.833333333333333/4.766666666666667/4.366666666666666/4.8/4.966666666666667
- mean overall (avg R/H/S/D/K): 4.746666666666667
### S2_ABL_NOASSET (n=30)
- mean runtime: 10.189533333333333
- mean R/H/S/D/K: 4.866666666666666/4.866666666666666/4.866666666666666/4.966666666666667/4.966666666666667
- mean overall (avg R/H/S/D/K): 4.906666666666666
### S2_ABL_NODEV (n=30)
- mean runtime: 9.4254
- mean R/H/S/D/K: 4.966666666666667/4.9/4.9/4.966666666666667/4.966666666666667
- mean overall (avg R/H/S/D/K): 4.9399999999999995
### S2_ABL_NOENV (n=30)
- mean runtime: 10.315233333333333
- mean R/H/S/D/K: 4.9/4.733333333333333/4.7/4.933333333333334/4.966666666666667
- mean overall (avg R/H/S/D/K): 4.846666666666667
### S2_ABL_NOINC (n=30)
- mean runtime: 10.068333333333333
- mean R/H/S/D/K: 4.8/4.833333333333333/4.966666666666667/4.966666666666667/4.966666666666667
- mean overall (avg R/H/S/D/K): 4.906666666666666

## Top missing elements (max 20)
- Offline-Workflow bei spotty connectivity: 3
- Kein expliziter Offline-Workflow trotz connectivity=spotty: 2
- Keine Nutzung der Asset-ID im Kontext: 2
- Kontextnutzung minimal (nur Asset-ID): 2
- Offline-Workflow (Gerät offline): 1
- Klarstellung: device_state betrifft Techniker-Gerät, nicht Asset: 1
- Keine Nutzung der Asset-ID im Workflow: 1
- Keine Berücksichtigung des intermittent-Charakters: 1
- Generische Ampel-Erwähnung ohne Kontext-Signal: 1
- Keine explizite Stop-Condition bei Gefahr: 1
- Kontext-Nutzung minimal (nur Asset-ID verwendet): 1
- Keine Anpassung an fehlende Umgebungs-/Device-Infos: 1
- Offline-Workflow nicht explizit erwähnt trotz spotty connectivity: 1
- Keine Nutzung von Kontext-Signalen (nur Asset-ID vorhanden): 1
- Keine Erwähnung von Offline-Workflow trotz minimalem Kontext: 1
- Keine Erwähnung lokaler Dokumentation/Synchronisation: 1
- Ticket-ID/Asset-ID explizit in Dokumentation: 1
- Zeitstempel für Maßnahmen: 1
- Keine Kontextnutzung (minimal context verfügbar): 1
- Keine Anpassung an Umgebung/Gerätezustand: 1
