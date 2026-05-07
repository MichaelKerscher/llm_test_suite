# Aggregation Report (506/gemini-2.5-flash) [signal]
- judge_version filter: **judge_v1_1**
- Tests (latest runs): **150**
- Incidents with any deltas: **30**

## Mean scores by context level (snapshot)
### L0 (n=30)
- mean runtime: 8.768233333333335
- mean R/H/S/D/K: 3.9/3.966666666666667/4.133333333333334/4.333333333333333/2.6666666666666665
- mean overall (avg R/H/S/D/K): 3.8
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.00, hallucination_suspected=0.20
### L2 (n=30)
- mean runtime: 11.080866666666667
- mean R/H/S/D/K: 4.933333333333334/4.9/4.966666666666667/5.0/4.733333333333333
- mean overall (avg R/H/S/D/K): 4.906666666666666
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.20, hallucination_suspected=0.00
### L2B (n=30)
- mean runtime: 10.025433333333332
- mean R/H/S/D/K: 4.933333333333334/4.933333333333334/4.933333333333334/5.0/5.0
- mean overall (avg R/H/S/D/K): 4.96
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.53, hallucination_suspected=0.00
### unknown (n=60)
- mean runtime: 10.792666666666666
- mean R/H/S/D/K: 4.55/4.566666666666666/4.716666666666667/4.783333333333333/4.266666666666667
- mean overall (avg R/H/S/D/K): 4.576666666666667
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.25, hallucination_suspected=0.00

## Mean scores by strategy (snapshot)
### S0 (n=30)
- mean runtime: 8.768233333333335
- mean R/H/S/D/K: 3.9/3.966666666666667/4.133333333333334/4.333333333333333/2.6666666666666665
- mean overall (avg R/H/S/D/K): 3.8
### S0_RAW (n=30)
- mean runtime: 10.661233333333334
- mean R/H/S/D/K: 4.766666666666667/4.733333333333333/4.833333333333333/4.966666666666667/4.6
- mean overall (avg R/H/S/D/K): 4.78
### S0_UNSTRUCTURED (n=30)
- mean runtime: 10.924100000000001
- mean R/H/S/D/K: 4.333333333333333/4.4/4.6/4.6/3.933333333333333
- mean overall (avg R/H/S/D/K): 4.373333333333333
### S1 (n=30)
- mean runtime: 11.080866666666667
- mean R/H/S/D/K: 4.933333333333334/4.9/4.966666666666667/5.0/4.733333333333333
- mean overall (avg R/H/S/D/K): 4.906666666666666
### S2 (n=30)
- mean runtime: 10.025433333333332
- mean R/H/S/D/K: 4.933333333333334/4.933333333333334/4.933333333333334/5.0/5.0
- mean overall (avg R/H/S/D/K): 4.96

## Top missing elements (max 20)
- offline_workflow_explicit: 4
- Keine Nutzung der Asset-ID im Kontext: 3
- Offline-Workflow (nicht erwartbar, da connectivity nicht im CONTEXT): 2
- Offline-Workflow (spotty connectivity im CONTEXT, aber nicht explizit adressiert): 2
- Unstrukturierter Kontext nur teilweise genutzt: 2
- Offline-Workflow (spotty connectivity im CONTEXT, aber nicht explizit erwähnt): 2
- offline_workflow: 2
- Widerspruch 'ohne Anforderungstaster' vs. 'Tasterausfall' wird zwar erkannt, aber dominiert die Antwort zu stark: 1
- Offline-Workflow nicht explizit erwähnt trotz 'offline' im Kontext: 1
- Offline-Workflow nicht explizit erwähnt trotz connectivity=offline: 1
- Offline-Workflow nicht explizit erwähnt trotz connectivity=offline im Context: 1
- Langzeitbeobachtung während Stoßzeit explizit priorisiert: 1
- Fehlerprotokoll/Diagnose-Logs erwähnt aber nicht zentral: 1
- Kontext-Tokens teilweise kryptisch, aber Modell interpretiert korrekt: 1
- Wetter/Sicht-Anpassungen (nicht erwartbar): 1
- Keine Erwähnung von Offline-Workflow (aber nicht erwartbar, da CONTEXT minimal): 1
- Hinweis auf historischen Vorfall (Datum 17.01. vs. 07.05.) könnte klarer sein: 1
- Keine Erwähnung von Offline-Workflow (nicht erwartbar bei L0_minimal): 1
- Offline-Workflow nicht explizit erwähnt (spotty connectivity im Kontext): 1
- Keine GPS-Koordinaten dokumentiert (nur Asset-ID): 1
