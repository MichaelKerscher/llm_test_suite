# Aggregation Report (506/gpt-4.1) [signal]
- judge_version filter: **judge_v1_1**
- Tests (latest runs): **150**
- Incidents with any deltas: **30**

## Mean scores by context level (snapshot)
### L0 (n=30)
- mean runtime: 7.944533333333334
- mean R/H/S/D/K: 3.8/3.966666666666667/4.0/4.166666666666667/2.3666666666666667
- mean overall (avg R/H/S/D/K): 3.6599999999999997
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.00, hallucination_suspected=0.40
### L2 (n=30)
- mean runtime: 10.3168
- mean R/H/S/D/K: 4.9/4.8/4.833333333333333/5.0/4.533333333333333
- mean overall (avg R/H/S/D/K): 4.8133333333333335
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.07, hallucination_suspected=0.00
### L2B (n=30)
- mean runtime: 10.347900000000001
- mean R/H/S/D/K: 4.933333333333334/4.933333333333334/4.933333333333334/5.0/5.0
- mean overall (avg R/H/S/D/K): 4.96
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.63, hallucination_suspected=0.00
### unknown (n=60)
- mean runtime: 10.354450000000002
- mean R/H/S/D/K: 4.566666666666666/4.6/4.716666666666667/4.75/4.35
- mean overall (avg R/H/S/D/K): 4.596666666666667
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.25, hallucination_suspected=0.00

## Mean scores by strategy (snapshot)
### S0 (n=30)
- mean runtime: 7.944533333333334
- mean R/H/S/D/K: 3.8/3.966666666666667/4.0/4.166666666666667/2.3666666666666667
- mean overall (avg R/H/S/D/K): 3.6599999999999997
### S0_RAW (n=30)
- mean runtime: 10.344866666666666
- mean R/H/S/D/K: 4.8/4.766666666666667/4.733333333333333/4.933333333333334/4.733333333333333
- mean overall (avg R/H/S/D/K): 4.793333333333334
### S0_UNSTRUCTURED (n=30)
- mean runtime: 10.364033333333333
- mean R/H/S/D/K: 4.333333333333333/4.433333333333334/4.7/4.566666666666666/3.966666666666667
- mean overall (avg R/H/S/D/K): 4.4
### S1 (n=30)
- mean runtime: 10.3168
- mean R/H/S/D/K: 4.9/4.8/4.833333333333333/5.0/4.533333333333333
- mean overall (avg R/H/S/D/K): 4.8133333333333335
### S2 (n=30)
- mean runtime: 10.347900000000001
- mean R/H/S/D/K: 4.933333333333334/4.933333333333334/4.933333333333334/5.0/5.0
- mean overall (avg R/H/S/D/K): 4.96

## Top missing elements (max 20)
- Keine Nutzung der Asset-ID im Kontext: 2
- Kontextnutzung minimal (nur Asset-ID): 2
- Offline-Workflow explizit (spotty connectivity vorhanden): 2
- Offline-Workflow nicht explizit erwähnt trotz spotty connectivity: 2
- Offline-Workflow (spotty connectivity): 2
- Offline-Workflow nicht erwähnt trotz offline im Kontext: 1
- Offline-Workflow nicht erwähnt trotz offline/low_battery im Kontext: 1
- Keine Erwähnung intermittierender Natur: 1
- Keine Priorisierung nach Verkehrszeit: 1
- Spekuliert über Ampel/Straßenlampe ohne Basis: 1
- Keine Anpassung an tatsächliche Umgebung: 1
- Offline-Workflow nicht explizit trotz spotty connectivity: 1
- Offline-Workflow könnte expliziter sein: 1
- Offline-Workflow nicht explizit (spotty connectivity vorhanden): 1
- Kontext-Nutzung: Koordinaten, Foto-Beschreibung, Wetter, Zeit fehlen komplett: 1
- Keine explizite Erwähnung 'mittleres Verkehrsaufkommen' aus Kontext: 1
- Keine Nutzung von Kontext-Signalen (severity, weather, traffic): 1
- Keine spezifische Priorisierung basierend auf Umgebungsbedingungen: 1
- Keine Nutzung des Kontexts (nur Asset-ID vorhanden): 1
- Keine Erwähnung von Umgebungsbedingungen (nicht im Kontext): 1
