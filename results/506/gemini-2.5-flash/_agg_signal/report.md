# Aggregation Report (506\gemini-2.5-flash) [signal]
- judge_version filter: **judge_v1_1**
- Tests (latest runs): **90**
- Incidents with any deltas: **30**

## Mean scores by context level (snapshot)
### L0 (n=30)
- mean runtime: 6.5145
- mean R/H/S/D/K: 3.8/3.9/3.9/4.133333333333334/2.566666666666667
- mean overall (avg R/H/S/D/K): 3.6599999999999997
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.00, hallucination_suspected=0.27
### L2 (n=30)
- mean runtime: 8.417266666666666
- mean R/H/S/D/K: 4.9/4.733333333333333/4.766666666666667/4.9/4.533333333333333
- mean overall (avg R/H/S/D/K): 4.766666666666667
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.10, hallucination_suspected=0.00
### L2B (n=30)
- mean runtime: 8.495766666666666
- mean R/H/S/D/K: 4.966666666666667/4.833333333333333/4.9/4.966666666666667/4.966666666666667
- mean overall (avg R/H/S/D/K): 4.926666666666667
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.57, hallucination_suspected=0.00

## Mean scores by strategy (snapshot)
### S0 (n=30)
- mean runtime: 6.5145
- mean R/H/S/D/K: 3.8/3.9/3.9/4.133333333333334/2.566666666666667
- mean overall (avg R/H/S/D/K): 3.6599999999999997
### S1 (n=30)
- mean runtime: 8.417266666666666
- mean R/H/S/D/K: 4.9/4.733333333333333/4.766666666666667/4.9/4.533333333333333
- mean overall (avg R/H/S/D/K): 4.766666666666667
### S2 (n=30)
- mean runtime: 8.495766666666666
- mean R/H/S/D/K: 4.966666666666667/4.833333333333333/4.9/4.966666666666667/4.966666666666667
- mean overall (avg R/H/S/D/K): 4.926666666666667

## Top missing elements (max 20)
- Offline-Workflow explizit erwähnen: 2
- Offline-Workflow bei spotty connectivity nicht explizit erwähnt: 2
- Offline-Workflow (Dokumentation lokal, spätere Sync): 1
- Keine Nutzung des minimalen Kontexts (nur asset_osm vorhanden): 1
- Spekuliert über nicht vorhandene Kontextinformationen (Notstrom, Schaltkasten): 1
- Severity-Bewusstsein (high): 1
- Kreuzung wie unbeschrankt behandeln: 1
- Umgebungsbedingungen (Wetter/Sicht) nicht erwähnt: 1
- Offline-Workflow nicht erwähnt (kein Signal im Kontext): 1
- Spekulative Details zu Ampel/Leuchte ohne Kontext: 1
- Überdetaillierte Maßnahmen ohne Kontextbasis: 1
- Offline-Workflow nicht explizit (spotty connectivity erwähnt, aber kein lokaler Workflow): 1
- Keine Nachfrage nach Asset-Typ: 1
- Severity-Einschätzung fehlt (kein Kontext vorhanden): 1
- Wetter/Sicht nicht erwähnt (kein Kontext vorhanden): 1
- Kontextnutzung (Umgebung, Severity, Traffic): 1
- Spezifische Priorisierung nach Severity: 1
- Keine Nutzung von Umgebungskontext (nicht vorhanden): 1
- Keine Priorisierung nach Severity (nicht vorhanden): 1
- Severity/Kontext-Nutzung schwach (nur minimal-Context): 1
