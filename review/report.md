# Übergabe: Reliabilitätsstudie zum LLM-as-judge

Dieses Dokument fasst einen separaten Chat zusammen, in dem
die vierte Forschungslücke aus §2.5 (LLM-as-a-judge ist für operative Rubriken
nicht validiert) durch eine unabhängige Zweitbewertung teilweise geschlossen
wurde. Es enthält den Ablauf, die Befunde, die daraus folgenden Korrekturen an
Code und Text sowie die fertigen Formulierungen für die Arbeit.

---

## 1. Was gemacht wurde

Eine vollfaktorielle Stichprobe von 30 Antworten aus dem Primärlauf
`results_single` wurde gezogen und ohne Sicht auf die Judge-Scores gegen
dieselbe Rubrik (R, H, S, D, K) und dieselben Verhaltensurteile nachbewertet.
Erst danach wurde mit den Judge-Scores verglichen.

**Keine zusätzlichen LLM-Läufe.** Es wurden ausschließlich vorhandene Logs
gelesen. Der Zweitbewerter war ein Modell derselben Familie wie der Judge.

### Artefakte im Repository

| Datei | Inhalt |
|---|---|
| `scripts/sample_blind_review.py` | Ziehung, erzeugt Blind-Pack, Manifest, versiegelte Judge-Scores |
| `scripts/check_judge_prompt.py` | Rekonstruiert den Judge-Prompt lokal, ohne API-Aufruf |
| `review/blind_pack.md` | 30 Fälle: User-Message, Judge-Kontext, Antworttext, ohne Scores |
| `review/sample_manifest.csv` | Zuordnung Blind-ID → test_id, Domäne, Modell, Strategie, Lauf |
| `review/sealed_judge.json` | Judge-Scores und Flags, erst nach Abschluss geöffnet |
| `review/independent_scores.json` | Eigene Bewertungen mit Kriterien und Einzelbegründungen |

### Vorregistriertes Ziehungskriterium

2 Domänen × 3 Backends × 5 Strategien = 30 Zellen. Pro Zelle ein Incident,
gezogen mit `random.Random(42)` aus der sortierten Liste der verfügbaren
`incident_id`, ohne Zurücklegen innerhalb einer Domäne; anschließend ein Lauf
aus den zehn Wiederholungen desselben Testcase, mit demselben Generator.
Lesereihenfolge gemischt. Ergebnis: 6 Fälle je Strategie, 10 je Backend,
15 je Domäne.

### Vorregistrierte Auswertung

Diese Festlegungen wurden **vor** der Bewertung getroffen, weil vier der fünf
Dimensionen in den Aggregaten zwischen 4,85 und 5,00 liegen und eine
Übereinstimmungszahl dort trivial hoch ausfällt.

1. **Primär — Sättigungsreproduktion.** Eine Dimension gilt als gesättigt bei
   Mittelwert ≥ 4,85 **und** Höchstwert-Anteil ≥ 80 %. Frage: Legt ein
   unabhängiger Durchgang dieselben vier Dimensionen ans Limit und trennt nur K?
2. **Sekundär — Übereinstimmung je Dimension.** Exakt, |Abweichung| ≤ 1, und
   mittlere vorzeichenbehaftete Differenz (die zeigt Richtung auch unter Sättigung).
3. **Tertiär — K allein.** Spearman nur hier, weil nur hier Streuung existiert.
   Bei nahezu varianzloser Variable ist Pearson/Spearman instabil bis undefiniert.

### Verhaltensurteile, getrennt erfasst

* **MENTION** — die Antwort nimmt Bezug auf Konnektivität, Netz, Empfang oder Offline-Zustand.
* **ADAPT** — die Antwort schreibt mindestens einen ohne Verbindung ausführbaren
  Schritt vor oder macht das Vorgehen vom Verbindungszustand abhängig.

Beide unabhängig voneinander, alle vier Kreuztabellenzellen erfasst.

---

## 2. Befunde aus dem Code (vor der Bewertung, lokal verifiziert)

Diese drei Punkte wurden mit `check_judge_prompt.py` belegt, ohne API-Aufruf.
Sie betreffen die Beschreibung des Judging-Protokolls im Text.

### 2.1 Expected Elements haben den Judge nie erreicht

