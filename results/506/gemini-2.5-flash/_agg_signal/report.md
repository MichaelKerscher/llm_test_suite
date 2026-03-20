# Aggregation Report (506\gemini-2.5-flash) [signal]
- judge_version filter: **judge_v1_1**
- Tests (latest runs): **90**
- Incidents with any deltas: **30**

## Mean scores by context level (snapshot)
### L0 (n=30)
- mean runtime: 5.9814
- mean R/H/S/D/K: 3.8666666666666667/3.966666666666667/3.933333333333333/4.2/2.8666666666666667
- mean overall (avg R/H/S/D/K): 3.7666666666666666
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.00, hallucination_suspected=0.03
### L2 (n=30)
- mean runtime: 8.954466666666667
- mean R/H/S/D/K: 4.866666666666666/4.8/4.866666666666666/4.933333333333334/4.333333333333333
- mean overall (avg R/H/S/D/K): 4.760000000000001
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.17, hallucination_suspected=0.00
### L2B (n=30)
- mean runtime: 8.739666666666666
- mean R/H/S/D/K: 4.933333333333334/4.966666666666667/4.9/4.9/4.9
- mean overall (avg R/H/S/D/K): 4.92
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.63, hallucination_suspected=0.03

## Mean scores by strategy (snapshot)
### S0 (n=30)
- mean runtime: 5.9814
- mean R/H/S/D/K: 3.8666666666666667/3.966666666666667/3.933333333333333/4.2/2.8666666666666667
- mean overall (avg R/H/S/D/K): 3.7666666666666666
### S1 (n=30)
- mean runtime: 8.954466666666667
- mean R/H/S/D/K: 4.866666666666666/4.8/4.866666666666666/4.933333333333334/4.333333333333333
- mean overall (avg R/H/S/D/K): 4.760000000000001
### S2 (n=30)
- mean runtime: 8.739666666666666
- mean R/H/S/D/K: 4.933333333333334/4.966666666666667/4.9/4.9/4.9
- mean overall (avg R/H/S/D/K): 4.92

## Top missing elements (max 20)
- Kontextnutzung minimal (nur Asset-ID): 2
- Offline-Workflow (spotty connectivity): 2
- Offline-Workflow bei spotty connectivity nicht explizit erwähnt: 2
- Offline-Workflow (nicht erwartbar, da CONTEXT kein connectivity-Signal enthält): 1
- Expliziter Offline-Workflow (offline/low_battery im CONTEXT, aber nicht als Workflow-Anpassung formuliert): 1
- Offline-Workflow (device.connectivity=offline nicht adressiert): 1
- Explizite Erwähnung severity=high: 1
- Polizei-Anforderung bei Hauptverkehrszeit: 1
- Severity-Bewusstsein (high) nicht erkennbar: 1
- Keine Priorisierung bei Eskalation sichtbar: 1
- Keine Priorisierung nach Hauptverkehrszeit/hohem Verkehr: 1
- Keine Erwähnung intermittierender Fehler: 1
- Keine Anpassung an Umgebungsbedingungen: 1
- Keine Rückfrage zu fehlenden Infos: 1
- Spotty connectivity könnte expliziter im Workflow stehen: 1
- Keine Nutzung der Asset-ID im Kontext (nur minimal vorhanden): 1
- Keine Erwähnung von Foto-Verfügbarkeit: 1
- Keine Nutzung von Kontext-Signalen (nur Asset-ID vorhanden): 1
- Keine Priorisierung nach Severity (nicht im Context): 1
- Keine Kontextnutzung (minimaler Context): 1
