# Aggregation Report (506/mistral-large)
- judge_version filter: **judge_v1_1**
- Tests (latest runs): **90**
- Incidents with any deltas: **30**

## Mean scores by context level (snapshot)
### L0 (n=30)
- mean runtime: 4.9317
- mean R/H/S/D/K: 3.5/3.8666666666666667/3.8666666666666667/4.1/2.8666666666666667
- mean overall (avg R/H/S/D/K): 3.64
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.00, hallucination_suspected=0.03
### L2 (n=30)
- mean runtime: 7.4581
- mean R/H/S/D/K: 4.8/4.633333333333334/4.733333333333333/4.8/3.7
- mean overall (avg R/H/S/D/K): 4.533333333333333
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.00, hallucination_suspected=0.07
### L2B (n=30)
- mean runtime: 8.323866666666667
- mean R/H/S/D/K: 5.0/4.933333333333334/4.9/5.0/5.0
- mean overall (avg R/H/S/D/K): 4.966666666666667
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.60, hallucination_suspected=0.00

## Mean scores by strategy (snapshot)
### S0 (n=30)
- mean runtime: 4.9317
- mean R/H/S/D/K: 3.5/3.8666666666666667/3.8666666666666667/4.1/2.8666666666666667
- mean overall (avg R/H/S/D/K): 3.64
### S1 (n=30)
- mean runtime: 7.4581
- mean R/H/S/D/K: 4.8/4.633333333333334/4.733333333333333/4.8/3.7
- mean overall (avg R/H/S/D/K): 4.533333333333333
### S2 (n=30)
- mean runtime: 8.323866666666667
- mean R/H/S/D/K: 5.0/4.933333333333334/4.9/5.0/5.0
- mean overall (avg R/H/S/D/K): 4.966666666666667

## Top missing elements (max 20)
- Offline-Workflow bei spotty connectivity: 7
- Lokale Dokumentation/Synchronisation später: 2
- Offline-Workflow (connectivity=offline): 2
- Offline-Workflow (lokal dokumentieren/Foto lokal speichern): 2
- Offline-Workflow (device.connectivity=offline): 1
- Klare Unterscheidung device vs. asset: 1
- Offline-Workflow (spotty connectivity): 1
- Offline-Workflow (lokal dokumentieren/später sync): 1
- Keine Nutzung der GPS-Koordinaten (nur Asset-ID erwähnt): 1
- Keine Erwähnung von Foto-Dokumentation trotz photo_available=true im späteren Kontext: 1
- Klarstellung: device.* = Techniker-Gerät, nicht Asset: 1
- Keine Nutzung der Koordinaten (nicht im Kontext): 1
- Keine Erwähnung des Fotos (nicht im Kontext): 1
- Keine Berücksichtigung von Wetter/Sicht (nicht im Kontext): 1
- Kontextnutzung minimal (nur Asset-ID): 1
- Keine Berücksichtigung von Umgebungsbedingungen: 1
- Keine Anpassung an Schweregrad/Tageszeit: 1
- Keine Nutzung von Umgebungskontext (Nacht/Nebel/Sicht): 1
- Keine Erwähnung von Verkehrsaufkommen: 1
- Keine Nutzung der Asset-ID für konkrete Diagnose: 1