`test_loader.load_testcases_from_csv` schreibt in `input.meta` genau vier
Schlüssel: `incident_id`, `context_level`, `strategy`, `csv_row`.
`test_runner` liest `meta.get("expected_elements_short", "")` — der Schlüssel
existiert nicht, der Default greift, der EXPECTED-ELEMENTS-Block im
Judge-Prompt war in **allen** Läufen leer. Aus derselben Ursache stand in der
Kopfzeile `Fault-Type: unknown, Domain: unknown`. Gilt für beide Modi.

Konsequenz für die Interpretation: Die Score-Heuristik der Rollenbeschreibung
(„0–1 erfüllt → Score 1–2", „6+ erfüllt → Score 5") war nie bindend, weil
nichts zu zählen war. Der Judge hat ausschließlich nach den 1/3/5-Ankern
bewertet — und die belohnen genau die Struktur, die die
Generator-Rollenbeschreibung vorschreibt. Das ist der Mechanismus hinter der
Sättigung, und er ist jetzt belegbar statt vermutet.

**Zu prüfen:** Falls Kapitel 5 oder 6 die Expected Elements als Bestandteil des
Judging-Protokolls beschreibt, muss das korrigiert werden.

### 2.2 Judge-Kontext der unstrukturierten Varianten

Der Kommentar in `_build_judge_prompt_single` sagt, S0_raw und S0_unstructured
würden gegen den ursprünglichen vierdimensionalen Kontext bewertet. Der
Datenfluss macht das nicht: `original_context = dict(input.context)` kopiert
die Korpuszeile, und die enthält bei TC4/TC5 bereits die abgeflachte
Repräsentation. Der Judge sieht also `{"_raw_text": ...}` bzw.
`{"_unstructured_text": ...}`.

Bei S0_raw ist das inhaltlich vollständig (lesbare Prosa). Bei
S0_unstructured muss der Judge dieselbe unbeschriftete Werteliste dekodieren
wie das Modell — eine Asymmetrie, die in die Interpretation der K-Werte gehört.

**Zu prüfen:** Falls der Text behauptet, diese beiden Varianten würden gegen
den vollen Kontext bewertet, korrigieren.

### 2.3 Judge-Kontext je Strategie (Ist-Zustand)

| Strategie | CONTEXT im Judge-Prompt |
|---|---|
| S0 | nur `{"asset_osm": ...}` |
| S0_raw | `{"_raw_text": ...}` |
| S0_unstructured | `{"_unstructured_text": ...}` |
| S1 | volle vier Dimensionen |
| S2 | S2-gepackter Kontext **inklusive** Guardrail-Notes |

Zwei Folgerungen. Erstens: Bei S0 kann der Judge unter der
Nicht-Spekulationsregel gar keinen Offline-Workflow erwarten, weil
`connectivity` nicht im Kontext steht. Die K-Separation von S0 misst also
Kontextknappheit, nicht schlechtere Nutzung. Zweitens: Beim Bewerten von S2
liest der Judge den Guardrail-Text, der das erwartete Verhalten ausformuliert;
bei S1 muss er es aus `device.connectivity` ableiten. Die Erwartung ist in
beiden Fällen regelkonform lizenziert, aber die Salienz unterscheidet sich.
Das ist ein dokumentierbarer Confound für rubrikbasierte K-Vergleiche zwischen
S1 und S2 — nicht für die behaviorale Aussage, die ohne Judge auskommt.

### 2.4 Policy-Artefakte in `context_policy_signal.py`

* Der Device-Guardrail feuert bei `offline OR spotty OR low_battery` mit einem
  gemeinsamen Notiztext. Bei `connectivity=online` und `device_state=low_battery`
  steht dann wörtlich „device.connectivity=online … Offline-Workflow anpassen".
* Der Satz „Bei signal_dark: Kreuzung wie unbeschrankt behandeln" steht fest im
  Sicherheits-Guardrail und wird auch bei `signal_stuck` ausgegeben.

Beides sind Auslöseartefakte, keine Fehlbewertungen. Sie gehören in die
Policy-Beschreibung, damit Code und Text nicht divergieren.

### 2.5 Kleinere Beobachtungen

* Der LAMP-Prosa-Formatter erzeugt „am Standort **None**", wenn `asset.name`
  fehlt. Die Modelle übernehmen das wörtlich. Dieselbe Klasse von Null-Artefakt,
  die beim SIGNAL-Korpus zur Migration v03→v04 geführt hat.
