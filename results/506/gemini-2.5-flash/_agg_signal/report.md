# Aggregation Report (506\gemini-2.5-flash) [signal]
- judge_version filter: **judge_v1_1**
- Tests (latest runs): **90**
- Incidents with any deltas: **30**

## Mean scores by context level (snapshot)
### L0 (n=30)
- mean runtime: 6.1133999999999995
- mean R/H/S/D/K: 3.8/3.8666666666666667/3.8666666666666667/4.166666666666667/2.7666666666666666
- mean overall (avg R/H/S/D/K): 3.6933333333333334
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.00, hallucination_suspected=0.03
### L2 (n=30)
- mean runtime: 8.281633333333334
- mean R/H/S/D/K: 4.833333333333333/4.833333333333333/4.833333333333333/4.9/4.466666666666667
- mean overall (avg R/H/S/D/K): 4.7733333333333325
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.10, hallucination_suspected=0.03
### L2B (n=30)
- mean runtime: 8.1765
- mean R/H/S/D/K: 4.9/4.9/4.933333333333334/4.933333333333334/5.0
- mean overall (avg R/H/S/D/K): 4.933333333333334
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.60, hallucination_suspected=0.00

## Mean scores by strategy (snapshot)
### S0 (n=30)
- mean runtime: 6.1133999999999995
- mean R/H/S/D/K: 3.8/3.8666666666666667/3.8666666666666667/4.166666666666667/2.7666666666666666
- mean overall (avg R/H/S/D/K): 3.6933333333333334
### S1 (n=30)
- mean runtime: 8.281633333333334
- mean R/H/S/D/K: 4.833333333333333/4.833333333333333/4.833333333333333/4.9/4.466666666666667
- mean overall (avg R/H/S/D/K): 4.7733333333333325
### S2 (n=30)
- mean runtime: 8.1765
- mean R/H/S/D/K: 4.9/4.9/4.933333333333334/4.933333333333334/5.0
- mean overall (avg R/H/S/D/K): 4.933333333333334

## Top missing elements (max 20)
- Offline-Workflow bei spotty connectivity nicht explizit erwähnt: 2
- Offline-Workflow bei spotty connectivity: 2
- Offline-Workflow (nicht erwartbar bei L0_minimal): 2
- Offline-Workflow explizit erwähnen: 1
- Offline-Workflow (nicht erwartbar, da CONTEXT kein connectivity-Signal enthält): 1
- Wetter/Sicht-Anpassungen (nicht erwartbar, da CONTEXT keine environment-Daten enthält): 1
- Offline-Workflow explizit (connectivity=offline im CONTEXT, aber nicht klar als 'lokale Doku, später sync' formuliert): 1
- Foto-Status explizit erwähnen (photo_available=true): 1
- Severity-Bewusstsein (high severity nicht erkennbar aus minimalem Kontext): 1
- Kreuzung als unreguliert behandeln (nicht explizit): 1
- Priorisierung Eskalation vor Diagnose bei kritischem Fehler: 1
- Keine Erwähnung der Hauptverkehrszeit als Beobachtungszeitpunkt: 1
- Keine spezifische Priorisierung für intermittierende Fehler: 1
- Kontextnutzung minimal (nur Asset-ID): 1
- Halluzination: Annahme 'Ampelanlage' ohne Basis: 1
- Keine Anpassung an fehlende Umgebungsdaten: 1
- Offline-Workflow nicht explizit (spotty connectivity): 1
- Offline-Workflow (spotty connectivity) nicht explizit erwähnt: 1
- Kontextnutzung minimal (nur Asset-ID vorhanden): 1
- Keine Nutzung von Foto-Info (nicht im Context): 1
