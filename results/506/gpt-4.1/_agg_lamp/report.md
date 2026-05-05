# Aggregation Report (506/gpt-4.1) [lamp]
- judge_version filter: **judge_v1_1**
- Tests (latest runs): **270**
- Incidents with any deltas: **30**

## Mean scores by context level (snapshot)
### L0 (n=30)
- mean runtime: 8.483733333333333
- mean R/H/S/D/K: 3.5/3.7333333333333334/3.7333333333333334/3.966666666666667/2.466666666666667
- mean overall (avg R/H/S/D/K): 3.4799999999999995
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.00, hallucination_suspected=0.03
### L2 (n=30)
- mean runtime: 10.897433333333334
- mean R/H/S/D/K: 4.9/4.866666666666666/4.866666666666666/4.9/4.6
- mean overall (avg R/H/S/D/K): 4.826666666666667
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.07, hallucination_suspected=0.00
### L2B (n=30)
- mean runtime: 10.773933333333334
- mean R/H/S/D/K: 5.0/5.0/4.933333333333334/5.0/5.0
- mean overall (avg R/H/S/D/K): 4.986666666666666
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.60, hallucination_suspected=0.00
### unknown (n=180)
- mean runtime: 11.273355555555556
- mean R/H/S/D/K: 4.711111111111111/4.683333333333334/4.75/4.838888888888889/4.694444444444445
- mean overall (avg R/H/S/D/K): 4.735555555555555
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.41, hallucination_suspected=0.01

## Mean scores by strategy (snapshot)
### S0 (n=30)
- mean runtime: 8.483733333333333
- mean R/H/S/D/K: 3.5/3.7333333333333334/3.7333333333333334/3.966666666666667/2.466666666666667
- mean overall (avg R/H/S/D/K): 3.4799999999999995
### S0_RAW (n=30)
- mean runtime: 11.383933333333333
- mean R/H/S/D/K: 4.566666666666666/4.5/4.7/4.8/4.466666666666667
- mean overall (avg R/H/S/D/K): 4.6066666666666665
### S0_UNSTRUCTURED (n=30)
- mean runtime: 11.533266666666666
- mean R/H/S/D/K: 4.233333333333333/4.3/4.5/4.5/3.8333333333333335
- mean overall (avg R/H/S/D/K): 4.2733333333333325
### S1 (n=30)
- mean runtime: 10.897433333333334
- mean R/H/S/D/K: 4.9/4.866666666666666/4.866666666666666/4.9/4.6
- mean overall (avg R/H/S/D/K): 4.826666666666667
### S2 (n=30)
- mean runtime: 10.773933333333334
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
- Offline-Workflow (nicht erwartbar, da connectivity nicht im CONTEXT): 5
- Kontextnutzung minimal (nur Asset-ID): 4
- Offline-Workflow explizit (offline im CONTEXT, aber nicht klar adressiert): 4
- offline_workflow_explicit: 3
- Keine Erwähnung von Foto-Workflow (nicht im Kontext): 3
- Keine Nutzung des Kontexts (nur Asset-ID vorhanden): 2
- Offline-Workflow nicht erwähnt (spotty connectivity im CONTEXT vorhanden): 2
- Keine Berücksichtigung von Umgebungsbedingungen (nicht im CONTEXT): 2
- Spezifische Stop-Conditions für Beobachtungsphase: 2
- Kein expliziter Offline-Workflow trotz 'spotty' connectivity: 2
- Offline-Workflow nicht explizit (spotty connectivity im Kontext): 2
- Offline-Workflow trotz spotty connectivity: 2
- Klare Stop-Condition für Beobachtungsphase: 1
- Konkrete Zeitangabe für Wiederholungsprüfung: 1
- Explizite Stop-Condition für Beobachtungsphase: 1
- Offline-Workflow nicht explizit genannt: 1
- Offline-Workflow nicht explizit erwähnt trotz 'offline' im Kontext: 1
- Keine Erwähnung der Feuchtigkeitsflecken oder Fotobeschreibung: 1
- Keine Anpassung an Umgebungsbedingungen (Nebel, Nacht, poor visibility): 1
- Keine explizite Priorisierung der Feuchtigkeitsprüfung als Hauptverdacht: 1
