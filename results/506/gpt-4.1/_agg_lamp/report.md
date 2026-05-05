# Aggregation Report (506/gpt-4.1) [lamp]
- judge_version filter: **judge_v1_1**
- Tests (latest runs): **270**
- Incidents with any deltas: **30**

## Mean scores by context level (snapshot)
### L0 (n=30)
- mean runtime: 8.344866666666666
- mean R/H/S/D/K: 3.6333333333333333/3.8333333333333335/3.7/4.166666666666667/2.533333333333333
- mean overall (avg R/H/S/D/K): 3.5733333333333333
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.00, hallucination_suspected=0.03
### L2 (n=30)
- mean runtime: 11.568533333333333
- mean R/H/S/D/K: 4.966666666666667/4.933333333333334/4.9/4.933333333333334/4.5
- mean overall (avg R/H/S/D/K): 4.846666666666667
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.07, hallucination_suspected=0.00
### L2B (n=30)
- mean runtime: 11.496633333333333
- mean R/H/S/D/K: 5.0/5.0/4.933333333333334/5.0/5.0
- mean overall (avg R/H/S/D/K): 4.986666666666666
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.60, hallucination_suspected=0.00
### unknown (n=180)
- mean runtime: 11.102405555555556
- mean R/H/S/D/K: 4.7555555555555555/4.727777777777778/4.7444444444444445/4.872222222222222/4.716666666666667
- mean overall (avg R/H/S/D/K): 4.763333333333334
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.40, hallucination_suspected=0.00

## Mean scores by strategy (snapshot)
### S0 (n=30)
- mean runtime: 8.344866666666666
- mean R/H/S/D/K: 3.6333333333333333/3.8333333333333335/3.7/4.166666666666667/2.533333333333333
- mean overall (avg R/H/S/D/K): 3.5733333333333333
### S0_RAW (n=30)
- mean runtime: 10.817866666666667
- mean R/H/S/D/K: 4.633333333333334/4.6/4.666666666666667/4.866666666666666/4.533333333333333
- mean overall (avg R/H/S/D/K): 4.66
### S0_UNSTRUCTURED (n=30)
- mean runtime: 11.073633333333333
- mean R/H/S/D/K: 4.433333333333334/4.466666666666667/4.5/4.633333333333334/3.9
- mean overall (avg R/H/S/D/K): 4.386666666666667
### S1 (n=30)
- mean runtime: 11.568533333333333
- mean R/H/S/D/K: 4.966666666666667/4.933333333333334/4.9/4.933333333333334/4.5
- mean overall (avg R/H/S/D/K): 4.846666666666667
### S2 (n=30)
- mean runtime: 11.496633333333333
- mean R/H/S/D/K: 5.0/5.0/4.933333333333334/5.0/5.0
- mean overall (avg R/H/S/D/K): 4.986666666666666
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
- offline_workflow: 11
- offline_workflow_explicit: 5
- Kontextnutzung minimal (nur Asset-ID): 2
- Spezifische Stop-Conditions für Beobachtungsphase: 2
- Keine Nutzung des Kontexts (nur Asset-ID vorhanden): 2
- Offline-Workflow fehlt (spotty connectivity im Kontext): 2
- Klare Stop-Condition für Beobachtungsphase: 1
- Konkrete Zeitangabe für Wiederholungsprüfung: 1
- Explizite Stop-Condition für Beobachtungsphase: 1
- Offline-Workflow nicht erwähnt (Kontext zeigt nur asset_osm, kein device.connectivity): 1
- Sporadischer Fehler-Kontext (intermittent) nicht explizit adressiert: 1
- Offline-Workflow nicht explizit (trotz offline im Kontext): 1
- Feuchtigkeitsflecken nicht erwähnt: 1
- Nebel/poor_visibility nicht berücksichtigt: 1
- Intermittent-Fehler nicht spezifisch adressiert: 1
- Intermittent-Trigger nicht explizit diskutiert: 1
- Intermittent-Beobachtungsstrategie könnte detaillierter sein: 1
- Asset-ID/Mast-Nummer explizit erwähnen: 1
- Ticket-ID/Asset-ID explizit in Dokumentation: 1
- Asset-ID/OSM-ID explizit im Protokoll erwähnen: 1
