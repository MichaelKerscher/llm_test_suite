# Aggregation Report (506/gemini-2.5-flash) [signal]
- judge_version filter: **judge_v1_1**
- Tests (latest runs): **150**
- Incidents with any deltas: **30**

## Mean scores by context level (snapshot)
### L0 (n=30)
- mean runtime: 7.780266666666666
- mean R/H/S/D/K: 3.8/3.966666666666667/4.0/4.1/2.6333333333333333
- mean overall (avg R/H/S/D/K): 3.7
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.00, hallucination_suspected=0.27
### L2 (n=30)
- mean runtime: 10.7851
- mean R/H/S/D/K: 4.933333333333334/4.9/4.966666666666667/4.9/4.7
- mean overall (avg R/H/S/D/K): 4.88
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.30, hallucination_suspected=0.00
### L2B (n=30)
- mean runtime: 10.181266666666666
- mean R/H/S/D/K: 5.0/5.0/5.0/4.933333333333334/5.0
- mean overall (avg R/H/S/D/K): 4.986666666666666
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.53, hallucination_suspected=0.00
### unknown (n=60)
- mean runtime: 10.719600000000002
- mean R/H/S/D/K: 4.583333333333333/4.583333333333333/4.75/4.733333333333333/4.333333333333333
- mean overall (avg R/H/S/D/K): 4.596666666666667
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.25, hallucination_suspected=0.02

## Mean scores by strategy (snapshot)
### S0 (n=30)
- mean runtime: 7.780266666666666
- mean R/H/S/D/K: 3.8/3.966666666666667/4.0/4.1/2.6333333333333333
- mean overall (avg R/H/S/D/K): 3.7
### S0_RAW (n=30)
- mean runtime: 9.859066666666667
- mean R/H/S/D/K: 4.866666666666666/4.833333333333333/4.933333333333334/5.0/4.733333333333333
- mean overall (avg R/H/S/D/K): 4.873333333333333
### S0_UNSTRUCTURED (n=30)
- mean runtime: 11.580133333333333
- mean R/H/S/D/K: 4.3/4.333333333333333/4.566666666666666/4.466666666666667/3.933333333333333
- mean overall (avg R/H/S/D/K): 4.319999999999999
### S1 (n=30)
- mean runtime: 10.7851
- mean R/H/S/D/K: 4.933333333333334/4.9/4.966666666666667/4.9/4.7
- mean overall (avg R/H/S/D/K): 4.88
### S2 (n=30)
- mean runtime: 10.181266666666666
- mean R/H/S/D/K: 5.0/5.0/5.0/4.933333333333334/5.0
- mean overall (avg R/H/S/D/K): 4.986666666666666

## Top missing elements (max 20)
- offline_workflow: 4
- Offline-Workflow (nicht erwartbar, da connectivity nicht im CONTEXT): 4
- Kontext-Nutzung minimal (nur Asset-ID): 3
- Expliziter Offline-Workflow (trotz 'offline' im Kontext): 2
- Keine Nutzung der Asset-ID im Kontext: 2
- Offline-Workflow (nicht erwartbar, da CONTEXT kein connectivity-Signal enthält): 2
- Expliziter Offline-Workflow (offline im CONTEXT, aber nicht klar adressiert): 2
- Offline-Workflow (Kontext zeigt nur Asset-ID, keine Offline-Signale): 1
- Explizite GPS-Koordinaten in Dokumentation: 1
- Keine GPS-Koordinaten erwähnt (nicht im Context): 1
- Keine Foto-Dokumentation explizit gefordert: 1
- Keine Zeitstempel-Dokumentation: 1
- Foto-Dokumentation nicht explizit erwähnt (obwohl photo_available im Context): 1
- Keine Kontextnutzung (nur Asset-ID verfügbar): 1
- Keine Anpassung an Umgebungsbedingungen: 1
- Keine explizite Erwähnung der Batterie-Warnung für Gerät: 1
- Langzeitbeobachtung während Stoßzeit: 1
- Muster-Erkennung bei Ausfällen: 1
- Explizite Nutzung GPS-Koordinaten: 1
- Sporadizitäts-Muster (nur allgemein erwähnt): 1