* `asset.lit` steht als P2-Feld in der LAMP-Selektion. In OSM ist `lit=yes` ein
  statisches Ausstattungsmerkmal, kein Live-Status. In C20 leitet das Modell
  daraus einen Widerspruch zu `fault_type=outage` ab. Kandidat für einen
  Guardrail oder für den Ausschluss aus der Selektion.
* `judge_raw.json` liegt einmal pro Testcase-Ordner und wird bei jedem der zehn
  Läufe überschrieben; nur das Rohartefakt des letzten Laufs überlebt. Für die
  Auswertung unkritisch, weil der geparste Judge-Block in jeder `run_XX.json` steht.

---

## 3. Ergebnisse der Nachbewertung

### 3.1 Sättigung — teilweise reproduziert

| Dimension | Judge Ø | Judge % max | eigen Ø | eigen % max | gesättigt Judge / eigen |
|---|---|---|---|---|---|
| R | 4,87 | 86,7 % | 4,87 | 93,3 % | ja / ja |
| H | 4,90 | 90,0 % | 4,80 | 80,0 % | ja / knapp nein |
| S | 4,93 | 93,3 % | 4,90 | 90,0 % | ja / ja |
| D | 4,97 | 96,7 % | 4,77 | 76,7 % | ja / nein |
| K | 4,63 | 66,7 % | 3,47 | 30,0 % | nein / nein |

Der Judge-Lauf auf diesen 30 Fällen zeigt dasselbe Muster wie die
Gesamtaggregate. Der zweite Durchgang reproduziert es für R und S klar, für
H und D knapp nicht, für K eindeutig.

Die H- und D-Abweichung kommt aus wörtlicher Ankeranwendung: H = 5 verlangt
Stop-Conditions oder klare Eskalationstrigger, D = 5 verlangt Asset-ID und Ort
in der Protokollliste. Sieben Antworten führen die Asset-ID nirgends im
Protokollteil auf, obwohl sie im Kontext steht.

### 3.2 Übereinstimmung

| Dimension | exakt | \|Abw\| ≤ 1 | mittlere Differenz (eigen − Judge) |
|---|---|---|---|
| R | 83,3 % | 96,7 % | ±0,00 |
| H | 76,7 % | 100 % | −0,10 |
| S | 90,0 % | 100 % | −0,03 |
| D | 80,0 % | 100 % | −0,20 |
| K | 43,3 % | 50,0 % | −1,17 |

Spearman auf K: ρ = −0,17, also praktisch keine Rangkorrelation. Kein
genereller Milde- oder Strenge-Bias — die mittleren Differenzen auf R, H, S, D
liegen zwischen 0,00 und −0,20.

### 3.3 K nach Strategie — reproduziert sich nicht

| Strategie | Judge Ø K | eigen Ø K |
|---|---|---|
| S0 | 3,83 | 4,17 |
| S0_raw | 4,83 | 3,67 |
| S0_unstructured | 4,83 | 2,67 |
| S1 | 4,83 | 2,50 |
| S2 | 4,83 | 4,33 |

Der Judge trennt in dieser Stichprobe nur S0 vom Rest; die vier übrigen
Bedingungen liegen exakt gleichauf. Das ist die berichtete Struktur im Kleinen.
Der zweite Durchgang kehrt die Ordnung um: S1 am niedrigsten, S0 an zweiter
Stelle, S2 vorn.

Die Ursache ist benennbar und kein Rauschen: Der Judge honoriert, dass Kontext
**aufgegriffen** wird; die Zweitbewertung zieht ab, wenn Kontext **falsch
verwendet** wird. Bei S0 gibt es kaum etwas, das man falsch verwenden könnte —
deshalb liegt S0 im zweiten Durchgang hoch. Die fünfzehn Fälle mit Divergenz
≥ 2 verteilen sich über alle drei Backends und alle Strategien außer S2.

### 3.4 Device-Fehldeutung

Von den 24 Fällen, in denen die Device-Dimension im Judge-Kontext steht:

| Strategie | Fehldeutung (Gerätestatus der Anlage zugeschrieben) |
|---|---|
| S1 | 5 von 6 |
| S0_unstructured | 1 von 6 |
| S0_raw | 0 von 6 |
| S2 | 1 von 6 |

Der einzige S2-Fall mit Fehldeutung ist C10 — der einzige S2-Fall, in dem der
Device-Guardrail nicht gefeuert hat, weil `connectivity=online` und
`device_state=ok` keinen Trigger auslösen. Das ist ein Innerhalb-S2-Kontrast
(Guardrail vorhanden vs. nicht bei sonst gleicher Strategie) und stützt die
Wirksamkeit der Annotation stärker als jeder Vergleich zwischen Strategien.

