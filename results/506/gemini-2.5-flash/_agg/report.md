# Aggregation Report (506/gemini-2.5-flash)
- judge_version filter: **judge_v1_1**
- Tests (latest runs): **90**
- Incidents with any deltas: **30**

## Mean scores by context level (snapshot)
### L0 (n=30)
- mean runtime: 6.358033333333334
- mean R/H/S/D/K: 3.566666666666667/3.7666666666666666/3.7666666666666666/4.1/2.8
- mean overall (avg R/H/S/D/K): 3.6
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.00, hallucination_suspected=0.00
### L2 (n=30)
- mean runtime: 9.446433333333333
- mean R/H/S/D/K: 4.6/4.5/4.666666666666667/4.8/4.066666666666666
- mean overall (avg R/H/S/D/K): 4.526666666666667
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.10, hallucination_suspected=0.07
### L2B (n=30)
- mean runtime: 9.352066666666667
- mean R/H/S/D/K: 4.966666666666667/4.933333333333334/4.866666666666666/5.0/4.966666666666667
- mean overall (avg R/H/S/D/K): 4.946666666666667
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.60, hallucination_suspected=0.00

## Mean scores by strategy (snapshot)
### S0 (n=30)
- mean runtime: 6.358033333333334
- mean R/H/S/D/K: 3.566666666666667/3.7666666666666666/3.7666666666666666/4.1/2.8
- mean overall (avg R/H/S/D/K): 3.6
### S1 (n=30)
- mean runtime: 9.446433333333333
- mean R/H/S/D/K: 4.6/4.5/4.666666666666667/4.8/4.066666666666666
- mean overall (avg R/H/S/D/K): 4.526666666666667
### S2 (n=30)
- mean runtime: 9.352066666666667
- mean R/H/S/D/K: 4.966666666666667/4.933333333333334/4.866666666666666/5.0/4.966666666666667
- mean overall (avg R/H/S/D/K): 4.946666666666667

## Top missing elements (max 20)
- Offline-Workflow bei spotty connectivity: 3
- Kontextnutzung minimal (nur Asset-ID): 3
- Offline-Workflow (connectivity=offline): 2
- Keine Kontextnutzung (nur Asset-ID vorhanden): 2
- Klarstellung device.* = Techniker-Gerät: 1
- Offline-Workflow explizit (spotty connectivity): 1
- Keine Offline-Workflow-Erwähnung (nicht erwartbar bei minimalem Kontext): 1
- Offline-Workflow nicht explizit genannt trotz spotty connectivity: 1
- Keine klare Stop-Condition vor Eskalation: 1
- Offline-Workflow (device.connectivity=offline): 1
- Offline-Workflow (lokal dokumentieren/später sync): 1
- Keine Anpassung an fehlende Umgebungsdaten: 1
- Offline-Workflow nicht explizit (spotty connectivity): 1
- Keine Nutzung von Kontext-Signalen (nur Asset-ID vorhanden): 1
- Keine Erwähnung von Nebel/Sicht (nicht im Kontext): 1
- Annahme am Ende ('Die Leuchte ist eine Straßenlampe') ist leichte Spekulation, aber vertretbar: 1
- Offline-Workflow (spotty connectivity): 1
- Keine Nutzung des minimalen Kontexts (nur asset_osm vorhanden): 1
- Keine Anpassung an fehlende Umwelt-/Geräte-Infos: 1
- Generische Schritte ohne Kontextbezug: 1
