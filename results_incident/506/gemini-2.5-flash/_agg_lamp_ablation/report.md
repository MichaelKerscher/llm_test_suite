# Aggregation Report (506/gemini-2.5-flash) [lamp]
- incident filter: **ablation**
- Tests (latest runs): **120**
- Incidents with any deltas: **0**

## Mean scores by context level (snapshot)
### unknown (n=120)
- mean runtime: 10.081441666666667
- mean R/H/S/D/K: 4.083333333333333/4.258333333333334/4.533333333333333/4.525/4.35
- mean overall (avg R/H/S/D/K): 4.35
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.50, hallucination_suspected=0.00

## Mean scores by strategy (snapshot)
### S2_ABL_NOASSET (n=30)
- mean runtime: 10.480933333333333
- mean R/H/S/D/K: 4.066666666666666/4.2/4.633333333333334/4.266666666666667/4.333333333333333
- mean overall (avg R/H/S/D/K): 4.3
### S2_ABL_NODEV (n=30)
- mean runtime: 9.774166666666668
- mean R/H/S/D/K: 4.3/4.333333333333333/4.6/4.666666666666667/3.9
- mean overall (avg R/H/S/D/K): 4.36
### S2_ABL_NOENV (n=30)
- mean runtime: 10.168299999999999
- mean R/H/S/D/K: 4.133333333333334/4.3/4.366666666666666/4.733333333333333/4.566666666666666
- mean overall (avg R/H/S/D/K): 4.42
### S2_ABL_NOINC (n=30)
- mean runtime: 9.902366666666667
- mean R/H/S/D/K: 3.8333333333333335/4.2/4.533333333333333/4.433333333333334/4.6
- mean overall (avg R/H/S/D/K): 4.319999999999999

## Top missing elements (max 20)
- Asset-ID fehlt (nicht im Kontext vorhanden): 5
- Gerätezustand nicht berücksichtigt: 3
- Offline-Workflow nicht erwähnt (device.connectivity fehlt im Kontext): 2
- Asset-ID fehlt (nicht im Kontext vorhanden, daher kein Fehler): 2
- Asset-ID/GPS-Koordinaten (nicht im Kontext vorhanden): 2
- Offline-Workflow nicht erwähnt (device.* fehlt im Kontext): 1
- Gerätezustand (low_battery) nicht berücksichtigt: 1
- Asset-ID/Standort fehlt (nicht im Kontext): 1
- GPS-Koordinaten nicht erwähnt (nicht verfügbar): 1
- Verkehrsaufkommen/Sicht nicht erwähnt (nicht im Kontext): 1
- Foto-Hinweis fehlt (nicht im Kontext): 1
- Feuchtigkeitsflecken nicht erwähnt (nicht im Kontext): 1
- Asset-ID/OSM-ID fehlt (nicht im Kontext vorhanden): 1
- Offline-Workflow nicht erwähnt (device.connectivity=spotty fehlt im Kontext): 1
- Asset-ID fehlt (nicht im Context): 1
- Offline-Workflow nicht erwähnt trotz fehlendem device-Context: 1
- Offline-Workflow nicht erwähnt (device-Kontext fehlt): 1
- Umweltbedingungen nicht erwähnt (nicht im Kontext): 1
- Severity/Eskalations-Trigger weniger explizit (incident.* fehlt): 1
- Offline-Workflow nicht erwähnt (device.connectivity fehlt im Kontext, daher kein Fehler): 1
