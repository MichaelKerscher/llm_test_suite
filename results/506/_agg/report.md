# Aggregation Report (506)
- judge_version filter: **judge_v1_1**
- Tests (latest runs): **90**
- Incidents with any deltas: **30**

## Mean scores by context level (snapshot)
### L0 (n=30)
- mean runtime: 4.020966666666667
- mean R/H/S/D/K: 3.433333333333333/3.466666666666667/3.1666666666666665/3.7666666666666666/2.6666666666666665
- mean overall (avg R/H/S/D/K): 3.3
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.00, hallucination_suspected=0.07
### L2 (n=30)
- mean runtime: 4.362366666666667
- mean R/H/S/D/K: 4.7/4.433333333333334/4.4/4.533333333333333/3.6666666666666665
- mean overall (avg R/H/S/D/K): 4.346666666666667
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.10, hallucination_suspected=0.10
### L2B (n=30)
- mean runtime: 4.768866666666667
- mean R/H/S/D/K: 4.933333333333334/4.933333333333334/4.566666666666666/4.9/5.0
- mean overall (avg R/H/S/D/K): 4.866666666666666
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.60, hallucination_suspected=0.00

## Mean scores by strategy (snapshot)
### S0 (n=30)
- mean runtime: 4.020966666666667
- mean R/H/S/D/K: 3.433333333333333/3.466666666666667/3.1666666666666665/3.7666666666666666/2.6666666666666665
- mean overall (avg R/H/S/D/K): 3.3
### S1 (n=30)
- mean runtime: 4.362366666666667
- mean R/H/S/D/K: 4.7/4.433333333333334/4.4/4.533333333333333/3.6666666666666665
- mean overall (avg R/H/S/D/K): 4.346666666666667
### S2 (n=30)
- mean runtime: 4.768866666666667
- mean R/H/S/D/K: 4.933333333333334/4.933333333333334/4.566666666666666/4.9/5.0
- mean overall (avg R/H/S/D/K): 4.866666666666666

## Top missing elements (max 20)
- Keine Nutzung der Asset-ID im Kontext: 2
- Generische Antwort ohne Fallbezug: 2
- Offline-Workflow bei spotty connectivity: 2
- Offline-Workflow (nicht erwartbar, da connectivity nicht im Context): 2
- Offline-Workflow (Gerät offline, low_battery): 1
- Keine Klarstellung: device.* = Techniker-Gerät, nicht Asset: 1
- Keine Priorisierung auf intermittent fault: 1
- Offline-Workflow (spotty connectivity): 1
- Keine Halluzination: 'Akku leer' bei Asset: 1
- Keine Kontextnutzung (minimaler Context): 1
- Keine Priorisierung nach Severity: 1
- Keine Anpassung an Umgebungsbedingungen: 1
- Kein expliziter Offline-Workflow trotz spotty connectivity: 1
- Low_battery nicht als Handlungseinschränkung adressiert: 1
- Offline-Workflow (nicht erwartbar, da kein Signal im Kontext): 1
- Wetter-/Verkehrsrisiko (nicht erwartbar): 1
- Foto-Workflow (nicht erwartbar): 1
- Offline-Workflow explizit (Gerät offline, Batterie schwach → lokale Doku/Sync fehlt): 1
- Foto lokal speichern (photo_available=true, aber kein Offline-Hinweis): 1
- Offline-Workflow (Kontext zeigt connectivity=offline, aber nicht erwähnt): 1
