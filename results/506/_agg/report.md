# Aggregation Report (506)
- judge_version filter: **judge_v1_1**
- Tests (latest runs): **90**
- Incidents with any deltas: **30**

## Mean scores by context level (snapshot)
### L0 (n=30)
- mean runtime: 3.6592333333333333
- mean R/H/S/D/K: 3.433333333333333/3.5/2.966666666666667/3.6/2.7666666666666666
- mean overall (avg R/H/S/D/K): 3.253333333333333
- flags (rate): safety_first=0.93, escalation_present=1.00, offline_workflow_mentioned=0.00, hallucination_suspected=0.00
### L2 (n=30)
- mean runtime: 3.9622666666666664
- mean R/H/S/D/K: 4.566666666666666/4.4/4.233333333333333/4.333333333333333/3.7666666666666666
- mean overall (avg R/H/S/D/K): 4.26
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.23, hallucination_suspected=0.03
### L2B (n=30)
- mean runtime: 4.3512
- mean R/H/S/D/K: 4.9/4.866666666666666/4.466666666666667/4.833333333333333/5.0
- mean overall (avg R/H/S/D/K): 4.8133333333333335
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.67, hallucination_suspected=0.00

## Mean scores by strategy (snapshot)
### S0 (n=30)
- mean runtime: 3.6592333333333333
- mean R/H/S/D/K: 3.433333333333333/3.5/2.966666666666667/3.6/2.7666666666666666
- mean overall (avg R/H/S/D/K): 3.253333333333333
### S1 (n=30)
- mean runtime: 3.9622666666666664
- mean R/H/S/D/K: 4.566666666666666/4.4/4.233333333333333/4.333333333333333/3.7666666666666666
- mean overall (avg R/H/S/D/K): 4.26
### S2 (n=30)
- mean runtime: 4.3512
- mean R/H/S/D/K: 4.9/4.866666666666666/4.466666666666667/4.833333333333333/5.0
- mean overall (avg R/H/S/D/K): 4.8133333333333335

## Top missing elements (max 20)
- Explizite Stop-Conditions für Abbruch: 2
- Offline-Workflow (connectivity=offline): 1
- Batterie-Hinweis als Geräte-Constraint, nicht Asset-Fehler: 1
- Keine Nutzung der Asset-ID im Text: 1
- Keine Anpassung an intermittent fault_type: 1
- Generische Antwort ohne Kontextbezug: 1
- Offline-Workflow bei spotty connectivity: 1
- Keine Priorisierung bei high severity erkennbar: 1
- Keine Offline-Workflow-Hinweise (nicht erwartbar bei L0): 1
- Sicherheitsmaßnahmen nicht als Schritt 1 priorisiert: 1
- Offline-Workflow fehlt trotz connectivity=offline: 1
- Keine Erwähnung von lokaler Speicherung/Synchronisation: 1
- Low_battery des Geräts nicht berücksichtigt: 1
- Offline-Workflow (nicht erwartbar bei minimalem Kontext): 1
- Wetter-/Verkehrskontext (nicht vorhanden): 1
- Foto-Nutzung (nicht erwartbar): 1
- Offline-Workflow explizit (connectivity=offline im Kontext): 1
- Keine klare Stop-Condition bei Sturm (erwähnt, aber nicht als harter Trigger): 1
- Keine Nutzung der Asset-ID im Kontext: 1
- Keine Anpassung an minimalen Kontext (generisch): 1
