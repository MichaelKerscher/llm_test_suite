# Aggregation Report (506/mistral-large) [signal]
- judge_version filter: **judge_v1_1**
- Tests (latest runs): **150**
- Incidents with any deltas: **30**

## Mean scores by context level (snapshot)
### L0 (n=30)
- mean runtime: 9.2927
- mean R/H/S/D/K: 3.7666666666666666/3.9/4.033333333333333/4.133333333333334/2.533333333333333
- mean overall (avg R/H/S/D/K): 3.6733333333333333
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.00, hallucination_suspected=0.40
### L2 (n=30)
- mean runtime: 12.109633333333333
- mean R/H/S/D/K: 4.866666666666666/4.833333333333333/4.866666666666666/4.933333333333334/4.6
- mean overall (avg R/H/S/D/K): 4.819999999999999
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.03, hallucination_suspected=0.00
### L2B (n=30)
- mean runtime: 10.9198
- mean R/H/S/D/K: 5.0/5.0/4.933333333333334/5.0/5.0
- mean overall (avg R/H/S/D/K): 4.986666666666666
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.53, hallucination_suspected=0.00
### unknown (n=60)
- mean runtime: 11.691566666666667
- mean R/H/S/D/K: 4.633333333333334/4.65/4.766666666666667/4.783333333333333/4.15
- mean overall (avg R/H/S/D/K): 4.596666666666667
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.22, hallucination_suspected=0.00

## Mean scores by strategy (snapshot)
### S0 (n=30)
- mean runtime: 9.2927
- mean R/H/S/D/K: 3.7666666666666666/3.9/4.033333333333333/4.133333333333334/2.533333333333333
- mean overall (avg R/H/S/D/K): 3.6733333333333333
### S0_RAW (n=30)
- mean runtime: 11.7024
- mean R/H/S/D/K: 4.8/4.766666666666667/4.8/4.9/4.4
- mean overall (avg R/H/S/D/K): 4.733333333333333
### S0_UNSTRUCTURED (n=30)
- mean runtime: 11.680733333333334
- mean R/H/S/D/K: 4.466666666666667/4.533333333333333/4.733333333333333/4.666666666666667/3.9
- mean overall (avg R/H/S/D/K): 4.46
### S1 (n=30)
- mean runtime: 12.109633333333333
- mean R/H/S/D/K: 4.866666666666666/4.833333333333333/4.866666666666666/4.933333333333334/4.6
- mean overall (avg R/H/S/D/K): 4.819999999999999
### S2 (n=30)
- mean runtime: 10.9198
- mean R/H/S/D/K: 5.0/5.0/4.933333333333334/5.0/5.0
- mean overall (avg R/H/S/D/K): 4.986666666666666

## Top missing elements (max 20)
- Kontextnutzung minimal (nur Asset-ID): 3
- Offline-Workflow nicht explizit (spotty connectivity vorhanden): 3
- Offline-Workflow (nicht erwartbar bei 'spotty'): 2
- Offline-Workflow nicht explizit (Kontext zeigt 'spotty', nicht offline): 2
- Offline-Workflow explizit (offline im Context, aber nicht klar adressiert): 2
- offline_workflow_explicit: 2
- Offline-Workflow explizit (nur implizit via Batterie-Check): 1
- Offline-Workflow explizit (Mobiltelefon/lokale Notizen): 1
- Offline-Workflow explizit erwähnen: 1
- Keine Nutzung der Asset-ID aus Context: 1
- Spekuliert über Steuergerät/Reset ohne Basis im Context: 1
- Erwähnt Polizei/Verkehrsregelung ohne Signal im Context: 1
- Keine Nutzung von Kontextinformationen (nur Asset-ID vorhanden): 1
- Keine Priorisierung nach Schweregrad (nicht im Context): 1
- Keine Anpassung an Umgebungsbedingungen (nicht im Context): 1
- Keine explizite Erwähnung des hohen Schweregrads in der Priorisierung: 1
- Offline-Workflow (nicht erwartbar, da kein Signal im CONTEXT): 1
- Spezifische Kontextnutzung (nur Asset-ID vorhanden): 1
- Halluzination: Annahmen über Asset-Typ (Straßenlampe/Ampel) ohne Basis: 1
- Offline-Workflow (nicht erwartbar, da 'instabil' nicht 'offline' ist): 1
