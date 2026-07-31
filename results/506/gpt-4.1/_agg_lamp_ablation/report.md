# Aggregation Report (506/gpt-4.1) [lamp]
- incident filter: **ablation**
- Tests (latest runs): **120**
- Incidents with any deltas: **0**

## Mean scores by context level (snapshot)
### unknown (n=120)
- mean runtime: 10.782108333333333
- mean R/H/S/D/K: 4.033333333333333/4.216666666666667/4.433333333333334/4.466666666666667/4.291666666666667
- mean overall (avg R/H/S/D/K): 4.288333333333333
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.45, hallucination_suspected=0.01

## Mean scores by strategy (snapshot)
### S2_ABL_NOASSET (n=30)
- mean runtime: 10.807566666666666
- mean R/H/S/D/K: 4.033333333333333/4.166666666666667/4.466666666666667/4.2/4.233333333333333
- mean overall (avg R/H/S/D/K): 4.22
### S2_ABL_NODEV (n=30)
- mean runtime: 10.620166666666668
- mean R/H/S/D/K: 4.366666666666666/4.3/4.533333333333333/4.633333333333334/3.8
- mean overall (avg R/H/S/D/K): 4.326666666666667
### S2_ABL_NOENV (n=30)
- mean runtime: 11.076933333333333
- mean R/H/S/D/K: 4.133333333333334/4.2/4.233333333333333/4.733333333333333/4.6
- mean overall (avg R/H/S/D/K): 4.38
### S2_ABL_NOINC (n=30)
- mean runtime: 10.623766666666667
- mean R/H/S/D/K: 3.6/4.2/4.5/4.3/4.533333333333333
- mean overall (avg R/H/S/D/K): 4.226666666666667

## Top missing elements (max 20)
- Asset-ID fehlt (nicht im Kontext vorhanden): 8
- Offline-Workflow nicht erwähnt (device.connectivity fehlt im Kontext): 5
- Severity/fault_type nicht bekannt, daher generischer: 2
- Asset-ID/GPS-Koordinaten (nicht verfügbar im Context): 2
- Asset-ID/GPS-Koordinaten (nicht im Kontext vorhanden): 2
- Severity/Foto-Info fehlt (nicht im Kontext): 2
- Offline-Workflow (connectivity fehlt im Context, daher nicht erwartbar): 2
- Severity/photo_description fehlen (nicht im Kontext): 1
- Asset-Identifikation fehlt (keine OSM-ID/GPS): 1
- Halluzination: Spekuliert über 'alten Vorfall' ohne Basis: 1
- Übermäßig detailliert für fehlenden Asset-Kontext: 1
- Keine explizite Erwähnung von Umweltbedingungen (Nebel/Nacht aus incident.photo_description): 1
- Umweltbedingungen (Nebel/Nacht/Verkehr) nicht berücksichtigt: 1
- Feuchtigkeitsflecken/Foto-Hinweise fehlen (kein incident-Kontext): 1
- Offline-Workflow (connectivity/device_state fehlen im Context): 1
- Stop-Conditions schwach: 1
- Offline-Workflow nicht erwähnt (connectivity fehlt im Kontext, daher nicht erwartbar): 1
- Offline-Workflow (device.connectivity=spotty fehlt im CONTEXT, daher nicht erwartbar – kein Fehler): 1
- Offline-Workflow nicht erwähnt (device.connectivity fehlt im Context): 1
- Sturm/Wetter nicht berücksichtigt (environment fehlt): 1
