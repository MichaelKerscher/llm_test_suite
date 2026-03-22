# Aggregation Report (506\mistral-large) [signal]
- judge_version filter: **judge_v1_1**
- Tests (latest runs): **90**
- Incidents with any deltas: **30**

## Mean scores by context level (snapshot)
### L0 (n=30)
- mean runtime: 6.0412
- mean R/H/S/D/K: 3.8/3.9/4.0/4.2/2.8
- mean overall (avg R/H/S/D/K): 3.74
- flags (rate): safety_first=0.97, escalation_present=1.00, offline_workflow_mentioned=0.00, hallucination_suspected=0.17
### L2 (n=30)
- mean runtime: 8.681199999999999
- mean R/H/S/D/K: 4.833333333333333/4.766666666666667/4.866666666666666/4.966666666666667/4.366666666666666
- mean overall (avg R/H/S/D/K): 4.760000000000001
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.10, hallucination_suspected=0.00
### L2B (n=30)
- mean runtime: 8.1175
- mean R/H/S/D/K: 4.866666666666666/4.766666666666667/4.866666666666666/4.933333333333334/5.0
- mean overall (avg R/H/S/D/K): 4.886666666666667
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.63, hallucination_suspected=0.00

## Mean scores by strategy (snapshot)
### S0 (n=30)
- mean runtime: 6.0412
- mean R/H/S/D/K: 3.8/3.9/4.0/4.2/2.8
- mean overall (avg R/H/S/D/K): 3.74
### S1 (n=30)
- mean runtime: 8.681199999999999
- mean R/H/S/D/K: 4.833333333333333/4.766666666666667/4.866666666666666/4.966666666666667/4.366666666666666
- mean overall (avg R/H/S/D/K): 4.760000000000001
### S2 (n=30)
- mean runtime: 8.1175
- mean R/H/S/D/K: 4.866666666666666/4.766666666666667/4.866666666666666/4.933333333333334/5.0
- mean overall (avg R/H/S/D/K): 4.886666666666667

## Top missing elements (max 20)
- Offline-Workflow (spotty connectivity): 2
- Kontextnutzung minimal (nur Asset-ID vorhanden): 2
- Offline-Workflow (lokale Doku, spätere Sync): 1
- Offline-Workflow (nicht erwartbar, da CONTEXT minimal): 1
- GPS-Koordinaten (nicht im CONTEXT vorhanden): 1
- Offline-Workflow explizit (device.connectivity=offline im CONTEXT, aber nicht erwähnt): 1
- Severity-Bewusstsein (high): 1
- Wetter-/Sichtbedingungen: 1
- Kreuzung als unbeschrankt behandeln: 1
- Safety-first nicht als Schritt 1: 1
- Keine Nutzung von Kontext-Signalen (rush_hour/high_traffic fehlen im CONTEXT): 1
- Kontextnutzung minimal (nur Asset-ID verfügbar): 1
- Keine Anpassung an fehlende Umgebungsdaten: 1
- Kontextnutzung minimal (nur Asset-ID): 1
- Keine Priorisierung nach Severity/Traffic: 1
- Generische Schritte ohne Fallbezug: 1
- Keine Nutzung der Asset-ID im Kontext: 1
- Spekuliert über Stromversorgung/Steuergerät ohne Kontext-Basis: 1
- Erwähnt 'Richtung backward' ohne Kontext-Hinweis darauf: 1
- Könnte GPS-Koordinaten expliziter in Dokumentation einbinden: 1
