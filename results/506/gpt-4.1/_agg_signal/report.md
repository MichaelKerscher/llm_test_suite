# Aggregation Report (506\gpt-4.1) [signal]
- judge_version filter: **judge_v1_1**
- Tests (latest runs): **90**
- Incidents with any deltas: **30**

## Mean scores by context level (snapshot)
### L0 (n=30)
- mean runtime: 7.482
- mean R/H/S/D/K: 3.8333333333333335/3.9/3.933333333333333/4.2/2.6333333333333333
- mean overall (avg R/H/S/D/K): 3.7
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.00, hallucination_suspected=0.13
### L2 (n=30)
- mean runtime: 8.631333333333334
- mean R/H/S/D/K: 4.833333333333333/4.766666666666667/4.766666666666667/4.9/4.4
- mean overall (avg R/H/S/D/K): 4.733333333333333
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.07, hallucination_suspected=0.00
### L2B (n=30)
- mean runtime: 9.334333333333332
- mean R/H/S/D/K: 4.933333333333334/4.933333333333334/4.9/4.933333333333334/4.966666666666667
- mean overall (avg R/H/S/D/K): 4.933333333333334
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.63, hallucination_suspected=0.00

## Mean scores by strategy (snapshot)
### S0 (n=30)
- mean runtime: 7.482
- mean R/H/S/D/K: 3.8333333333333335/3.9/3.933333333333333/4.2/2.6333333333333333
- mean overall (avg R/H/S/D/K): 3.7
### S1 (n=30)
- mean runtime: 8.631333333333334
- mean R/H/S/D/K: 4.833333333333333/4.766666666666667/4.766666666666667/4.9/4.4
- mean overall (avg R/H/S/D/K): 4.733333333333333
### S2 (n=30)
- mean runtime: 9.334333333333332
- mean R/H/S/D/K: 4.933333333333334/4.933333333333334/4.9/4.933333333333334/4.966666666666667
- mean overall (avg R/H/S/D/K): 4.933333333333334

## Top missing elements (max 20)
- Kontextnutzung minimal (nur Asset-ID): 3
- Offline-Workflow bei spotty connectivity nicht explizit erwähnt: 2
- Offline-Workflow (nicht erwartbar, da CONTEXT minimal): 1
- Konkrete Eskalations-Trigger: 1
- Offline-Workflow explizit (device.connectivity=offline vorhanden, aber nicht als 'lokale Doku, später sync' formuliert): 1
- Offline-Workflow nicht explizit erwähnt trotz connectivity=offline: 1
- Keine Nutzung der verfügbaren Kontextinformationen (nur Asset-ID vorhanden): 1
- Keine Rückfrage nach fehlenden kritischen Infos (GPS, Severity, Photo): 1
- Dokumentation könnte GPS-Koordinaten expliziter in Checkliste nennen: 1
- Severity-Einschätzung fehlt (nur minimal context): 1
- Keine Erwähnung von Kreuzungsregelung bei Dunkelampel: 1
- Intermittierender Fehler nicht explizit adressiert: 1
- Keine Erwähnung der Beobachtung während Hauptverkehrszeit als Trigger: 1
- Keine Anpassung an fehlende Umgebungsdaten: 1
- Offline-Workflow nicht explizit (spotty connectivity): 1
- Offline-Workflow explizit (spotty connectivity): 1
- Offline-Workflow (spotty connectivity + low_battery): 1
- Severity/Umgebung nicht erkennbar genutzt: 1
- Spekulation über Fundament/Korrosion ohne Kontext: 1
- Offline-Workflow (nicht erwartbar bei L0_minimal): 1
