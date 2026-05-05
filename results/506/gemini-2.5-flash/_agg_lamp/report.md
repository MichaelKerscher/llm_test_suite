# Aggregation Report (506/gemini-2.5-flash) [lamp]
- judge_version filter: **judge_v1_1**
- Tests (latest runs): **270**
- Incidents with any deltas: **30**

## Mean scores by context level (snapshot)
### L0 (n=30)
- mean runtime: 7.8415333333333335
- mean R/H/S/D/K: 3.5/3.7/3.7333333333333334/3.966666666666667/2.466666666666667
- mean overall (avg R/H/S/D/K): 3.4733333333333336
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.00, hallucination_suspected=0.07
### L2 (n=30)
- mean runtime: 10.780033333333334
- mean R/H/S/D/K: 4.9/4.9/4.933333333333334/4.966666666666667/4.533333333333333
- mean overall (avg R/H/S/D/K): 4.846666666666667
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.07, hallucination_suspected=0.00
### L2B (n=30)
- mean runtime: 10.553933333333333
- mean R/H/S/D/K: 5.0/5.0/5.0/5.0/5.0
- mean overall (avg R/H/S/D/K): 5.0
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.60, hallucination_suspected=0.00
### unknown (n=180)
- mean runtime: 9.718177777777777
- mean R/H/S/D/K: 4.716666666666667/4.716666666666667/4.772222222222222/4.822222222222222/4.633333333333334
- mean overall (avg R/H/S/D/K): 4.732222222222222
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.41, hallucination_suspected=0.01

## Mean scores by strategy (snapshot)
### S0 (n=30)
- mean runtime: 7.8415333333333335
- mean R/H/S/D/K: 3.5/3.7/3.7333333333333334/3.966666666666667/2.466666666666667
- mean overall (avg R/H/S/D/K): 3.4733333333333336
### S0_RAW (n=30)
- mean runtime: 10.396233333333333
- mean R/H/S/D/K: 4.533333333333333/4.5/4.7/4.7/4.3
- mean overall (avg R/H/S/D/K): 4.546666666666667
### S0_UNSTRUCTURED (n=30)
- mean runtime: 10.640566666666667
- mean R/H/S/D/K: 4.3/4.4/4.566666666666666/4.433333333333334/3.6333333333333333
- mean overall (avg R/H/S/D/K): 4.266666666666667
### S1 (n=30)
- mean runtime: 10.780033333333334
- mean R/H/S/D/K: 4.9/4.9/4.933333333333334/4.966666666666667/4.533333333333333
- mean overall (avg R/H/S/D/K): 4.846666666666667
### S2 (n=30)
- mean runtime: 10.553933333333333
- mean R/H/S/D/K: 5.0/5.0/5.0/5.0/5.0
- mean overall (avg R/H/S/D/K): 5.0
### S2_ABL_NOASSET (n=30)
- mean runtime: 9.480966666666665
- mean R/H/S/D/K: 4.9/4.933333333333334/4.866666666666666/4.966666666666667/5.0
- mean overall (avg R/H/S/D/K): 4.933333333333334
### S2_ABL_NODEV (n=30)
- mean runtime: 8.9771
- mean R/H/S/D/K: 4.933333333333334/4.866666666666666/4.866666666666666/5.0/5.0
- mean overall (avg R/H/S/D/K): 4.933333333333334
### S2_ABL_NOENV (n=30)
- mean runtime: 9.661033333333334
- mean R/H/S/D/K: 4.866666666666666/4.766666666666667/4.766666666666667/4.9/4.933333333333334
- mean overall (avg R/H/S/D/K): 4.846666666666667
### S2_ABL_NOINC (n=30)
- mean runtime: 9.153166666666667
- mean R/H/S/D/K: 4.766666666666667/4.833333333333333/4.866666666666666/4.933333333333334/4.933333333333334
- mean overall (avg R/H/S/D/K): 4.866666666666666

## Top missing elements (max 20)
- Keine Nutzung des Kontexts (nur Asset-ID vorhanden): 3
- offline_workflow: 3
- Keine Nutzung von Kontext (nur Asset-ID vorhanden): 2
- Offline-Workflow (erwartbar bei spotty connectivity + low_battery): 2
- Offline-Workflow explizit: 2
- Offline-Workflow nicht explizit erwähnt (obwohl 'offline' im CONTEXT steht): 2
- Kein expliziter Offline-Workflow trotz connectivity=spotty: 2
- Offline-Workflow nicht explizit erwähnt trotz spotty connectivity: 2
- Offline-Workflow explizit (offline im Context): 2
- Offline-Workflow (Gerät offline nicht erwähnt): 1
- Kontextnutzung minimal (nur Asset-ID): 1
- Batterie-Hinweis könnte klarer priorisiert sein: 1
- Offline-Workflow nicht explizit erwähnt (Gerät offline im Kontext): 1
- Keine Erwähnung von Feuchtigkeitsflecken oder Foto: 1
- Keine Anpassung an Umgebung (Nebel/Nacht/poor visibility): 1
- Keine explizite Stop-Condition bei Gefahr: 1
- Priorisierung könnte klarer sein: 1
- Unstrukturierter Kontext erschwert Parsing: 1
- Rückfrage am Ende ist gut, aber nicht zwingend nötig: 1
- Offline-Workflow (nicht erwartbar, da CONTEXT nur asset_osm enthält): 1
