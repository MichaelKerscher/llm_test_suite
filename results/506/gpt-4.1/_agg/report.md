# Aggregation Report (506)
- judge_version filter: **judge_v1_1**
- Tests (latest runs): **90**
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
- Keine Kontextnutzung (minimal context verfügbar): 1
- Keine Anpassung an Umgebung/Gerätezustand: 1
- Kein expliziter Offline-Workflow trotz spotty connectivity: 1
- Batterie-Warnung fehlt (low_battery): 1
