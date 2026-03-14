# Aggregation Report (506/mistral-large)
- judge_version filter: **judge_v1_1**
- Tests (latest runs): **90**
- Incidents with any deltas: **30**

## Mean scores by context level (snapshot)
### L0 (n=30)
- mean runtime: 5.202366666666666
- mean R/H/S/D/K: 3.6/3.8333333333333335/3.8/4.0/2.8666666666666667
- mean overall (avg R/H/S/D/K): 3.6199999999999997
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.00, hallucination_suspected=0.03
### L2 (n=30)
- mean runtime: 8.389866666666666
- mean R/H/S/D/K: 4.8/4.6/4.566666666666666/4.933333333333334/3.8666666666666667
- mean overall (avg R/H/S/D/K): 4.553333333333333
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.10, hallucination_suspected=0.13
### L2B (n=30)
- mean runtime: 8.615433333333334
- mean R/H/S/D/K: 4.866666666666666/4.8/4.766666666666667/4.966666666666667/4.966666666666667
- mean overall (avg R/H/S/D/K): 4.873333333333333
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.60, hallucination_suspected=0.00

## Mean scores by strategy (snapshot)
### S0 (n=30)
- mean runtime: 5.202366666666666
- mean R/H/S/D/K: 3.6/3.8333333333333335/3.8/4.0/2.8666666666666667
- mean overall (avg R/H/S/D/K): 3.6199999999999997
### S1 (n=30)
- mean runtime: 8.389866666666666
- mean R/H/S/D/K: 4.8/4.6/4.566666666666666/4.933333333333334/3.8666666666666667
- mean overall (avg R/H/S/D/K): 4.553333333333333
### S2 (n=30)
- mean runtime: 8.615433333333334
- mean R/H/S/D/K: 4.866666666666666/4.8/4.766666666666667/4.966666666666667/4.966666666666667
- mean overall (avg R/H/S/D/K): 4.873333333333333

## Top missing elements (max 20)
- Offline-Workflow bei spotty connectivity: 6
- Keine Nutzung der Asset-ID im Kontext (nur minimal vorhanden): 3
- Offline-Workflow explizit (lokal speichern/später sync): 2
- Offline-Workflow (spotty connectivity): 2
- Keine Spekulation über 'low_battery' als Asset-Problem: 1
- Gerätestatus-Hinweis für Techniker: 1
- Offline-Workflow nicht erwartbar (kein Signal im Context): 1
- Sturm/Wetter nicht erwartbar (kein Signal im Context): 1
- Offline-Workflow fehlt (connectivity=offline, device_state=low_battery im Context): 1
- Keine Erwähnung lokaler Speicherung/Synchronisation: 1
- Offline-Workflow (connectivity=offline nicht erkennbar im Kontext): 1
- Spezifische Risikobewertung (severity/weather fehlen im Kontext): 1
- Foto-Nutzung (photo_available nicht im Kontext): 1
- Offline-Workflow explizit (connectivity=offline → lokal dokumentieren/später sync): 1
- Klare Stop-Condition vor Schritt 5: 1
- Severity-Bewertung fehlt (keine Priorisierung erkennbar): 1
- Keine Anpassung an Umgebungsbedingungen (Zeit/Wetter unbekannt): 1
- Keine Offline-Workflow-Erwähnung trotz minimalem Kontext: 1
- Keine Nutzung der Asset-ID im Kontext erkennbar: 1
- Keine spezifische Anpassung an intermittent fault_type: 1
