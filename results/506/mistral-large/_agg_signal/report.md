# Aggregation Report (506/mistral-large) [signal]
- judge_version filter: **judge_v1_1**
- Tests (latest runs): **150**
- Incidents with any deltas: **30**

## Mean scores by context level (snapshot)
### L0 (n=30)
- mean runtime: 9.159533333333334
- mean R/H/S/D/K: 3.8666666666666667/3.933333333333333/4.033333333333333/4.166666666666667/2.566666666666667
- mean overall (avg R/H/S/D/K): 3.713333333333333
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.00, hallucination_suspected=0.37
### L2 (n=30)
- mean runtime: 11.845799999999999
- mean R/H/S/D/K: 4.866666666666666/4.766666666666667/4.9/4.866666666666666/4.6
- mean overall (avg R/H/S/D/K): 4.8
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.20, hallucination_suspected=0.00
### L2B (n=30)
- mean runtime: 10.954833333333333
- mean R/H/S/D/K: 5.0/4.933333333333334/5.0/4.9/5.0
- mean overall (avg R/H/S/D/K): 4.966666666666667
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.57, hallucination_suspected=0.00
### unknown (n=60)
- mean runtime: 11.925116666666668
- mean R/H/S/D/K: 4.566666666666666/4.533333333333333/4.8/4.683333333333334/4.2
- mean overall (avg R/H/S/D/K): 4.556666666666667
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.20, hallucination_suspected=0.00

## Mean scores by strategy (snapshot)
### S0 (n=30)
- mean runtime: 9.159533333333334
- mean R/H/S/D/K: 3.8666666666666667/3.933333333333333/4.033333333333333/4.166666666666667/2.566666666666667
- mean overall (avg R/H/S/D/K): 3.713333333333333
### S0_RAW (n=30)
- mean runtime: 11.598466666666667
- mean R/H/S/D/K: 4.866666666666666/4.866666666666666/4.933333333333334/4.933333333333334/4.6
- mean overall (avg R/H/S/D/K): 4.84
### S0_UNSTRUCTURED (n=30)
- mean runtime: 12.251766666666667
- mean R/H/S/D/K: 4.266666666666667/4.2/4.666666666666667/4.433333333333334/3.8
- mean overall (avg R/H/S/D/K): 4.2733333333333325
### S1 (n=30)
- mean runtime: 11.845799999999999
- mean R/H/S/D/K: 4.866666666666666/4.766666666666667/4.9/4.866666666666666/4.6
- mean overall (avg R/H/S/D/K): 4.8
### S2 (n=30)
- mean runtime: 10.954833333333333
- mean R/H/S/D/K: 5.0/4.933333333333334/5.0/4.9/5.0
- mean overall (avg R/H/S/D/K): 4.966666666666667

## Top missing elements (max 20)
- Kontext-Nutzung minimal (nur Asset-ID): 3
- Offline-Workflow (spotty connectivity): 3
- Offline-Workflow nicht explizit erwähnt: 2
- Keine Erwähnung von Umgebungsbedingungen (nicht im Context): 2
- Keine Nutzung der Asset-ID im Kontext: 2
- Keine Kontextnutzung erkennbar (nur Asset-ID vorhanden): 2
- offline_workflow: 2
- Offline-Workflow bei spotty connectivity: 2
- Kontextnutzung minimal (nur Asset-ID): 2
- offline_workflow_explicit: 2
- Offline-Workflow (nicht erwartbar aus minimalem Context): 1
- Spezifische Koordinaten (nicht im Context): 1
- Wetter/Sicht-Anpassungen (nicht im Context): 1
- Offline-Workflow explizit (Context zeigt offline): 1
- Offline-Workflow explizit (aber Context zeigt offline): 1
- Keine GPS-Koordinaten genutzt (im Context vorhanden): 1
- Keine Nutzung von fault_type/severity aus Context: 1
- Spekuliert über Detektoren/Induktionsschleifen ohne Basis: 1
- Asset-ID n444763520 nicht explizit in Dokumentation erwähnt: 1
- Kontextnutzung minimal (nur Asset-ID vorhanden): 1
