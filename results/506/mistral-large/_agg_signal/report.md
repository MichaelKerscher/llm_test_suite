# Aggregation Report (506\mistral-large) [signal]
- judge_version filter: **judge_v1_1**
- Tests (latest runs): **90**
- Incidents with any deltas: **30**

## Mean scores by context level (snapshot)
### L0 (n=30)
- mean runtime: 6.4619333333333335
- mean R/H/S/D/K: 3.8666666666666667/3.9/4.0/4.2/2.7666666666666666
- mean overall (avg R/H/S/D/K): 3.746666666666667
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.00, hallucination_suspected=0.10
### L2 (n=30)
- mean runtime: 8.420166666666667
- mean R/H/S/D/K: 4.866666666666666/4.8/4.866666666666666/4.933333333333334/4.533333333333333
- mean overall (avg R/H/S/D/K): 4.8
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.17, hallucination_suspected=0.00
### L2B (n=30)
- mean runtime: 9.351666666666667
- mean R/H/S/D/K: 4.933333333333334/4.933333333333334/4.9/5.0/4.966666666666667
- mean overall (avg R/H/S/D/K): 4.946666666666667
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.63, hallucination_suspected=0.00

## Mean scores by strategy (snapshot)
### S0 (n=30)
- mean runtime: 6.4619333333333335
- mean R/H/S/D/K: 3.8666666666666667/3.9/4.0/4.2/2.7666666666666666
- mean overall (avg R/H/S/D/K): 3.746666666666667
### S1 (n=30)
- mean runtime: 8.420166666666667
- mean R/H/S/D/K: 4.866666666666666/4.8/4.866666666666666/4.933333333333334/4.533333333333333
- mean overall (avg R/H/S/D/K): 4.8
### S2 (n=30)
- mean runtime: 9.351666666666667
- mean R/H/S/D/K: 4.933333333333334/4.933333333333334/4.9/5.0/4.966666666666667
- mean overall (avg R/H/S/D/K): 4.946666666666667

## Top missing elements (max 20)
- Offline-Workflow (nicht erwartbar bei minimalem Context): 2
- Offline-Workflow explizit (device.connectivity=offline vorhanden, aber nicht als 'lokale Doku, später sync' formuliert): 2
- Kontextnutzung minimal (nur Asset-ID vorhanden): 2
- Umgebungsbedingungen (nicht im Context): 2
- Spezifische Kontextnutzung (kaum Kontext vorhanden): 1
- Offline-Workflow (nicht erwartbar, da CONTEXT kein connectivity-Signal enthält): 1
- Kontextnutzung minimal (nur Asset-ID vorhanden, keine Umwelt-/Severity-Daten): 1
- Offline-Workflow explizit (CONTEXT zeigt connectivity=offline, aber nicht als Workflow-Schritt genannt): 1
- Severity-Einschätzung fehlt (kein Kontext vorhanden): 1
- Keine Priorisierung bei Eskalation erkennbar: 1
- Keine Nutzung der Asset-ID im Kontext: 1
- Keine Erwähnung von Langzeitbeobachtung während Hauptverkehrszeit: 1
- Offline-Workflow (spotty connectivity): 1
- Offline-Workflow explizit (spotty connectivity): 1
- Keine Kontextnutzung (nur Asset-ID vorhanden): 1
- Offline-Workflow (spotty connectivity + low_battery): 1
- Kontextnutzung minimal (nur Asset-ID): 1
- Keine Anpassung an Umgebungsbedingungen: 1
- Offline-Workflow (nicht erwartbar bei L0_minimal): 1
- Keine Anpassung an Umweltbedingungen (Kontext minimal): 1
