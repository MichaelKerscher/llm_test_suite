# Aggregation Report (506/gemini-2.5-flash) [lamp]
- judge_version filter: **judge_v1_1**
- Tests (latest runs): **270**
- Incidents with any deltas: **30**

## Mean scores by context level (snapshot)
### L0 (n=30)
- mean runtime: 7.488833333333333
- mean R/H/S/D/K: 3.6/3.7666666666666666/3.7666666666666666/3.966666666666667/2.6
- mean overall (avg R/H/S/D/K): 3.54
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.00, hallucination_suspected=0.10
### L2 (n=30)
- mean runtime: 10.395733333333334
- mean R/H/S/D/K: 4.833333333333333/4.8/4.833333333333333/4.833333333333333/4.333333333333333
- mean overall (avg R/H/S/D/K): 4.7266666666666675
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.03, hallucination_suspected=0.03
### L2B (n=30)
- mean runtime: 11.167
- mean R/H/S/D/K: 5.0/5.0/4.966666666666667/5.0/5.0
- mean overall (avg R/H/S/D/K): 4.993333333333334
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.60, hallucination_suspected=0.00
### unknown (n=180)
- mean runtime: 9.593277777777777
- mean R/H/S/D/K: 4.7444444444444445/4.727777777777778/4.777777777777778/4.855555555555555/4.711111111111111
- mean overall (avg R/H/S/D/K): 4.763333333333334
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.40, hallucination_suspected=0.00

## Mean scores by strategy (snapshot)
### S0 (n=30)
- mean runtime: 7.488833333333333
- mean R/H/S/D/K: 3.6/3.7666666666666666/3.7666666666666666/3.966666666666667/2.6
- mean overall (avg R/H/S/D/K): 3.54
### S0_RAW (n=30)
- mean runtime: 9.8911
- mean R/H/S/D/K: 4.666666666666667/4.666666666666667/4.766666666666667/4.8/4.566666666666666
- mean overall (avg R/H/S/D/K): 4.693333333333333
### S0_UNSTRUCTURED (n=30)
- mean runtime: 10.3963
- mean R/H/S/D/K: 4.333333333333333/4.3/4.533333333333333/4.533333333333333/3.8333333333333335
- mean overall (avg R/H/S/D/K): 4.306666666666667
### S1 (n=30)
- mean runtime: 10.395733333333334
- mean R/H/S/D/K: 4.833333333333333/4.8/4.833333333333333/4.833333333333333/4.333333333333333
- mean overall (avg R/H/S/D/K): 4.7266666666666675
### S2 (n=30)
- mean runtime: 11.167
- mean R/H/S/D/K: 5.0/5.0/4.966666666666667/5.0/5.0
- mean overall (avg R/H/S/D/K): 4.993333333333334
### S2_ABL_NOASSET (n=30)
- mean runtime: 9.480966666666665
- mean R/H/S/D/K: 4.9/4.933333333333334/4.866666666666666/4.966666666666667/5.0
- mean overall (avg R/H/S/D/K): 4.933333333333334
### S2_ABL_NODEV (n=30)
- mean runtime: 8.9771
- mean R/H/S/D/K: 4.933333333333334/4.866666666666666/4.866666666666666/5.0/5.0
- mean overall (avg R/H/S/D/K): 4.933333333333334
### S2_ABL_NOENV (n=30)
- mean runtime: 9.661033333333334
- mean R/H/S/D/K: 4.866666666666666/4.766666666666667/4.766666666666667/4.9/4.933333333333334
- mean overall (avg R/H/S/D/K): 4.846666666666667
### S2_ABL_NOINC (n=30)
- mean runtime: 9.153166666666667
- mean R/H/S/D/K: 4.766666666666667/4.833333333333333/4.866666666666666/4.933333333333334/4.933333333333334
- mean overall (avg R/H/S/D/K): 4.866666666666666

## Top missing elements (max 20)
- offline_workflow: 4
- Offline-Workflow (spotty connectivity): 2
- offline_workflow_explicit: 2
- Offline-Workflow (nicht erwartbar, da connectivity nicht im CONTEXT): 2
- Offline-Workflow (erwartbar wegen spotty connectivity): 2
- Offline-Workflow explizit erwähnt: 2
- Kontextnutzung (Kontext minimal, aber Antwort nutzt ihn nicht sichtbar): 1
- Foto-Workflow (kein Hinweis auf vorhandenes Foto): 1
- Umgebungsbedingungen (Nebel/Nacht/Verkehr nicht erwähnt): 1
- Leichte Redundanz in Struktur (sehr ausführlich, könnte kompakter sein): 1
- Offline-Workflow nicht erwähnt (aber auch nicht erwartbar, da connectivity nicht im CONTEXT): 1
- Offline-Workflow fehlt trotz spotty connectivity: 1
- Halluzination: 'Gerätezustand low_battery' als mögliche Ursache für Lampenausfall interpretiert (device.* beschreibt Techniker-Gerät, nicht Asset): 1
- Offline-Workflow nicht explizit erwähnt, obwohl spotty connectivity im CONTEXT: 1
- Explizite Ticket-ID-Erfassung: 1
- Zeitstempel-Dokumentation: 1
- Explizite Stop-Conditions für Abbruch: 1
- Offline-Workflow (spotty connectivity vorhanden, aber nicht in Handlungsempfehlungen integriert): 1
- Offline-Workflow (spotty connectivity erkennbar, aber nicht explizit adressiert): 1
- Offline-Workflow (nicht erwartbar, da CONTEXT kein connectivity-Signal enthält): 1
