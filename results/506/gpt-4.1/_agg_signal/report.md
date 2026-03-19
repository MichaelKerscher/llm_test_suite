# Aggregation Report (506\gpt-4.1) [signal]
- judge_version filter: **judge_v1_1**
- Tests (latest runs): **90**
- Incidents with any deltas: **30**

## Mean scores by context level (snapshot)
### L0 (n=30)
- mean runtime: 7.207
- mean R/H/S/D/K: 3.8666666666666667/3.9/4.066666666666666/4.2/2.8666666666666667
- mean overall (avg R/H/S/D/K): 3.7800000000000002
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.00, hallucination_suspected=0.10
### L2 (n=30)
- mean runtime: 8.833400000000001
- mean R/H/S/D/K: 4.933333333333334/4.833333333333333/4.866666666666666/4.9/4.666666666666667
- mean overall (avg R/H/S/D/K): 4.84
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.20, hallucination_suspected=0.00
### L2B (n=30)
- mean runtime: 9.833566666666666
- mean R/H/S/D/K: 4.966666666666667/4.866666666666666/4.833333333333333/4.933333333333334/4.966666666666667
- mean overall (avg R/H/S/D/K): 4.913333333333333
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.63, hallucination_suspected=0.00

## Mean scores by strategy (snapshot)
### S0 (n=30)
- mean runtime: 7.207
- mean R/H/S/D/K: 3.8666666666666667/3.9/4.066666666666666/4.2/2.8666666666666667
- mean overall (avg R/H/S/D/K): 3.7800000000000002
### S1 (n=30)
- mean runtime: 8.833400000000001
- mean R/H/S/D/K: 4.933333333333334/4.833333333333333/4.866666666666666/4.9/4.666666666666667
- mean overall (avg R/H/S/D/K): 4.84
### S2 (n=30)
- mean runtime: 9.833566666666666
- mean R/H/S/D/K: 4.966666666666667/4.866666666666666/4.833333333333333/4.933333333333334/4.966666666666667
- mean overall (avg R/H/S/D/K): 4.913333333333333

## Top missing elements (max 20)
- Kontextnutzung minimal (nur Asset-ID): 2
- Offline-Workflow (lokale Doku, spätere Sync): 1
- Offline-Workflow explizit (spotty connectivity): 1
- Offline-Workflow (spotty connectivity + low_battery): 1
- Severity-basierte Priorisierung: 1
- Umgebungsbedingungen (Wetter/Verkehr/Sicht): 1
- Spekuliert über Ampel/Lampe ohne Kontext: 1
- Keine Anpassung an tatsächliche Umgebung: 1
- Keine explizite Beobachtungsdauer genannt: 1
- Ticket-Struktur könnte klarer sein: 1
- Severity-Einschätzung fehlt (kein Kontext vorhanden): 1
- Umgebungsbedingungen nicht berücksichtigt (kein Kontext): 1
- Severity-angepasste Eskalation (high severity nicht erkennbar aus Kontext): 1
- Spotty connectivity → Offline-Workflow nicht erwähnt (aber auch nicht im Kontext): 1
- Offline-Workflow bei spotty connectivity nicht explizit erwähnt: 1
- Offline-Workflow (nicht erwartbar bei L0): 1
- Kreuzung als unbeschrankt behandeln (nicht explizit): 1
- Wetter/Sicht-Anpassungen (nicht im Context): 1
- Offline-Workflow (spotty connectivity nicht explizit adressiert): 1
- Offline-Workflow (spotty connectivity) nicht explizit erwähnt: 1
