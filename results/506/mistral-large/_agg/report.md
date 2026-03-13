# Aggregation Report (506/mistral-large)
- judge_version filter: **judge_v1_1**
- Tests (latest runs): **90**
- Incidents with any deltas: **30**

## Mean scores by context level (snapshot)
### L0 (n=30)
- mean runtime: 5.9969
- mean R/H/S/D/K: 3.566666666666667/3.9/3.7/4.033333333333333/2.9
- mean overall (avg R/H/S/D/K): 3.6199999999999997
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.00, hallucination_suspected=0.03
### L2 (n=30)
- mean runtime: 8.453933333333334
- mean R/H/S/D/K: 4.8/4.6/4.633333333333334/4.9/4.166666666666667
- mean overall (avg R/H/S/D/K): 4.62
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.07, hallucination_suspected=0.07
### L2B (n=30)
- mean runtime: 8.6692
- mean R/H/S/D/K: 4.933333333333334/4.866666666666666/4.666666666666667/4.966666666666667/4.966666666666667
- mean overall (avg R/H/S/D/K): 4.88
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.60, hallucination_suspected=0.00

## Mean scores by strategy (snapshot)
### S0 (n=30)
- mean runtime: 5.9969
- mean R/H/S/D/K: 3.566666666666667/3.9/3.7/4.033333333333333/2.9
- mean overall (avg R/H/S/D/K): 3.6199999999999997
### S1 (n=30)
- mean runtime: 8.453933333333334
- mean R/H/S/D/K: 4.8/4.6/4.633333333333334/4.9/4.166666666666667
- mean overall (avg R/H/S/D/K): 4.62
### S2 (n=30)
- mean runtime: 8.6692
- mean R/H/S/D/K: 4.933333333333334/4.866666666666666/4.666666666666667/4.966666666666667/4.966666666666667
- mean overall (avg R/H/S/D/K): 4.88

## Top missing elements (max 20)
- Offline-Workflow bei spotty connectivity: 4
- Offline-Workflow bei spotty connectivity nicht explizit erwähnt: 3
- Kein expliziter Offline-Workflow trotz connectivity=spotty: 2
- Kontextnutzung minimal (nur Asset-ID): 2
- Offline-Workflow (device.connectivity=offline): 1
- Klarstellung device.* = Techniker-Gerät: 1
- Keine Nutzung des minimalen Kontexts (nur asset_osm vorhanden): 1
- Generische Antwort ohne Bezug zu verfügbaren Daten: 1
- Offline-Workflow explizit (spotty connectivity): 1
- Offline-Workflow (lokal dokumentieren/später sync): 1
- Offline-Workflow (nicht erwartbar, da CONTEXT connectivity nicht zeigt): 1
- Sturm/Wetter-Kontext (nicht im CONTEXT vorhanden): 1
- Offline-Workflow nur erwähnt ('nicht möglich'), aber keine klare lokale Dokumentations-Anweisung: 1
- Offline-Workflow (connectivity=offline im Context): 1
- Keine Priorisierung nach severity (nicht im Context): 1
- Keine Berücksichtigung von Umgebungsbedingungen (nicht im Context): 1
- Keine Nutzung der Foto-Hinweise (nicht im Context): 1
- Keine Berücksichtigung von Wetter/Sicht (nicht im Context): 1
- Generische Antwort ohne spezifische Kontextanpassung: 1
- Keine Anpassung an Umgebung/Zeit/Wetter: 1
