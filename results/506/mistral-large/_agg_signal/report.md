# Aggregation Report (506\mistral-large) [signal]
- judge_version filter: **judge_v1_1**
- Tests (latest runs): **90**
- Incidents with any deltas: **30**

## Mean scores by context level (snapshot)
### L0 (n=30)
- mean runtime: 6.0534
- mean R/H/S/D/K: 3.8666666666666667/3.933333333333333/4.1/4.166666666666667/2.7
- mean overall (avg R/H/S/D/K): 3.753333333333333
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.00, hallucination_suspected=0.07
### L2 (n=30)
- mean runtime: 9.078766666666667
- mean R/H/S/D/K: 4.933333333333334/4.833333333333333/4.866666666666666/4.966666666666667/4.6
- mean overall (avg R/H/S/D/K): 4.84
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.20, hallucination_suspected=0.00
### L2B (n=30)
- mean runtime: 8.367233333333333
- mean R/H/S/D/K: 4.933333333333334/5.0/4.966666666666667/4.9/4.966666666666667
- mean overall (avg R/H/S/D/K): 4.953333333333333
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.57, hallucination_suspected=0.00

## Mean scores by strategy (snapshot)
### S0 (n=30)
- mean runtime: 6.0534
- mean R/H/S/D/K: 3.8666666666666667/3.933333333333333/4.1/4.166666666666667/2.7
- mean overall (avg R/H/S/D/K): 3.753333333333333
### S1 (n=30)
- mean runtime: 9.078766666666667
- mean R/H/S/D/K: 4.933333333333334/4.833333333333333/4.866666666666666/4.966666666666667/4.6
- mean overall (avg R/H/S/D/K): 4.84
### S2 (n=30)
- mean runtime: 8.367233333333333
- mean R/H/S/D/K: 4.933333333333334/5.0/4.966666666666667/4.9/4.966666666666667
- mean overall (avg R/H/S/D/K): 4.953333333333333

## Top missing elements (max 20)
- Offline-Workflow (nicht erwartbar, da CONTEXT minimal): 2
- Offline-Workflow bei spotty connectivity: 2
- Offline-Workflow (lokale Dokumentation, spätere Sync): 1
- Keine GPS-Koordinaten dokumentiert (nicht im Context verfügbar): 1
- Keine Nutzung von photo_available (nicht im Context): 1
- Severity-Bewusstsein (high nicht erkennbar): 1
- Kreuzung wie unbeschrankt behandeln: 1
- GPS-Koordinaten explizit dokumentieren: 1
- Keine Priorisierung nach severity/traffic: 1
- Keine Nutzung von Kontext-Signalen (rush_hour, high_traffic nicht erkennbar): 1
- Offline-Workflow nicht erwähnt (kein Signal im Kontext): 1
- Umgebungsfaktoren (Wetter/Sicht) nicht genutzt (nicht im Kontext): 1
- Beobachtungsmuster für sporadische Störung gut, aber Priorisierung schwach: 1
- Offline-Workflow nicht explizit genannt (spotty connectivity vorhanden): 1
- Beobachtungsmuster gut, aber keine klare Stop-Condition für Eskalation: 1
- Kontextnutzung (Umwelt/Gerät fehlt komplett): 1
- Keine Nutzung des minimalen Kontexts (nur OSM-ID vorhanden): 1
- Spekuliert über Schaltkasten/Sicherungen ohne Kontext-Basis: 1
- Erwähnt 'Polizei' ohne dass severity/traffic dies im Kontext nahelegen: 1
- Severity-Einschätzung fehlt (high nicht erkennbar aus Kontext): 1
