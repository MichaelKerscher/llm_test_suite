# Aggregation Report (506\gemini-2.5-flash) [signal]
- judge_version filter: **judge_v1_1**
- Tests (latest runs): **90**
- Incidents with any deltas: **30**

## Mean scores by context level (snapshot)
### L0 (n=30)
- mean runtime: 6.138533333333333
- mean R/H/S/D/K: 3.7666666666666666/3.9/4.066666666666666/4.133333333333334/2.7333333333333334
- mean overall (avg R/H/S/D/K): 3.7199999999999998
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.00, hallucination_suspected=0.13
### L2 (n=30)
- mean runtime: 8.556266666666666
- mean R/H/S/D/K: 4.833333333333333/4.766666666666667/4.8/4.866666666666666/4.5
- mean overall (avg R/H/S/D/K): 4.753333333333333
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.17, hallucination_suspected=0.03
### L2B (n=30)
- mean runtime: 9.4974
- mean R/H/S/D/K: 4.9/4.9/4.866666666666666/4.966666666666667/4.933333333333334
- mean overall (avg R/H/S/D/K): 4.913333333333333
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.63, hallucination_suspected=0.00

## Mean scores by strategy (snapshot)
### S0 (n=30)
- mean runtime: 6.138533333333333
- mean R/H/S/D/K: 3.7666666666666666/3.9/4.066666666666666/4.133333333333334/2.7333333333333334
- mean overall (avg R/H/S/D/K): 3.7199999999999998
### S1 (n=30)
- mean runtime: 8.556266666666666
- mean R/H/S/D/K: 4.833333333333333/4.766666666666667/4.8/4.866666666666666/4.5
- mean overall (avg R/H/S/D/K): 4.753333333333333
### S2 (n=30)
- mean runtime: 9.4974
- mean R/H/S/D/K: 4.9/4.9/4.866666666666666/4.966666666666667/4.933333333333334
- mean overall (avg R/H/S/D/K): 4.913333333333333

## Top missing elements (max 20)
- Offline-Workflow bei spotty connectivity nicht explizit erwähnt: 3
- Offline-Workflow (nicht erwartbar, da kein Signal im Context): 2
- Kontextnutzung minimal (nur Asset-ID vorhanden): 2
- Keine Anpassung an fehlende Umgebungs-/Severity-Infos: 2
- Offline-Workflow (lokale Dokumentation, spätere Sync): 1
- Keine GPS-Koordinaten dokumentiert (nicht im Context verfügbar): 1
- Keine explizite Erwähnung von severity=high: 1
- Severity-Einschätzung fehlt (kein Kontext vorhanden): 1
- Umgebungsbedingungen nicht berücksichtigt: 1
- GPS-Koordinaten nicht explizit in Doku erwähnt: 1
- Keine Nutzung des Kontexts (nur Asset-ID vorhanden): 1
- Keine Erwähnung von intermittent fault_type: 1
- Keine Priorisierung basierend auf rush_hour/high_traffic: 1
- Offline-Workflow explizit (spotty connectivity): 1
- Offline-Workflow (spotty connectivity) nicht explizit erwähnt: 1
- Keine Nutzung von Umgebungs-/Severity-Kontext (nicht vorhanden): 1
- Keine Erwähnung von Foto (nicht im Context): 1
- Kontextnutzung minimal (nur Asset-ID): 1
- Spekuliert über Stromschlag/Elektrik ohne Kontext-Signal: 1
- Konkrete Timing-Beobachtungsanleitung schwach: 1
