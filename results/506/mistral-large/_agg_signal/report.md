# Aggregation Report (506/mistral-large) [signal]
- Tests (latest runs): **150**
- Incidents with any deltas: **30**

## Mean scores by context level (snapshot)
### L0 (n=30)
- mean runtime: 8.2045
- mean R/H/S/D/K: 3.9/4.0/4.233333333333333/4.366666666666666/2.433333333333333
- mean overall (avg R/H/S/D/K): 3.7866666666666666
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.00, hallucination_suspected=0.37
### L2 (n=30)
- mean runtime: 10.112599999999999
- mean R/H/S/D/K: 4.866666666666666/4.8/4.866666666666666/4.833333333333333/4.3
- mean overall (avg R/H/S/D/K): 4.733333333333333
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.13, hallucination_suspected=0.00
### L2B (n=30)
- mean runtime: 9.6319
- mean R/H/S/D/K: 4.966666666666667/4.966666666666667/4.9/4.966666666666667/5.0
- mean overall (avg R/H/S/D/K): 4.96
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.63, hallucination_suspected=0.00
### unknown (n=60)
- mean runtime: 10.350383333333333
- mean R/H/S/D/K: 4.75/4.683333333333334/4.816666666666666/4.833333333333333/4.35
- mean overall (avg R/H/S/D/K): 4.6866666666666665
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.23, hallucination_suspected=0.02

## Mean scores by strategy (snapshot)
### S0 (n=30)
- mean runtime: 8.2045
- mean R/H/S/D/K: 3.9/4.0/4.233333333333333/4.366666666666666/2.433333333333333
- mean overall (avg R/H/S/D/K): 3.7866666666666666
### S0_RAW (n=30)
- mean runtime: 10.231133333333332
- mean R/H/S/D/K: 4.933333333333334/4.9/4.9/5.0/4.8
- mean overall (avg R/H/S/D/K): 4.906666666666666
### S0_UNSTRUCTURED (n=30)
- mean runtime: 10.469633333333332
- mean R/H/S/D/K: 4.566666666666666/4.466666666666667/4.733333333333333/4.666666666666667/3.9
- mean overall (avg R/H/S/D/K): 4.466666666666667
### S1 (n=30)
- mean runtime: 10.112599999999999
- mean R/H/S/D/K: 4.866666666666666/4.8/4.866666666666666/4.833333333333333/4.3
- mean overall (avg R/H/S/D/K): 4.733333333333333
### S2 (n=30)
- mean runtime: 9.6319
- mean R/H/S/D/K: 4.966666666666667/4.966666666666667/4.9/4.966666666666667/5.0
- mean overall (avg R/H/S/D/K): 4.96

## Top missing elements (max 20)
- Kontextnutzung minimal (nur Asset-ID): 4
- Offline-Workflow (spotty connectivity): 4
- Kontextnutzung minimal: 2
- Keine Nutzung der Asset-ID im Kontext: 2
- Offline-Workflow bei spotty connectivity: 2
- Offline-Workflow (nicht erwartbar, da CONTEXT minimal): 1
- Gerätezustand (nicht im CONTEXT): 1
- Offline-Workflow (device.connectivity=offline, device.device_state=low_battery im CONTEXT, aber nicht als Geräte-Constraint interpretiert): 1
- Offline-Workflow explizit (offline/low_battery im CONTEXT, aber nicht klar als Geräte-Constraint behandelt): 1
- Offline-Workflow (nicht erwartbar, da CONTEXT kein connectivity-Signal enthält): 1
- Halluzination: Steuerschrank, Sicherungen, FI-Schalter, Hauptschalter werden detailliert erwähnt, obwohl CONTEXT nur asset_osm enthält: 1
- Offline-Workflow nicht explizit (obwohl connectivity=offline): 1
- Interpretation 'connectivity offline deutet auf Problem mit Steuerung' ist spekulativ, aber nicht falsch: 1
- Offline-Workflow nicht explizit erwähnt (obwohl connectivity=offline im CONTEXT): 1
- Koordinaten/GPS-Nutzung: 1
- Foto-Status erwähnen: 1
- Kontextnutzung minimal (nur Asset-ID vorhanden): 1
- Hinweis auf low_battery des Geräts könnte expliziter sein: 1
- Keine Nutzung der Asset-ID im Kontext (nur minimal vorhanden): 1
- Keine Erwähnung der Konnektivität (online-Status nicht genutzt): 1
