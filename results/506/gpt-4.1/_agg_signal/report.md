# Aggregation Report (506\gpt-4.1) [signal]
- judge_version filter: **judge_v1_1**
- Tests (latest runs): **90**
- Incidents with any deltas: **30**

## Mean scores by context level (snapshot)
### L0 (n=30)
- mean runtime: 7.0107
- mean R/H/S/D/K: 3.7666666666666666/3.966666666666667/3.933333333333333/4.1/2.6666666666666665
- mean overall (avg R/H/S/D/K): 3.6866666666666665
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.00, hallucination_suspected=0.07
### L2 (n=30)
- mean runtime: 9.077466666666668
- mean R/H/S/D/K: 4.9/4.666666666666667/4.866666666666666/4.966666666666667/4.366666666666666
- mean overall (avg R/H/S/D/K): 4.753333333333333
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.10, hallucination_suspected=0.03
### L2B (n=30)
- mean runtime: 9.264299999999999
- mean R/H/S/D/K: 4.933333333333334/4.866666666666666/4.9/4.933333333333334/4.933333333333334
- mean overall (avg R/H/S/D/K): 4.913333333333333
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.60, hallucination_suspected=0.00

## Mean scores by strategy (snapshot)
### S0 (n=30)
- mean runtime: 7.0107
- mean R/H/S/D/K: 3.7666666666666666/3.966666666666667/3.933333333333333/4.1/2.6666666666666665
- mean overall (avg R/H/S/D/K): 3.6866666666666665
### S1 (n=30)
- mean runtime: 9.077466666666668
- mean R/H/S/D/K: 4.9/4.666666666666667/4.866666666666666/4.966666666666667/4.366666666666666
- mean overall (avg R/H/S/D/K): 4.753333333333333
### S2 (n=30)
- mean runtime: 9.264299999999999
- mean R/H/S/D/K: 4.933333333333334/4.866666666666666/4.9/4.933333333333334/4.933333333333334
- mean overall (avg R/H/S/D/K): 4.913333333333333

## Top missing elements (max 20)
- Kontextnutzung minimal (nur Asset-ID vorhanden): 3
- Kontextnutzung minimal (nur Asset-ID): 2
- Offline-Workflow bei spotty connectivity: 2
- Offline-Workflow explizit (lokale Doku, spätere Sync): 1
- Offline-Workflow (connectivity=offline im CONTEXT, aber nicht erwähnt): 1
- Severity-Bewusstsein (high nicht erkennbar): 1
- Kreuzung als unbeschrankt behandeln: 1
- Keine Anpassung an Umgebungsbedingungen: 1
- Offline-Workflow explizit erwähnen: 1
- Severity-Bewusstsein (high) fehlt im Kontext: 1
- Wetter/Sicht-Anpassung nicht möglich (kein Kontext): 1
- Offline-Workflow (spotty connectivity + low_battery): 1
- Offline-Workflow (nicht erwartbar bei L0_minimal): 1
- Keine Erwähnung der intermittierenden Natur des Fehlers: 1
- Keine spezifische Beobachtungsdauer empfohlen: 1
- Severity-Einschätzung fehlt (high nicht erkennbar aus minimalem Kontext): 1
- Umgebungsbedingungen nicht berücksichtigt (nicht im Kontext vorhanden): 1
- Keine Erwähnung von Foto-Verfügbarkeit: 1
- Keine Nutzung der Kontextinformationen (severity, photo_description, environment): 1
- Keine Erwähnung von Offline-Workflow trotz spotty connectivity: 1
