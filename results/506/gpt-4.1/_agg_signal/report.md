# Aggregation Report (506/gpt-4.1) [signal]
- judge_version filter: **judge_v1_1**
- Tests (latest runs): **150**
- Incidents with any deltas: **30**

## Mean scores by context level (snapshot)
### L0 (n=30)
- mean runtime: 8.2029
- mean R/H/S/D/K: 3.933333333333333/4.033333333333333/4.033333333333333/4.3/2.566666666666667
- mean overall (avg R/H/S/D/K): 3.7733333333333334
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.00, hallucination_suspected=0.27
### L2 (n=30)
- mean runtime: 10.449266666666666
- mean R/H/S/D/K: 4.9/4.833333333333333/4.833333333333333/4.9/4.6
- mean overall (avg R/H/S/D/K): 4.8133333333333335
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.17, hallucination_suspected=0.00
### L2B (n=30)
- mean runtime: 10.4326
- mean R/H/S/D/K: 4.966666666666667/4.933333333333334/4.9/4.933333333333334/4.966666666666667
- mean overall (avg R/H/S/D/K): 4.9399999999999995
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.50, hallucination_suspected=0.00
### unknown (n=60)
- mean runtime: 10.388883333333332
- mean R/H/S/D/K: 4.633333333333334/4.65/4.65/4.766666666666667/4.283333333333333
- mean overall (avg R/H/S/D/K): 4.596666666666667
- flags (rate): safety_first=0.98, escalation_present=1.00, offline_workflow_mentioned=0.23, hallucination_suspected=0.00

## Mean scores by strategy (snapshot)
### S0 (n=30)
- mean runtime: 8.2029
- mean R/H/S/D/K: 3.933333333333333/4.033333333333333/4.033333333333333/4.3/2.566666666666667
- mean overall (avg R/H/S/D/K): 3.7733333333333334
### S0_RAW (n=30)
- mean runtime: 10.629733333333332
- mean R/H/S/D/K: 4.866666666666666/4.866666666666666/4.833333333333333/4.933333333333334/4.633333333333334
- mean overall (avg R/H/S/D/K): 4.826666666666667
### S0_UNSTRUCTURED (n=30)
- mean runtime: 10.148033333333332
- mean R/H/S/D/K: 4.4/4.433333333333334/4.466666666666667/4.6/3.933333333333333
- mean overall (avg R/H/S/D/K): 4.366666666666666
### S1 (n=30)
- mean runtime: 10.449266666666666
- mean R/H/S/D/K: 4.9/4.833333333333333/4.833333333333333/4.9/4.6
- mean overall (avg R/H/S/D/K): 4.8133333333333335
### S2 (n=30)
- mean runtime: 10.4326
- mean R/H/S/D/K: 4.966666666666667/4.933333333333334/4.9/4.933333333333334/4.966666666666667
- mean overall (avg R/H/S/D/K): 4.9399999999999995

## Top missing elements (max 20)
- Offline-Workflow (nicht erwartbar, da connectivity nicht im CONTEXT): 3
- Kontextnutzung minimal (nur Asset-ID vorhanden): 3
- Offline-Workflow nicht explizit (spotty connectivity im Context): 2
- Offline-Workflow nicht erwähnt (aber auch nicht erwartbar bei L0_minimal): 2
- Safety-first nicht explizit als Schritt 1: 1
- Offline-Workflow (nicht erwartbar aus CONTEXT): 1
- Halluzinationen: Warndreieck, Warnblinkanlage, PSA-Annahme ohne Basis: 1
- Offline-Workflow nicht explizit (aber offline im CONTEXT): 1
- Offline-Workflow nicht explizit erwähnt (aber offline im CONTEXT): 1
- Kontextnutzung schwach (nur Asset-ID vorhanden, keine Nutzung von Umgebungsdaten): 1
- Polizei-Anforderung nicht explizit erwähnt (nur 'manuelle Verkehrsregelung durch geschultes Personal'): 1
- Severity-Bewusstsein (high nicht erkennbar): 1
- Umgebungsbedingungen (Wetter/Sicht fehlen im Context): 1
- GPS-Koordinaten nicht explizit in Doku erwähnt: 1
- Low_battery-Hinweis könnte klarer priorisiert werden: 1
- Keine Nutzung des Kontexts (nur Asset-ID vorhanden): 1
- Spekuliert über Fehlerprotokolle ohne Kontext-Basis: 1
- Erwähnt Steuergerät-Diagnose ohne Hinweis darauf im Kontext: 1
- Unstrukturierter Kontext erschwert vollständige Nutzung: 1
- Keine explizite Erwähnung der OSM-ID oder Koordinaten: 1
