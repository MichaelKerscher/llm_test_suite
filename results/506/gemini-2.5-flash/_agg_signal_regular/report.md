# Aggregation Report (506/gemini-2.5-flash) [signal]
- incident filter: **regular**
- Tests (latest runs): **150**
- Incidents with any deltas: **30**

## Mean scores by context level (snapshot)
### L0 (n=30)
- mean runtime: 10.094433333333335
- mean R/H/S/D/K: 3.8666666666666667/3.966666666666667/4.1/4.366666666666666/2.533333333333333
- mean overall (avg R/H/S/D/K): 3.7666666666666666
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.00, hallucination_suspected=0.30
### L2 (n=30)
- mean runtime: 11.4494
- mean R/H/S/D/K: 4.933333333333334/4.933333333333334/4.9/4.933333333333334/4.533333333333333
- mean overall (avg R/H/S/D/K): 4.846666666666667
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.17, hallucination_suspected=0.00
### L2B (n=30)
- mean runtime: 11.708033333333333
- mean R/H/S/D/K: 5.0/5.0/5.0/5.0/5.0
- mean overall (avg R/H/S/D/K): 5.0
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.63, hallucination_suspected=0.00
### unknown (n=60)
- mean runtime: 11.801966666666667
- mean R/H/S/D/K: 4.7/4.7/4.85/4.75/4.516666666666667
- mean overall (avg R/H/S/D/K): 4.703333333333333
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.27, hallucination_suspected=0.00

## Mean scores by strategy (snapshot)
### S0 (n=30)
- mean runtime: 10.094433333333335
- mean R/H/S/D/K: 3.8666666666666667/3.966666666666667/4.1/4.366666666666666/2.533333333333333
- mean overall (avg R/H/S/D/K): 3.7666666666666666
### S0_RAW (n=30)
- mean runtime: 11.915766666666666
- mean R/H/S/D/K: 4.933333333333334/4.933333333333334/4.933333333333334/4.966666666666667/4.833333333333333
- mean overall (avg R/H/S/D/K): 4.92
### S0_UNSTRUCTURED (n=30)
- mean runtime: 11.688166666666666
- mean R/H/S/D/K: 4.466666666666667/4.466666666666667/4.766666666666667/4.533333333333333/4.2
- mean overall (avg R/H/S/D/K): 4.486666666666666
### S1 (n=30)
- mean runtime: 11.4494
- mean R/H/S/D/K: 4.933333333333334/4.933333333333334/4.9/4.933333333333334/4.533333333333333
- mean overall (avg R/H/S/D/K): 4.846666666666667
### S2 (n=30)
- mean runtime: 11.708033333333333
- mean R/H/S/D/K: 5.0/5.0/5.0/5.0/5.0
- mean overall (avg R/H/S/D/K): 5.0

## Top missing elements (max 20)
- Kontextnutzung minimal (nur Asset-ID): 6
- Offline-Workflow (nicht erwartbar, da connectivity nicht im CONTEXT): 2
- Kontextnutzung minimal (nur Asset-ID vorhanden): 2
- Offline-Workflow (spotty connectivity im Kontext, aber nicht explizit erwähnt): 2
- Offline-Workflow nicht explizit (spotty connectivity vorhanden): 2
- Offline-Workflow nicht explizit (spotty/low_battery vorhanden): 2
- Offline-Workflow (spotty connectivity im CONTEXT, aber nicht explizit erwähnt): 2
- offline_workflow_explicit: 2
- Offline-Workflow nicht erwähnt (trotz connectivity=offline): 1
- Offline-Workflow nicht explizit (aber offline im CONTEXT): 1
- Keine Nutzung von Koordinaten/Umgebungsdaten (nicht vorhanden): 1
- Keine Erwähnung von Foto/Bildbeschreibung (nicht vorhanden): 1
- Unstrukturierter Kontext erschwert Nutzung, aber Modell extrahiert Kerninfos gut: 1
- Halluzinationen: Schaltkasten, Sicherungen, Brandgeruch ohne Kontext-Basis: 1
- Offline-Workflow nicht erwartbar (kein Signal im Context): 1
- Batterie-Interpretation könnte präziser sein (Gerät vs. Anlage): 1
- Batterie-Hinweis etwas spekulativ interpretiert: 1
- Keine Nutzung der Asset-ID im Kontext erkennbar: 1
- Keine Erwähnung der Intermittenz-Problematik: 1
- Unstrukturierter Kontext erschwert Nachvollziehbarkeit der Kontextnutzung leicht: 1
