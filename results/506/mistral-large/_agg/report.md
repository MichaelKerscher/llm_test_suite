# Aggregation Report (506/mistral-large)
- judge_version filter: **judge_v1_1**
- Tests (latest runs): **90**
- Incidents with any deltas: **30**

## Mean scores by context level (snapshot)
### L0 (n=30)
- mean runtime: 6.248833333333334
- mean R/H/S/D/K: 3.5/3.9/3.8/4.166666666666667/2.9
- mean overall (avg R/H/S/D/K): 3.6533333333333333
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.00, hallucination_suspected=0.03
### L2 (n=30)
- mean runtime: 8.778566666666668
- mean R/H/S/D/K: 4.8/4.633333333333334/4.7/4.766666666666667/4.066666666666666
- mean overall (avg R/H/S/D/K): 4.593333333333334
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.07, hallucination_suspected=0.03
### L2B (n=30)
- mean runtime: 9.322933333333333
- mean R/H/S/D/K: 5.0/4.966666666666667/4.9/5.0/5.0
- mean overall (avg R/H/S/D/K): 4.973333333333333
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.60, hallucination_suspected=0.00

## Mean scores by strategy (snapshot)
### S0 (n=30)
- mean runtime: 6.248833333333334
- mean R/H/S/D/K: 3.5/3.9/3.8/4.166666666666667/2.9
- mean overall (avg R/H/S/D/K): 3.6533333333333333
### S1 (n=30)
- mean runtime: 8.778566666666668
- mean R/H/S/D/K: 4.8/4.633333333333334/4.7/4.766666666666667/4.066666666666666
- mean overall (avg R/H/S/D/K): 4.593333333333334
### S2 (n=30)
- mean runtime: 9.322933333333333
- mean R/H/S/D/K: 5.0/4.966666666666667/4.9/5.0/5.0
- mean overall (avg R/H/S/D/K): 4.973333333333333

## Top missing elements (max 20)
- Offline-Workflow bei spotty connectivity: 6
- Offline-Workflow (connectivity=offline): 2
- Offline-Workflow bei spotty connectivity nicht explizit erwähnt: 2
- Offline-Workflow explizit (connectivity=offline): 1
- Explizite Erwähnung low_battery-Implikationen: 1
- Offline-Workflow (connectivity=offline, device_state=low_battery): 1
- Offline-Workflow (Kontext zeigt keine connectivity-Info): 1
- Foto-Nutzung (nicht erwähnt, obwohl plausibel): 1
- Spezifische Kontaktprüfung am Anschlusskabel: 1
- Offline-Workflow explizit (connectivity=offline im Kontext): 1
- GPS-Koordinaten in Doku: 1
- Intermittent-Fehler-Strategie (längere Beobachtung): 1
- Kontextnutzung minimal (nur Asset-ID): 1
- Keine explizite Priorisierung bei severity=high erkennbar: 1
- Keine Nutzung der GPS-Koordinaten aus CONTEXT: 1
- GPS-Koordinaten nicht explizit in Dokumentation erwähnt: 1
- Keine Nutzung der verfügbaren Asset-ID im Kontext: 1
- Keine Erwähnung von Umgebungsbedingungen (nicht im Kontext vorhanden): 1
- Keine Nutzung des minimalen Kontexts (nur asset_osm vorhanden): 1
- Viele Details ohne Kontextbasis (z.B. Ampelausfall, Wassereintritt, Bauarbeiten): 1
