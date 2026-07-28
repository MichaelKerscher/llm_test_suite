# Aggregation Report (506/gpt-4.1) [signal]
- Tests (latest runs): **150**
- Incidents with any deltas: **30**

## Mean scores by context level (snapshot)
### L0 (n=30)
- mean runtime: 8.4522
- mean R/H/S/D/K: 3.9/3.966666666666667/4.1/4.3/2.466666666666667
- mean overall (avg R/H/S/D/K): 3.746666666666667
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.00, hallucination_suspected=0.30
### L2 (n=30)
- mean runtime: 10.557766666666668
- mean R/H/S/D/K: 4.866666666666666/4.8/4.833333333333333/4.9/4.566666666666666
- mean overall (avg R/H/S/D/K): 4.793333333333334
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.13, hallucination_suspected=0.00
### L2B (n=30)
- mean runtime: 10.375333333333334
- mean R/H/S/D/K: 4.966666666666667/4.966666666666667/5.0/4.866666666666666/4.966666666666667
- mean overall (avg R/H/S/D/K): 4.953333333333333
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.63, hallucination_suspected=0.00
### unknown (n=60)
- mean runtime: 10.970949999999998
- mean R/H/S/D/K: 4.666666666666667/4.666666666666667/4.783333333333333/4.783333333333333/4.35
- mean overall (avg R/H/S/D/K): 4.65
- flags (rate): safety_first=0.98, escalation_present=1.00, offline_workflow_mentioned=0.27, hallucination_suspected=0.00

## Mean scores by strategy (snapshot)
### S0 (n=30)
- mean runtime: 8.4522
- mean R/H/S/D/K: 3.9/3.966666666666667/4.1/4.3/2.466666666666667
- mean overall (avg R/H/S/D/K): 3.746666666666667
### S0_RAW (n=30)
- mean runtime: 10.914299999999999
- mean R/H/S/D/K: 4.833333333333333/4.8/4.833333333333333/4.933333333333334/4.633333333333334
- mean overall (avg R/H/S/D/K): 4.806666666666667
### S0_UNSTRUCTURED (n=30)
- mean runtime: 11.0276
- mean R/H/S/D/K: 4.5/4.533333333333333/4.733333333333333/4.633333333333334/4.066666666666666
- mean overall (avg R/H/S/D/K): 4.493333333333334
### S1 (n=30)
- mean runtime: 10.557766666666668
- mean R/H/S/D/K: 4.866666666666666/4.8/4.833333333333333/4.9/4.566666666666666
- mean overall (avg R/H/S/D/K): 4.793333333333334
### S2 (n=30)
- mean runtime: 10.375333333333334
- mean R/H/S/D/K: 4.966666666666667/4.966666666666667/5.0/4.866666666666666/4.966666666666667
- mean overall (avg R/H/S/D/K): 4.953333333333333

## Top missing elements (max 20)
- Kontextnutzung minimal (nur Asset-ID): 6
- Offline-Workflow (nicht erwartbar, da connectivity nicht im Context): 5
- Offline-Workflow nicht explizit erwähnt: 3
- Kontextnutzung minimal (nur Asset-ID vorhanden): 2
- Expliziter Offline-Workflow-Hinweis (spotty connectivity im Context): 2
- Offline-Workflow (Gerät offline nicht erkannt): 1
- Wetter/Sicht-Kontext (Regen, poor_visibility nicht genutzt): 1
- Offline-Workflow (connectivity=offline vorhanden, aber nicht explizit als Dokumentations-Anpassung erwähnt): 1
- Offline-Workflow (connectivity=offline im Kontext, aber nicht explizit adressiert): 1
- Keine Anpassung an fehlende Umwelt-/Severity-Infos: 1
- Kontextnutzung schwach: 1
- Halluzinationen (RSA, Polizei, Induktionsschleifen ohne Kontext-Signal): 1
- Safety-first nicht explizit Schritt 1: 1
- Kontext nur teilweise genutzt (unstrukturiert): 1
- Offline-Workflow nicht erwähnt (aber auch nicht erwartbar aus minimalem Context): 1
- Sporadik-spezifische Beobachtungsmuster fehlen teilweise: 1
- Offline-Workflow nicht explizit (spotty connectivity im Context, aber nicht klar adressiert): 1
- Koordinaten/GPS-Daten nicht erwähnt: 1
- Foto-Status nicht dokumentiert: 1
- Foto-Status nicht explizit als 'vorhanden' dokumentiert: 1
