# Aggregation Report (506/gemini-2.5-flash)
- judge_version filter: **judge_v1_1**
- Tests (latest runs): **90**
- Incidents with any deltas: **30**

## Mean scores by context level (snapshot)
### L0 (n=30)
- mean runtime: 5.658
- mean R/H/S/D/K: 3.533333333333333/3.8333333333333335/3.8/3.966666666666667/2.9
- mean overall (avg R/H/S/D/K): 3.606666666666667
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.00, hallucination_suspected=0.07
### L2 (n=30)
- mean runtime: 8.548399999999999
- mean R/H/S/D/K: 4.766666666666667/4.566666666666666/4.7/4.9/4.1
- mean overall (avg R/H/S/D/K): 4.6066666666666665
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.07, hallucination_suspected=0.03
### L2B (n=30)
- mean runtime: 9.509066666666666
- mean R/H/S/D/K: 4.966666666666667/4.966666666666667/4.9/5.0/5.0
- mean overall (avg R/H/S/D/K): 4.966666666666667
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.60, hallucination_suspected=0.00

## Mean scores by strategy (snapshot)
### S0 (n=30)
- mean runtime: 5.658
- mean R/H/S/D/K: 3.533333333333333/3.8333333333333335/3.8/3.966666666666667/2.9
- mean overall (avg R/H/S/D/K): 3.606666666666667
### S1 (n=30)
- mean runtime: 8.548399999999999
- mean R/H/S/D/K: 4.766666666666667/4.566666666666666/4.7/4.9/4.1
- mean overall (avg R/H/S/D/K): 4.6066666666666665
### S2 (n=30)
- mean runtime: 9.509066666666666
- mean R/H/S/D/K: 4.966666666666667/4.966666666666667/4.9/5.0/5.0
- mean overall (avg R/H/S/D/K): 4.966666666666667

## Top missing elements (max 20)
- Offline-Workflow bei spotty connectivity: 4
- Offline-Workflow bei spotty connectivity nicht explizit erwähnt: 3
- Offline-Workflow explizit (spotty connectivity): 2
- Kontextnutzung minimal (nur Asset-ID): 2
- Offline-Workflow (connectivity=offline): 1
- Korrekte Interpretation device.* (Techniker-Gerät, nicht Asset): 1
- Keine Nutzung des minimalen Kontexts (nur OSM-ID): 1
- Keine Anpassung an fehlende Umgebungs-/Incident-Daten: 1
- Offline-Workflow (connectivity=offline, device_state=low_battery): 1
- Offline-Workflow (nicht erwartbar, da connectivity nicht im CONTEXT): 1
- Konkrete Priorisierung bei Sturm/Wetter (nicht erwartbar, da weather fehlt): 1
- Nutzung von photo_available (nicht erwartbar, da nicht im CONTEXT): 1
- Offline-Workflow explizit (connectivity=offline → lokale Doku/Sync später): 1
- Offline-Workflow (Kontext zeigt kein connectivity-Signal, daher nicht erwartbar): 1
- Explizite Erwähnung severity=low (aber Priorisierung passt): 1
- Explizite Nennung 'Offline-Workflow' (implizit aber klar umgesetzt): 1
- Kontext-Nutzung fehlt komplett (nur Asset-ID vorhanden): 1
- Spekuliert über Ampelanlage ohne Basis: 1
- Erfundene Details (Vorschaltgerät, Induktionsschleifen, Steuerungsschrank): 1
- Keine Nutzung der verfügbaren Asset-ID im Kontext: 1
