# Aggregation Report (506/mistral-large)
- judge_version filter: **judge_v1_1**
- Tests (latest runs): **90**
- Incidents with any deltas: **30**

## Mean scores by context level (snapshot)
### L0 (n=30)
- mean runtime: 5.4668
- mean R/H/S/D/K: 3.566666666666667/3.8666666666666667/3.8666666666666667/4.1/2.8666666666666667
- mean overall (avg R/H/S/D/K): 3.6533333333333333
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.00, hallucination_suspected=0.03
### L2 (n=30)
- mean runtime: 7.7861
- mean R/H/S/D/K: 4.733333333333333/4.666666666666667/4.666666666666667/4.833333333333333/3.7333333333333334
- mean overall (avg R/H/S/D/K): 4.526666666666667
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.07, hallucination_suspected=0.17
### L2B (n=30)
- mean runtime: 8.664866666666667
- mean R/H/S/D/K: 4.9/4.866666666666666/4.8/4.966666666666667/5.0
- mean overall (avg R/H/S/D/K): 4.906666666666666
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.60, hallucination_suspected=0.00

## Mean scores by strategy (snapshot)
### S0 (n=30)
- mean runtime: 5.4668
- mean R/H/S/D/K: 3.566666666666667/3.8666666666666667/3.8666666666666667/4.1/2.8666666666666667
- mean overall (avg R/H/S/D/K): 3.6533333333333333
### S1 (n=30)
- mean runtime: 7.7861
- mean R/H/S/D/K: 4.733333333333333/4.666666666666667/4.666666666666667/4.833333333333333/3.7333333333333334
- mean overall (avg R/H/S/D/K): 4.526666666666667
### S2 (n=30)
- mean runtime: 8.664866666666667
- mean R/H/S/D/K: 4.9/4.866666666666666/4.8/4.966666666666667/5.0
- mean overall (avg R/H/S/D/K): 4.906666666666666

## Top missing elements (max 20)
- Offline-Workflow bei spotty connectivity: 6
- Offline-Workflow (spotty connectivity): 2
- Kontextnutzung minimal (nur Asset-ID): 2
- Keine Nutzung der Asset-ID im Text: 1
- Keine spezifischen Hinweise zu intermittierenden Fehlern: 1
- Keine Spekulation über Batterie/Solarpanel ohne Kontext-Basis: 1
- Klarstellung device_state bezieht sich auf Techniker-Gerät: 1
- Offline-Workflow (device.connectivity=offline): 1
- Lokale Dokumentation/Foto-Speicherung erwähnen: 1
- Offline-Workflow (nicht erwartbar bei L0): 1
- Konkrete Kontextnutzung (nur Asset-ID vorhanden): 1
- Offline-Workflow explizit (connectivity=offline im Context): 1
- Offline-Workflow (lokal dokumentieren/Foto lokal speichern): 1
- Keine Online-Schritte bei connectivity=offline: 1
- Keine Berücksichtigung sporadischer Fehler-Spezifika (Beobachtungszeitraum, Reproduktion): 1
- Keine Priorisierung bei unklarem Fehlerbild: 1
- Offline-Workflow bei spotty connectivity nicht erwähnt: 1
- Missverständnis: device_state/connectivity als Asset-Problem interpretiert: 1
- Keine Nutzung der Umgebungsinformationen (Nebel, Nacht, Sicht): 1
- Keine Erwähnung der Severity-Einordnung: 1
