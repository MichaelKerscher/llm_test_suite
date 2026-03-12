# Aggregation Report (506)
- judge_version filter: **judge_v1_1**
- Tests (latest runs): **90**
- Incidents with any deltas: **30**

## Mean scores by context level (snapshot)
### L0 (n=30)
- mean runtime: 3.9913000000000003
- mean R/H/S/D/K: 3.4/3.5/3.1666666666666665/3.7333333333333334/2.6666666666666665
- mean overall (avg R/H/S/D/K): 3.2933333333333334
- flags (rate): safety_first=0.97, escalation_present=1.00, offline_workflow_mentioned=0.00, hallucination_suspected=0.03
### L2 (n=30)
- mean runtime: 4.322100000000001
- mean R/H/S/D/K: 4.533333333333333/4.4/4.333333333333333/4.433333333333334/3.7
- mean overall (avg R/H/S/D/K): 4.28
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.23, hallucination_suspected=0.00
### L2B (n=30)
- mean runtime: 4.2818000000000005
- mean R/H/S/D/K: 4.9/4.833333333333333/4.5/4.833333333333333/4.933333333333334
- mean overall (avg R/H/S/D/K): 4.8
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.67, hallucination_suspected=0.00

## Mean scores by strategy (snapshot)
### S0 (n=30)
- mean runtime: 3.9913000000000003
- mean R/H/S/D/K: 3.4/3.5/3.1666666666666665/3.7333333333333334/2.6666666666666665
- mean overall (avg R/H/S/D/K): 3.2933333333333334
### S1 (n=30)
- mean runtime: 4.322100000000001
- mean R/H/S/D/K: 4.533333333333333/4.4/4.333333333333333/4.433333333333334/3.7
- mean overall (avg R/H/S/D/K): 4.28
### S2 (n=30)
- mean runtime: 4.2818000000000005
- mean R/H/S/D/K: 4.9/4.833333333333333/4.5/4.833333333333333/4.933333333333334
- mean overall (avg R/H/S/D/K): 4.8

## Top missing elements (max 20)
- Kontext-Nutzung minimal (nur Asset-ID): 3
- Generische Schritte ohne Priorisierung: 2
- Offline-Workflow nicht explizit (spotty connectivity): 2
- Keine Offline-Workflow-Erwähnung (aber nicht erwartbar bei minimalem Context): 2
- Offline-Workflow nicht erwähnt (spotty connectivity): 2
- Keine explizite Erwähnung von severity=medium als Priorisierungsfaktor: 2
- Keine Nutzung der Asset-ID im Kontext: 2
- Offline-Workflow (Gerät offline, lokal dokumentieren): 1
- Keine Nutzung der Kontextinformationen (nur Asset-ID vorhanden): 1
- Generische Antwort ohne Bezug zu 'intermittent fault': 1
- Keine Priorisierung auf zeitweisen Ausfall: 1
- Keine Anpassung an Tageszeit/Umgebung: 1
- Batterie-Hinweis könnte klarer sein (Gerät vs. Asset): 1
- Keine Nutzung der Asset-ID im Kontext (nur minimal vorhanden): 1
- Keine Erwähnung von Offline-Workflow (nicht erwartbar bei minimalem Kontext): 1
- Offline-Workflow explizit (spotty connectivity + low_battery): 1
- Keine spezifische Priorisierung bei 'Unsicherheit': 1
- Offline-Workflow fehlt komplett (connectivity=offline, device_state=low_battery): 1
- Keine Erwähnung lokaler Dokumentation/Foto-Speicherung: 1
- Schritt 'im System protokollieren' setzt Online-Zugriff voraus: 1
