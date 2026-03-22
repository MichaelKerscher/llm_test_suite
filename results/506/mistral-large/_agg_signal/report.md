# Aggregation Report (506\mistral-large) [signal]
- judge_version filter: **judge_v1_1**
- Tests (latest runs): **90**
- Incidents with any deltas: **30**

## Mean scores by context level (snapshot)
### L0 (n=30)
- mean runtime: 6.344966666666666
- mean R/H/S/D/K: 3.8333333333333335/3.9/3.966666666666667/4.3/2.7666666666666666
- mean overall (avg R/H/S/D/K): 3.753333333333333
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.00, hallucination_suspected=0.10
### L2 (n=30)
- mean runtime: 7.935033333333333
- mean R/H/S/D/K: 4.966666666666667/4.8/4.833333333333333/5.0/4.6
- mean overall (avg R/H/S/D/K): 4.84
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.23, hallucination_suspected=0.00
### L2B (n=30)
- mean runtime: 8.5548
- mean R/H/S/D/K: 4.933333333333334/4.866666666666666/4.866666666666666/4.933333333333334/4.933333333333334
- mean overall (avg R/H/S/D/K): 4.906666666666666
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.63, hallucination_suspected=0.00

## Mean scores by strategy (snapshot)
### S0 (n=30)
- mean runtime: 6.344966666666666
- mean R/H/S/D/K: 3.8333333333333335/3.9/3.966666666666667/4.3/2.7666666666666666
- mean overall (avg R/H/S/D/K): 3.753333333333333
### S1 (n=30)
- mean runtime: 7.935033333333333
- mean R/H/S/D/K: 4.966666666666667/4.8/4.833333333333333/5.0/4.6
- mean overall (avg R/H/S/D/K): 4.84
### S2 (n=30)
- mean runtime: 8.5548
- mean R/H/S/D/K: 4.933333333333334/4.866666666666666/4.866666666666666/4.933333333333334/4.933333333333334
- mean overall (avg R/H/S/D/K): 4.906666666666666

## Top missing elements (max 20)
- Kontextnutzung minimal (nur Asset-ID vorhanden): 2
- Offline-Workflow explizit erwähnen: 1
- Offline-Workflow bei spotty connectivity: 1
- Offline-Workflow explizit (spotty connectivity): 1
- Spekuliert über nicht vorhandene Kontextdaten (Steuergerät, Fehlercodes, Messgeräte): 1
- Könnte Guardrail-Hinweis expliziter umsetzen: 1
- Severity-Einschätzung fehlt (kein Signal im Kontext): 1
- Wetter/Sicht nicht erwähnt (kein Signal im Kontext): 1
- Offline-Workflow (spotty connectivity + low_battery): 1
- Keine Nutzung der Asset-ID im Kontext: 1
- Keine Priorisierung nach Severity: 1
- Keine Erwähnung von Connectivity/Device-State: 1
- Keine explizite Nutzung von _selection_meta (aber nicht zwingend erwartet): 1
- Keine Anpassung an Umgebungsbedingungen (Kontext minimal): 1
- Keine Kontextnutzung (nur Asset-ID vorhanden): 1
- Keine Erwähnung von Foto-Dokumentation trotz photo_available: 1
- Keine Erwähnung des Offline-Workflows trotz low_battery: 1
- Severity-angepasste Priorisierung: 1
- Umgebungsbedingungen (Wetter/Sicht): 1
- Foto-Verweis: 1
