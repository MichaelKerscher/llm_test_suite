# Aggregation Report (506\gpt-4.1) [signal]
- judge_version filter: **judge_v1_1**
- Tests (latest runs): **90**
- Incidents with any deltas: **30**

## Mean scores by context level (snapshot)
### L0 (n=30)
- mean runtime: 6.536966666666667
- mean R/H/S/D/K: 3.8333333333333335/3.933333333333333/4.0/4.133333333333334/2.7
- mean overall (avg R/H/S/D/K): 3.7199999999999998
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.00, hallucination_suspected=0.07
### L2 (n=30)
- mean runtime: 8.926633333333333
- mean R/H/S/D/K: 4.933333333333334/4.866666666666666/4.833333333333333/4.966666666666667/4.6
- mean overall (avg R/H/S/D/K): 4.84
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.20, hallucination_suspected=0.00
### L2B (n=30)
- mean runtime: 8.881266666666667
- mean R/H/S/D/K: 4.933333333333334/4.933333333333334/4.9/4.966666666666667/5.0
- mean overall (avg R/H/S/D/K): 4.946666666666667
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.67, hallucination_suspected=0.00

## Mean scores by strategy (snapshot)
### S0 (n=30)
- mean runtime: 6.536966666666667
- mean R/H/S/D/K: 3.8333333333333335/3.933333333333333/4.0/4.133333333333334/2.7
- mean overall (avg R/H/S/D/K): 3.7199999999999998
### S1 (n=30)
- mean runtime: 8.926633333333333
- mean R/H/S/D/K: 4.933333333333334/4.866666666666666/4.833333333333333/4.966666666666667/4.6
- mean overall (avg R/H/S/D/K): 4.84
### S2 (n=30)
- mean runtime: 8.881266666666667
- mean R/H/S/D/K: 4.933333333333334/4.933333333333334/4.9/4.966666666666667/5.0
- mean overall (avg R/H/S/D/K): 4.946666666666667

## Top missing elements (max 20)
- Kontextnutzung minimal (nur Asset-ID): 3
- Kontextnutzung minimal (nur Asset-ID vorhanden): 2
- Keine Anpassung an Umgebungsbedingungen: 2
- Offline-Workflow bei spotty connectivity nicht explizit erwähnt: 2
- Offline-Workflow (spotty connectivity): 2
- Offline-Workflow explizit (device.connectivity=offline): 1
- Offline-Workflow nicht explizit erwähnt: 1
- Keine Nutzung des verfügbaren Kontexts (nur Asset-ID): 1
- Keine Erwähnung von Foto-Verfügbarkeit trotz photo_available=true im Kontext: 1
- Keine Anpassung an Hauptverkehrszeit/hohen Verkehr erkennbar: 1
- Intermittierender Fehler nicht explizit adressiert: 1
- Offline-Workflow nicht explizit (spotty connectivity): 1
- GPS-Koordinaten nicht erwähnt (waren im CONTEXT vorhanden): 1
- Keine Anpassung an Umgebungsbedingungen (nicht erwartbar bei L0): 1
- Keine Offline-Workflow-Erwähnung (nicht erwartbar bei L0): 1
- Offline-Workflow nicht explizit erwähnt (spotty connectivity vorhanden): 1
- GPS-Koordinaten (nicht im Context verfügbar): 1
- Spezifische Behandlung 'signal_dark' (Rechts-vor-Links): 1
- Keine Kontextnutzung erkennbar (minimaler Context): 1
- Severity/Dringlichkeit nicht priorisiert: 1
