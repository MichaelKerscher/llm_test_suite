# Aggregation Report (506\mistral-large) [signal]
- judge_version filter: **judge_v1_1**
- Tests (latest runs): **90**
- Incidents with any deltas: **30**

## Mean scores by context level (snapshot)
### L0 (n=30)
- mean runtime: 6.169366666666666
- mean R/H/S/D/K: 3.7666666666666666/3.8666666666666667/4.166666666666667/4.1/2.8
- mean overall (avg R/H/S/D/K): 3.74
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.00, hallucination_suspected=0.03
### L2 (n=30)
- mean runtime: 8.329633333333334
- mean R/H/S/D/K: 4.833333333333333/4.733333333333333/4.766666666666667/4.9/4.433333333333334
- mean overall (avg R/H/S/D/K): 4.733333333333333
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.17, hallucination_suspected=0.03
### L2B (n=30)
- mean runtime: 8.270999999999999
- mean R/H/S/D/K: 4.933333333333334/4.9/4.8/4.933333333333334/4.966666666666667
- mean overall (avg R/H/S/D/K): 4.906666666666666
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.53, hallucination_suspected=0.00

## Mean scores by strategy (snapshot)
### S0 (n=30)
- mean runtime: 6.169366666666666
- mean R/H/S/D/K: 3.7666666666666666/3.8666666666666667/4.166666666666667/4.1/2.8
- mean overall (avg R/H/S/D/K): 3.74
### S1 (n=30)
- mean runtime: 8.329633333333334
- mean R/H/S/D/K: 4.833333333333333/4.733333333333333/4.766666666666667/4.9/4.433333333333334
- mean overall (avg R/H/S/D/K): 4.733333333333333
### S2 (n=30)
- mean runtime: 8.270999999999999
- mean R/H/S/D/K: 4.933333333333334/4.9/4.8/4.933333333333334/4.966666666666667
- mean overall (avg R/H/S/D/K): 4.906666666666666

## Top missing elements (max 20)
- Keine Priorisierung bei intermittent fault: 2
- Offline-Workflow (nicht erwartbar bei minimalem Context): 2
- Offline-Workflow bei spotty connectivity: 2
- Offline-Workflow explizit (Gerät offline/low_battery): 1
- Offline-Workflow nicht explizit erwähnt trotz connectivity=offline: 1
- Severity-Einschätzung fehlt (kein CONTEXT dazu): 1
- Umgebungsbedingungen nicht erwähnt (kein CONTEXT dazu): 1
- Offline-Workflow (spotty connectivity): 1
- Severity-Einschätzung fehlt (nicht im Context): 1
- Wetter/Sicht nicht erwähnt (nicht im Context): 1
- Offline-Workflow (nicht erwartbar bei L0_minimal): 1
- Keine Nutzung der Kontextinformationen (nur Asset-ID vorhanden): 1
- Keine Anpassung an Umgebungsbedingungen (nicht erwartbar bei L0): 1
- Kontextnutzung minimal (nur Asset-ID): 1
- Generische Schritte ohne Fallbezug: 1
- Keine Anpassung an Umgebungsbedingungen (Kontext minimal): 1
- Keine Erwähnung der Richtung 'backward': 1
- Keine Priorisierung bei hoher Severity: 1
- Severity-angepasste Priorisierung fehlt (high severity nicht erkennbar): 1
- Keine Erwähnung von Wetter/Sicht-Bedingungen (im Kontext nicht vorhanden): 1
