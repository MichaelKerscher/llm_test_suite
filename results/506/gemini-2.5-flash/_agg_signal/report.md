# Aggregation Report (506\gemini-2.5-flash) [signal]
- judge_version filter: **judge_v1_1**
- Tests (latest runs): **90**
- Incidents with any deltas: **30**

## Mean scores by context level (snapshot)
### L0 (n=30)
- mean runtime: 7.086366666666667
- mean R/H/S/D/K: 3.9/3.966666666666667/4.2/4.333333333333333/2.8333333333333335
- mean overall (avg R/H/S/D/K): 3.8466666666666667
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.00, hallucination_suspected=0.00
### L2 (n=30)
- mean runtime: 8.920800000000002
- mean R/H/S/D/K: 4.866666666666666/4.833333333333333/4.8/4.933333333333334/4.6
- mean overall (avg R/H/S/D/K): 4.806666666666667
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.20, hallucination_suspected=0.00
### L2B (n=30)
- mean runtime: 9.390333333333333
- mean R/H/S/D/K: 4.966666666666667/4.933333333333334/4.933333333333334/4.9/4.933333333333334
- mean overall (avg R/H/S/D/K): 4.933333333333334
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.67, hallucination_suspected=0.00

## Mean scores by strategy (snapshot)
### S0 (n=30)
- mean runtime: 7.086366666666667
- mean R/H/S/D/K: 3.9/3.966666666666667/4.2/4.333333333333333/2.8333333333333335
- mean overall (avg R/H/S/D/K): 3.8466666666666667
### S1 (n=30)
- mean runtime: 8.920800000000002
- mean R/H/S/D/K: 4.866666666666666/4.833333333333333/4.8/4.933333333333334/4.6
- mean overall (avg R/H/S/D/K): 4.806666666666667
### S2 (n=30)
- mean runtime: 9.390333333333333
- mean R/H/S/D/K: 4.966666666666667/4.933333333333334/4.933333333333334/4.9/4.933333333333334
- mean overall (avg R/H/S/D/K): 4.933333333333334

## Top missing elements (max 20)
- Offline-Workflow (device.connectivity=offline nicht adressiert): 2
- Offline-Workflow bei spotty connectivity nicht explizit erwähnt: 2
- Keine Nutzung des verfügbaren Kontexts (nur Asset-ID): 1
- Keine Erwähnung des Fotos (photo_available=true im vollen Kontext nicht sichtbar hier): 1
- Offline-Workflow explizit (spotty connectivity): 1
- Keine Nutzung der Asset-ID im Kontext (nur in Dokumentation erwähnt): 1
- Keine Anpassung an tatsächliche Umgebungsbedingungen (generisch): 1
- Offline-Workflow (spotty connectivity + low_battery): 1
- Offline-Workflow (nicht erwartbar bei minimalem Kontext): 1
- Keine Nutzung des minimalen Kontexts (nur asset_osm vorhanden): 1
- Keine Anpassung an fehlende Umgebungsinformationen: 1
- Kontextnutzung minimal (nur Asset-ID): 1
- Keine Priorisierung nach Severity/Traffic: 1
- Keine Erwähnung von Beobachtungsdauer bei intermittent: 1
- Keine explizite Beobachtungsdauer-Empfehlung: 1
- Umgebungsbedingungen (Wetter/Sicht/Verkehr) nicht berücksichtigt: 1
- Keine Priorisierung bei mittlerer Severity erkennbar: 1
- Offline-Workflow (spotty connectivity): 1
- Severity-Einschätzung fehlt (high nicht erkennbar aus Kontext): 1
- Offline-Workflow nicht erwähnt (aber auch nicht erwartbar bei L0): 1
