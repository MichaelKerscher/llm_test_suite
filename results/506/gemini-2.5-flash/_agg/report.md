# Aggregation Report (506/gemini-2.5-flash)
- judge_version filter: **judge_v1_1**
- Tests (latest runs): **90**
- Incidents with any deltas: **30**

## Mean scores by context level (snapshot)
### L0 (n=30)
- mean runtime: 5.818266666666667
- mean R/H/S/D/K: 3.6/3.9/3.9/3.966666666666667/2.7333333333333334
- mean overall (avg R/H/S/D/K): 3.6199999999999997
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.00, hallucination_suspected=0.03
### L2 (n=30)
- mean runtime: 9.056366666666666
- mean R/H/S/D/K: 4.833333333333333/4.8/4.733333333333333/4.966666666666667/3.966666666666667
- mean overall (avg R/H/S/D/K): 4.66
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.03, hallucination_suspected=0.10
### L2B (n=30)
- mean runtime: 10.296033333333334
- mean R/H/S/D/K: 4.966666666666667/4.933333333333334/4.766666666666667/4.966666666666667/5.0
- mean overall (avg R/H/S/D/K): 4.926666666666667
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.60, hallucination_suspected=0.00

## Mean scores by strategy (snapshot)
### S0 (n=30)
- mean runtime: 5.818266666666667
- mean R/H/S/D/K: 3.6/3.9/3.9/3.966666666666667/2.7333333333333334
- mean overall (avg R/H/S/D/K): 3.6199999999999997
### S1 (n=30)
- mean runtime: 9.056366666666666
- mean R/H/S/D/K: 4.833333333333333/4.8/4.733333333333333/4.966666666666667/3.966666666666667
- mean overall (avg R/H/S/D/K): 4.66
### S2 (n=30)
- mean runtime: 10.296033333333334
- mean R/H/S/D/K: 4.966666666666667/4.933333333333334/4.766666666666667/4.966666666666667/5.0
- mean overall (avg R/H/S/D/K): 4.926666666666667

## Top missing elements (max 20)
- Offline-Workflow bei spotty connectivity: 5
- Offline-Workflow explizit (spotty connectivity): 2
- Kontextnutzung minimal (nur Asset-ID): 2
- Keine Offline-Workflow-Erwähnung (nicht erwartbar bei L0): 2
- Offline-Workflow (connectivity=offline): 2
- Offline-Workflow (lokal dokumentieren/später sync): 1
- Klarstellung: device.* = Techniker-Gerät, nicht Asset: 1
- Keine Nutzung der Asset-ID im Kontext (nur OSM-ID vorhanden): 1
- Keine spezifische Anpassung an intermittent fault_type: 1
- Offline-Workflow explizit (device.connectivity=offline): 1
- Offline-Workflow fehlt (connectivity=offline im CONTEXT): 1
- Keine Erwähnung lokaler Speicherung/Synchronisation: 1
- Keine Kontextnutzung (nur Asset-ID vorhanden): 1
- Generische Antwort ohne spezifische Anpassung: 1
- Offline-Workflow nicht erwähnt (spotty connectivity): 1
- Low_power_mode als Asset-Problem fehlinterpretiert: 1
- Offline-Workflow (nicht erwartbar, da CONTEXT kein connectivity-Signal enthält): 1
- Keine Nutzung von Kontext (nur Asset-ID vorhanden): 1
- Keine Anpassung an Umgebungsbedingungen (Wetter/Verkehr unbekannt): 1
- Kontext-Nutzung minimal (nur Asset-ID vorhanden): 1
