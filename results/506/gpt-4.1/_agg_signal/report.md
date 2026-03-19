# Aggregation Report (506\gpt-4.1) [signal]
- judge_version filter: **judge_v1_1**
- Tests (latest runs): **90**
- Incidents with any deltas: **30**

## Mean scores by context level (snapshot)
### L0 (n=30)
- mean runtime: 6.942866666666666
- mean R/H/S/D/K: 3.966666666666667/3.966666666666667/4.1/4.4/2.8
- mean overall (avg R/H/S/D/K): 3.8466666666666667
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.00, hallucination_suspected=0.07
### L2 (n=30)
- mean runtime: 9.2522
- mean R/H/S/D/K: 4.833333333333333/4.7/4.9/4.933333333333334/4.566666666666666
- mean overall (avg R/H/S/D/K): 4.786666666666666
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.10, hallucination_suspected=0.00
### L2B (n=30)
- mean runtime: 9.278500000000001
- mean R/H/S/D/K: 4.966666666666667/4.9/4.933333333333334/4.966666666666667/5.0
- mean overall (avg R/H/S/D/K): 4.953333333333333
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.57, hallucination_suspected=0.00

## Mean scores by strategy (snapshot)
### S0 (n=30)
- mean runtime: 6.942866666666666
- mean R/H/S/D/K: 3.966666666666667/3.966666666666667/4.1/4.4/2.8
- mean overall (avg R/H/S/D/K): 3.8466666666666667
### S1 (n=30)
- mean runtime: 9.2522
- mean R/H/S/D/K: 4.833333333333333/4.7/4.9/4.933333333333334/4.566666666666666
- mean overall (avg R/H/S/D/K): 4.786666666666666
### S2 (n=30)
- mean runtime: 9.278500000000001
- mean R/H/S/D/K: 4.966666666666667/4.9/4.933333333333334/4.966666666666667/5.0
- mean overall (avg R/H/S/D/K): 4.953333333333333

## Top missing elements (max 20)
- Offline-Workflow bei spotty connectivity: 5
- Offline-Workflow nicht explizit erwähnt: 1
- Offline-Workflow (lokal speichern, später sync): 1
- Keine Nutzung des minimalen Kontexts (nur asset_osm vorhanden): 1
- Spekuliert über Fehlerspeicher/Steuerung ohne Kontext-Basis: 1
- Kontextnutzung minimal (nur Asset-ID): 1
- Annahme 'Straßenlampe/Ampel' nicht durch Context gedeckt: 1
- Offline-Workflow nicht explizit erwähnt trotz spotty connectivity: 1
- Severity-Einschätzung fehlt (kein Kontext vorhanden): 1
- Wetter/Sicht nicht erwähnt (kein Kontext vorhanden): 1
- Offline-Workflow (spotty connectivity): 1
- Keine Anpassung an Umweltbedingungen (Kontext minimal): 1
- Keine Nutzung von GPS-Daten zur Lokalisierung: 1
- Severity-Einschätzung fehlt (kein Signal im Kontext): 1
- Umgebungsbedingungen nicht erwähnt (nicht im Kontext): 1
- Offline-Workflow (nicht erwartbar bei L0): 1
- Wetter-/Sichtbedingungen (nicht im Context): 1
- Offline-Workflow bei spotty connectivity nicht explizit erwähnt: 1
- Offline-Workflow nicht erwähnt trotz device.connectivity=offline: 1
- Offline-Workflow (lokale Dokumentation, spätere Sync): 1
