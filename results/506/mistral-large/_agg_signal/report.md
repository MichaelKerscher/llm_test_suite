# Aggregation Report (506/mistral-large) [signal]
- judge_version filter: **judge_v1_1**
- Tests (latest runs): **150**
- Incidents with any deltas: **30**

## Mean scores by context level (snapshot)
### L0 (n=30)
- mean runtime: 8.7101
- mean R/H/S/D/K: 3.966666666666667/4.0/4.2/4.2/2.6666666666666665
- mean overall (avg R/H/S/D/K): 3.8066666666666666
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.00, hallucination_suspected=0.20
### L2 (n=30)
- mean runtime: 11.540666666666665
- mean R/H/S/D/K: 4.966666666666667/4.933333333333334/4.966666666666667/4.933333333333334/4.533333333333333
- mean overall (avg R/H/S/D/K): 4.866666666666666
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.13, hallucination_suspected=0.00
### L2B (n=30)
- mean runtime: 10.249966666666667
- mean R/H/S/D/K: 4.966666666666667/4.933333333333334/5.0/4.933333333333334/4.966666666666667
- mean overall (avg R/H/S/D/K): 4.96
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.57, hallucination_suspected=0.00
### unknown (n=60)
- mean runtime: 10.995166666666668
- mean R/H/S/D/K: 4.616666666666666/4.6/4.75/4.8/4.25
- mean overall (avg R/H/S/D/K): 4.6033333333333335
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.23, hallucination_suspected=0.02

## Mean scores by strategy (snapshot)
### S0 (n=30)
- mean runtime: 8.7101
- mean R/H/S/D/K: 3.966666666666667/4.0/4.2/4.2/2.6666666666666665
- mean overall (avg R/H/S/D/K): 3.8066666666666666
### S0_RAW (n=30)
- mean runtime: 10.456533333333335
- mean R/H/S/D/K: 4.866666666666666/4.833333333333333/4.866666666666666/5.0/4.7
- mean overall (avg R/H/S/D/K): 4.8533333333333335
### S0_UNSTRUCTURED (n=30)
- mean runtime: 11.533800000000001
- mean R/H/S/D/K: 4.366666666666666/4.366666666666666/4.633333333333334/4.6/3.8
- mean overall (avg R/H/S/D/K): 4.3533333333333335
### S1 (n=30)
- mean runtime: 11.540666666666665
- mean R/H/S/D/K: 4.966666666666667/4.933333333333334/4.966666666666667/4.933333333333334/4.533333333333333
- mean overall (avg R/H/S/D/K): 4.866666666666666
### S2 (n=30)
- mean runtime: 10.249966666666667
- mean R/H/S/D/K: 4.966666666666667/4.933333333333334/5.0/4.933333333333334/4.966666666666667
- mean overall (avg R/H/S/D/K): 4.96

## Top missing elements (max 20)
- offline_workflow: 4
- offline_workflow_explicit: 3
- Kontextnutzung minimal (nur Asset-ID): 2
- Offline-Workflow (nicht erwartbar, da connectivity nicht im Context): 2
- Offline-Workflow nicht explizit erwähnt (spotty connectivity im Kontext): 2
- Offline-Workflow (nicht erwartbar, da CONTEXT minimal): 1
- Spezifische Kontextnutzung (nur Asset-ID vorhanden): 1
- Offline-Workflow (offline/low_battery im CONTEXT, aber nicht klar adressiert): 1
- Offline-Workflow explizit (offline/low_battery im CONTEXT, aber nicht klar adressiert): 1
- Keine Nutzung des minimalen Kontexts (nur asset_osm vorhanden): 1
- Spekuliert über Steuergerät/Schaltschrank ohne Kontext-Basis: 1
- Erfindet Details zu Stromversorgung/Sicherungen ohne Hinweise: 1
- Keine Anpassung an fehlende Umgebungs-/Severity-Infos: 1
- Schwache Batterie des Geräts nicht explizit in Workflow integriert: 1
- Gerätebatterie-Status nicht in Workflow-Planung integriert: 1
- Keine Nutzung der Asset-ID im Kontext: 1
- Keine Erwähnung von Koordinaten/GPS (nicht im CONTEXT vorhanden): 1
- Unstrukturierter Kontext erschwert Nutzung: 1
- Offline-Workflow nicht erwartbar (kein Signal im CONTEXT): 1
- Offline-Workflow nicht explizit erwähnt, aber spotty connectivity im CONTEXT vorhanden: 1
