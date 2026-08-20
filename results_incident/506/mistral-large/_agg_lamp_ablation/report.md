# Aggregation Report (506/mistral-large) [lamp]
- incident filter: **ablation**
- Tests (latest runs): **120**
- Incidents with any deltas: **0**

## Mean scores by context level (snapshot)
### unknown (n=120)
- mean runtime: 11.895441666666667
- mean R/H/S/D/K: 4.033333333333333/4.191666666666666/4.633333333333334/4.516666666666667/4.316666666666666
- mean overall (avg R/H/S/D/K): 4.338333333333334
- flags (rate): safety_first=0.99, escalation_present=1.00, offline_workflow_mentioned=0.47, hallucination_suspected=0.00

## Mean scores by strategy (snapshot)
### S2_ABL_NOASSET (n=30)
- mean runtime: 12.874666666666666
- mean R/H/S/D/K: 4.0/4.066666666666666/4.7/4.166666666666667/4.2
- mean overall (avg R/H/S/D/K): 4.226666666666667
### S2_ABL_NODEV (n=30)
- mean runtime: 11.0288
- mean R/H/S/D/K: 4.333333333333333/4.3/4.733333333333333/4.6/3.9
- mean overall (avg R/H/S/D/K): 4.373333333333333
### S2_ABL_NOENV (n=30)
- mean runtime: 12.310599999999999
- mean R/H/S/D/K: 4.133333333333334/4.2/4.333333333333333/4.866666666666666/4.566666666666666
- mean overall (avg R/H/S/D/K): 4.42
### S2_ABL_NOINC (n=30)
- mean runtime: 11.367700000000001
- mean R/H/S/D/K: 3.6666666666666665/4.2/4.766666666666667/4.433333333333334/4.6
- mean overall (avg R/H/S/D/K): 4.333333333333333

## Top missing elements (max 20)
- Asset-ID fehlt (nicht im Kontext vorhanden): 6
- Asset-ID/GPS-Koordinaten (nicht im Kontext vorhanden): 3
- Offline-Workflow nicht erwähnt (connectivity fehlt im Kontext): 2
- Offline-Workflow nicht erwähnt (device.connectivity fehlt im Context): 2
- Offline-Workflow nicht erwähnt (device.connectivity fehlt im Kontext, daher nicht erwartbar): 2
- Offline-Workflow nicht erwähnt (low_battery könnte Offline-Risiko bedeuten): 2
- Asset-ID/Standort explizit dokumentieren: 1
- Offline-Workflow: 1
- Safety-first explizit als Schritt 1: 1
- Asset-ID/Standort fehlt (nicht im Kontext): 1
- Umweltbedingungen (Nebel/poor visibility) nicht berücksichtigt: 1
- Foto-Hinweis nicht genutzt: 1
- Feuchtigkeitsflecken nicht erwähnt: 1
- Asset-ID/GPS-Koordinaten (nicht verfügbar im Kontext): 1
- Offline-Workflow (device.connectivity/device_state fehlen im Kontext, daher nicht erwartbar): 1
- Severity/Dringlichkeit nicht explizit aus incident abgeleitet: 1
- Offline-Workflow (device.connectivity fehlt im Kontext, daher nicht erwartbar): 1
- Asset-ID fehlt (nicht im Context vorhanden): 1
- Severity/photo_description fehlen (nicht im Context): 1
- Offline-Workflow nicht erwähnt: 1
