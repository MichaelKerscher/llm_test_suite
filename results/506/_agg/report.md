# Aggregation Report (506)
- judge_version filter: **judge_v1_1**
- Tests (latest runs): **90**
- Incidents with any deltas: **30**

## Mean scores by context level (snapshot)
### L0 (n=30)
- mean runtime: 4.434366666666667
- mean R/H/S/D/K: 3.4/3.466666666666667/3.033333333333333/3.6666666666666665/2.8
- mean overall (avg R/H/S/D/K): 3.2733333333333334
- flags (rate): safety_first=0.93, escalation_present=1.00, offline_workflow_mentioned=0.00, hallucination_suspected=0.00
### L2 (n=30)
- mean runtime: 4.4948
- mean R/H/S/D/K: 4.566666666666666/4.366666666666666/4.233333333333333/4.366666666666666/3.8666666666666667
- mean overall (avg R/H/S/D/K): 4.28
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.20, hallucination_suspected=0.03
### L2B (n=30)
- mean runtime: 4.877933333333333
- mean R/H/S/D/K: 4.866666666666666/4.8/4.466666666666667/4.9/5.0
- mean overall (avg R/H/S/D/K): 4.806666666666667
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.63, hallucination_suspected=0.00

## Mean scores by strategy (snapshot)
### S0 (n=30)
- mean runtime: 4.434366666666667
- mean R/H/S/D/K: 3.4/3.466666666666667/3.033333333333333/3.6666666666666665/2.8
- mean overall (avg R/H/S/D/K): 3.2733333333333334
### S1 (n=30)
- mean runtime: 4.4948
- mean R/H/S/D/K: 4.566666666666666/4.366666666666666/4.233333333333333/4.366666666666666/3.8666666666666667
- mean overall (avg R/H/S/D/K): 4.28
### S2 (n=30)
- mean runtime: 4.877933333333333
- mean R/H/S/D/K: 4.866666666666666/4.8/4.466666666666667/4.9/5.0
- mean overall (avg R/H/S/D/K): 4.806666666666667

## Top missing elements (max 20)
- Keine Kontextnutzung (nur Asset-ID vorhanden): 3
- Offline-Workflow bei spotty connectivity: 2
- Offline-Workflow bei spotty connectivity nicht explizit erwähnt: 2
- Offline-Workflow (device.connectivity=offline): 1
- Klarstellung device.* = Techniker-Gerät: 1
- Keine Nutzung des minimalen Kontexts (nur asset_osm vorhanden): 1
- Keine Anpassung an fehlende Umgebungs-/Device-Infos: 1
- Kein expliziter Offline-Workflow trotz connectivity=spotty: 1
- Device-State (low_battery) wird erwähnt, aber nicht klar als Techniker-Gerät abgegrenzt: 1
- Keine spezifische Priorisierung bei fehlenden Umgebungsdaten: 1
- Kein expliziter Offline-Workflow trotz spotty connectivity: 1
- Low_battery des Geräts nicht als Handlungseinschränkung erwähnt: 1
- Keine Offline-Workflow-Erwähnung (nicht erwartbar bei minimalem Context): 1
- Severity/Traffic-Kontext fehlt (nicht im Context): 1
- Keine explizite Priorisierung bei Absicherung: 1
- Offline-Workflow nicht explizit (Gerät offline + low_battery): 1
- Keine Anweisung 'lokal dokumentieren/später sync': 1
- Offline-Workflow (kein Signal im Kontext): 1
- Foto-Nutzung (kein Signal im Kontext): 1
- Wetter/Sturm (kein Signal im Kontext): 1
