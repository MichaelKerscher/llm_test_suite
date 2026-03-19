# Aggregation Report (506\gpt-4.1) [signal]
- judge_version filter: **judge_v1_1**
- Tests (latest runs): **90**
- Incidents with any deltas: **30**

## Mean scores by context level (snapshot)
### L0 (n=30)
- mean runtime: 6.8145
- mean R/H/S/D/K: 3.8666666666666667/4.0/4.033333333333333/4.1/2.8666666666666667
- mean overall (avg R/H/S/D/K): 3.7733333333333334
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.00, hallucination_suspected=0.07
### L2 (n=30)
- mean runtime: 8.964400000000001
- mean R/H/S/D/K: 4.933333333333334/4.833333333333333/4.833333333333333/4.933333333333334/4.566666666666666
- mean overall (avg R/H/S/D/K): 4.819999999999999
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.27, hallucination_suspected=0.00
### L2B (n=30)
- mean runtime: 9.059333333333333
- mean R/H/S/D/K: 5.0/4.933333333333334/4.9/4.966666666666667/5.0
- mean overall (avg R/H/S/D/K): 4.96
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.57, hallucination_suspected=0.00

## Mean scores by strategy (snapshot)
### S0 (n=30)
- mean runtime: 6.8145
- mean R/H/S/D/K: 3.8666666666666667/4.0/4.033333333333333/4.1/2.8666666666666667
- mean overall (avg R/H/S/D/K): 3.7733333333333334
### S1 (n=30)
- mean runtime: 8.964400000000001
- mean R/H/S/D/K: 4.933333333333334/4.833333333333333/4.833333333333333/4.933333333333334/4.566666666666666
- mean overall (avg R/H/S/D/K): 4.819999999999999
### S2 (n=30)
- mean runtime: 9.059333333333333
- mean R/H/S/D/K: 5.0/4.933333333333334/4.9/4.966666666666667/5.0
- mean overall (avg R/H/S/D/K): 4.96

## Top missing elements (max 20)
- Offline-Workflow (nicht erwartbar, da CONTEXT kein offline-Signal enthält): 2
- Offline-Workflow (spotty connectivity) nicht explizit erwähnt: 2
- Wetter/Sicht-Bezug (nicht erwartbar, da CONTEXT keine environment-Daten enthält): 1
- Offline-Workflow nicht erwähnt (aber auch nicht erwartbar bei minimalem Kontext): 1
- Offline-Workflow bei spotty connectivity nicht explizit genannt: 1
- Explizite Erwähnung von Regen/Wetter aus Kontext: 1
- Nutzung der GPS-Koordinaten: 1
- Severity-Einschätzung fehlt (nur Asset-ID gegeben): 1
- Wetter/Sicht nicht erwähnt (nicht im Context): 1
- Guardrail-Hinweis (signal_dark-Behandlung) nicht explizit aufgegriffen: 1
- Severity-Einschätzung fehlt (nur minimal context): 1
- Kein Hinweis auf Foto-Dokumentation trotz photo_available: 1
- Offline-Workflow nicht explizit erwähnt trotz spotty connectivity: 1
- Keine Nutzung des minimalen Kontexts (nur asset_osm): 1
- Spekulation über Asset-Typ (Straßenlampe/Ampel) ohne Basis: 1
- GPS-Koordinaten nicht explizit in Dokumentation erwähnt: 1
- Kontextnutzung minimal (nur Asset-ID vorhanden): 1
- Keine Nutzung der Asset-ID im Kontext erkennbar: 1
- Keine Erwähnung von Umgebungsbedingungen (rush_hour/high traffic nicht aus CONTEXT ableitbar): 1
- Severity-Bewusstsein (high) nicht explizit: 1