Die Prosa-Variante trifft die Zuordnung in allen sechs Fällen, weil der
Formatter „Technikgerät des Außendienstmitarbeiters" ausschreibt. Der Feldname
`device` leistet das nicht. Konkreter Mechanismus für den nicht-monotonen
Formatbefund.

Gegenbeleg zur Zwangsläufigkeit: C23 ist ein S1-Fall ohne jede Annotation, und
die Antwort schreibt ausdrücklich, der Gerätestatus betreffe „die Meldung
selbst, nicht die Straßenlampe". Die Fehldeutung ist häufig, nicht unvermeidlich.

### 3.5 Verhaltensflag — Kernaussage unabhängig bestätigt

Beschränkt auf die elf Fälle mit `connectivity ∈ {offline, spotty}` im
Judge-Kontext:

| | Anzahl |
|---|---|
| Judge-Flag `offline_workflow_mentioned` gesetzt | 9 von 11 |
| MENTION (Konnektivität thematisiert) | 11 von 11 |
| ADAPT (offlinefähiger Schritt vorgeschrieben) | **2 von 11** |

Beide ADAPT-Fälle sind S2. Aufgeschlüsselt: S2 2/2, alle übrigen Strategien
0/9. Bei n = 11 kein Test, aber dasselbe Muster wie in den 990 Antworten,
unabhängig und von Hand nachvollziehbar.

Drei Fälle gehen über Unterlassen hinaus und schreiben unter eingeschränkter
Konnektivität ausdrücklich online-abhängige Schritte vor:
„Verbindung zum System herstellen", „Updates senden, auch bei instabiler
Konnektivität", „Status im System aktualisieren".

Ein Fall (C30, S0_raw, offline) ordnet das Gerät korrekt zu und macht daraus
den ersten Diagnoseschritt: Konnektivität herstellen und Batterie laden, weil
Dokumentation ohne funktionierendes Gerät „nicht möglich" sei. Information
vorhanden, Zuordnung korrekt, Operation invertiert — die klarste Einzelillustration
des Aufbereitungsproblems in der Stichprobe.

### 3.6 Zwei Judge-Fehler, objektiv prüfbar

* **C09** (S0_raw, Mistral): Die Asset-ID `n6896979362` wird zweimal als
  `n689679362` wiedergegeben, unter anderem in der Liste der an die Leitstelle
  zu übermittelnden Daten. Der Judge vergab K = 5 und setzte
  `hallucination_suspected = false`.
* **C03** (S1, Mistral): Aus `device_state=low_battery` wird eine Notstrombatterie
  der Ampelanlage abgeleitet und als solche eskaliert. Judge ebenfalls K = 5,
  Flag nicht gesetzt.

Der harte Cap „Halluzination → K ≤ 2" hat in dieser Stichprobe nicht gegriffen.
Falls im Text steht, der Judge erkenne Faktenerfindungen, gehört dort ein
„in dieser Stichprobe nicht zuverlässig" hin.

### 3.7 Zwei Grenzfälle für `verify_offline_flag.py`

* **C08** schreibt lokale Speicherung mit späterer Synchronisierung vor,
  verwendet dabei aber kein Konnektivitätswort — kein „offline", „Netz",
  „Verbindung", „Empfang". Falsch-negativ, falls „synchronisieren" nicht im
  Lexikon steht.
* **C25** enthält „offline" nur als kopierten Wert in einer Aufzählung, ohne
  jede Aussage über Konnektivität. Falsch-positiv. Der Judge hat diesen Fall
  ebenfalls geflaggt.

Beide gegen das Skript prüfen, bevor die lexikalischen Zahlen final zitiert werden.

---

## 4. Einschränkungen

* **Verblindung nur partiell.** Der zur Bewertung nötige CONTEXT-Block
  identifiziert die Strategie in allen fünf Bedingungen eindeutig (S0 an der
  bloßen ID, S0_raw an `_raw_text`, S0_unstructured an `_unstructured_text`,
  S1 an `crs`, S2 an den Guardrail-Notes). Verdeckt blieb durchgehend das Backend.
