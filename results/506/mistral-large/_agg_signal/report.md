# Aggregation Report (506\mistral-large) [signal]
- judge_version filter: **judge_v1_1**
- Tests (latest runs): **90**
- Incidents with any deltas: **30**

## Mean scores by context level (snapshot)
### L0 (n=30)
- mean runtime: 6.092633333333334
- mean R/H/S/D/K: 3.8666666666666667/3.966666666666667/4.233333333333333/4.266666666666667/2.566666666666667
- mean overall (avg R/H/S/D/K): 3.7800000000000002
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.00, hallucination_suspected=0.13
### L2 (n=30)
- mean runtime: 8.565666666666667
- mean R/H/S/D/K: 4.9/4.7/4.866666666666666/4.9/4.5
- mean overall (avg R/H/S/D/K): 4.7733333333333325
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.13, hallucination_suspected=0.03
### L2B (n=30)
- mean runtime: 8.390466666666667
- mean R/H/S/D/K: 4.9/4.866666666666666/4.9/4.866666666666666/4.966666666666667
- mean overall (avg R/H/S/D/K): 4.9
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.60, hallucination_suspected=0.00

## Mean scores by strategy (snapshot)
### S0 (n=30)
- mean runtime: 6.092633333333334
- mean R/H/S/D/K: 3.8666666666666667/3.966666666666667/4.233333333333333/4.266666666666667/2.566666666666667
- mean overall (avg R/H/S/D/K): 3.7800000000000002
### S1 (n=30)
- mean runtime: 8.565666666666667
- mean R/H/S/D/K: 4.9/4.7/4.866666666666666/4.9/4.5
- mean overall (avg R/H/S/D/K): 4.7733333333333325
### S2 (n=30)
- mean runtime: 8.390466666666667
- mean R/H/S/D/K: 4.9/4.866666666666666/4.9/4.866666666666666/4.966666666666667
- mean overall (avg R/H/S/D/K): 4.9

## Top missing elements (max 20)
- Keine Nutzung der Asset-ID im Kontext: 3
- Offline-Workflow bei spotty connectivity nicht explizit erwähnt: 3
- Keine Erwähnung von Umweltbedingungen (nicht im Context): 2
- Kontextnutzung minimal (nur Asset-ID vorhanden): 2
- Offline-Workflow (nicht erwartbar, da CONTEXT minimal): 1
- GPS-Nutzung (nicht erwartbar): 1
- Expliziter Offline-Workflow (Sync-Hinweis fehlt): 1
- Offline-Workflow (nicht erwartbar, da CONTEXT kein connectivity-Signal enthält): 1
- Offline-Workflow explizit (connectivity=offline im CONTEXT, aber nicht klar als Workflow-Anpassung adressiert): 1
- Severity-Einschätzung fehlt (nur Asset-ID vorhanden): 1
- Keine Erwähnung von Kreuzungsbehandlung als unbeschrankt: 1
- Keine Priorisierung auf Hauptverkehrszeit/hohen Verkehr: 1
- Keine Erwähnung intermittierender Fehlersuche: 1
- Keine klaren Stop-Conditions: 1
- Kein Hinweis auf Offline-Workflow trotz fehlendem Kontext: 1
- Spekulation über Asset-Typ (Straßenlampe/Ampel) ohne Basis: 1
- Offline-Workflow nicht erwähnt trotz spotty connectivity: 1
- Spekulation über Asset-Typ am Ende: 1
- Keine GPS-Koordinaten erwähnt (nicht im CONTEXT verfügbar): 1
- Keine Erwähnung von Foto (photo_available=true im Original-Context): 1
