# Aggregation Report (506\gemini-2.5-flash) [signal]
- judge_version filter: **judge_v1_1**
- Tests (latest runs): **90**
- Incidents with any deltas: **30**

## Mean scores by context level (snapshot)
### L0 (n=30)
- mean runtime: 5.904566666666667
- mean R/H/S/D/K: 3.8333333333333335/3.966666666666667/4.1/4.233333333333333/2.7333333333333334
- mean overall (avg R/H/S/D/K): 3.7733333333333334
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.00, hallucination_suspected=0.10
### L2 (n=30)
- mean runtime: 8.8231
- mean R/H/S/D/K: 4.966666666666667/4.9/4.966666666666667/4.966666666666667/4.666666666666667
- mean overall (avg R/H/S/D/K): 4.8933333333333335
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.07, hallucination_suspected=0.00
### L2B (n=30)
- mean runtime: 8.9956
- mean R/H/S/D/K: 4.966666666666667/4.933333333333334/4.933333333333334/4.933333333333334/5.0
- mean overall (avg R/H/S/D/K): 4.953333333333333
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.63, hallucination_suspected=0.00

## Mean scores by strategy (snapshot)
### S0 (n=30)
- mean runtime: 5.904566666666667
- mean R/H/S/D/K: 3.8333333333333335/3.966666666666667/4.1/4.233333333333333/2.7333333333333334
- mean overall (avg R/H/S/D/K): 3.7733333333333334
### S1 (n=30)
- mean runtime: 8.8231
- mean R/H/S/D/K: 4.966666666666667/4.9/4.966666666666667/4.966666666666667/4.666666666666667
- mean overall (avg R/H/S/D/K): 4.8933333333333335
### S2 (n=30)
- mean runtime: 8.9956
- mean R/H/S/D/K: 4.966666666666667/4.933333333333334/4.933333333333334/4.933333333333334/5.0
- mean overall (avg R/H/S/D/K): 4.953333333333333

## Top missing elements (max 20)
- Offline-Workflow (spotty connectivity): 2
- Offline-Workflow explizit (Doku lokal, später sync): 1
- Offline-Workflow explizit erwähnen: 1
- Keine GPS-Koordinaten dokumentiert (nicht im Context verfügbar): 1
- Spekuliert über USV/Notstrom ohne Basis im Context: 1
- Severity-Einschätzung fehlt (nur minimal context): 1
- Keine Priorisierung bei Eskalation erkennbar: 1
- Offline-Workflow (nicht erwartbar, da CONTEXT connectivity nicht offline zeigt): 1
- GPS-Koordinaten explizit genannt (nur Asset-ID vorhanden): 1
- Kontextnutzung minimal (nur Asset-ID): 1
- Keine Priorisierung nach Verkehr/Umgebung: 1
- Generische Antwort ohne Umweltbezug: 1
- Kontextnutzung (Wetter/Zeit/Verkehr nicht erwähnt, da nicht im CONTEXT): 1
- Spezifische Trigger für Eskalation könnten klarer sein: 1
- Severity-Bewusstsein (high nicht erkennbar): 1
- Umgebungsbedingungen (Nacht/Sturm/poor visibility): 1
- Foto-Nutzung: 1
- Foto-Nutzung explizit erwähnen: 1
- Keine Nutzung von Kontextinformationen (minimaler Kontext): 1
- Keine Erwähnung von Umgebungsbedingungen (Wetter/Sicht): 1
