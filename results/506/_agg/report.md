# Aggregation Report (506)
- judge_version filter: **judge_v1_1**
- Tests (latest runs): **90**
- Incidents with any deltas: **30**

## Mean scores by context level (snapshot)
### L0 (n=30)
- mean runtime: 4.1960999999999995
- mean R/H/S/D/K: 3.4/3.466666666666667/2.8666666666666667/3.566666666666667/2.566666666666667
- mean overall (avg R/H/S/D/K): 3.1733333333333333
- flags (rate): safety_first=0.93, escalation_present=1.00, offline_workflow_mentioned=0.00, hallucination_suspected=0.10
### L2 (n=30)
- mean runtime: 4.6555
- mean R/H/S/D/K: 4.4/4.233333333333333/4.1/4.333333333333333/3.5
- mean overall (avg R/H/S/D/K): 4.113333333333333
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.13, hallucination_suspected=0.20
### L2B (n=30)
- mean runtime: 5.1643
- mean R/H/S/D/K: 4.766666666666667/4.766666666666667/4.466666666666667/4.766666666666667/4.866666666666666
- mean overall (avg R/H/S/D/K): 4.7266666666666675
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.70, hallucination_suspected=0.07

## Mean scores by strategy (snapshot)
### S0 (n=30)
- mean runtime: 4.1960999999999995
- mean R/H/S/D/K: 3.4/3.466666666666667/2.8666666666666667/3.566666666666667/2.566666666666667
- mean overall (avg R/H/S/D/K): 3.1733333333333333
### S1 (n=30)
- mean runtime: 4.6555
- mean R/H/S/D/K: 4.4/4.233333333333333/4.1/4.333333333333333/3.5
- mean overall (avg R/H/S/D/K): 4.113333333333333
### S2 (n=30)
- mean runtime: 5.1643
- mean R/H/S/D/K: 4.766666666666667/4.766666666666667/4.466666666666667/4.766666666666667/4.866666666666666
- mean overall (avg R/H/S/D/K): 4.7266666666666675

## Top missing elements (max 20)
- Offline-Workflow bei spotty connectivity: 4
- Offline-Workflow (Kontext fehlt, daher nicht erwartbar): 2
- Keine Nutzung der Asset-ID im Kontext: 2
- Offline-Workflow (Kontext zeigt kein offline-Signal, daher nicht erwartbar): 1
- Konkrete Priorisierung bei low severity: 1
- Offline-Workflow explizit (connectivity=offline im Kontext): 1
- Klarstellung: device_state betrifft Techniker-Gerät, nicht Asset: 1
- Keine Nutzung des minimalen Kontexts (Asset-ID wird nur wiederholt): 1
- Keine spezifische Anpassung an intermittent fault_type: 1
- Generische Schritte ohne Priorisierung auf zeitweisen Ausfall: 1
- Keine explizite Erwähnung der Tageszeit (nachts) bei Absicherung: 1
- Foto-Workflow könnte klarer integriert sein: 1
- Extras.context_notes werden nicht explizit berücksichtigt (device.* vs Asset): 1
- Foto-Workflow könnte expliziter sein (photo_available=true): 1
- Keine Spekulation über Batteriezustand des Assets: 1
- Kontextnutzung minimal (nur Asset-ID vorhanden): 1
- Keine Anpassung an Umgebungsbedingungen (nicht erwartbar): 1
- Textfehler/Artefakte ('pipeline-nahem', 'excuse', 'procurement', 'IQ', 'ultimately'): 1
- Offline-Workflow nur angedeutet, nicht klar strukturiert: 1
- Nebel/Dämmerung-Sicherheit erwähnt, aber nicht priorisiert: 1
