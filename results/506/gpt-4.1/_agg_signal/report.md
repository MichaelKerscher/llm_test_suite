# Aggregation Report (506\gpt-4.1) [signal]
- judge_version filter: **judge_v1_1**
- Tests (latest runs): **90**
- Incidents with any deltas: **30**

## Mean scores by context level (snapshot)
### L0 (n=30)
- mean runtime: 6.926233333333333
- mean R/H/S/D/K: 3.8666666666666667/3.966666666666667/3.933333333333333/4.2/2.7333333333333334
- mean overall (avg R/H/S/D/K): 3.74
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.00, hallucination_suspected=0.13
### L2 (n=30)
- mean runtime: 9.854066666666666
- mean R/H/S/D/K: 4.966666666666667/4.9/4.866666666666666/5.0/4.666666666666667
- mean overall (avg R/H/S/D/K): 4.88
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.20, hallucination_suspected=0.00
### L2B (n=30)
- mean runtime: 9.366466666666668
- mean R/H/S/D/K: 4.966666666666667/4.966666666666667/4.9/4.933333333333334/4.966666666666667
- mean overall (avg R/H/S/D/K): 4.946666666666667
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.57, hallucination_suspected=0.00

## Mean scores by strategy (snapshot)
### S0 (n=30)
- mean runtime: 6.926233333333333
- mean R/H/S/D/K: 3.8666666666666667/3.966666666666667/3.933333333333333/4.2/2.7333333333333334
- mean overall (avg R/H/S/D/K): 3.74
### S1 (n=30)
- mean runtime: 9.854066666666666
- mean R/H/S/D/K: 4.966666666666667/4.9/4.866666666666666/5.0/4.666666666666667
- mean overall (avg R/H/S/D/K): 4.88
### S2 (n=30)
- mean runtime: 9.366466666666668
- mean R/H/S/D/K: 4.966666666666667/4.966666666666667/4.9/4.933333333333334/4.966666666666667
- mean overall (avg R/H/S/D/K): 4.946666666666667

## Top missing elements (max 20)
- Kontextnutzung minimal (nur Asset-ID): 3
- Offline-Workflow bei spotty connectivity nicht explizit erwähnt: 2
- Offline-Workflow (nicht erwartbar, da CONTEXT kein connectivity-Signal enthält): 1
- Wetter/Sicht-Anpassungen (nicht erwartbar, da CONTEXT keine environment-Daten enthält): 1
- Severity/Traffic nicht aus Kontext abgeleitet: 1
- Spekulative Details (UVV, Sicherungskasten, Steuergerät-Reset): 1
- Foto-Nutzung nicht explizit erwähnt (photo_available=true): 1
- Severity-Bewusstsein (high severity nicht erkennbar aus Kontext): 1
- Umgebungsfaktoren (Wetter/Sicht nicht verfügbar): 1
- Keine Nutzung von Kontext-Signalen (rush_hour, high traffic): 1
- Keine Priorisierung auf intermittent fault pattern: 1
- Keine Anpassung an Umgebung/Wetter/Zeit: 1
- Keine Offline-Workflow-Erwähnung trotz fehlendem Kontext: 1
- Offline-Workflow nicht explizit (trotz spotty connectivity): 1
- Kontextnutzung minimal (nur Asset-ID vorhanden): 1
- Spekuliert über Notstromversorgung ohne Kontext-Basis: 1
- Erwähnt Stromausfall/Straßenbeleuchtung ohne Signal dafür: 1
- Severity-Bewusstsein (high nicht erkennbar aus Kontext): 1
- Wetter-/Sichtbedingungen (nicht im Kontext vorhanden): 1
- Polizei-Einbindung (bei high severity + storm + poor visibility sinnvoll): 1
