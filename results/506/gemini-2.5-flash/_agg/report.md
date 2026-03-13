# Aggregation Report (506/gemini-2.5-flash)
- judge_version filter: **judge_v1_1**
- Tests (latest runs): **90**
- Incidents with any deltas: **30**

## Mean scores by context level (snapshot)
### L0 (n=30)
- mean runtime: 5.5879
- mean R/H/S/D/K: 3.466666666666667/3.8333333333333335/3.9/4.033333333333333/2.8333333333333335
- mean overall (avg R/H/S/D/K): 3.6133333333333337
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.00, hallucination_suspected=0.03
### L2 (n=30)
- mean runtime: 8.964233333333334
- mean R/H/S/D/K: 4.733333333333333/4.6/4.633333333333334/4.9/3.7333333333333334
- mean overall (avg R/H/S/D/K): 4.52
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.03, hallucination_suspected=0.10
### L2B (n=30)
- mean runtime: 9.6204
- mean R/H/S/D/K: 4.833333333333333/4.833333333333333/4.8/5.0/4.966666666666667
- mean overall (avg R/H/S/D/K): 4.886666666666667
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.60, hallucination_suspected=0.00

## Mean scores by strategy (snapshot)
### S0 (n=30)
- mean runtime: 5.5879
- mean R/H/S/D/K: 3.466666666666667/3.8333333333333335/3.9/4.033333333333333/2.8333333333333335
- mean overall (avg R/H/S/D/K): 3.6133333333333337
### S1 (n=30)
- mean runtime: 8.964233333333334
- mean R/H/S/D/K: 4.733333333333333/4.6/4.633333333333334/4.9/3.7333333333333334
- mean overall (avg R/H/S/D/K): 4.52
### S2 (n=30)
- mean runtime: 9.6204
- mean R/H/S/D/K: 4.833333333333333/4.833333333333333/4.8/5.0/4.966666666666667
- mean overall (avg R/H/S/D/K): 4.886666666666667

## Top missing elements (max 20)
- Offline-Workflow bei spotty connectivity: 7
- Kontextnutzung minimal (nur Asset-ID): 3
- Offline-Workflow fehlt trotz connectivity=offline: 2
- Keine Anpassung an Offline-Bedingungen erkennbar: 1
- Generische Schritte ohne Priorisierung nach Severity: 1
- Offline-Workflow nicht explizit erwähnt trotz connectivity=offline: 1
- Device-Status erwähnt, aber nicht als Workflow-Constraint genutzt: 1
- Kontextnutzung (nur Asset-ID vorhanden, keine Umwelt-/Geräte-Infos genutzt): 1
- Spezifische Priorisierung bei intermittent fault: 1
- Beobachtungsdauer/Trigger für intermittierenden Fehler: 1
- Klarstellung device_state vs. Asset-Fehler: 1
- Offline-Workflow (connectivity=offline, device_state=low_battery): 1
- Keine Offline-Workflow-Erwähnung (aber nicht erwartbar bei minimalem Kontext): 1
- Offline-Workflow bei spotty connectivity nicht explizit erwähnt: 1
- Offline-Workflow (connectivity=offline): 1
- Klare Priorisierung Offline-Dokumentation: 1
- Offline-Workflow (connectivity=spotty, device_state=low_power_mode): 1
- Keine Nutzung der GPS-Koordinaten (nur Asset-ID erwähnt): 1
- Keine Prüfung auf weitere betroffene Lampen in der Umgebung: 1
- Etwas langatmig/redundant formuliert (z.B. Begrüßung, Wiederholungen): 1
