# Aggregation Report (506\gpt-4.1) [signal]
- judge_version filter: **judge_v1_1**
- Tests (latest runs): **90**
- Incidents with any deltas: **30**

## Mean scores by context level (snapshot)
### L0 (n=30)
- mean runtime: 6.761933333333333
- mean R/H/S/D/K: 3.8666666666666667/3.9/3.933333333333333/4.066666666666666/2.6666666666666665
- mean overall (avg R/H/S/D/K): 3.6866666666666665
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.00, hallucination_suspected=0.07
### L2 (n=30)
- mean runtime: 9.393733333333333
- mean R/H/S/D/K: 4.966666666666667/4.9/4.933333333333334/5.0/4.5
- mean overall (avg R/H/S/D/K): 4.86
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.13, hallucination_suspected=0.00
### L2B (n=30)
- mean runtime: 9.3431
- mean R/H/S/D/K: 5.0/4.933333333333334/4.966666666666667/4.966666666666667/4.933333333333334
- mean overall (avg R/H/S/D/K): 4.96
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.53, hallucination_suspected=0.00

## Mean scores by strategy (snapshot)
### S0 (n=30)
- mean runtime: 6.761933333333333
- mean R/H/S/D/K: 3.8666666666666667/3.9/3.933333333333333/4.066666666666666/2.6666666666666665
- mean overall (avg R/H/S/D/K): 3.6866666666666665
### S1 (n=30)
- mean runtime: 9.393733333333333
- mean R/H/S/D/K: 4.966666666666667/4.9/4.933333333333334/5.0/4.5
- mean overall (avg R/H/S/D/K): 4.86
### S2 (n=30)
- mean runtime: 9.3431
- mean R/H/S/D/K: 5.0/4.933333333333334/4.966666666666667/4.966666666666667/4.933333333333334
- mean overall (avg R/H/S/D/K): 4.96

## Top missing elements (max 20)
- Offline-Workflow (spotty connectivity): 3
- Kontextnutzung minimal (nur Asset-ID): 2
- Offline-Workflow (Gerät offline/low_battery): 1
- Offline-Workflow explizit erwähnen: 1
- Keine Nutzung der GPS-Koordinaten aus Context: 1
- Keine Erwähnung des Foto-Status trotz photo_available=true im vollen Context: 1
- Könnte photo_description expliziter nutzen für Dokumentation: 1
- severity/traffic context: 1
- weather/visibility conditions: 1
- photo_available flag: 1
- Keine Erwähnung der intermittierenden Natur des Fehlers: 1
- Keine Priorisierung der Beobachtung während Hauptverkehrszeit: 1
- Halluzination: Annahme 'Ampelgehäuse' ohne Basis: 1
- Keine Anpassung an fehlende Umgebungsdaten: 1
- Offline-Workflow nicht erwähnt trotz spotty connectivity: 1
- Annahme 'Straßenlampe' ist Spekulation, aber transparent gemacht: 1
- Keine Nutzung von severity=high aus Kontext: 1
- Keine Erwähnung von Regen/Wetter: 1
- Severity-angepasste Eskalation (high severity nicht erkennbar aus Kontext): 1
- Umgebungsbedingungen (Zeit/Wetter/Verkehr nicht im Kontext): 1
