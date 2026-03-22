# Aggregation Report (506\mistral-large) [signal]
- judge_version filter: **judge_v1_1**
- Tests (latest runs): **90**
- Incidents with any deltas: **30**

## Mean scores by context level (snapshot)
### L0 (n=30)
- mean runtime: 6.351533333333333
- mean R/H/S/D/K: 3.7333333333333334/4.0/3.933333333333333/4.266666666666667/2.6666666666666665
- mean overall (avg R/H/S/D/K): 3.7199999999999998
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.00, hallucination_suspected=0.17
### L2 (n=30)
- mean runtime: 8.646433333333333
- mean R/H/S/D/K: 4.866666666666666/4.7/4.733333333333333/4.9/4.566666666666666
- mean overall (avg R/H/S/D/K): 4.753333333333333
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.10, hallucination_suspected=0.00
### L2B (n=30)
- mean runtime: 8.375966666666667
- mean R/H/S/D/K: 4.866666666666666/4.8/4.733333333333333/4.833333333333333/4.933333333333334
- mean overall (avg R/H/S/D/K): 4.833333333333333
- flags (rate): safety_first=0.97, escalation_present=1.00, offline_workflow_mentioned=0.60, hallucination_suspected=0.00

## Mean scores by strategy (snapshot)
### S0 (n=30)
- mean runtime: 6.351533333333333
- mean R/H/S/D/K: 3.7333333333333334/4.0/3.933333333333333/4.266666666666667/2.6666666666666665
- mean overall (avg R/H/S/D/K): 3.7199999999999998
### S1 (n=30)
- mean runtime: 8.646433333333333
- mean R/H/S/D/K: 4.866666666666666/4.7/4.733333333333333/4.9/4.566666666666666
- mean overall (avg R/H/S/D/K): 4.753333333333333
### S2 (n=30)
- mean runtime: 8.375966666666667
- mean R/H/S/D/K: 4.866666666666666/4.8/4.733333333333333/4.833333333333333/4.933333333333334
- mean overall (avg R/H/S/D/K): 4.833333333333333

## Top missing elements (max 20)
- Kontextnutzung minimal (nur Asset-ID): 4
- Offline-Workflow (nicht erwartbar bei L0_minimal): 2
- Offline-Workflow bei spotty connectivity nicht explizit erwähnt: 2
- Offline-Workflow (lokale Doku, spätere Sync): 1
- Keine Nutzung der GPS-Koordinaten (nicht im Context vorhanden): 1
- Keine Erwähnung des Foto-Status (nicht im Context vorhanden): 1
- Severity-angepasste Dringlichkeit (high severity nicht erkennbar im Kontext): 1
- Kreuzung ohne Regelung explizit erwähnen: 1
- Low_battery Hinweis könnte klarer als Geräte-Constraint formuliert sein: 1
- Keine Nutzung von Kontext-Signalen (rush_hour, high_traffic) trotz Verfügbarkeit: 1
- Keine Priorisierung basierend auf Verkehrsexposition: 1
- Keine explizite Erwähnung von GPS-Koordinaten in Dokumentation (obwohl vorhanden): 1
- Schwächere Ursachenhypothesen als TC2: 1
- Halluzinationen: Spannungsfreischaltung, Leuchtmittel/Optiken, Vorschaltgerät ohne Kontext: 1
- Keine Anpassung an sporadische Natur (intermittent) erkennbar: 1
- Offline-Workflow nicht erwähnt trotz spotty connectivity: 1
- Rückfrage zu Asset-Typ sinnvoll, aber nicht zwingend erwartet: 1
- GPS-Koordinaten (nicht im Context verfügbar): 1
- Spezifische Kontextnutzung (nur Asset-ID vorhanden): 1
- Severity-Bewusstsein (high nicht erkennbar): 1
