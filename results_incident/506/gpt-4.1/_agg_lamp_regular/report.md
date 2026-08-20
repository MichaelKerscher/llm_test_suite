# Aggregation Report (506/gpt-4.1) [lamp]
- incident filter: **regular**
- Tests (latest runs): **150**
- Incidents with any deltas: **30**

## Mean scores by context level (snapshot)
### L0 (n=30)
- mean runtime: 6.545833333333333
- mean R/H/S/D/K: 3.566666666666667/3.7/3.7333333333333334/4.066666666666666/2.5
- mean overall (avg R/H/S/D/K): 3.5133333333333336
- flags (rate): safety_first=0.97, escalation_present=1.00, offline_workflow_mentioned=0.00, hallucination_suspected=0.03
### L2 (n=30)
- mean runtime: 8.862033333333333
- mean R/H/S/D/K: 4.866666666666666/4.766666666666667/4.8/4.833333333333333/4.466666666666667
- mean overall (avg R/H/S/D/K): 4.746666666666667
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.17, hallucination_suspected=0.00
### L2B (n=30)
- mean runtime: 10.0511
- mean R/H/S/D/K: 4.966666666666667/4.933333333333334/4.966666666666667/5.0/5.0
- mean overall (avg R/H/S/D/K): 4.973333333333333
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.60, hallucination_suspected=0.00
### unknown (n=60)
- mean runtime: 8.67065
- mean R/H/S/D/K: 4.466666666666667/4.416666666666667/4.516666666666667/4.7/4.1
- mean overall (avg R/H/S/D/K): 4.4399999999999995
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.30, hallucination_suspected=0.02

## Mean scores by strategy (snapshot)
### S0 (n=30)
- mean runtime: 6.545833333333333
- mean R/H/S/D/K: 3.566666666666667/3.7/3.7333333333333334/4.066666666666666/2.5
- mean overall (avg R/H/S/D/K): 3.5133333333333336
### S0_RAW (n=30)
- mean runtime: 8.194566666666667
- mean R/H/S/D/K: 4.6/4.5/4.566666666666666/4.833333333333333/4.433333333333334
- mean overall (avg R/H/S/D/K): 4.586666666666667
### S0_UNSTRUCTURED (n=30)
- mean runtime: 9.146733333333334
- mean R/H/S/D/K: 4.333333333333333/4.333333333333333/4.466666666666667/4.566666666666666/3.7666666666666666
- mean overall (avg R/H/S/D/K): 4.293333333333334
### S1 (n=30)
- mean runtime: 8.862033333333333
- mean R/H/S/D/K: 4.866666666666666/4.766666666666667/4.8/4.833333333333333/4.466666666666667
- mean overall (avg R/H/S/D/K): 4.746666666666667
### S2 (n=30)
- mean runtime: 10.0511
- mean R/H/S/D/K: 4.966666666666667/4.933333333333334/4.966666666666667/5.0/5.0
- mean overall (avg R/H/S/D/K): 4.973333333333333

## Top missing elements (max 20)
- Kontextnutzung minimal (nur Asset-ID): 2
- Keine Nutzung der Asset-ID im Kontext: 2
- Keine Priorisierung nach Severity/Traffic: 2
- Offline-Workflow explizit (spotty connectivity + low_power_mode): 2
- Keine Nutzung der Asset-ID im Kontext (nur minimal vorhanden): 2
- Offline-Workflow nicht explizit (spotty connectivity vorhanden): 2
- Offline-Workflow (spotty connectivity im CONTEXT, aber nicht explizit erwähnt): 2
- Offline-Workflow nicht explizit erwähnt trotz offline/low_battery: 1
- Kein Bezug zu Standort/Koordinaten (nicht im Context): 1
- Keine Erwähnung intermittent-Fehler (nicht im Context): 1
- Keine Nutzung von Foto/Umgebungsdaten (nicht vorhanden): 1
- Offline-Workflow (spotty connectivity → lokale Dokumentation nicht explizit): 1
- Offline-Workflow (spotty connectivity nicht explizit adressiert): 1
- Offline-Workflow bei spotty connectivity nicht explizit: 1
- Offline-Workflow bei spotty connectivity nicht explizit erwähnt: 1
- Keine Anpassung an Umgebung/Gerätezustand: 1
- Generische Antwort ohne spezifische Signale: 1
- Offline-Workflow nicht explizit (spotty connectivity): 1
- Offline-Workflow nicht erwähnt (spotty connectivity): 1
- Unstrukturierter Kontext teilweise nicht optimal genutzt: 1
