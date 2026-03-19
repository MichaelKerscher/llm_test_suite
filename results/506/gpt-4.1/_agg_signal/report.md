# Aggregation Report (506\gpt-4.1) [signal]
- judge_version filter: **judge_v1_1**
- Tests (latest runs): **90**
- Incidents with any deltas: **30**

## Mean scores by context level (snapshot)
### L0 (n=30)
- mean runtime: 6.811766666666667
- mean R/H/S/D/K: 3.8/3.9/3.8666666666666667/4.266666666666667/2.7
- mean overall (avg R/H/S/D/K): 3.7066666666666666
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.00, hallucination_suspected=0.17
### L2 (n=30)
- mean runtime: 8.976266666666668
- mean R/H/S/D/K: 4.9/4.733333333333333/4.7/4.933333333333334/4.6
- mean overall (avg R/H/S/D/K): 4.7733333333333325
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.20, hallucination_suspected=0.03
### L2B (n=30)
- mean runtime: 8.996533333333334
- mean R/H/S/D/K: 4.966666666666667/4.866666666666666/4.833333333333333/4.966666666666667/5.0
- mean overall (avg R/H/S/D/K): 4.926666666666667
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.53, hallucination_suspected=0.00

## Mean scores by strategy (snapshot)
### S0 (n=30)
- mean runtime: 6.811766666666667
- mean R/H/S/D/K: 3.8/3.9/3.8666666666666667/4.266666666666667/2.7
- mean overall (avg R/H/S/D/K): 3.7066666666666666
### S1 (n=30)
- mean runtime: 8.976266666666668
- mean R/H/S/D/K: 4.9/4.733333333333333/4.7/4.933333333333334/4.6
- mean overall (avg R/H/S/D/K): 4.7733333333333325
### S2 (n=30)
- mean runtime: 8.996533333333334
- mean R/H/S/D/K: 4.966666666666667/4.866666666666666/4.833333333333333/4.966666666666667/5.0
- mean overall (avg R/H/S/D/K): 4.926666666666667

## Top missing elements (max 20)
- Offline-Workflow bei spotty connectivity: 3
- Offline-Workflow explizit (lokale Doku, spätere Sync): 1
- Offline-Workflow (lokale Doku, spätere Sync) nicht explizit erwähnt: 1
- Severity-Bewusstsein (high): 1
- Umwelt-/Sichtbedingungen: 1
- Foto-Nutzung: 1
- Kreuzung als ungeregelt behandeln: 1
- Kontextnutzung minimal (nur Asset-ID): 1
- Sporadizitäts-Diagnose generisch: 1
- Halluzination: 'Straßenlampe/Ampelanlage' ohne Basis im Kontext: 1
- Offline-Workflow nicht explizit (spotty connectivity): 1
- Asset-Typ-Klärung bleibt offen: 1
- Offline-Workflow (spotty connectivity + low_power_mode nicht explizit adressiert): 1
- Kontext-Nutzung (nur Asset-ID vorhanden, keine Umwelt-/Incident-Details genutzt): 1
- Spekulative Details (z.B. 'außerorts 100m', 'Sicherungen im Schaltkasten') ohne Basis im CONTEXT: 1
- Severity-Einschätzung fehlt (kein Kontext vorhanden): 1
- Umgebungsbedingungen nicht erwähnt (kein Kontext): 1
- Keine Nutzung der Asset-ID im Kontext erkennbar: 1
- Keine Priorisierung bei medium severity + high traffic: 1
- Sporadik-spezifische Beobachtungsstrategie schwach: 1
