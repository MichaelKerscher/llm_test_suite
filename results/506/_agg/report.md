# Aggregation Report (506)
- judge_version filter: **judge_v1_1**
- Tests (latest runs): **90**
- Incidents with any deltas: **30**

## Mean scores by context level (snapshot)
### L0 (n=30)
- mean runtime: 4.081933333333334
- mean R/H/S/D/K: 3.433333333333333/3.433333333333333/3.066666666666667/3.7/2.7666666666666666
- mean overall (avg R/H/S/D/K): 3.2800000000000002
- flags (rate): safety_first=0.97, escalation_present=1.00, offline_workflow_mentioned=0.00, hallucination_suspected=0.00
### L2 (n=30)
- mean runtime: 4.565033333333333
- mean R/H/S/D/K: 4.633333333333334/4.266666666666667/4.2/4.533333333333333/3.933333333333333
- mean overall (avg R/H/S/D/K): 4.3133333333333335
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.20, hallucination_suspected=0.03
### L2B (n=30)
- mean runtime: 4.873866666666667
- mean R/H/S/D/K: 4.933333333333334/4.833333333333333/4.433333333333334/4.8/4.966666666666667
- mean overall (avg R/H/S/D/K): 4.793333333333334
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.67, hallucination_suspected=0.00

## Mean scores by strategy (snapshot)
### S0 (n=30)
- mean runtime: 4.081933333333334
- mean R/H/S/D/K: 3.433333333333333/3.433333333333333/3.066666666666667/3.7/2.7666666666666666
- mean overall (avg R/H/S/D/K): 3.2800000000000002
### S1 (n=30)
- mean runtime: 4.565033333333333
- mean R/H/S/D/K: 4.633333333333334/4.266666666666667/4.2/4.533333333333333/3.933333333333333
- mean overall (avg R/H/S/D/K): 4.3133333333333335
### S2 (n=30)
- mean runtime: 4.873866666666667
- mean R/H/S/D/K: 4.933333333333334/4.833333333333333/4.433333333333334/4.8/4.966666666666667
- mean overall (avg R/H/S/D/K): 4.793333333333334

## Top missing elements (max 20)
- Keine Nutzung der Asset-ID im Kontext: 2
- Keine explizite Stop-Condition bei Gefahr: 2
- Keine explizite Stop-Condition: 2
- Keine Nutzung von Kontext (nur Asset-ID): 2
- Offline-Workflow (lokal dokumentieren/Foto lokal speichern): 1
- Keine Berücksichtigung von Umgebungsfaktoren (nicht im Context): 1
- Generische Schritte ohne Fallspezifik: 1
- Keine Nutzung des Kontexts (nur Asset-ID vorhanden): 1
- Keine Anpassung an tatsächlich verfügbare Infos: 1
- Kein expliziter Offline-Workflow trotz connectivity=spotty: 1
- Batterie-Hinweis erwähnt, aber nicht klar als Geräte-Constraint kommuniziert: 1
- Keine Kontextnutzung (nur Asset-ID vorhanden): 1
- Keine Priorisierung nach Severity: 1
- Keine Anpassung an Umgebungsbedingungen: 1
- Offline-Workflow bei spotty connectivity nicht explizit erwähnt: 1
- Keine Kontextnutzung (minimaler Context nicht genutzt): 1
- Keine Anpassung an Umgebung/Zeit/Wetter (nicht verfügbar): 1
- Offline-Workflow nur angedeutet (Hinweis auf schlechte Konnektivität), aber nicht explizit als Handlungsschritt (lokal dokumentieren/später sync): 1
- Offline-Workflow nicht erwartbar (kein Signal im Context): 1
- Foto-Workflow nicht erwartbar (kein Signal im Context): 1
