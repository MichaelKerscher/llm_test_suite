# Aggregation Report (506/mistral-large) [signal]
- judge_version filter: **judge_v1_1**
- Tests (latest runs): **150**
- Incidents with any deltas: **30**

## Mean scores by context level (snapshot)
### L0 (n=30)
- mean runtime: 9.319333333333333
- mean R/H/S/D/K: 3.9/4.0/4.166666666666667/4.233333333333333/2.6333333333333333
- mean overall (avg R/H/S/D/K): 3.7866666666666666
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.00, hallucination_suspected=0.30
### L2 (n=30)
- mean runtime: 11.523966666666666
- mean R/H/S/D/K: 4.933333333333334/4.933333333333334/4.9/4.966666666666667/4.7
- mean overall (avg R/H/S/D/K): 4.886666666666667
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.23, hallucination_suspected=0.00
### L2B (n=30)
- mean runtime: 10.452866666666667
- mean R/H/S/D/K: 5.0/5.0/4.9/5.0/5.0
- mean overall (avg R/H/S/D/K): 4.98
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.53, hallucination_suspected=0.00
### unknown (n=60)
- mean runtime: 11.825533333333334
- mean R/H/S/D/K: 4.516666666666667/4.583333333333333/4.75/4.7/4.233333333333333
- mean overall (avg R/H/S/D/K): 4.556666666666667
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.23, hallucination_suspected=0.00

## Mean scores by strategy (snapshot)
### S0 (n=30)
- mean runtime: 9.319333333333333
- mean R/H/S/D/K: 3.9/4.0/4.166666666666667/4.233333333333333/2.6333333333333333
- mean overall (avg R/H/S/D/K): 3.7866666666666666
### S0_RAW (n=30)
- mean runtime: 11.6952
- mean R/H/S/D/K: 4.766666666666667/4.766666666666667/4.833333333333333/4.9/4.633333333333334
- mean overall (avg R/H/S/D/K): 4.78
### S0_UNSTRUCTURED (n=30)
- mean runtime: 11.955866666666667
- mean R/H/S/D/K: 4.266666666666667/4.4/4.666666666666667/4.5/3.8333333333333335
- mean overall (avg R/H/S/D/K): 4.333333333333333
### S1 (n=30)
- mean runtime: 11.523966666666666
- mean R/H/S/D/K: 4.933333333333334/4.933333333333334/4.9/4.966666666666667/4.7
- mean overall (avg R/H/S/D/K): 4.886666666666667
### S2 (n=30)
- mean runtime: 10.452866666666667
- mean R/H/S/D/K: 5.0/5.0/4.9/5.0/5.0
- mean overall (avg R/H/S/D/K): 4.98

## Top missing elements (max 20)
- offline_workflow: 4
- Keine Erwähnung von Wetter/Sicht (nicht im Kontext): 2
- Offline-Workflow (nicht erwartbar, da connectivity=spotty, nicht offline): 2
- Offline-Workflow (nicht erwartbar, da connectivity nicht im CONTEXT): 2
- Offline-Workflow nicht explizit erwähnt: 1
- Offline-Workflow nicht erwähnt trotz offline/low_battery im Kontext: 1
- Offline-Workflow (nicht erwartbar, da CONTEXT minimal): 1
- GPS-Koordinaten (nicht im CONTEXT vorhanden): 1
- Offline-Workflow explizit (offline im CONTEXT, aber nicht klar hervorgehoben): 1
- Keine GPS-Koordinaten genutzt: 1
- Keine Nutzung der Verkehrszeit-Info aus Context: 1
- Koordinaten nicht explizit in Dokumentation integriert: 1
- Keine Kontextnutzung erkennbar (nur Asset-ID vorhanden): 1
- Annahmen über thermische Probleme/Überlastung ohne Basis im Context: 1
- Fehlerprotokolle im Steuerungskasten erwähnt ohne Hinweis auf Zugriff: 1
- Unstructured Context nur teilweise sichtbar genutzt (Koordinaten, Schweregrad erwähnt, aber nicht explizit zitiert): 1
- Offline-Workflow nicht erwähnt (aber auch nicht erwartbar aus CONTEXT): 1
- Spekuliert über Ampel/Straßenlampe ohne Basis: 1
- Offline-Workflow nicht explizit erwähnt trotz 'spotty' im unstructured text: 1
- Kontext minimal, aber Antwort nutzt Schweregrad/Verkehr plausibel: 1
