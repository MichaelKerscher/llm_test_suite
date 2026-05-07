# Aggregation Report (506/mistral-large) [signal]
- judge_version filter: **judge_v1_1**
- Tests (latest runs): **150**
- Incidents with any deltas: **30**

## Mean scores by context level (snapshot)
### L0 (n=30)
- mean runtime: 8.2268
- mean R/H/S/D/K: 3.8666666666666667/3.966666666666667/4.166666666666667/4.1/2.566666666666667
- mean overall (avg R/H/S/D/K): 3.7333333333333334
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.00, hallucination_suspected=0.23
### L2 (n=30)
- mean runtime: 11.557266666666667
- mean R/H/S/D/K: 4.966666666666667/4.933333333333334/4.933333333333334/4.933333333333334/4.766666666666667
- mean overall (avg R/H/S/D/K): 4.906666666666666
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.13, hallucination_suspected=0.00
### L2B (n=30)
- mean runtime: 10.2663
- mean R/H/S/D/K: 4.933333333333334/4.933333333333334/4.933333333333334/4.966666666666667/4.966666666666667
- mean overall (avg R/H/S/D/K): 4.946666666666667
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.57, hallucination_suspected=0.00
### unknown (n=60)
- mean runtime: 11.799733333333334
- mean R/H/S/D/K: 4.633333333333334/4.666666666666667/4.8/4.75/4.266666666666667
- mean overall (avg R/H/S/D/K): 4.623333333333333
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.27, hallucination_suspected=0.03

## Mean scores by strategy (snapshot)
### S0 (n=30)
- mean runtime: 8.2268
- mean R/H/S/D/K: 3.8666666666666667/3.966666666666667/4.166666666666667/4.1/2.566666666666667
- mean overall (avg R/H/S/D/K): 3.7333333333333334
### S0_RAW (n=30)
- mean runtime: 11.077833333333333
- mean R/H/S/D/K: 4.833333333333333/4.833333333333333/4.9/4.9/4.7
- mean overall (avg R/H/S/D/K): 4.833333333333333
### S0_UNSTRUCTURED (n=30)
- mean runtime: 12.521633333333334
- mean R/H/S/D/K: 4.433333333333334/4.5/4.7/4.6/3.8333333333333335
- mean overall (avg R/H/S/D/K): 4.413333333333333
### S1 (n=30)
- mean runtime: 11.557266666666667
- mean R/H/S/D/K: 4.966666666666667/4.933333333333334/4.933333333333334/4.933333333333334/4.766666666666667
- mean overall (avg R/H/S/D/K): 4.906666666666666
### S2 (n=30)
- mean runtime: 10.2663
- mean R/H/S/D/K: 4.933333333333334/4.933333333333334/4.933333333333334/4.966666666666667/4.966666666666667
- mean overall (avg R/H/S/D/K): 4.946666666666667

## Top missing elements (max 20)
- offline_workflow: 4
- offline_workflow_explicit: 4
- Keine Nutzung der Asset-ID im Kontext: 3
- Offline-Workflow (nicht erwartbar aus minimalem Context): 2
- Offline-Workflow (spotty connectivity nicht explizit adressiert): 2
- Offline-Workflow (nicht erwartbar, da connectivity nicht im CONTEXT): 2
- Offline-Workflow (spotty connectivity im CONTEXT, aber nicht explizit erwähnt): 2
- Offline-Workflow nicht explizit erwähnt trotz 'offline' im Kontext: 1
- Offline-Workflow (nicht erwartbar, da connectivity nicht im Context): 1
- GPS-Koordinaten (nicht im Context vorhanden): 1
- Expliziter Offline-Workflow (offline im Context, aber nicht als Workflow adressiert): 1
- Expliziter Offline-Workflow (offline im Context, aber nicht klar adressiert): 1
- Keine GPS-Koordinaten genutzt (nur Asset-ID vorhanden): 1
- Keine Kontextnutzung bzgl. Foto/Bildbeschreibung (nicht im CONTEXT): 1
- Keine Kontextnutzung (nur Asset-ID vorhanden): 1
- Annahme 'Ampelanlage' ohne Bestätigung: 1
- Offline-Workflow nicht erwähnt, obwohl nicht erwartbar (kein Signal im CONTEXT): 1
- Offline-Workflow nicht explizit erwähnt, obwohl 'spotty' connectivity im CONTEXT: 1
- Offline-Workflow nicht explizit erwähnt, obwohl 'spotty' im CONTEXT steht: 1
- Kontext-Nutzung (Asset-ID wird nur bestätigt, keine weiteren Kontextdaten vorhanden): 1
