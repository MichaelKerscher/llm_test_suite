# Aggregation Report (506\gemini-2.5-flash) [signal]
- judge_version filter: **judge_v1_1**
- Tests (latest runs): **90**
- Incidents with any deltas: **30**

## Mean scores by context level (snapshot)
### L0 (n=30)
- mean runtime: 6.489633333333333
- mean R/H/S/D/K: 3.7666666666666666/3.9/3.8666666666666667/4.1/2.7
- mean overall (avg R/H/S/D/K): 3.6666666666666665
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.00, hallucination_suspected=0.13
### L2 (n=30)
- mean runtime: 8.773766666666667
- mean R/H/S/D/K: 4.9/4.833333333333333/4.8/4.966666666666667/4.6
- mean overall (avg R/H/S/D/K): 4.819999999999999
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.20, hallucination_suspected=0.00
### L2B (n=30)
- mean runtime: 8.962066666666667
- mean R/H/S/D/K: 4.966666666666667/4.966666666666667/4.9/4.933333333333334/4.966666666666667
- mean overall (avg R/H/S/D/K): 4.946666666666667
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.63, hallucination_suspected=0.00

## Mean scores by strategy (snapshot)
### S0 (n=30)
- mean runtime: 6.489633333333333
- mean R/H/S/D/K: 3.7666666666666666/3.9/3.8666666666666667/4.1/2.7
- mean overall (avg R/H/S/D/K): 3.6666666666666665
### S1 (n=30)
- mean runtime: 8.773766666666667
- mean R/H/S/D/K: 4.9/4.833333333333333/4.8/4.966666666666667/4.6
- mean overall (avg R/H/S/D/K): 4.819999999999999
### S2 (n=30)
- mean runtime: 8.962066666666667
- mean R/H/S/D/K: 4.966666666666667/4.966666666666667/4.9/4.933333333333334/4.966666666666667
- mean overall (avg R/H/S/D/K): 4.946666666666667

## Top missing elements (max 20)
- Offline-Workflow bei spotty connectivity nicht explizit erwähnt: 2
- Severity-Bewertung fehlt (kein Kontext vorhanden): 1
- Umweltbedingungen nicht erwähnt (kein Kontext vorhanden): 1
- Keine GPS-Koordinaten dokumentiert (nicht im Context): 1
- Keine explizite Priorisierung bei erneutem Ausfall während Rush Hour: 1
- Kontextnutzung minimal (nur Asset-ID): 1
- Keine Anpassung an Umgebungsbedingungen: 1
- Keine Offline-Workflow-Erwähnung trotz fehlendem Kontext: 1
- Offline-Workflow nicht explizit erwähnt trotz spotty connectivity: 1
- Severity-Einschätzung fehlt (kein Signal im Kontext): 1
- Keine Priorisierung bei minimalem Kontext erkennbar: 1
- Offline-Workflow (spotty connectivity + low_battery): 1
- Kontextnutzung minimal (nur Asset-ID vorhanden): 1
- Erfundene Details (RSA, Kran, Kabelbrüche) nicht im Context: 1
- Severity/Traffic/Weather nicht bekannt, aber behandelt: 1
- Kontextnutzung (traffic_exposure, noise_level, time_of_day nicht erwähnt, da nicht im CONTEXT): 1
- Keine Nachfrage nach fehlenden Infos (severity, fault_type, environment): 1
- GPS-Koordinaten nicht explizit in Doku genannt: 1
- Severity-Einschätzung fehlt (nur Asset-ID vorhanden): 1
- Keine Priorisierung nach Verkehrslage/Umwelt: 1
