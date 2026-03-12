# Aggregation Report (506)
- judge_version filter: **judge_v1_1**
- Tests (latest runs): **90**
- Incidents with any deltas: **30**

## Mean scores by context level (snapshot)
### L0 (n=30)
- mean runtime: 4.074133333333333
- mean R/H/S/D/K: 3.466666666666667/3.5/2.8666666666666667/3.6666666666666665/2.8333333333333335
- mean overall (avg R/H/S/D/K): 3.2666666666666666
- flags (rate): safety_first=0.93, escalation_present=1.00, offline_workflow_mentioned=0.00, hallucination_suspected=0.03
### L2 (n=30)
- mean runtime: 4.419833333333333
- mean R/H/S/D/K: 4.7/4.4/4.133333333333334/4.5/3.7333333333333334
- mean overall (avg R/H/S/D/K): 4.293333333333334
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.10, hallucination_suspected=0.10
### L2B (n=30)
- mean runtime: 4.4808666666666666
- mean R/H/S/D/K: 4.9/4.866666666666666/4.433333333333334/4.9/5.0
- mean overall (avg R/H/S/D/K): 4.819999999999999
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.70, hallucination_suspected=0.00

## Mean scores by strategy (snapshot)
### S0 (n=30)
- mean runtime: 4.074133333333333
- mean R/H/S/D/K: 3.466666666666667/3.5/2.8666666666666667/3.6666666666666665/2.8333333333333335
- mean overall (avg R/H/S/D/K): 3.2666666666666666
### S1 (n=30)
- mean runtime: 4.419833333333333
- mean R/H/S/D/K: 4.7/4.4/4.133333333333334/4.5/3.7333333333333334
- mean overall (avg R/H/S/D/K): 4.293333333333334
### S2 (n=30)
- mean runtime: 4.4808666666666666
- mean R/H/S/D/K: 4.9/4.866666666666666/4.433333333333334/4.9/5.0
- mean overall (avg R/H/S/D/K): 4.819999999999999

## Top missing elements (max 20)
- Offline-Workflow (lokal dokumentieren/Foto lokal speichern): 2
- Offline-Workflow bei spotty connectivity: 2
- Keine Kontextnutzung (nur Asset-ID vorhanden): 2
- Offline-Workflow (Kontext zeigt kein connectivity-Signal): 2
- Keine Nutzung von Kontext (nur Asset-ID vorhanden): 2
- Keine Nutzung der Asset-ID im Workflow: 1
- Keine Berücksichtigung von Umgebungsbedingungen (nicht im Context): 1
- Generische Schritte ohne fallspezifische Anpassung: 1
- Offline-Workflow (spotty connectivity): 1
- Klare Trennung device vs. asset: 1
- Keine Offline-Workflow-Erwähnung trotz minimalem Kontext: 1
- Kein expliziter Offline-Workflow trotz spotty connectivity: 1
- Batterie-Warnung nicht als Handlungseinschränkung thematisiert: 1
- Offline-Workflow nicht erwartbar (kein Signal im Context): 1
- Sturm/Wetter nicht erwartbar (kein Signal im Context): 1
- Verkehrsexposition nicht erwartbar (kein Signal im Context): 1
- Offline-Workflow (connectivity=offline, device_state=low_battery) nicht explizit erwähnt: 1
- Keine klare Stop-Condition bei Mastinstabilität: 1
- Konkrete Nutzung der Asset-ID im Workflow: 1
- Wetter-/Umgebungskontext (nicht im CONTEXT vorhanden): 1
