# Aggregation Report (506\mistral-large) [signal]
- judge_version filter: **judge_v1_1**
- Tests (latest runs): **90**
- Incidents with any deltas: **30**

## Mean scores by context level (snapshot)
### L0 (n=30)
- mean runtime: 6.309933333333333
- mean R/H/S/D/K: 3.9/3.966666666666667/3.966666666666667/4.166666666666667/2.9
- mean overall (avg R/H/S/D/K): 3.7800000000000002
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.00, hallucination_suspected=0.10
### L2 (n=30)
- mean runtime: 8.665566666666667
- mean R/H/S/D/K: 4.933333333333334/4.833333333333333/4.866666666666666/4.966666666666667/4.533333333333333
- mean overall (avg R/H/S/D/K): 4.826666666666667
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.20, hallucination_suspected=0.00
### L2B (n=30)
- mean runtime: 8.3345
- mean R/H/S/D/K: 4.966666666666667/4.9/4.933333333333334/4.866666666666666/5.0
- mean overall (avg R/H/S/D/K): 4.933333333333334
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.60, hallucination_suspected=0.00

## Mean scores by strategy (snapshot)
### S0 (n=30)
- mean runtime: 6.309933333333333
- mean R/H/S/D/K: 3.9/3.966666666666667/3.966666666666667/4.166666666666667/2.9
- mean overall (avg R/H/S/D/K): 3.7800000000000002
### S1 (n=30)
- mean runtime: 8.665566666666667
- mean R/H/S/D/K: 4.933333333333334/4.833333333333333/4.866666666666666/4.966666666666667/4.533333333333333
- mean overall (avg R/H/S/D/K): 4.826666666666667
### S2 (n=30)
- mean runtime: 8.3345
- mean R/H/S/D/K: 4.966666666666667/4.9/4.933333333333334/4.866666666666666/5.0
- mean overall (avg R/H/S/D/K): 4.933333333333334

## Top missing elements (max 20)
- Severity-basierte Priorisierung: 2
- Offline-Workflow (device.connectivity=offline, device_state=low_battery nicht adressiert): 1
- Offline-Workflow explizit (Kontext zeigt offline): 1
- GPS-Koordinaten (nicht im Context verfügbar): 1
- Spezifische Eskalationskriterien für severity=high: 1
- Kontextnutzung minimal (nur Asset-ID): 1
- Halluzinationen: Ampel/Straßenlampe nicht im Context: 1
- Keine Anpassung an Umgebung/Wetter/Konnektivität: 1
- Kreuzung als unbeschrankt behandeln (signal_dark-spezifisch): 1
- Kreuzung als unbeschrankt behandeln (explizit): 1
- Keine Nutzung der GPS-Koordinaten (nicht im Context vorhanden): 1
- Keine Erwähnung von Foto-Dokumentation (nicht im Context signalisiert): 1
- Keine explizite Erwähnung der device_state-Diskrepanz (ok vs. Fehlfunktion): 1
- Keine Erwähnung freiliegender Kabel (nicht im CONTEXT): 1
- Keine Priorisierung nach Severity (nicht im CONTEXT): 1
- Offline-Workflow explizit (lokale Speicherung, spätere Sync): 1
- Keine Nutzung von Umweltkontext (Wetter/Sicht/Traffic nicht erwähnt, da nicht im CONTEXT): 1
- Intermittierender Fehler nicht explizit adressiert: 1
- Längere Beobachtungszeit nicht erwähnt: 1
- Keine Erwähnung von Wetter/Sicht (nicht im Kontext): 1
