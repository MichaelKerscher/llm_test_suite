# Aggregation Report (506/gemini-2.5-flash) [signal]
- judge_version filter: **judge_v1_1**
- Tests (latest runs): **150**
- Incidents with any deltas: **30**

## Mean scores by context level (snapshot)
### L0 (n=30)
- mean runtime: 8.7123
- mean R/H/S/D/K: 3.933333333333333/3.966666666666667/4.066666666666666/4.133333333333334/2.7333333333333334
- mean overall (avg R/H/S/D/K): 3.7666666666666666
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.00, hallucination_suspected=0.20
### L2 (n=30)
- mean runtime: 10.632100000000001
- mean R/H/S/D/K: 4.966666666666667/4.933333333333334/4.966666666666667/4.933333333333334/4.6
- mean overall (avg R/H/S/D/K): 4.88
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.07, hallucination_suspected=0.00
### L2B (n=30)
- mean runtime: 10.354933333333333
- mean R/H/S/D/K: 5.0/5.0/4.966666666666667/5.0/5.0
- mean overall (avg R/H/S/D/K): 4.993333333333334
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.53, hallucination_suspected=0.00
### unknown (n=60)
- mean runtime: 10.5927
- mean R/H/S/D/K: 4.6/4.6/4.716666666666667/4.683333333333334/4.266666666666667
- mean overall (avg R/H/S/D/K): 4.573333333333333
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.25, hallucination_suspected=0.00

## Mean scores by strategy (snapshot)
### S0 (n=30)
- mean runtime: 8.7123
- mean R/H/S/D/K: 3.933333333333333/3.966666666666667/4.066666666666666/4.133333333333334/2.7333333333333334
- mean overall (avg R/H/S/D/K): 3.7666666666666666
### S0_RAW (n=30)
- mean runtime: 10.579533333333334
- mean R/H/S/D/K: 4.833333333333333/4.833333333333333/4.833333333333333/4.933333333333334/4.666666666666667
- mean overall (avg R/H/S/D/K): 4.819999999999999
### S0_UNSTRUCTURED (n=30)
- mean runtime: 10.605866666666666
- mean R/H/S/D/K: 4.366666666666666/4.366666666666666/4.6/4.433333333333334/3.8666666666666667
- mean overall (avg R/H/S/D/K): 4.326666666666667
### S1 (n=30)
- mean runtime: 10.632100000000001
- mean R/H/S/D/K: 4.966666666666667/4.933333333333334/4.966666666666667/4.933333333333334/4.6
- mean overall (avg R/H/S/D/K): 4.88
### S2 (n=30)
- mean runtime: 10.354933333333333
- mean R/H/S/D/K: 5.0/5.0/4.966666666666667/5.0/5.0
- mean overall (avg R/H/S/D/K): 4.993333333333334

## Top missing elements (max 20)
- offline_workflow: 4
- Offline-Workflow (nicht erwartbar, da connectivity nicht im CONTEXT): 3
- Explizite Erwähnung 'Kreuzung wie unbeschrankt behandeln': 3
- Offline-Workflow explizit (erwartbar, da offline im CONTEXT): 2
- Kontext-Nutzung minimal (nur Asset-ID): 2
- Keine Nutzung der Asset-ID im Kontext: 2
- Offline-Workflow nicht explizit erwähnt (spotty connectivity im Kontext): 2
- Offline-Workflow explizit: 2
- offline_workflow_explicit: 1
- Wetter/Sicht-Bezug (nicht erwartbar): 1
- Keine GPS-Koordinaten genutzt (im Context vorhanden): 1
- Keine Nutzung von Foto-Hinweisen: 1
- Spekuliert über Reset-Möglichkeiten ohne Basis im Context: 1
- Foto-Verfügbarkeit nicht explizit erwähnt: 1
- Keine Anpassung an fehlende Umgebungsdaten: 1
- Low_battery-Hinweis nur in Rückfragen, nicht in Hauptworkflow integriert: 1
- Keine klare Priorisierung bei intermittierendem Fehler: 1
- Verkehrsabhängigkeit könnte stärker betont werden: 1
- Wartungsdatum-Interpretation unklar: 1
- Konkrete Trigger für Eskalation bei sporadischer Störung: 1
