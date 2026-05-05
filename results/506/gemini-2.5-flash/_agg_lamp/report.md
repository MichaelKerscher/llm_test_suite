# Aggregation Report (506/gemini-2.5-flash) [lamp]
- judge_version filter: **judge_v1_1**
- Tests (latest runs): **270**
- Incidents with any deltas: **30**

## Mean scores by context level (snapshot)
### L0 (n=30)
- mean runtime: 9.0787
- mean R/H/S/D/K: 3.6/3.6333333333333333/3.8333333333333335/4.033333333333333/2.5
- mean overall (avg R/H/S/D/K): 3.52
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.00, hallucination_suspected=0.10
### L2 (n=30)
- mean runtime: 12.142366666666668
- mean R/H/S/D/K: 4.933333333333334/4.9/4.966666666666667/4.933333333333334/4.4
- mean overall (avg R/H/S/D/K): 4.826666666666667
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.07, hallucination_suspected=0.00
### L2B (n=30)
- mean runtime: 11.2948
- mean R/H/S/D/K: 5.0/4.966666666666667/4.966666666666667/4.966666666666667/5.0
- mean overall (avg R/H/S/D/K): 4.98
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.60, hallucination_suspected=0.00
### unknown (n=180)
- mean runtime: 10.010022222222222
- mean R/H/S/D/K: 4.727777777777778/4.727777777777778/4.7555555555555555/4.85/4.655555555555556
- mean overall (avg R/H/S/D/K): 4.743333333333333
- flags (rate): safety_first=0.99, escalation_present=1.00, offline_workflow_mentioned=0.41, hallucination_suspected=0.01

## Mean scores by strategy (snapshot)
### S0 (n=30)
- mean runtime: 9.0787
- mean R/H/S/D/K: 3.6/3.6333333333333333/3.8333333333333335/4.033333333333333/2.5
- mean overall (avg R/H/S/D/K): 3.52
### S0_RAW (n=30)
- mean runtime: 11.623766666666667
- mean R/H/S/D/K: 4.566666666666666/4.566666666666666/4.6/4.766666666666667/4.266666666666667
- mean overall (avg R/H/S/D/K): 4.553333333333333
### S0_UNSTRUCTURED (n=30)
- mean runtime: 11.1641
- mean R/H/S/D/K: 4.333333333333333/4.4/4.566666666666666/4.533333333333333/3.8
- mean overall (avg R/H/S/D/K): 4.326666666666667
### S1 (n=30)
- mean runtime: 12.142366666666668
- mean R/H/S/D/K: 4.933333333333334/4.9/4.966666666666667/4.933333333333334/4.4
- mean overall (avg R/H/S/D/K): 4.826666666666667
### S2 (n=30)
- mean runtime: 11.2948
- mean R/H/S/D/K: 5.0/4.966666666666667/4.966666666666667/4.966666666666667/5.0
- mean overall (avg R/H/S/D/K): 4.98
### S2_ABL_NOASSET (n=30)
- mean runtime: 9.480966666666665
- mean R/H/S/D/K: 4.9/4.933333333333334/4.866666666666666/4.966666666666667/5.0
- mean overall (avg R/H/S/D/K): 4.933333333333334
### S2_ABL_NODEV (n=30)
- mean runtime: 8.9771
- mean R/H/S/D/K: 4.933333333333334/4.866666666666666/4.866666666666666/5.0/5.0
- mean overall (avg R/H/S/D/K): 4.933333333333334
### S2_ABL_NOENV (n=30)
- mean runtime: 9.661033333333334
- mean R/H/S/D/K: 4.866666666666666/4.766666666666667/4.766666666666667/4.9/4.933333333333334
- mean overall (avg R/H/S/D/K): 4.846666666666667
### S2_ABL_NOINC (n=30)
- mean runtime: 9.153166666666667
- mean R/H/S/D/K: 4.766666666666667/4.833333333333333/4.866666666666666/4.933333333333334/4.933333333333334
- mean overall (avg R/H/S/D/K): 4.866666666666666

## Top missing elements (max 20)
- Explizite Stop-Conditions: 4
- offline_workflow: 4
- Offline-Workflow bei 'spotty' connectivity nicht explizit erwähnt: 3
- Offline-Workflow (Kontext zeigt nur asset_osm, kein connectivity-Signal): 2
- Kontextnutzung minimal (nur Asset-ID): 2
- Offline-Workflow explizit (offline im CONTEXT, aber nicht klar adressiert): 2
- Offline-Workflow (nicht erwartbar, da connectivity nicht im CONTEXT): 2
- Offline-Workflow (spotty connectivity): 2
- Offline-Workflow nicht explizit trotz connectivity=offline: 1
- Safety-first nicht als Schritt 1 positioniert: 1
- Kontextnutzung (Standort/Foto/Wetter): 1
- Fokus auf intermittent fault: 1
- Feuchtigkeitsflecken-Hinweis: 1
- Kürzere Schrittfolge: 1
- Vollständige Kontextnutzung (unstructured schwer lesbar): 1
- Offline-Workflow (nicht erwartbar, da CONTEXT keine connectivity-Probleme zeigt): 1
- Offline-Workflow explizit (spotty connectivity + low_battery erwähnt, aber kein klarer Offline-Workflow wie 'lokal dokumentieren, später synchronisieren'): 1
- Offline-Workflow explizit (instabile Konnektivität + schwache Batterie erwähnt, aber kein klarer Offline-Workflow-Hinweis wie 'lokal speichern, später synchronisieren'): 1
- Offline-Workflow (spotty connectivity im CONTEXT, aber nicht als Handlungsanweisung umgesetzt): 1
- Gerätezustand (low_battery) nur als Diagnose-Hinweis, nicht als Constraint für Dokumentation/Workflow: 1
