# Aggregation Report (506/gpt-4.1) [lamp]
- judge_version filter: **judge_v1_1**
- Tests (latest runs): **270**
- Incidents with any deltas: **30**

## Mean scores by context level (snapshot)
### L0 (n=30)
- mean runtime: 8.687533333333333
- mean R/H/S/D/K: 3.6666666666666665/3.7666666666666666/3.8666666666666667/4.0/2.566666666666667
- mean overall (avg R/H/S/D/K): 3.5733333333333333
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.00, hallucination_suspected=0.13
### L2 (n=30)
- mean runtime: 11.5713
- mean R/H/S/D/K: 4.9/4.9/4.866666666666666/4.966666666666667/4.533333333333333
- mean overall (avg R/H/S/D/K): 4.833333333333333
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.07, hallucination_suspected=0.00
### L2B (n=30)
- mean runtime: 11.654866666666667
- mean R/H/S/D/K: 5.0/5.0/4.966666666666667/5.0/5.0
- mean overall (avg R/H/S/D/K): 4.993333333333334
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.60, hallucination_suspected=0.00
### unknown (n=180)
- mean runtime: 11.20985
- mean R/H/S/D/K: 4.772222222222222/4.722222222222222/4.761111111111111/4.844444444444444/4.711111111111111
- mean overall (avg R/H/S/D/K): 4.762222222222222
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.38, hallucination_suspected=0.00

## Mean scores by strategy (snapshot)
### S0 (n=30)
- mean runtime: 8.687533333333333
- mean R/H/S/D/K: 3.6666666666666665/3.7666666666666666/3.8666666666666667/4.0/2.566666666666667
- mean overall (avg R/H/S/D/K): 3.5733333333333333
### S0_RAW (n=30)
- mean runtime: 10.5782
- mean R/H/S/D/K: 4.666666666666667/4.6/4.766666666666667/4.766666666666667/4.466666666666667
- mean overall (avg R/H/S/D/K): 4.653333333333333
### S0_UNSTRUCTURED (n=30)
- mean runtime: 11.957966666666666
- mean R/H/S/D/K: 4.5/4.433333333333334/4.5/4.566666666666666/3.933333333333333
- mean overall (avg R/H/S/D/K): 4.386666666666667
### S1 (n=30)
- mean runtime: 11.5713
- mean R/H/S/D/K: 4.9/4.9/4.866666666666666/4.966666666666667/4.533333333333333
- mean overall (avg R/H/S/D/K): 4.833333333333333
### S2 (n=30)
- mean runtime: 11.654866666666667
- mean R/H/S/D/K: 5.0/5.0/4.966666666666667/5.0/5.0
- mean overall (avg R/H/S/D/K): 4.993333333333334
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
- Keine Nutzung des Kontexts (nur Asset-ID vorhanden): 3
- Offline-Workflow (nicht erwartbar, da CONTEXT kein connectivity-Signal enthält): 2
- Offline-Workflow bei spotty connectivity: 2
- Offline-Workflow explizit (offline-Signal vorhanden, aber nicht klar adressiert): 2
- Spezifische Stop-Conditions für Beobachtungsphase: 2
- Keine Nutzung von Kontext (nur Asset-ID vorhanden): 2
- Unstrukturierter Kontext erschwert Nutzung: 2
- Offline-Workflow nicht erwähnt (kein Signal im CONTEXT): 2
- Offline-Workflow bei 'spotty' connectivity nicht explizit erwähnt: 2
- offline_workflow: 2
- Offline-Workflow nicht explizit erwähnt (trotz 'offline' im CONTEXT): 2
- Offline-Workflow (spotty connectivity): 2
- Offline-Workflow (spotty connectivity im Kontext): 2
- Klare Stop-Condition für Beobachtungsphase: 1
- Konkrete Zeitangabe für Wiederholungsprüfung: 1
- Explizite Stop-Condition für Beobachtungsphase: 1
- Offline-Workflow nicht explizit genannt: 1
- Offline-Workflow nicht explizit erwähnt trotz offline-Signal: 1
- Keine Erwähnung von Feuchtigkeitsflecken oder Foto: 1
- Keine Anpassung an Umgebungsbedingungen: 1
