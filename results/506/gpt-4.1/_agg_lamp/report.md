# Aggregation Report (506/gpt-4.1) [lamp]
- judge_version filter: **judge_v1_1**
- Tests (latest runs): **270**
- Incidents with any deltas: **30**

## Mean scores by context level (snapshot)
### L0 (n=30)
- mean runtime: 8.6387
- mean R/H/S/D/K: 3.566666666666667/3.7/3.8666666666666667/3.966666666666667/2.5
- mean overall (avg R/H/S/D/K): 3.52
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.00, hallucination_suspected=0.13
### L2 (n=30)
- mean runtime: 12.154166666666667
- mean R/H/S/D/K: 4.833333333333333/4.766666666666667/4.8/4.8/4.366666666666666
- mean overall (avg R/H/S/D/K): 4.713333333333334
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.13, hallucination_suspected=0.03
### L2B (n=30)
- mean runtime: 12.873966666666666
- mean R/H/S/D/K: 5.0/5.0/5.0/5.0/5.0
- mean overall (avg R/H/S/D/K): 5.0
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.60, hallucination_suspected=0.00
### unknown (n=180)
- mean runtime: 11.29443888888889
- mean R/H/S/D/K: 4.727777777777778/4.705555555555556/4.7555555555555555/4.816666666666666/4.611111111111111
- mean overall (avg R/H/S/D/K): 4.723333333333334
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.39, hallucination_suspected=0.00

## Mean scores by strategy (snapshot)
### S0 (n=30)
- mean runtime: 8.6387
- mean R/H/S/D/K: 3.566666666666667/3.7/3.8666666666666667/3.966666666666667/2.5
- mean overall (avg R/H/S/D/K): 3.52
### S0_RAW (n=30)
- mean runtime: 11.345866666666666
- mean R/H/S/D/K: 4.6/4.566666666666666/4.666666666666667/4.7/4.266666666666667
- mean overall (avg R/H/S/D/K): 4.5600000000000005
### S0_UNSTRUCTURED (n=30)
- mean runtime: 11.697833333333334
- mean R/H/S/D/K: 4.3/4.366666666666666/4.566666666666666/4.466666666666667/3.533333333333333
- mean overall (avg R/H/S/D/K): 4.246666666666666
### S1 (n=30)
- mean runtime: 12.154166666666667
- mean R/H/S/D/K: 4.833333333333333/4.766666666666667/4.8/4.8/4.366666666666666
- mean overall (avg R/H/S/D/K): 4.713333333333334
### S2 (n=30)
- mean runtime: 12.873966666666666
- mean R/H/S/D/K: 5.0/5.0/5.0/5.0/5.0
- mean overall (avg R/H/S/D/K): 5.0
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
- Offline-Workflow bei spotty connectivity: 3
- Offline-Workflow nicht explizit erwähnt: 2
- Keine Nutzung der Asset-ID im Kontext: 2
- Offline-Workflow (nicht erwartbar, da connectivity nicht im CONTEXT): 2
- Offline-Workflow nicht explizit trotz 'spotty' connectivity: 2
- Spezifische Stop-Conditions für Beobachtungsphase: 2
- Keine Nutzung von Kontext-Signalen (nur Asset-ID vorhanden): 2
- Keine Priorisierung nach Severity (nicht im Context): 2
- Keine Nutzung des Kontexts (nur Asset-ID vorhanden): 2
- Offline-Workflow nicht erwähnt trotz 'spotty' im CONTEXT: 2
- Klare Stop-Condition für Beobachtungsphase: 1
- Konkrete Zeitangabe für Wiederholungsprüfung: 1
- Explizite Stop-Condition für Beobachtungsphase: 1
- Offline-Workflow (lokal speichern) nicht explizit: 1
- Keine Erwähnung von Umgebungsbedingungen (Nebel/Nacht): 1
- Keine Bezugnahme auf vorhandenes Foto: 1
- Standortname nicht explizit erwähnt: 1
- Asset-ID/Mast-Nummer explizit erwähnen: 1
- Ticket-ID/Asset-ID explizit in Dokumentation: 1
