# Aggregation Report (506\gemini-2.5-flash) [signal]
- judge_version filter: **judge_v1_1**
- Tests (latest runs): **90**
- Incidents with any deltas: **30**

## Mean scores by context level (snapshot)
### L0 (n=30)
- mean runtime: 6.249233333333334
- mean R/H/S/D/K: 3.8333333333333335/4.0/3.933333333333333/4.066666666666666/2.6333333333333333
- mean overall (avg R/H/S/D/K): 3.6933333333333334
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.00, hallucination_suspected=0.17
### L2 (n=30)
- mean runtime: 8.836266666666667
- mean R/H/S/D/K: 4.966666666666667/4.933333333333334/4.933333333333334/5.0/4.633333333333334
- mean overall (avg R/H/S/D/K): 4.8933333333333335
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.23, hallucination_suspected=0.03
### L2B (n=30)
- mean runtime: 9.127233333333333
- mean R/H/S/D/K: 4.9/4.933333333333334/4.933333333333334/4.966666666666667/4.966666666666667
- mean overall (avg R/H/S/D/K): 4.9399999999999995
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.63, hallucination_suspected=0.00

## Mean scores by strategy (snapshot)
### S0 (n=30)
- mean runtime: 6.249233333333334
- mean R/H/S/D/K: 3.8333333333333335/4.0/3.933333333333333/4.066666666666666/2.6333333333333333
- mean overall (avg R/H/S/D/K): 3.6933333333333334
### S1 (n=30)
- mean runtime: 8.836266666666667
- mean R/H/S/D/K: 4.966666666666667/4.933333333333334/4.933333333333334/5.0/4.633333333333334
- mean overall (avg R/H/S/D/K): 4.8933333333333335
### S2 (n=30)
- mean runtime: 9.127233333333333
- mean R/H/S/D/K: 4.9/4.933333333333334/4.933333333333334/4.966666666666667/4.966666666666667
- mean overall (avg R/H/S/D/K): 4.9399999999999995

## Top missing elements (max 20)
- Kontextnutzung minimal (nur Asset-ID): 4
- Offline-Workflow (spotty connectivity): 2
- Offline-Workflow (nicht erwartbar, da kein Signal im Context): 1
- Wetter-/Sichtbedingungen (nicht im Context vorhanden): 1
- Spekuliert über Stromausfall ohne Kontext-Signal: 1
- RSA-Details nicht erwartbar aus minimalem Kontext: 1
- Keine Nutzung der Asset-ID im Kontext (nur minimal vorhanden): 1
- Keine Erwähnung des intermittierenden Charakters: 1
- Spekuliert über Ampel/Straßenlampe ohne Basis: 1
- Keine Anpassung an fehlende Umgebungsdaten: 1
- Lokale Speicherung/Synchronisation: 1
- Konkrete Nutzung der Asset-ID im Workflow: 1
- Spezifische Fehlerdiagnose bei signal_dark: 1
- Keine Nutzung der GPS-Koordinaten (nicht im Context): 1
- Keine Erwähnung von Umgebungsbedingungen (nicht im Context): 1
- Keine Berücksichtigung von Umweltbedingungen (nicht im Context): 1
- Keine Priorisierung nach Severity (nicht im Context): 1
- Offline-Workflow (nicht erwartbar bei L0): 1
- GPS-Koordinaten (nicht im Context): 1
- Keine Berücksichtigung von Umgebungsbedingungen: 1
