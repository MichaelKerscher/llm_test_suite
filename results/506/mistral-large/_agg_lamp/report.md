# Aggregation Report (506/mistral-large) [lamp]
- judge_version filter: **judge_v1_1**
- Tests (latest runs): **270**
- Incidents with any deltas: **30**

## Mean scores by context level (snapshot)
### L0 (n=30)
- mean runtime: 7.446633333333334
- mean R/H/S/D/K: 3.466666666666667/3.7/3.6666666666666665/4.066666666666666/2.3666666666666667
- mean overall (avg R/H/S/D/K): 3.453333333333333
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.00, hallucination_suspected=0.10
### L2 (n=30)
- mean runtime: 10.2567
- mean R/H/S/D/K: 4.833333333333333/4.8/4.666666666666667/4.8/4.4
- mean overall (avg R/H/S/D/K): 4.7
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.03, hallucination_suspected=0.03
### L2B (n=30)
- mean runtime: 14.735133333333332
- mean R/H/S/D/K: 4.933333333333334/4.933333333333334/4.833333333333333/5.0/5.0
- mean overall (avg R/H/S/D/K): 4.9399999999999995
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.60, hallucination_suspected=0.00
### unknown (n=180)
- mean runtime: 9.389011111111111
- mean R/H/S/D/K: 4.75/4.7555555555555555/4.761111111111111/4.866666666666666/4.694444444444445
- mean overall (avg R/H/S/D/K): 4.765555555555555
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.41, hallucination_suspected=0.01

## Mean scores by strategy (snapshot)
### S0 (n=30)
- mean runtime: 7.446633333333334
- mean R/H/S/D/K: 3.466666666666667/3.7/3.6666666666666665/4.066666666666666/2.3666666666666667
- mean overall (avg R/H/S/D/K): 3.453333333333333
### S0_RAW (n=30)
- mean runtime: 10.063233333333333
- mean R/H/S/D/K: 4.7/4.633333333333334/4.7/4.833333333333333/4.5
- mean overall (avg R/H/S/D/K): 4.673333333333333
### S0_UNSTRUCTURED (n=30)
- mean runtime: 9.578233333333333
- mean R/H/S/D/K: 4.4/4.466666666666667/4.5/4.566666666666666/3.8
- mean overall (avg R/H/S/D/K): 4.346666666666667
### S1 (n=30)
- mean runtime: 10.2567
- mean R/H/S/D/K: 4.833333333333333/4.8/4.666666666666667/4.8/4.4
- mean overall (avg R/H/S/D/K): 4.7
### S2 (n=30)
- mean runtime: 14.735133333333332
- mean R/H/S/D/K: 4.933333333333334/4.933333333333334/4.833333333333333/5.0/5.0
- mean overall (avg R/H/S/D/K): 4.9399999999999995
### S2_ABL_NOASSET (n=30)
- mean runtime: 9.7382
- mean R/H/S/D/K: 4.866666666666666/4.9/4.866666666666666/4.933333333333334/4.966666666666667
- mean overall (avg R/H/S/D/K): 4.906666666666666
### S2_ABL_NODEV (n=30)
- mean runtime: 9.3244
- mean R/H/S/D/K: 4.966666666666667/4.933333333333334/4.866666666666666/5.0/4.966666666666667
- mean overall (avg R/H/S/D/K): 4.946666666666667
### S2_ABL_NOENV (n=30)
- mean runtime: 8.850366666666668
- mean R/H/S/D/K: 4.833333333333333/4.766666666666667/4.7/4.9/4.933333333333334
- mean overall (avg R/H/S/D/K): 4.826666666666667
### S2_ABL_NOINC (n=30)
- mean runtime: 8.779633333333333
- mean R/H/S/D/K: 4.733333333333333/4.833333333333333/4.933333333333334/4.966666666666667/5.0
- mean overall (avg R/H/S/D/K): 4.8933333333333335

## Top missing elements (max 20)
- offline_workflow: 7
- Keine Nutzung der Asset-ID im Kontext: 3
- Offline-Workflow trotz spotty connectivity: 2
- Offline-Workflow explizit (connectivity=spotty): 2
- Offline-Workflow nicht erwähnt trotz 'spotty' connectivity: 2
- Offline-Workflow nicht explizit erwähnt (spotty connectivity im CONTEXT): 2
- Offline-Workflow (spotty connectivity im CONTEXT, aber nicht explizit erwähnt): 2
- Generische Antwort ohne Kontextbezug: 2
- Keine Priorisierung nach Severity: 2
- Klare Stop-Condition für Beobachtungsphase fehlt: 1
- Offline-Workflow (device.connectivity=offline nicht erkannt): 1
- Low-battery-Hinweis (device_state=low_battery nicht genutzt): 1
- Offline-Workflow explizit (offline/low_battery erkannt, aber kein Offline-Dokumentations-Hinweis): 1
- Keine Nutzung des Kontexts (nur asset_osm vorhanden): 1
- Keine Erwähnung von Feuchtigkeitsflecken oder Foto: 1
- Keine Priorisierung auf intermittierenden Fehler: 1
- Explizite Erwähnung der Asset-ID (n4427359783) in Dokumentation: 1
- Keine Kontextnutzung (Umgebung, Gerätezustand): 1
- Offline-Workflow nicht erwähnt trotz minimalem Kontext: 1
- Annahme zu low_battery/spotty korrekt, aber Workflow-Konsequenz fehlt: 1
