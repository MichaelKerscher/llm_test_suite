# Aggregation Report (506/gpt-4.1) [lamp]
- judge_version filter: **judge_v1_1**
- Tests (latest runs): **270**
- Incidents with any deltas: **30**

## Mean scores by context level (snapshot)
### L0 (n=30)
- mean runtime: 8.201699999999999
- mean R/H/S/D/K: 3.6/3.7666666666666666/3.6333333333333333/3.966666666666667/2.5
- mean overall (avg R/H/S/D/K): 3.493333333333333
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.00, hallucination_suspected=0.07
### L2 (n=30)
- mean runtime: 10.952966666666667
- mean R/H/S/D/K: 4.966666666666667/4.9/4.866666666666666/4.966666666666667/4.633333333333334
- mean overall (avg R/H/S/D/K): 4.866666666666666
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.13, hallucination_suspected=0.00
### L2B (n=30)
- mean runtime: 11.349866666666665
- mean R/H/S/D/K: 5.0/4.933333333333334/4.933333333333334/5.0/5.0
- mean overall (avg R/H/S/D/K): 4.973333333333333
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.60, hallucination_suspected=0.00
### unknown (n=180)
- mean runtime: 11.065138888888889
- mean R/H/S/D/K: 4.7555555555555555/4.7/4.761111111111111/4.855555555555555/4.722222222222222
- mean overall (avg R/H/S/D/K): 4.758888888888889
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.39, hallucination_suspected=0.00

## Mean scores by strategy (snapshot)
### S0 (n=30)
- mean runtime: 8.201699999999999
- mean R/H/S/D/K: 3.6/3.7666666666666666/3.6333333333333333/3.966666666666667/2.5
- mean overall (avg R/H/S/D/K): 3.493333333333333
### S0_RAW (n=30)
- mean runtime: 10.673633333333333
- mean R/H/S/D/K: 4.7/4.6/4.733333333333333/4.833333333333333/4.566666666666666
- mean overall (avg R/H/S/D/K): 4.6866666666666665
### S0_UNSTRUCTURED (n=30)
- mean runtime: 10.994266666666666
- mean R/H/S/D/K: 4.366666666666666/4.3/4.533333333333333/4.566666666666666/3.9
- mean overall (avg R/H/S/D/K): 4.333333333333333
### S1 (n=30)
- mean runtime: 10.952966666666667
- mean R/H/S/D/K: 4.966666666666667/4.9/4.866666666666666/4.966666666666667/4.633333333333334
- mean overall (avg R/H/S/D/K): 4.866666666666666
### S2 (n=30)
- mean runtime: 11.349866666666665
- mean R/H/S/D/K: 5.0/4.933333333333334/4.933333333333334/5.0/5.0
- mean overall (avg R/H/S/D/K): 4.973333333333333
### S2_ABL_NOASSET (n=30)
- mean runtime: 10.9962
- mean R/H/S/D/K: 4.9/4.933333333333334/4.933333333333334/4.9/4.966666666666667
- mean overall (avg R/H/S/D/K): 4.926666666666667
### S2_ABL_NODEV (n=30)
- mean runtime: 10.410633333333333
- mean R/H/S/D/K: 4.933333333333334/4.8/4.766666666666667/4.933333333333334/4.966666666666667
- mean overall (avg R/H/S/D/K): 4.88
### S2_ABL_NOENV (n=30)
- mean runtime: 11.9838
- mean R/H/S/D/K: 4.8/4.666666666666667/4.7/4.9/4.966666666666667
- mean overall (avg R/H/S/D/K): 4.806666666666667
### S2_ABL_NOINC (n=30)
- mean runtime: 11.3323
- mean R/H/S/D/K: 4.833333333333333/4.9/4.9/5.0/4.966666666666667
- mean overall (avg R/H/S/D/K): 4.92

## Top missing elements (max 20)
- offline_workflow: 5
- Offline-Workflow (erwartbar wegen spotty connectivity, aber nicht explizit genannt): 2
- Offline-Workflow nicht explizit (trotz 'offline' im Kontext): 2
- Keine Kontextnutzung erkennbar (nur Asset-ID vorhanden): 2
- Spezifische Stop-Conditions für Beobachtungsphase: 2
- Offline-Workflow explizit (connectivity=spotty, aber nicht offline → nicht zwingend): 2
- Offline-Workflow (nicht erwartbar, da connectivity nicht im CONTEXT): 2
- Klare Stop-Condition für Beobachtungsphase: 1
- Konkrete Zeitangabe für Wiederholungsprüfung: 1
- Explizite Stop-Condition für Beobachtungsphase: 1
- Offline-Workflow nicht erwähnt (Kontext zeigt nur asset_osm, kein device.connectivity): 1
- Offline-Workflow nicht explizit (trotz device.connectivity=offline im Kontext): 1
- Offline-Workflow nicht explizit erwähnt trotz 'offline' im Kontext: 1
- Feuchtigkeitsflecken nicht erwähnt: 1
- Nebel/poor_visibility nicht berücksichtigt: 1
- Foto-Hinweis fehlt: 1
- Unstrukturierter Kontext erschwert Parsing: 1
- Asset-ID/Mast-Nummer explizit erwähnen: 1
- Ticket-ID/Asset-ID explizit in Dokumentation: 1
- Asset-ID/OSM-ID explizit im Protokoll erwähnen: 1