* **Gleiche Modellfamilie.** Zweitbewerter und Judge stammen aus derselben
  Familie; korrelierte Fehler bleiben unsichtbar. Die Studie belegt Reliabilität
  und Operationalisierbarkeit der Rubrik, nicht deren Konstruktvalidität.
* **Vorbefassung.** Der Zweitbewerter kannte vor der Bewertung die Aussage, dass
  vier Dimensionen im Aggregat zwischen 4,85 und 5,00 liegen. Gegenmaßnahme:
  Abzugskriterien wurden vorab je Dimension fixiert und gefundene Mängel je Fall
  getrennt vom vergebenen Score notiert.
* **n = 6 pro Strategie.** Die nicht reproduzierte K-Rangordnung ist kein
  Gegenbeweis der berichteten Separation, sondern ein Hinweis auf einen
  Konstruktunterschied.

---

## 5. Textbausteine für die Arbeit

Gesamtumfang etwa eine halbe Seite. Die detaillierten Artefakte bleiben im
Repository und werden einmal referenziert.

### §2.5, ein Satz am Ende der vierten Lücke

> Diese Lücke wird in der vorliegenden Arbeit teilweise adressiert: Abschnitt
> \ref{sec:judge-reliability} berichtet eine unabhängige Zweitbewertung einer
> geschichteten Stichprobe gegen dieselbe Rubrik.

### Ergebnisteil (neuer Unterabschnitt, `\label{sec:judge-reliability}`)

> Zur Reliabilitätsprüfung des Judge wurde eine vollfaktorielle Stichprobe von
> 30 Antworten gezogen (2 Domänen × 3 Backends × 5 Strategien, je ein Incident
> und ein Lauf, \texttt{Random(42)}, Ziehungsskript und Manifest im Repository)
> und ohne Sicht auf die Judge-Scores gegen dieselbe Rubrik nachbewertet. Die
> Sättigung reproduziert sich für Relevanz und Sicherheit (Mittelwerte 4{,}87
> und 4{,}90 gegenüber 4{,}87 und 4{,}93 des Judge); Handlungsfähigkeit und
> Dokumentation liegen im zweiten Durchgang mit 4{,}80 und 4{,}77 knapp
> unterhalb der vorab festgelegten Sättigungsschwelle, Kontextnutzung ist in
> beiden Durchgängen die einzige nicht gesättigte Dimension. Die Übereinstimmung
> beträgt auf den gesättigten Dimensionen 76{,}7 bis 90{,}0 Prozent exakt und
> ist dort wegen der geringen Varianz nicht aussagekräftig; auf K sinkt sie auf
> 43{,}3 Prozent bei einer mittleren Differenz von $-1{,}17$ Punkten. Die
> Ursache ist systematisch: Der Judge honoriert, dass Kontext aufgegriffen wird,
> während die Zweitbewertung fehlerhafte Verwendung abzieht — in fünf von sechs
> S1-Fällen wurde die Device-Dimension der Anlage statt dem Technikergerät
> zugeschrieben und dennoch mit K = 5 bewertet. Die K-Separation von S0 ist
> somit als Maß des Kontextaufgriffs zu lesen, nicht der Kontextkorrektheit.
> Die behaviorale Aussage bestätigt sich dagegen unabhängig: In den elf Fällen
> mit eingeschränkter Konnektivität thematisierten alle elf Antworten den
> Verbindungszustand, während nur zwei ein offlinefähiges Vorgehen vorschrieben
> — beide unter S2.

### Limitationen, ein Satz

> Die Zweitbewertung erfolgte durch ein Modell derselben Familie wie der Judge
> und war nur teilweise verblindet, da der zur Bewertung erforderliche
> Kontextblock die Strategie erkennen lässt; sie belegt daher Reliabilität und
> Operationalisierbarkeit der Rubrik, nicht deren Konstruktvalidität.

---

## 6. Offene Punkte

1. Kapitel 5/6 gegen die Befunde aus Abschnitt 2 prüfen: Expected Elements,
   Judge-Referenz der unstrukturierten Varianten, Aussagen zur
   Halluzinationserkennung.
2. Policy-Beschreibung um die beiden Guardrail-Auslöseartefakte ergänzen.
3. `verify_offline_flag.py` gegen C08 und C25 prüfen.
4. Seitenbudget: Der neue Unterabschnitt kostet etwa eine halbe Seite bei einem
   90-Seiten-Limit; Gegenkürzung festlegen.
5. Abschnittsnummern nach dem Einfügen prüfen — Querverweise verschieben sich.
