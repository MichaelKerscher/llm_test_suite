# Aggregation Report (506/gemini-2.5-flash) [signal]
- judge_version filter: **judge_v1_1**
- Tests (latest runs): **150**
- Incidents with any deltas: **30**

## Mean scores by context level (snapshot)
### L0 (n=30)
- mean runtime: 8.631566666666666
- mean R/H/S/D/K: 3.8666666666666667/3.933333333333333/4.166666666666667/4.066666666666666/2.6333333333333333
- mean overall (avg R/H/S/D/K): 3.7333333333333334
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.00, hallucination_suspected=0.20
### L2 (n=30)
- mean runtime: 10.602033333333333
- mean R/H/S/D/K: 4.933333333333334/4.9/4.8/4.933333333333334/4.633333333333334
- mean overall (avg R/H/S/D/K): 4.84
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.03, hallucination_suspected=0.00
### L2B (n=30)
- mean runtime: 10.417133333333334
- mean R/H/S/D/K: 5.0/5.0/4.9/4.966666666666667/5.0
- mean overall (avg R/H/S/D/K): 4.973333333333333
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.50, hallucination_suspected=0.00
### unknown (n=60)
- mean runtime: 11.286683333333334
- mean R/H/S/D/K: 4.516666666666667/4.566666666666666/4.766666666666667/4.616666666666666/4.233333333333333
- mean overall (avg R/H/S/D/K): 4.54
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.25, hallucination_suspected=0.03

## Mean scores by strategy (snapshot)
### S0 (n=30)
- mean runtime: 8.631566666666666
- mean R/H/S/D/K: 3.8666666666666667/3.933333333333333/4.166666666666667/4.066666666666666/2.6333333333333333
- mean overall (avg R/H/S/D/K): 3.7333333333333334
### S0_RAW (n=30)
- mean runtime: 11.182799999999999
- mean R/H/S/D/K: 4.766666666666667/4.8/4.833333333333333/4.833333333333333/4.533333333333333
- mean overall (avg R/H/S/D/K): 4.753333333333333
### S0_UNSTRUCTURED (n=30)
- mean runtime: 11.390566666666667
- mean R/H/S/D/K: 4.266666666666667/4.333333333333333/4.7/4.4/3.933333333333333
- mean overall (avg R/H/S/D/K): 4.326666666666667
### S1 (n=30)
- mean runtime: 10.602033333333333
- mean R/H/S/D/K: 4.933333333333334/4.9/4.8/4.933333333333334/4.633333333333334
- mean overall (avg R/H/S/D/K): 4.84
### S2 (n=30)
- mean runtime: 10.417133333333334
- mean R/H/S/D/K: 5.0/5.0/4.9/4.966666666666667/5.0
- mean overall (avg R/H/S/D/K): 4.973333333333333

## Top missing elements (max 20)
- offline_workflow: 6
- offline_workflow_explicit: 3
- Offline-Workflow (spotty connectivity): 3
- Offline-Workflow (nicht erwartbar, da CONTEXT kein offline-Signal enthält): 2
- Kontextnutzung minimal (nur Asset-ID verwendet): 1
- Offline-Workflow nicht explizit erwähnt (obwohl offline + low_battery im CONTEXT): 1
- Offline-Workflow nicht explizit erwähnt (obwohl offline im CONTEXT steht): 1
- Offline-Workflow (nicht erwartbar, da CONTEXT kein connectivity-Signal enthält): 1
- Konkrete GPS-Koordinaten (nicht im CONTEXT vorhanden): 1
- Keine GPS-Koordinaten erwähnt (nicht im Context): 1
- Keine Foto-Dokumentation explizit gefordert (nur allgemein): 1
- Asset-ID nicht explizit in Dokumentation genannt: 1
- Keine klare Priorisierung bei intermittierendem Fehler (Beobachtung vs. Eskalation): 1
- Keine Erwähnung von Verkehrsregelung bei erneutem Ausfall: 1
- Keine explizite Erwähnung von Verkehrsregelung bei erneutem Ausfall während Beobachtung: 1
- Kontext-Nutzung etwas schwächer (unstrukturierter Text nicht vollständig ausgeschöpft): 1
- Offline-Workflow (nicht erwartbar, da connectivity nicht im CONTEXT): 1
- Sporadisches Muster-Erkennung (erwähnt, aber nicht priorisiert): 1
- Wetter/Sicht-Bezug (nicht erwartbar, da nicht im CONTEXT): 1
- Offline-Workflow explizit (connectivity=spotty im CONTEXT, aber nur indirekt erwähnt): 1
