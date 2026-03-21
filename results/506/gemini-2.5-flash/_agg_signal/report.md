# Aggregation Report (506\gemini-2.5-flash) [signal]
- judge_version filter: **judge_v1_1**
- Tests (latest runs): **90**
- Incidents with any deltas: **30**

## Mean scores by context level (snapshot)
### L0 (n=30)
- mean runtime: 5.961200000000001
- mean R/H/S/D/K: 3.9/3.933333333333333/4.266666666666667/4.1/2.7
- mean overall (avg R/H/S/D/K): 3.7800000000000002
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.00, hallucination_suspected=0.10
### L2 (n=30)
- mean runtime: 8.619499999999999
- mean R/H/S/D/K: 4.966666666666667/4.866666666666666/4.966666666666667/4.933333333333334/4.5
- mean overall (avg R/H/S/D/K): 4.846666666666667
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.03, hallucination_suspected=0.00
### L2B (n=30)
- mean runtime: 8.212366666666666
- mean R/H/S/D/K: 4.966666666666667/4.933333333333334/4.966666666666667/4.9/5.0
- mean overall (avg R/H/S/D/K): 4.953333333333333
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.57, hallucination_suspected=0.00

## Mean scores by strategy (snapshot)
### S0 (n=30)
- mean runtime: 5.961200000000001
- mean R/H/S/D/K: 3.9/3.933333333333333/4.266666666666667/4.1/2.7
- mean overall (avg R/H/S/D/K): 3.7800000000000002
### S1 (n=30)
- mean runtime: 8.619499999999999
- mean R/H/S/D/K: 4.966666666666667/4.866666666666666/4.966666666666667/4.933333333333334/4.5
- mean overall (avg R/H/S/D/K): 4.846666666666667
### S2 (n=30)
- mean runtime: 8.212366666666666
- mean R/H/S/D/K: 4.966666666666667/4.933333333333334/4.966666666666667/4.9/5.0
- mean overall (avg R/H/S/D/K): 4.953333333333333

## Top missing elements (max 20)
- Offline-Workflow (spotty connectivity): 2
- Kontextnutzung minimal (nur Asset-ID vorhanden): 2
- Offline-Workflow bei spotty connectivity: 2
- Offline-Workflow explizit erwähnen: 1
- Keine GPS-Koordinaten dokumentiert (nicht im Context verfügbar): 1
- Foto-Status nicht erwähnt (nicht im Context verfügbar): 1
- Severity-Bewusstsein (high) nicht explizit: 1
- Kreuzung wie unbeschrankt behandeln fehlt: 1
- Keine Nutzung der Asset-ID im Kontext (nur minimal vorhanden): 1
- Keine Erwähnung von Hauptverkehrszeit-spezifischen Maßnahmen: 1
- Kontextnutzung minimal (nur Asset-ID): 1
- Keine Anpassung an sporadisches Fehlerbild: 1
- Generische Schritte ohne Priorisierung: 1
- Keine Nutzung der GPS-Koordinaten aus CONTEXT: 1
- Keine Erwähnung des photo_available-Flags: 1
- Offline-Workflow nicht explizit erwähnt trotz spotty connectivity: 1
- Offline-Workflow (nicht erwartbar bei L0_minimal): 1
- Offline-Workflow fehlt (device.connectivity=offline → lokale Dokumentation, spätere Sync): 1
- Keine Nutzung des verfügbaren Kontexts (Asset-ID): 1
- Spekulative Details ohne Kontextbasis (z.B. Dämmerungsschalter, Bewegungsmelder, Batteriepuffer): 1
