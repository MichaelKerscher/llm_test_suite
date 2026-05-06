# Aggregation Report (506/gpt-4.1) [signal]
- judge_version filter: **judge_v1_1**
- Tests (latest runs): **150**
- Incidents with any deltas: **30**

## Mean scores by context level (snapshot)
### L0 (n=30)
- mean runtime: 8.053266666666667
- mean R/H/S/D/K: 3.7333333333333334/3.9/3.8333333333333335/4.2/2.3333333333333335
- mean overall (avg R/H/S/D/K): 3.6
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.00, hallucination_suspected=0.27
### L2 (n=30)
- mean runtime: 10.277700000000001
- mean R/H/S/D/K: 4.9/4.866666666666666/4.766666666666667/4.966666666666667/4.733333333333333
- mean overall (avg R/H/S/D/K): 4.846666666666667
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.20, hallucination_suspected=0.00
### L2B (n=30)
- mean runtime: 10.118033333333333
- mean R/H/S/D/K: 4.966666666666667/4.966666666666667/4.933333333333334/5.0/5.0
- mean overall (avg R/H/S/D/K): 4.973333333333333
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.53, hallucination_suspected=0.00
### unknown (n=60)
- mean runtime: 10.072383333333333
- mean R/H/S/D/K: 4.55/4.566666666666666/4.633333333333334/4.733333333333333/4.266666666666667
- mean overall (avg R/H/S/D/K): 4.55
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.25, hallucination_suspected=0.00

## Mean scores by strategy (snapshot)
### S0 (n=30)
- mean runtime: 8.053266666666667
- mean R/H/S/D/K: 3.7333333333333334/3.9/3.8333333333333335/4.2/2.3333333333333335
- mean overall (avg R/H/S/D/K): 3.6
### S0_RAW (n=30)
- mean runtime: 10.374533333333334
- mean R/H/S/D/K: 4.8/4.8/4.766666666666667/4.966666666666667/4.666666666666667
- mean overall (avg R/H/S/D/K): 4.8
### S0_UNSTRUCTURED (n=30)
- mean runtime: 9.770233333333332
- mean R/H/S/D/K: 4.3/4.333333333333333/4.5/4.5/3.8666666666666667
- mean overall (avg R/H/S/D/K): 4.3
### S1 (n=30)
- mean runtime: 10.277700000000001
- mean R/H/S/D/K: 4.9/4.866666666666666/4.766666666666667/4.966666666666667/4.733333333333333
- mean overall (avg R/H/S/D/K): 4.846666666666667
### S2 (n=30)
- mean runtime: 10.118033333333333
- mean R/H/S/D/K: 4.966666666666667/4.966666666666667/4.933333333333334/5.0/5.0
- mean overall (avg R/H/S/D/K): 4.973333333333333

## Top missing elements (max 20)
- Keine Nutzung der Asset-ID im Kontext: 4
- offline_workflow: 4
- Offline-Workflow nicht explizit erwähnt: 2
- Unstrukturierter Kontext nur teilweise genutzt: 2
- Offline-Workflow bei spotty connectivity nicht explizit erwähnt: 2
- Kontextnutzung minimal (nur Asset-ID): 2
- Unstrukturierter Kontext erschwert Nutzung: 2
- Offline-Workflow explizit erwähnen: 1
- Keine Erwähnung der Hauptverkehrszeit als Eskalationstrigger: 1
- Keine explizite Erwähnung des Fotos: 1
- Intermittierender Fehler nicht explizit adressiert: 1
- Hauptverkehrszeit-Kontext nicht genutzt: 1
- Keine Priorisierung auf Beobachtung während Stoßzeit: 1
- Keine explizite Erwähnung von 'medium severity' in Priorisierung: 1
- Keine Nutzung des Kontexts (nur Asset-ID vorhanden): 1
- Keine Anpassung an sporadische Störung erkennbar: 1
- Generische Checkliste ohne Fallbezug: 1
- Kein Offline-Workflow trotz 'spotty' connectivity: 1
- Offline-Workflow (nicht erwartbar, da CONTEXT minimal): 1
- Offline-Workflow (spotty connectivity im CONTEXT, aber nicht explizit adressiert): 1
