# Aggregation Report (506\gemini-2.5-flash) [signal]
- judge_version filter: **judge_v1_1**
- Tests (latest runs): **90**
- Incidents with any deltas: **30**

## Mean scores by context level (snapshot)
### L0 (n=30)
- mean runtime: 6.427966666666666
- mean R/H/S/D/K: 3.8333333333333335/3.9/3.966666666666667/4.166666666666667/2.6666666666666665
- mean overall (avg R/H/S/D/K): 3.7066666666666666
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.00, hallucination_suspected=0.13
### L2 (n=30)
- mean runtime: 8.722166666666668
- mean R/H/S/D/K: 4.9/4.766666666666667/4.733333333333333/5.0/4.666666666666667
- mean overall (avg R/H/S/D/K): 4.8133333333333335
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.27, hallucination_suspected=0.00
### L2B (n=30)
- mean runtime: 8.880066666666666
- mean R/H/S/D/K: 4.966666666666667/4.933333333333334/4.9/5.0/5.0
- mean overall (avg R/H/S/D/K): 4.96
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.53, hallucination_suspected=0.00

## Mean scores by strategy (snapshot)
### S0 (n=30)
- mean runtime: 6.427966666666666
- mean R/H/S/D/K: 3.8333333333333335/3.9/3.966666666666667/4.166666666666667/2.6666666666666665
- mean overall (avg R/H/S/D/K): 3.7066666666666666
### S1 (n=30)
- mean runtime: 8.722166666666668
- mean R/H/S/D/K: 4.9/4.766666666666667/4.733333333333333/5.0/4.666666666666667
- mean overall (avg R/H/S/D/K): 4.8133333333333335
### S2 (n=30)
- mean runtime: 8.880066666666666
- mean R/H/S/D/K: 4.966666666666667/4.933333333333334/4.9/5.0/5.0
- mean overall (avg R/H/S/D/K): 4.96

## Top missing elements (max 20)
- Kontextnutzung minimal (nur Asset-ID): 5
- Keine Anpassung an Umgebungsbedingungen: 2
- Offline-Workflow (lokale Doku, spätere Sync) nicht explizit erwähnt: 1
- Offline-Workflow nicht explizit erwähnt trotz connectivity=offline: 1
- Kontext-Nutzung minimal (nur Asset-ID verfügbar): 1
- Keine Nutzung der Asset-ID im Kontext: 1
- Übermäßige Detailtiefe ohne Kontextbasis (RSA, Induktionsschleifen, Radarsensoren): 1
- Spekulative technische Details (Belastungstest, Spannungsmessung) ohne Hinweis im Kontext: 1
- Generische Antwort ohne spezifische Priorisierung: 1
- Offline-Workflow (spotty connectivity): 1
- Severity-Einschätzung aus Kontext: 1
- Konkrete GPS-Koordinaten in Doku: 1
- Severity-Bewusstsein (high nicht erkennbar aus Kontext): 1
- Wetter-/Sichtbedingungen (nicht im Kontext vorhanden): 1
- Priorisierung Eskalation bei high severity: 1
- Offline-Workflow (spotty connectivity + low_battery): 1
- Offline-Workflow (nicht erwartbar aus minimalem Context): 1
- Spekulation über 'backward'-Bedeutung ohne Basis: 1
- Keine Nutzung von Kontext-Signalen (severity, environment): 1
- Keine Priorisierung nach Verkehrslage/Sichtbedingungen: 1
