# Aggregation Report (506)
- judge_version filter: **judge_v1_1**
- Tests (latest runs): **90**
- Incidents with any deltas: **30**

## Mean scores by context level (snapshot)
### L0 (n=30)
- mean runtime: 3.6509666666666667
- mean R/H/S/D/K: 3.433333333333333/3.433333333333333/3.066666666666667/3.7666666666666666/2.7
- mean overall (avg R/H/S/D/K): 3.2800000000000002
- flags (rate): safety_first=0.93, escalation_present=1.00, offline_workflow_mentioned=0.00, hallucination_suspected=0.00
### L2 (n=30)
- mean runtime: 4.198766666666667
- mean R/H/S/D/K: 4.6/4.333333333333333/4.166666666666667/4.5/3.9
- mean overall (avg R/H/S/D/K): 4.3
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.27, hallucination_suspected=0.03
### L2B (n=30)
- mean runtime: 4.468933333333334
- mean R/H/S/D/K: 4.933333333333334/4.833333333333333/4.466666666666667/4.933333333333334/4.933333333333334
- mean overall (avg R/H/S/D/K): 4.819999999999999
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.63, hallucination_suspected=0.00

## Mean scores by strategy (snapshot)
### S0 (n=30)
- mean runtime: 3.6509666666666667
- mean R/H/S/D/K: 3.433333333333333/3.433333333333333/3.066666666666667/3.7666666666666666/2.7
- mean overall (avg R/H/S/D/K): 3.2800000000000002
### S1 (n=30)
- mean runtime: 4.198766666666667
- mean R/H/S/D/K: 4.6/4.333333333333333/4.166666666666667/4.5/3.9
- mean overall (avg R/H/S/D/K): 4.3
### S2 (n=30)
- mean runtime: 4.468933333333334
- mean R/H/S/D/K: 4.933333333333334/4.833333333333333/4.466666666666667/4.933333333333334/4.933333333333334
- mean overall (avg R/H/S/D/K): 4.819999999999999

## Top missing elements (max 20)
- Keine Nutzung der Asset-ID im Kontext: 5
- Kein expliziter Offline-Workflow trotz spotty connectivity: 2
- Offline-Workflow bei spotty connectivity nicht explizit erwähnt: 2
- Keine Priorisierung nach Severity: 2
- Offline-Workflow (lokal dokumentieren/Foto lokal speichern): 1
- Kontextnutzung minimal (nur Asset-ID vorhanden): 1
- Keine spezifische Anpassung an Umgebung/Zeit: 1
- Keine Kontextnutzung erkennbar (minimaler Context): 1
- Keine Anpassung an Umgebungsbedingungen: 1
- Generische Antwort ohne Fallspezifik: 1
- Low_battery des Geräts erwähnt, aber nicht klar als Techniker-Gerät abgegrenzt: 1
- Offline-Workflow nicht erwähnt (Kontext zeigt keine Connectivity-Probleme, daher nicht erwartbar): 1
- Kontextnutzung minimal (nur Asset-ID verwendet): 1
- Offline-Workflow nur indirekt erwähnt ('alternative Kommunikationswege'), nicht explizit als lokale Dokumentation/Foto-Speicherung: 1
- Keine Offline-Workflow-Erwähnung (aber nicht erwartbar bei L0_minimal): 1
- Offline-Workflow fehlt (connectivity=offline, device_state=low_battery im CONTEXT): 1
- Keine Erwähnung lokaler Speicherung/Synchronisation: 1
- Offline-Workflow (nicht erwartbar, da connectivity nicht im Context): 1
- Wetter-/Umgebungskontext (nicht vorhanden): 1
- Foto-Workflow (photo_available nicht im Context): 1
