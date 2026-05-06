# Aggregation Report (506/gpt-4.1) [signal]
- judge_version filter: **judge_v1_1**
- Tests (latest runs): **150**
- Incidents with any deltas: **30**

## Mean scores by context level (snapshot)
### L0 (n=30)
- mean runtime: 7.952833333333333
- mean R/H/S/D/K: 3.8333333333333335/3.8666666666666667/3.8666666666666667/4.2/2.466666666666667
- mean overall (avg R/H/S/D/K): 3.646666666666667
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.00, hallucination_suspected=0.27
### L2 (n=30)
- mean runtime: 10.116966666666666
- mean R/H/S/D/K: 4.9/4.866666666666666/4.9/4.933333333333334/4.666666666666667
- mean overall (avg R/H/S/D/K): 4.8533333333333335
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.13, hallucination_suspected=0.00
### L2B (n=30)
- mean runtime: 10.510666666666667
- mean R/H/S/D/K: 4.966666666666667/4.966666666666667/4.966666666666667/4.933333333333334/4.966666666666667
- mean overall (avg R/H/S/D/K): 4.96
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.57, hallucination_suspected=0.00
### unknown (n=60)
- mean runtime: 10.697283333333333
- mean R/H/S/D/K: 4.65/4.65/4.75/4.75/4.4
- mean overall (avg R/H/S/D/K): 4.64
- flags (rate): safety_first=1.00, escalation_present=1.00, offline_workflow_mentioned=0.23, hallucination_suspected=0.00

## Mean scores by strategy (snapshot)
### S0 (n=30)
- mean runtime: 7.952833333333333
- mean R/H/S/D/K: 3.8333333333333335/3.8666666666666667/3.8666666666666667/4.2/2.466666666666667
- mean overall (avg R/H/S/D/K): 3.646666666666667
### S0_RAW (n=30)
- mean runtime: 10.884466666666667
- mean R/H/S/D/K: 4.866666666666666/4.866666666666666/4.866666666666666/4.9/4.766666666666667
- mean overall (avg R/H/S/D/K): 4.8533333333333335
### S0_UNSTRUCTURED (n=30)
- mean runtime: 10.5101
- mean R/H/S/D/K: 4.433333333333334/4.433333333333334/4.633333333333334/4.6/4.033333333333333
- mean overall (avg R/H/S/D/K): 4.426666666666667
### S1 (n=30)
- mean runtime: 10.116966666666666
- mean R/H/S/D/K: 4.9/4.866666666666666/4.9/4.933333333333334/4.666666666666667
- mean overall (avg R/H/S/D/K): 4.8533333333333335
### S2 (n=30)
- mean runtime: 10.510666666666667
- mean R/H/S/D/K: 4.966666666666667/4.966666666666667/4.966666666666667/4.933333333333334/4.966666666666667
- mean overall (avg R/H/S/D/K): 4.96

## Top missing elements (max 20)
- Kontextnutzung minimal (nur Asset-ID): 3
- Keine Nutzung der Asset-ID im Kontext: 2
- Offline-Workflow (nicht erwartbar, da connectivity nicht im Context): 2
- Offline-Workflow nicht erwähnt trotz 'spotty' connectivity: 2
- offline_workflow: 2
- offline_workflow_explicit: 2
- Offline-Workflow (offline/low_power_mode im CONTEXT, aber nicht explizit adressiert): 2
- Offline-Workflow (spotty connectivity) nicht explizit erwähnt: 2
- Offline-Workflow (nicht erwartbar, da CONTEXT kein offline-Signal enthält): 1
- Spekulation über 'backward' und 'unknown' ohne Basis im CONTEXT: 1
- Offline-Workflow nicht explizit erwähnt (trotz offline/low_battery im CONTEXT): 1
- Offline-Workflow nicht explizit genannt (aber offline-Status erkannt): 1
- Offline-Workflow (manuelle Notizen, spätere Synchronisation) nicht explizit erwähnt: 1
- Offline-Workflow (nicht erwartbar, da connectivity nicht im CONTEXT): 1
- Offline-Workflow (spotty connectivity im CONTEXT, aber nicht explizit adressiert): 1
- Keine GPS-Koordinaten erwähnt (nicht im Context verfügbar): 1
- Halluzinationen: Stromversorgung, Sicherungskasten, Schaltschrank ohne Kontext-Basis: 1
- Spannungsmessung ohne Geräte-Info im Kontext: 1
- Spezifische Hinweise auf freiliegende Kabel (nicht im Context): 1
- Gerätezustand (nicht im Context): 1
