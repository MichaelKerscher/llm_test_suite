# Aggregation Report (506/mistral-large) [lamp]
- judge_version filter: **judge_v1_1**
- Tests (latest runs): **270**
- Incidents with any deltas: **30**

## Mean scores by context level (snapshot)
### L0 (n=30)
- mean runtime: 7.598233333333334
- mean R/H/S/D/K: 3.6666666666666665/3.8333333333333335/3.7/4.166666666666667/2.533333333333333
- mean overall (avg R/H/S/D/K): 3.58
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.00, hallucination_suspected=0.10
### L2 (n=30)
- mean runtime: 10.767433333333335
- mean R/H/S/D/K: 4.9/4.8/4.833333333333333/4.866666666666666/4.366666666666666
- mean overall (avg R/H/S/D/K): 4.753333333333333
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.00, hallucination_suspected=0.00
### L2B (n=30)
- mean runtime: 10.799900000000001
- mean R/H/S/D/K: 4.966666666666667/4.966666666666667/4.866666666666666/5.0/5.0
- mean overall (avg R/H/S/D/K): 4.96
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.60, hallucination_suspected=0.00
### unknown (n=180)
- mean runtime: 9.268627777777779
- mean R/H/S/D/K: 4.738888888888889/4.738888888888889/4.727777777777778/4.894444444444445/4.694444444444445
- mean overall (avg R/H/S/D/K): 4.758888888888889
- flags (rate): safety_first=0.99, escalation_present=1.00, offline_workflow_mentioned=0.41, hallucination_suspected=0.01

## Mean scores by strategy (snapshot)
### S0 (n=30)
- mean runtime: 7.598233333333334
- mean R/H/S/D/K: 3.6666666666666665/3.8333333333333335/3.7/4.166666666666667/2.533333333333333
- mean overall (avg R/H/S/D/K): 3.58
### S0_RAW (n=30)
- mean runtime: 9.088833333333334
- mean R/H/S/D/K: 4.666666666666667/4.633333333333334/4.633333333333334/4.866666666666666/4.533333333333333
- mean overall (avg R/H/S/D/K): 4.666666666666667
### S0_UNSTRUCTURED (n=30)
- mean runtime: 9.830333333333334
- mean R/H/S/D/K: 4.366666666666666/4.366666666666666/4.366666666666666/4.7/3.7666666666666666
- mean overall (avg R/H/S/D/K): 4.3133333333333335
### S1 (n=30)
- mean runtime: 10.767433333333335
- mean R/H/S/D/K: 4.9/4.8/4.833333333333333/4.866666666666666/4.366666666666666
- mean overall (avg R/H/S/D/K): 4.753333333333333
### S2 (n=30)
- mean runtime: 10.799900000000001
- mean R/H/S/D/K: 4.966666666666667/4.966666666666667/4.866666666666666/5.0/5.0
- mean overall (avg R/H/S/D/K): 4.96
### S2_ABL_NOASSET (n=30)
- mean runtime: 9.7382
- mean R/H/S/D/K: 4.866666666666666/4.9/4.866666666666666/4.933333333333334/4.966666666666667
- mean overall (avg R/H/S/D/K): 4.906666666666666
### S2_ABL_NODEV (n=30)
- mean runtime: 9.3244
- mean R/H/S/D/K: 4.966666666666667/4.933333333333334/4.866666666666666/5.0/4.966666666666667
- mean overall (avg R/H/S/D/K): 4.946666666666667
### S2_ABL_NOENV (n=30)
- mean runtime: 8.850366666666668
- mean R/H/S/D/K: 4.833333333333333/4.766666666666667/4.7/4.9/4.933333333333334
- mean overall (avg R/H/S/D/K): 4.826666666666667
### S2_ABL_NOINC (n=30)
- mean runtime: 8.779633333333333
- mean R/H/S/D/K: 4.733333333333333/4.833333333333333/4.933333333333334/4.966666666666667/5.0
- mean overall (avg R/H/S/D/K): 4.8933333333333335

## Top missing elements (max 20)
- offline_workflow: 5
- Offline-Workflow nicht explizit trotz connectivity=offline: 2
- Offline-Workflow explizit (spotty connectivity vorhanden): 2
- Offline-Workflow (spotty connectivity im Context): 2
- Keine Nutzung des Kontexts (nur Asset-ID vorhanden): 2
- Keine Nutzung der Asset-ID im Kontext: 2
- Kein expliziter Offline-Workflow trotz 'spotty' connectivity: 2
- Kein expliziter Offline-Workflow trotz spotty connectivity: 2
- Klare Stop-Condition für Beobachtungsphase fehlt: 1
- Offline-Workflow nicht erwähnt trotz connectivity=offline: 1
- Explizite Erwähnung der Asset-ID (n4427359783) in Dokumentation: 1
- Keine Anpassung an Umgebungsbedingungen (nicht erwartbar aus CONTEXT): 1
- Offline-Workflow nicht explizit erwähnt (trotz connectivity=offline im CONTEXT): 1
- Offline-Workflow nicht explizit erwähnt (trotz offline/low_battery im CONTEXT): 1
- Offline-Workflow (Gerät offline, aber nicht erwähnt): 1
- Sturm/Wetter-Kontext fehlt: 1
- Loses Kabel nicht erkannt: 1
- Foto-Hinweis nicht genutzt: 1
- Offline-Workflow nicht explizit (Gerät offline): 1
- Sync-Hinweis fehlt: 1
