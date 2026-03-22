# Aggregation Report (506\mistral-large) [signal]
- judge_version filter: **judge_v1_1**
- Tests (latest runs): **90**
- Incidents with any deltas: **30**

## Mean scores by context level (snapshot)
### L0 (n=30)
- mean runtime: 6.326766666666667
- mean R/H/S/D/K: 3.8666666666666667/3.933333333333333/4.066666666666666/4.133333333333334/2.7333333333333334
- mean overall (avg R/H/S/D/K): 3.746666666666667
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.00, hallucination_suspected=0.07
### L2 (n=30)
- mean runtime: 9.402633333333334
- mean R/H/S/D/K: 4.966666666666667/4.833333333333333/4.866666666666666/5.0/4.5
- mean overall (avg R/H/S/D/K): 4.833333333333333
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.10, hallucination_suspected=0.00
### L2B (n=30)
- mean runtime: 8.531
- mean R/H/S/D/K: 4.966666666666667/4.9/4.9/4.966666666666667/4.966666666666667
- mean overall (avg R/H/S/D/K): 4.9399999999999995
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.63, hallucination_suspected=0.00

## Mean scores by strategy (snapshot)
### S0 (n=30)
- mean runtime: 6.326766666666667
- mean R/H/S/D/K: 3.8666666666666667/3.933333333333333/4.066666666666666/4.133333333333334/2.7333333333333334
- mean overall (avg R/H/S/D/K): 3.746666666666667
### S1 (n=30)
- mean runtime: 9.402633333333334
- mean R/H/S/D/K: 4.966666666666667/4.833333333333333/4.866666666666666/5.0/4.5
- mean overall (avg R/H/S/D/K): 4.833333333333333
### S2 (n=30)
- mean runtime: 8.531
- mean R/H/S/D/K: 4.966666666666667/4.9/4.9/4.966666666666667/4.966666666666667
- mean overall (avg R/H/S/D/K): 4.9399999999999995

## Top missing elements (max 20)
- Offline-Workflow bei spotty connectivity nicht explizit erwähnt: 4
- Kontextnutzung minimal (nur Asset-ID vorhanden): 2
- Offline-Workflow (nicht erwartbar, da kein Signal im Kontext): 1
- Expliziter Offline-Workflow (device.connectivity=offline vorhanden, aber nicht als 'lokale Speicherung/spätere Sync' formuliert): 1
- Offline-Workflow explizit (lokale Doku, spätere Sync): 1
- Severity-Bewusstsein (high severity nicht erkennbar aus minimalem Context): 1
- Umgebungsbedingungen (Wetter/Sicht nicht im Context): 1
- Kreuzung als ungeregelt behandeln (nicht explizit): 1
- Explizite Erwähnung 'Kreuzung wie unbeschrankt behandeln' (implizit vorhanden, aber nicht wörtlich): 1
- Keine GPS-Koordinaten genutzt (waren im Context): 1
- Keine Erwähnung der Hauptverkehrszeit-Spezifik in Diagnose: 1
- Offline-Workflow (nicht erwartbar bei minimalem Context): 1
- Spezifische Umgebungsbedingungen (nicht im Context): 1
- Offline-Workflow explizit (spotty connectivity vorhanden): 1
- Offline-Workflow (spotty connectivity + low_power_mode) nicht explizit adressiert: 1
- Keine Nutzung der Asset-ID im Kontext: 1
- Spekuliert über Unfallstelle ohne Hinweis darauf: 1
- Erwähnt Polizei/Behörden ohne Signal dafür: 1
- Offline-Workflow (spotty connectivity): 1
- Offline-Workflow (nicht erwartbar aus minimalem Kontext): 1
