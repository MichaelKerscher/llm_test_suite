# Aggregation Report (506/gpt-4.1) [lamp]
- judge_version filter: **judge_v1_1**
- Tests (latest runs): **270**
- Incidents with any deltas: **30**

## Mean scores by context level (snapshot)
### L0 (n=30)
- mean runtime: 9.289233333333334
- mean R/H/S/D/K: 3.6/3.7/3.7666666666666666/4.033333333333333/2.466666666666667
- mean overall (avg R/H/S/D/K): 3.5133333333333336
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.00, hallucination_suspected=0.10
### L2 (n=30)
- mean runtime: 12.170766666666667
- mean R/H/S/D/K: 4.966666666666667/4.933333333333334/4.833333333333333/4.966666666666667/4.5
- mean overall (avg R/H/S/D/K): 4.84
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.10, hallucination_suspected=0.00
### L2B (n=30)
- mean runtime: 11.985866666666668
- mean R/H/S/D/K: 5.0/5.0/5.0/5.0/5.0
- mean overall (avg R/H/S/D/K): 5.0
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.60, hallucination_suspected=0.00
### unknown (n=180)
- mean runtime: 11.213227777777778
- mean R/H/S/D/K: 4.761111111111111/4.722222222222222/4.777777777777778/4.85/4.677777777777778
- mean overall (avg R/H/S/D/K): 4.757777777777777
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.40, hallucination_suspected=0.00

## Mean scores by strategy (snapshot)
### S0 (n=30)
- mean runtime: 9.289233333333334
- mean R/H/S/D/K: 3.6/3.7/3.7666666666666666/4.033333333333333/2.466666666666667
- mean overall (avg R/H/S/D/K): 3.5133333333333336
### S0_RAW (n=30)
- mean runtime: 11.2287
- mean R/H/S/D/K: 4.766666666666667/4.7/4.766666666666667/4.8/4.5
- mean overall (avg R/H/S/D/K): 4.706666666666666
### S0_UNSTRUCTURED (n=30)
- mean runtime: 11.327733333333333
- mean R/H/S/D/K: 4.333333333333333/4.333333333333333/4.6/4.566666666666666/3.7
- mean overall (avg R/H/S/D/K): 4.306666666666667
### S1 (n=30)
- mean runtime: 12.170766666666667
- mean R/H/S/D/K: 4.966666666666667/4.933333333333334/4.833333333333333/4.966666666666667/4.5
- mean overall (avg R/H/S/D/K): 4.84
### S2 (n=30)
- mean runtime: 11.985866666666668
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
- Offline-Workflow (nicht erwartbar, da CONTEXT kein connectivity-Signal enthält): 4
- Kontextnutzung minimal (nur Asset-ID): 3
- Keine Nutzung der Asset-ID im Kontext: 3
- Offline-Workflow explizit (spotty connectivity vorhanden, aber nicht klar adressiert): 2
- offline_workflow: 2
- Keine Nutzung des Kontexts (nur Asset-ID vorhanden): 2
- Spezifische Stop-Conditions für Beobachtungsphase: 2
- Offline-Workflow nicht erwähnt trotz 'spotty' connectivity: 2
- Offline-Workflow nicht erwähnt (spotty connectivity im CONTEXT): 2
- Klare Stop-Condition für Beobachtungsphase: 1
- Konkrete Zeitangabe für Wiederholungsprüfung: 1
- Explizite Stop-Condition für Beobachtungsphase: 1
- Offline-Workflow (Gerät offline nicht erwähnt): 1
- Safety-first nicht explizit Schritt 1 (erst nach Gerätehinweis): 1
- Eskalation könnte klarer priorisiert sein: 1
- Offline-Workflow nicht erwähnt (Gerät offline): 1
- Kontextnutzung teils spekulativ (low_battery als Lampen-Problem interpretiert): 1
- Kontextnutzung (Standort/Foto): 1
- Feuchtigkeitsflecken-Fokus: 1
- Nebel/Sicht-Risiko: 1
