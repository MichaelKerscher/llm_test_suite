# Aggregation Report (506/gemini-2.5-flash) [lamp]
- judge_version filter: **judge_v1_1**
- Tests (latest runs): **270**
- Incidents with any deltas: **30**

## Mean scores by context level (snapshot)
### L0 (n=30)
- mean runtime: 8.9197
- mean R/H/S/D/K: 3.533333333333333/3.7333333333333334/3.7666666666666666/4.0/2.566666666666667
- mean overall (avg R/H/S/D/K): 3.52
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.00, hallucination_suspected=0.07
### L2 (n=30)
- mean runtime: 10.648966666666666
- mean R/H/S/D/K: 4.966666666666667/4.933333333333334/4.966666666666667/5.0/4.533333333333333
- mean overall (avg R/H/S/D/K): 4.88
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.03, hallucination_suspected=0.00
### L2B (n=30)
- mean runtime: 11.350733333333332
- mean R/H/S/D/K: 5.0/5.0/5.0/5.0/5.0
- mean overall (avg R/H/S/D/K): 5.0
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.60, hallucination_suspected=0.00
### unknown (n=180)
- mean runtime: 9.803344444444445
- mean R/H/S/D/K: 4.705555555555556/4.711111111111111/4.783333333333333/4.861111111111111/4.694444444444445
- mean overall (avg R/H/S/D/K): 4.751111111111111
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.40, hallucination_suspected=0.01

## Mean scores by strategy (snapshot)
### S0 (n=30)
- mean runtime: 8.9197
- mean R/H/S/D/K: 3.533333333333333/3.7333333333333334/3.7666666666666666/4.0/2.566666666666667
- mean overall (avg R/H/S/D/K): 3.52
### S0_RAW (n=30)
- mean runtime: 10.965433333333333
- mean R/H/S/D/K: 4.566666666666666/4.533333333333333/4.7/4.833333333333333/4.5
- mean overall (avg R/H/S/D/K): 4.626666666666667
### S0_UNSTRUCTURED (n=30)
- mean runtime: 10.582366666666667
- mean R/H/S/D/K: 4.2/4.333333333333333/4.633333333333334/4.533333333333333/3.8
- mean overall (avg R/H/S/D/K): 4.3
### S1 (n=30)
- mean runtime: 10.648966666666666
- mean R/H/S/D/K: 4.966666666666667/4.933333333333334/4.966666666666667/5.0/4.533333333333333
- mean overall (avg R/H/S/D/K): 4.88
### S2 (n=30)
- mean runtime: 11.350733333333332
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
- offline_workflow: 5
- Offline-Workflow (nicht erwartbar, da connectivity nicht im CONTEXT): 4
- Kontextnutzung minimal (nur Asset-ID): 3
- Offline-Workflow nicht erwartbar (online): 3
- Offline-Workflow (spotty connectivity im CONTEXT, aber nicht explizit erwähnt): 2
- Offline-Workflow (spotty connectivity): 2
- Offline-Workflow nicht erwähnt (kein Signal im CONTEXT): 2
- Offline-Workflow explizit (offline im CONTEXT, aber nicht klar adressiert): 2
- Offline-Workflow nicht explizit (trotz connectivity=offline): 1
- Offline-Workflow nicht explizit (obwohl 'offline' im CONTEXT): 1
- Kontextnutzung (Standort, Foto, Nebel, Feuchtigkeitsflecken nicht erwähnt): 1
- Spezifische Diagnose für intermittierenden Fehler: 1
- Thermografie-Erwähnung (nicht im Kontext, aber plausibel): 1
- Explizite Ticket-ID-Erfassung: 1
- Zeitstempel-Dokumentation: 1
- Explizite Stop-Conditions für Abbruch: 1
- Keine Eskalations-Trigger für severity=high: 1
- Offline-Workflow nicht explizit erwähnt (trotz connectivity=offline im CONTEXT): 1
- Offline-Workflow nicht explizit erwähnt (trotz 'offline' im CONTEXT): 1
- Offline-Workflow (Gerät offline nicht erwähnt): 1
