# Blind Pack -- Nachbewertung LLM-as-judge

Seed 42. Reihenfolge gemischt. Strategie und Modell sind nicht aufgefuehrt; der CONTEXT-Block ist derselbe, den der Judge gesehen hat.

## C01

- Domaene: LAMP

### USER MESSAGE

```
Hinweis auf Steuerungsproblem: Segment fällt zeitgleich aus.
```

### CONTEXT (wie vom Judge gesehen)

```json
{
  "_raw_text": "Die Straßenlampe befindet sich am Standort None (OSM-ID: n12520351647, Koordinaten: 47.8502243, 12.1179478). Gemeldeter Fehler: control_box_issue, Schweregrad mittel. Gemeldet am 2026-01-20T18:31:50+01:00 von Bürger. Kein Foto verfügbar. Umgebung: nachts, Wetter Nebel, Lichtverhältnisse poor_visibility, Verkehrsaufkommen mittel. Technikgerät des Außendienstmitarbeiters: Konnektivität online, Gerätezustand in Ordnung."
}
```

### EXPECTED ELEMENTS

```
(leer -- test_loader schreibt keinen Schluessel expected_elements_short in input.meta, der Judge erhielt hier keinen Inhalt)
```

### MODEL ANSWER

Ein Steuerungsproblem wurde gemeldet: Ein Straßenlampensegment fällt am Standort (OSM-ID: n12520351647, Koordinaten: 47.8502243, 12.1179478) zeitgleich aus. Der gemeldete Fehler ist ein "control_box_issue" mit mittlerem Schweregrad, gemeldet am 20.01.2026 um 18:31:50 Uhr. Die Umgebung ist nachts, bei Nebel, schlechter Sicht und mittlerem Verkehrsaufkommen.

**Priorität: Sicherheit und Verkehrssicherung**

Hier ist die Schritt-für-Schritt-Checkliste für den Außendienst:

1.  **Absicherung (Sicherheit geht vor)**
    *   **Verkehrssicherung:** Unverzüglich die Arbeitsstelle gemäß den Vorschriften für Arbeiten im öffentlichen Verkehrsraum absichern (Warnleuchten, Warndreiecke, Absperrbaken). Besondere Vorsicht ist aufgrund der schlechten Sichtverhältnisse (Nebel, Nacht) und des mittleren Verkehrsaufkommens geboten.
    *   **Persönliche Schutzausrüstung (PSA):** Sicherstellen, dass die vollständige PSA (Warnkleidung, Sicherheitsschuhe, Handschuhe) getragen wird.
    *   **Gefahrenbereich:** Den Bereich um den Steuerungskasten und die betroffenen Lampen großräumig absperren, um Passanten und Verkehrsteilnehmer zu schützen.

2.  **Sichtprüfung (Erste Einschätzung)**
    *   **Steuerungskasten:** Den Steuerungskasten auf offensichtliche Beschädigungen (z.B. Vandalismus, Korrosion, offene Klappen, Wassereintritt) prüfen.
    *   **Kabel und Anschlüsse:** Sichtprüfung der externen Kabel und Anschlüsse auf Beschädigungen oder lose Verbindungen.
    *   **Umgebung:** Gibt es Anzeichen für externe Einflüsse (z.B. Baufahrzeuge, Unfälle, Baumwurzeln), die den Steuerungskasten oder die Zuleitungen beschädigt haben könnten?
    *   **Betroffene Lampen:** Prüfen, ob alle Lampen des Segments tatsächlich dunkel sind oder ob es einzelne Ausnahmen gibt.

3.  **Diagnose/Beobachtung (Fehleranalyse)**
    *   **Schaltzustand:** Prüfen, ob der Steuerungskasten unter Spannung steht und ob die Sicherungen intakt sind.
    *   **Fehleranzeigen:** Gibt es Fehlercodes oder Statusleuchten am Steuerungskasten, die auf eine spezifische Störung hinweisen?
    *   **Wiederholbarkeit:** Beobachten, ob der Ausfall konstant ist oder ob es zu intermittierenden Problemen kommt.
    *   **Systemprüfung:** Falls möglich und sicher, eine grundlegende Funktionsprüfung des Steuerungssystems durchführen (z.B. manuelles Schalten, Reset).

4.  **Dokumentation (Beweissicherung)**
    *   **Fotos:** Trotz fehlendem Bürgerfoto eigene Fotos vom Steuerungskasten, den betroffenen Lampen und der abgesicherten Arbeitsstelle machen.
    *   **Fehlerbeschreibung:** Genaue Beschreibung der festgestellten Mängel und Beobachtungen.
    *   **Maßnahmen:** Dokumentation der durchgeführten Absicherungs- und Diagnosemaßnahmen.
    *   **Zeitstempel:** Alle Schritte mit Datum und Uhrzeit festhalten.
    *   **Gerätezustand:** Der Außendienstmitarbeiter hat online Konnektivität und ein intaktes Gerät, was die Dokumentation vor Ort erleichtert.

5.  **Eskalation (Nächste Schritte)**
    *   **Meldung:** Umgehende Meldung der Ergebnisse an die zuständige Leitstelle oder den Vorgesetzten.
    *   **Priorisierung:** Aufgrund des mittleren Schweregrads und der schlechten Sichtverhältnisse in der Nacht ist eine schnelle Behebung wichtig.
    *   **Fachpersonal:** Falls der Fehler nicht direkt behoben werden kann, die Notwendigkeit der Hinzuziehung von spezialisiertem Fachpersonal (Elektriker, Steuerungstechniker) kommunizieren.
    *   **Ersatzteile:** Falls eine Reparatur vor Ort möglich ist, prüfen, ob die notwendigen Ersatzteile verfügbar sind.

**Annahme:** Da ein "control_box_issue" gemeldet wurde und ein ganzes Segment ausfällt, liegt die Vermutung nahe, dass der Fehler zentral im Steuerungskasten oder der Zuleitung zum Segment liegt und nicht an einzelnen Lampen.

---

## C02

- Domaene: LAMP

### USER MESSAGE

```
Kurze Aussetzer und Flackern, mögliche Kontaktprobleme. (Asset-ID: n8486238431)
```

### CONTEXT (wie vom Judge gesehen)

```json
{
  "asset_osm": "n8486238431"
}
```

### EXPECTED ELEMENTS

```
(leer -- test_loader schreibt keinen Schluessel expected_elements_short in input.meta, der Judge erhielt hier keinen Inhalt)
```

### MODEL ANSWER

Bei kurzen Aussetzern und Flackern der Straßenlampe (Asset-ID: n8486238431) gehen Sie bitte wie folgt vor, um Sicherheit und Verkehrssicherung zu gewährleisten:

### Schritt-für-Schritt-Checkliste:

1.  **Absicherung:**
    *   Sichern Sie den Bereich um die betroffene Straßenlampe umgehend mit Warnbaken und/oder Absperrband, um Passanten und Verkehrsteilnehmer zu schützen.
    *   Stellen Sie sicher, dass keine unmittelbare Gefahr durch herabfallende Teile oder Stromschläge besteht.
    *   Prüfen Sie, ob eine Meldung an die örtliche Verkehrsleitstelle oder Polizei notwendig ist, falls die Verkehrssicherheit stark beeinträchtigt ist.

2.  **Sichtprüfung:**
    *   Überprüfen Sie die Lampe und den Mast auf offensichtliche Beschädigungen (z.B. Risse, Korrosion, Vandalismus).
    *   Achten Sie auf lose Kabel, offene Gehäuse oder sichtbare Abnutzungserscheinungen an den Anschlüssen.
    *   Kontrollieren Sie, ob die Leuchteinheit korrekt im Gehäuse sitzt.

3.  **Diagnose/Beobachtung:**
    *   Beobachten Sie das Flackerverhalten: Ist es konstant, sporadisch, oder tritt es nur unter bestimmten Bedingungen (z.B. Wind) auf?
    *   Falls gefahrlos möglich und Sie dazu autorisiert sind: Prüfen Sie die Zugänglichkeit der Anschlusskästen und die Festigkeit der sichtbaren Kabelverbindungen (Vorsicht: Stromschlaggefahr!).
    *   Mögliche Ursachen könnten ein defektes Leuchtmittel, ein Vorschaltgerät, lose Kontakte oder ein Problem in der Zuleitung sein.

4.  **Dokumentation:**
    *   Halten Sie den genauen Zeitpunkt der Feststellung und die beobachteten Symptome (kurze Aussetzer, Flackern) fest.
    *   Machen Sie Fotos von der Situation und eventuellen Beschädigungen.
    *   Notieren Sie die Asset-ID: n8486238431.
    *   Erfassen Sie alle durchgeführten Absicherungsmaßnahmen.

5.  **Eskalation:**
    *   Melden Sie den Vorfall umgehend an die zuständige Fachabteilung oder den Bereitschaftsdienst.
    *   Geben Sie alle gesammelten Informationen (Asset-ID, Beobachtungen, Fotos) weiter.
    *   Fordern Sie die Entsendung von Fachpersonal (Elektriker) zur weiteren Fehleranalyse und Behebung an, da Kontaktprobleme und Flackern auf elektrische Defekte hindeuten, die nur von qualifiziertem Personal behoben werden dürfen.

---

## C03

- Domaene: SIGNAL

### USER MESSAGE

```
Ampel ausgefallen, Fahrzeuge weichen unsicher aus. (Hauptverkehrszeit / hoher Verkehr).
```

### CONTEXT (wie vom Judge gesehen)

```json
{
  "asset": {
    "asset_osm": "n54564039",
    "longitude": 12.1102904,
    "latitude": 47.8549167,
    "crs": "EPSG:4326",
    "traffic_signals": null,
    "traffic_signals:direction": null,
    "button_operated": null
  },
  "incident": {
    "fault_type": "signal_dark",
    "severity": "high",
    "reported_at": "2026-01-22T06:37:20+01:00",
    "reporter": "patrol",
    "photo_available": true,
    "photo_description": "Alle Signalphasen dunkel, keine Lichtausgabe sichtbar. Ampelgehäuse äußerlich intakt. Kreuzung ohne Regelung."
  },
  "environment": {
    "time_of_day": "rush_hour",
    "weather": "storm",
    "visibility": "poor_visibility",
    "traffic_exposure": "high",
    "noise_level": "medium"
  },
  "device": {
    "device_state": "low_battery",
    "connectivity": "online"
  }
}
```

### EXPECTED ELEMENTS

```
(leer -- test_loader schreibt keinen Schluessel expected_elements_short in input.meta, der Judge erhielt hier keinen Inhalt)
```

### MODEL ANSWER

Ampelausfall bei Hauptverkehrszeit und Sturm erfordert schnelles und umsichtiges Handeln. Priorität hat die Verkehrssicherung.

**Schritt-für-Schritt-Checkliste:**

1.  **Absicherung (Verkehrssicherung):**
    *   Sofortige Absicherung der Unfallstelle mit Warndreiecken und Warnblinklicht.
    *   Bei hohem Verkehrsaufkommen und schlechter Sicht (Sturm) umgehend die Polizei zur Verkehrsregelung anfordern.
    *   Sicherstellen, dass keine Fahrzeuge in den Kreuzungsbereich einfahren, ohne die Vorfahrt zu beachten.

2.  **Sichtprüfung:**
    *   Überprüfen Sie das Ampelgehäuse auf äußerliche Beschädigungen. (Laut Bericht: Gehäuse intakt).
    *   Kontrollieren Sie sichtbare Kabel und Anschlüsse auf offensichtliche Defekte oder Trennungen.
    *   Prüfen Sie, ob andere Verkehrsteilnehmer (Fußgänger, Radfahrer) durch den Ausfall gefährdet sind.

3.  **Diagnose/Beobachtung:**
    *   Bestätigen Sie, dass alle Signalphasen dunkel sind und keine Lichtausgabe erfolgt. (Laut Bericht: Alle Signalphasen dunkel).
    *   Beachten Sie den Gerätestatus "low_battery". Dies deutet auf ein Problem mit der Stromversorgung oder der Notstrombatterie hin.
    *   Überprüfen Sie, ob der Ampelschrank zugänglich ist und ob dort Fehleranzeigen sichtbar sind.

4.  **Dokumentation:**
    *   Halten Sie den genauen Zeitpunkt des Ausfalls und Ihrer Feststellungen fest.
    *   Notieren Sie die aktuellen Wetterbedingungen und das Verkehrsaufkommen.
    *   Ergänzen Sie die bereits vorhandene Fotodokumentation bei Bedarf mit weiteren Aufnahmen der Situation.
    *   Dokumentieren Sie alle getroffenen Absicherungsmaßnahmen.

5.  **Eskalation:**
    *   Umgehende Meldung an die zuständige technische Leitstelle/Störungsdienst mit allen gesammelten Informationen, insbesondere dem Gerätestatus "low_battery".
    *   Betonen Sie die hohe Dringlichkeit aufgrund von Hauptverkehrszeit, hohem Verkehrsaufkommen und schlechter Sicht durch Sturm.
    *   Fordern Sie bei Bedarf weiterhin Unterstützung durch die Polizei zur Verkehrsregelung an, bis die Ampelanlage wieder funktionstüchtig ist oder eine temporäre Lösung (z.B. mobile Ampel) installiert wurde.

---

## C04

- Domaene: SIGNAL

### USER MESSAGE

```
Signalgeber ohne Funktion; keine Lichtsignale sichtbar. (Richtung: forward). (Asset-ID: n6887356469)
```

### CONTEXT (wie vom Judge gesehen)

```json
{
  "asset_osm": "n6887356469"
}
```

### EXPECTED ELEMENTS

```
(leer -- test_loader schreibt keinen Schluessel expected_elements_short in input.meta, der Judge erhielt hier keinen Inhalt)
```

### MODEL ANSWER

Ein Signalgeber ist ohne Funktion, keine Lichtsignale sichtbar (Asset-ID: n6887356469, Richtung: forward). Dies ist ein sicherheitsrelevanter Mangel.

**Schritt-für-Schritt-Checkliste:**

1.  **Absicherung:**
    *   Unverzügliche Sicherung der Gefahrenstelle.
    *   Verkehrsteilnehmer warnen (z.B. Warndreieck, Warnleuchten).
    *   Bei Bedarf und Möglichkeit: Verkehr regeln, bis Fachpersonal eintrifft.

2.  **Sichtprüfung:**
    *   Überprüfung des Signalgebers auf offensichtliche Beschädigungen (z.B. Vandalismus, Unfallschäden, lose Kabel).
    *   Kontrolle des Anschlusskabels am Signalgeber und am Steuergerät.
    *   Prüfung des Steuergeräts auf sichtbare Fehleranzeigen oder Beschädigungen.

3.  **Diagnose/Beobachtung:**
    *   Funktionieren andere Signalgeber an derselben Kreuzung/Anlage? (Hinweis auf zentralen Fehler oder Einzelfall).
    *   Gibt es Anzeichen für eine Stromunterbrechung (z.B. Sicherung ausgelöst, allgemeiner Stromausfall im Bereich)?
    *   Umwelteinflüsse prüfen (z.B. Sturmschäden, Blitzeinschlag).

4.  **Dokumentation:**
    *   Genaue Beschreibung des Zustands und der Beobachtungen.
    *   Fotos des defekten Signalgebers und der Gesamtsituation.
    *   Bestätigung der Asset-ID: n6887356469.
    *   Datum, Uhrzeit und durchgeführte Maßnahmen festhalten.

5.  **Eskalation:**
    *   Sofortige Meldung an die zuständige Leitstelle/Fachabteilung unter Angabe aller gesammelten Informationen.
    *   Anforderung eines umgehenden Reparatur-/Wartungseinsatzes aufgrund der Verkehrssicherheitsrelevanz.

---

## C05

- Domaene: SIGNAL

### USER MESSAGE

```
Gehäuse beschädigt; Teile lose. Bitte umgehend sichern. (Richtung: forward).
```

### CONTEXT (wie vom Judge gesehen)

```json
{
  "_unstructured_text": "patrol | night | high | 2026-01-17T19:41:26+01:00 | low_battery | low | medium | Sichtbare Beschädigung am Signalkopf, Gehäuse geöffnet oder verformt. Kabelisolierung teilweise freiliegend. | True | 12.0965134 | 47.8512715 | poor_visibility | spotty | physical_damage | clear | n6896979357 | forward"
}
```

### EXPECTED ELEMENTS

```
(leer -- test_loader schreibt keinen Schluessel expected_elements_short in input.meta, der Judge erhielt hier keinen Inhalt)
```

### MODEL ANSWER

Verstanden. Die Situation erfordert umgehendes Handeln mit höchster Priorität auf Sicherheit. Hier ist die Schritt-für-Schritt-Checkliste für den Vor-Ort-Einsatz:

**Checkliste: Beschädigter Signalkopf (ID: n6896979357)**

**1. Absicherung (Priorität: Hoch)**
*   **Verkehrssicherung:** Unverzüglich die Einsatzstelle gemäß RSA/ZTV-SA absichern. Besondere Vorsicht aufgrund von "poor_visibility" und "night".
    *   Warnblinkanlage am Einsatzfahrzeug.
    *   Warndreiecke/Leitkegel in ausreichendem Abstand aufstellen.
    *   Ggf. zusätzliche Warnleuchten/Blitzleuchten einsetzen.
*   **Personenschutz:** Persönliche Schutzausrüstung (PSA) tragen (Warnkleidung, Handschuhe, Sicherheitsschuhe).
*   **Gefahrenbereich:** Den Bereich unterhalb des beschädigten Signalkopfes großräumig absperren, um Passanten vor herabfallenden Teilen zu schützen.
*   **Stromversorgung:** Bei freiliegender Kabelisolierung und der Gefahr eines Kurzschlusses oder Stromschlags: Wenn möglich und sicher, die Stromzufuhr zum Signalkopf unterbrechen (Sicherung/Schalter).

**2. Sichtprüfung (Detailliert)**
*   **Schadensausmaß:** Art und Umfang der Beschädigung am Signalkopf (Gehäuse geöffnet/verformt, Teile lose) genau feststellen.
*   **Kabelisolierung:** Prüfen, wie stark die Kabelisolierung freiliegt und ob blanke Drähte sichtbar sind.
*   **Stabilität:** Ist der Signalkopf noch sicher befestigt oder droht er herabzufallen?
*   **Richtung:** Bestätigen, dass der Schaden den "forward" gerichteten Verkehr betrifft.
*   **Umgebung:** Gibt es weitere Schäden an der Mastkonstruktion oder anderen Komponenten?

**3. Diagnose/Beobachtung**
*   **Funktion:** Funktionieren die Leuchtmittel noch? Gibt es Flackerlicht oder Ausfälle?
*   **Ursache (wenn erkennbar):** Hinweise auf die Schadensursache (z.B. Vandalismus, Kollision, Materialermüdung, Sturm).

**4. Dokumentation**
*   **Fotos:** Mehrere Fotos aus verschiedenen Perspektiven anfertigen, die den Schaden, die Absicherung und die Umgebung zeigen.
*   **Protokoll:**
    *   Datum, Uhrzeit des Einsatzes.
    *   Genaue Position (Koordinaten: 12.0965134, 47.8512715).
    *   Beschreibung des Schadens und der getroffenen Absicherungsmaßnahmen.
    *   Beobachtungen zur Ursache.
    *   Angaben zu "poor_visibility" und "night".
    *   Hinweis auf "low_battery" und "spotty" Konnektivität für die Kommunikation.
*   **Asset ID:** n6896979357

**5. Eskalation**
*   **Meldung:** Unverzügliche Meldung an die zuständige Leitstelle/Fachabteilung mit allen gesammelten Informationen und Fotos.
*   **Handlungsempfehlung:** Klare Empfehlung für die weiteren Schritte (z.B. Notinstandsetzung, Austausch des Signalkopfes, Beauftragung eines Elektrikers).
*   **Folgeauftrag:** Sicherstellen, dass ein Folgeauftrag zur dauerhaften Behebung des Schadens erstellt wird.

**Wichtiger Hinweis:** Aufgrund der freiliegenden Kabelisolierung besteht akute Gefahr. Eine provisorische Sicherung (z.B. mit Kabelbindern, Klebeband) ist nur zulässig, wenn dadurch keine weitere Gefahr entsteht und die dauerhafte Reparatur umgehend erfolgt. Priorität hat immer die Gefahrenabwehr.

---

## C06

- Domaene: SIGNAL

### USER MESSAGE

```
Ampelanlage komplett dunkel. Verkehr ist unklar geregelt. (Richtung: backward).
```

### CONTEXT (wie vom Judge gesehen)

```json
{
  "asset": {
    "asset_osm": "n12872023046",
    "longitude": 12.1183078,
    "latitude": 47.8584206,
    "crs": "EPSG:4326",
    "traffic_signals": null,
    "traffic_signals:direction": "backward",
    "button_operated": null
  },
  "incident": {
    "fault_type": "signal_dark",
    "severity": "high",
    "reported_at": "2026-01-18T10:05:03+01:00",
    "reporter": "dispatch",
    "photo_available": true,
    "photo_description": "Alle Signalphasen dunkel, keine Lichtausgabe sichtbar. Ampelgehäuse äußerlich intakt. Kreuzung ohne Regelung."
  },
  "environment": {
    "time_of_day": "day",
    "weather": "clear",
    "visibility": "normal_visibility",
    "traffic_exposure": "medium",
    "noise_level": "medium"
  },
  "device": {
    "device_state": "ok",
    "connectivity": "spotty"
  }
}
```

### EXPECTED ELEMENTS

```
(leer -- test_loader schreibt keinen Schluessel expected_elements_short in input.meta, der Judge erhielt hier keinen Inhalt)
```

### MODEL ANSWER

Ampelanlage komplett dunkel – das ist eine kritische Situation. Hier ist die Schritt-für-Schritt-Checkliste für den Außendienst, um die Sicherheit zu gewährleisten und die Störung zu beheben:

**Checkliste: Ampelanlage komplett dunkel**

1.  **Absicherung (Priorität: Sicherheit & Verkehrssicherung)**
    *   **Unmittelbare Gefahrenstelle sichern:** Warndreiecke, Warnleuchten und ggf. Verkehrsleitkegel gemäß StVO aufstellen.
    *   **Verkehr regeln:** Bei hohem Verkehrsaufkommen oder unübersichtlicher Kreuzung umgehend Polizei oder Ordnungsamt zur Verkehrsregelung anfordern.
    *   **PSA anlegen:** Warnkleidung (mind. Klasse 2), Sicherheitsschuhe, Handschuhe.
    *   **Fahrzeug sicher positionieren:** Warnblinkanlage einschalten, Fahrzeug so abstellen, dass es den Verkehr nicht zusätzlich behindert, aber als Absicherung dient.

2.  **Sichtprüfung (Erste Einschätzung vor Ort)**
    *   **Gesamtzustand der Anlage:** Äußerliche Beschädigungen am Mast, Signalgebern oder Schaltkasten? (Laut Meldung: "Ampelgehäuse äußerlich intakt").
    *   **Zuleitungen:** Sind Kabel sichtbar beschädigt oder abgerissen?
    *   **Sicherungskasten/Hauptschalter:** Ist der Hauptschalter der Anlage in der "Ein"-Position? Sind Sicherungen ausgelöst (falls zugänglich und ohne Gefahr prüfbar)?
    *   **Umgebung:** Gibt es Anzeichen für einen Stromausfall im weiteren Umfeld (z.B. andere dunkle Straßenlampen, Gebäude ohne Strom)?

3.  **Diagnose/Beobachtung (Fehlersuche)**
    *   **Spannungsprüfung:** Mit geeignetem Messgerät die Spannungsversorgung am Schaltkasten prüfen (Eingang und Ausgang).
    *   **Fehlerstromschutzschalter (FI-Schalter):** Ist dieser ausgelöst? Wenn ja, versuchen zurückzusetzen und beobachten.
    *   **Steuerung:** Reagiert die Steuerung auf manuelle Eingaben (falls vorhanden und sicher bedienbar)?
    *   **Interne Sicherungen:** Prüfen der internen Sicherungen im Schaltkasten (nur durch geschultes Personal).
    *   **Fehlermeldungen:** Gibt es Anzeigen oder Fehlermeldungen an der Steuerung?

4.  **Dokumentation**
    *   **Uhrzeit und Datum:** Beginn und Ende der Maßnahmen.
    *   **Feststellungen:** Alle Beobachtungen und Messergebnisse (z.B. "Spannung am Eingang vorhanden, am Ausgang nicht", "FI ausgelöst").
    *   **Durchgeführte Maßnahmen:** Was wurde unternommen (z.B. "Sicherungen geprüft", "FI zurückgesetzt").
    *   **Fotos:** Detaillierte Fotos der Situation, beschädigter Komponenten oder Fehlermeldungen. (Laut Meldung ist bereits ein Foto vorhanden, aber weitere vor Ort sind wichtig).
    *   **Verkehrssituation:** Beschreibung der Verkehrslage und ggf. der Maßnahmen zur Verkehrsregelung.

5.  **Eskalation**
    *   **Bei unklarer Ursache/nicht behebbarer Störung:** Umgehende Meldung an die Leitstelle/Fachabteilung mit allen gesammelten Informationen.
    *   **Bei Stromausfall im Netz:** Kontaktaufnahme mit dem örtlichen Energieversorger.
    *   **Bei Gefahr im Verzug (z.B. offene Kabel, stark beschädigte Masten):** Sofortige Absperrung des Bereichs und Meldung an die Leitstelle/Feuerwehr.
    *   **Anforderung von Spezialwerkzeug/Ersatzteilen:** Falls die Diagnose spezifische Komponenten oder Werkzeuge erfordert.

**Annahme:** Da die Ampelanlage komplett dunkel ist und die Meldung "device_state: ok" angibt, gehe ich davon aus, dass sich "device_state" auf den allgemeinen Zustand des Geräts vor dem Ausfall bezieht oder auf eine Komponente, die noch intakt ist, während die Stromversorgung unterbrochen ist. Die "spotty connectivity" deutet darauf hin, dass eine Fernwartung oder -diagnose erschwert sein könnte, was den Vor-Ort-Einsatz umso wichtiger macht.

---

## C07

- Domaene: SIGNAL

### USER MESSAGE

```
Ampel funktioniert aktuell, aber wiederholt Ausfälle gemeldet. (Richtung: forward). (Asset-ID: n6896979346)
```

### CONTEXT (wie vom Judge gesehen)

```json
{
  "asset_osm": "n6896979346"
}
```

### EXPECTED ELEMENTS

```
(leer -- test_loader schreibt keinen Schluessel expected_elements_short in input.meta, der Judge erhielt hier keinen Inhalt)
```

### MODEL ANSWER

Die gemeldeten wiederholten Ausfälle der Ampelanlage (Asset-ID: n6896979346) erfordern eine sorgfältige Überprüfung, auch wenn sie aktuell funktioniert. Priorität hat die Verkehrssicherheit.

Hier ist die Schritt-für-Schritt-Checkliste für den Außendienst:

**1. Absicherung der Einsatzstelle**
*   **Verkehrssicherung:** Bei Bedarf und je nach Verkehrslage die Einsatzstelle gemäß StVO absichern (Warnblinkanlage, Warndreieck, Warnleuchten).
*   **Persönliche Schutzausrüstung (PSA):** Warnkleidung tragen, um die eigene Sicherheit zu gewährleisten.

**2. Sichtprüfung (bei aktuellem Betrieb)**
*   **Gesamtzustand der Ampelanlage:**
    *   Sind alle Signalgeber intakt (keine Risse, Beschädigungen)?
    *   Funktionieren alle Leuchtmittel korrekt (kein Flackern, keine Ausfälle)?
    *   Sind die Signalbilder klar und deutlich erkennbar?
    *   Gibt es sichtbare Beschädigungen an Masten, Kabeln oder Schaltkästen?
*   **Umgebung:**
    *   Gibt es Hindernisse, die die Sicht auf die Ampel beeinträchtigen könnten?
    *   Sind die Induktionsschleifen im Fahrbahnbelag intakt (falls vorhanden)?
    *   Gibt es Anzeichen für Vandalismus oder äußere Einwirkungen?
*   **Schaltkasten:**
    *   Ist der Schaltkasten verschlossen und unbeschädigt?
    *   Gibt es Anzeichen für Feuchtigkeitseintritt oder Überhitzung (Geruch)?

**3. Diagnose/Beobachtung (Fokus auf intermittierende Fehler)**
*   **Fehlerspeicher auslesen:** Falls möglich, den Fehlerspeicher der Steuerung auslesen. Dies ist der wichtigste Schritt bei wiederkehrenden, nicht dauerhaften Fehlern.
*   **Verkehrsfluss beobachten:**
    *   Tritt der Fehler zu bestimmten Tageszeiten oder unter bestimmten Verkehrsbedingungen auf?
    *   Gibt es Auffälligkeiten im Schaltverhalten der Ampel (z.B. zu kurze Grünphasen, fehlende Phasen)?
    *   Reagiert die Ampel korrekt auf Fahrzeugdetektion (falls vorhanden)?
*   **Akustische/Optische Auffälligkeiten:**
    *   Gibt es ungewöhnliche Geräusche aus dem Schaltkasten?
    *   Gibt es Anzeichen für Überhitzung (z.B. Verfärbungen an Komponenten)?
*   **Wetterbedingungen:** Gab es in der Vergangenheit extreme Wetterereignisse (Sturm, Starkregen, Hitze), die mit den Ausfällen korrelierten?

**4. Dokumentation**
*   **Datum und genaue Uhrzeit des Einsatzes.**
*   **Asset-ID:** n6896979346.
*   **Genaue Beschreibung der Beobachtungen:** Was wurde festgestellt, auch wenn die Ampel aktuell funktioniert.
*   **Ausgelesene Fehlermeldungen** (falls vorhanden).
*   **Fotos:** Dokumentation von Auffälligkeiten, Beschädigungen oder der Gesamtsituation.
*   **Angaben zur Umgebung und Wetterbedingungen** während der Beobachtung.
*   **Durchgeführte Maßnahmen** (z.B. Sichtprüfung, Fehlerspeicher ausgelesen).

**5. Eskalation**
*   **Bei akuter Gefahr:** Wenn die Ampel während der Beobachtung ausfällt oder ein unsicheres Schaltverhalten zeigt, sofort die zuständige Leitstelle informieren und gegebenenfalls weitere Absicherungsmaßnahmen einleiten.
*   **Bei wiederkehrenden Fehlern:** Auch wenn aktuell kein akuter Fehler vorliegt, aber der Fehlerspeicher Einträge zeigt oder die Beobachtungen auf ein tieferliegendes Problem hindeuten, ist eine Eskalation an die Fachabteilung für eine detailliertere Analyse und gegebenenfalls präventive Wartung oder Reparatur erforderlich.
*   **Empfehlung:** Aufgrund der wiederholten Ausfälle ist eine tiefergehende technische Prüfung durch einen Spezialisten dringend anzuraten, auch wenn die Ampel derzeit funktioniert.

---

## C08

- Domaene: SIGNAL

### USER MESSAGE

```
Ampel ausgefallen, Fahrzeuge weichen unsicher aus. (Richtung: forward; Hauptverkehrszeit / hoher Verkehr).
```

### CONTEXT (wie vom Judge gesehen)

```json
{
  "incident": {
    "fault_type": "signal_dark",
    "severity": "high",
    "reported_at": "2026-01-16T18:17:59+01:00",
    "reporter": "dispatch",
    "photo_description": "Alle Signalphasen dunkel, keine Lichtausgabe sichtbar. Ampelgehäuse äußerlich intakt. Kreuzung ohne Regelung."
  },
  "asset": {
    "asset_osm": "n2991186127",
    "longitude": 12.1280783,
    "latitude": 47.8502392
  },
  "device": {
    "connectivity": "online",
    "device_state": "low_battery"
  },
  "environment": {
    "visibility": "poor_visibility",
    "time_of_day": "rush_hour",
    "traffic_exposure": "high",
    "weather": "rain",
    "noise_level": "high"
  },
  "_guardrail_notes": [
    "HINWEIS: device.connectivity=online und device.device_state=low_battery beziehen sich auf das Technikgerät (Smartphone/Tablet), NICHT auf die Ampelanlage selbst. Offline-Workflow anpassen: Dokumentation lokal, spätere Synchronisation.",
    "SICHERHEITSHINWEIS: fault_type=signal_dark / severity=high → Sofortige Absicherung der Kreuzung erforderlich. Bei signal_dark: Kreuzung wie unbeschrankt behandeln. Eskalation an Leitstelle priorisieren."
  ]
}
```

### EXPECTED ELEMENTS

```
(leer -- test_loader schreibt keinen Schluessel expected_elements_short in input.meta, der Judge erhielt hier keinen Inhalt)
```

### MODEL ANSWER

Hier ist die Schritt-für-Schritt-Checkliste für den Ausfall der Ampelanlage:

**Ampelausfall: Signal dunkel, hohe Dringlichkeit, Hauptverkehrszeit, Regen, schlechte Sicht**

**1. Absicherung (Priorität: Sicherheit & Verkehrssicherung)**
*   **Eigenschutz:** Warnweste anlegen, Warnblinklicht am Fahrzeug einschalten.
*   **Gefahrenbereich absichern:** Unverzüglich die Kreuzung mit Warndreiecken und/oder Blitzleuchten absichern.
*   **Verkehr regeln:** Bei hohem Verkehrsaufkommen und unsicherem Ausweichen der Fahrzeuge ist eine manuelle Verkehrsregelung durch geschultes Personal (ggf. Polizei anfordern) zwingend erforderlich, bis die Anlage wieder funktioniert oder eine temporäre Lösung gefunden ist. Die Kreuzung ist wie eine unbeschrankte Kreuzung zu behandeln.
*   **Polizei informieren:** Aufgrund der hohen Gefährdungslage (Hauptverkehrszeit, Regen, schlechte Sicht, unsicheres Ausweichen) umgehend die Polizei zur Unterstützung bei der Verkehrsregelung anfordern.

**2. Sichtprüfung (Erste Einschätzung vor Ort)**
*   **Ampelgehäuse:** Äußerliche Unversehrtheit des Ampelgehäuses prüfen (gemäß Beschreibung intakt).
*   **Kabel/Anschlüsse:** Sichtprüfung auf offensichtliche Beschädigungen an Kabeln oder Anschlüssen im zugänglichen Bereich.
*   **Umgebung:** Prüfen, ob externe Faktoren (z.B. umgestürzte Bäume, Baufahrzeuge) die Anlage beschädigt haben könnten.
*   **Gesamtkreuzung:** Überblick über die gesamte Kreuzung verschaffen, um weitere Gefahrenquellen zu identifizieren.

**3. Diagnose/Beobachtung (Fehleranalyse & Situationsbewertung)**
*   **Fehlerbild bestätigen:** Bestätigen, dass alle Signalphasen dunkel sind und keine Lichtausgabe erfolgt.
*   **Verkehrsfluss:** Beobachten, wie sich der Verkehr ohne Regelung verhält und wo die größten Konfliktpunkte entstehen.
*   **Umwelteinflüsse:** Die aktuellen Bedingungen (Regen, schlechte Sicht, hoher Lärmpegel) bei der weiteren Planung berücksichtigen.

**4. Dokumentation (Wichtig für Nachverfolgung & Reparatur)**
*   **Fotos:** Wenn möglich, Fotos der Situation und der Ampelanlage machen. (Hinweis: Bei niedrigem Akkustand des Geräts die wichtigsten Aufnahmen priorisieren und ggf. auf manuelle Notizen ausweichen).
*   **Beobachtungen:** Alle Feststellungen (z.B. genaue Uhrzeit des Eintreffens, Wetterbedingungen, Verkehrsaufkommen, beobachtetes Verkehrsverhalten) detailliert notieren.
*   **Gerätestatus:** Den niedrigen Akkustand des Endgeräts (Smartphone/Tablet) beachten. Dokumentation lokal speichern und bei nächster Gelegenheit synchronisieren.

**5. Eskalation (Informationsfluss & Unterstützung anfordern)**
*   **Leitstelle informieren:** Umgehend die Leitstelle über die kritische Situation, die durchgeführten Absicherungsmaßnahmen und die ersten Erkenntnisse informieren.
*   **Unterstützung anfordern:** Klare Anweisungen für benötigte Unterstützung geben (z.B. Polizei zur Verkehrsregelung, Elektriker, Ersatzteile, Notstromversorgung).
*   **Priorität:** Die hohe Dringlichkeit des "signal_dark"-Fehlers und die Gefährdungslage betonen, um eine schnelle Reaktion sicherzustellen.

---

## C09

- Domaene: SIGNAL

### USER MESSAGE

```
Ampelphasen passen nicht zum Verkehr; Rückstau/Beinahe-Situationen. (Richtung: backward; Hauptverkehrszeit / hoher Verkehr).
```

### CONTEXT (wie vom Judge gesehen)

```json
{
  "_raw_text": "Betroffene Lichtsignalanlage: OSM-ID n6896979362, Koordinaten 47.8492581, 12.0934822, Richtung backward. Gemeldeter Fehler: Schaltzeitproblem, Schweregrad hoch. Gemeldet am 2026-01-19T02:05:35+01:00 von Streife. Foto vorhanden. Bildbeschreibung: Stark verkürzte Grünphase erkennbar, Fußgänger überqueren bei Rot. Sicherheitskritisch. Umgebung: Stoßzeit, Wetter Regen, Sichtweite poor_visibility, Verkehrsaufkommen hoch. Technikgerät des Außendienstmitarbeiters: Konnektivität instabil, Gerätezustand in Ordnung."
}
```

### EXPECTED ELEMENTS

```
(leer -- test_loader schreibt keinen Schluessel expected_elements_short in input.meta, der Judge erhielt hier keinen Inhalt)
```

### MODEL ANSWER

Die Situation ist aufgrund der verkürzten Grünphase, Fußgängerquerungen bei Rot und des hohen Verkehrsaufkommens während der Stoßzeit bei schlechter Sicht als hoch sicherheitskritisch einzustufen. Priorität hat die umgehende Sicherung der Unfallstelle und die Wiederherstellung der Verkehrssicherheit.

**Vorgehensweise vor Ort (Checkliste):**

1.  **Absicherung:**
    *   **Eigenschutz:** Persönliche Schutzausrüstung (PSA) tragen.
    *   **Verkehrssicherung:** Unverzüglich Warnblinkanlage einschalten, Warndreieck/Blitzleuchten aufstellen, um auf die Gefahrenstelle aufmerksam zu machen und den Arbeitsbereich abzusichern.
    *   **Gefahrenbereich:** Falls möglich, den Bereich um die defekte Ampel meiden oder nur mit äußerster Vorsicht betreten.

2.  **Sichtprüfung:**
    *   **Ampelzustand:** Überprüfen Sie alle Signalgeber der betroffenen Lichtsignalanlage (OSM-ID n689679362) auf mechanische Beschädigungen, Vandalismus oder offensichtliche Defekte (z.B. ausgefallene Leuchtmittel, lose Kabel).
    *   **Umgebung:** Beachten Sie die Umgebung (Verkehrsfluss, Fußgängerverhalten, andere Verkehrsteilnehmer) im Hinblick auf die gemeldete Richtung "backward".
    *   **Steuergerät:** Falls zugänglich und sicher, eine Sichtprüfung des Steuergeräts auf offensichtliche Fehleranzeigen (LEDs, Displaymeldungen) durchführen.

3.  **Diagnose/Beobachtung:**
    *   **Phasenablauf:** Beobachten Sie den vollständigen Phasenablauf der Ampel über mehrere Zyklen, insbesondere die Grünphase in der gemeldeten Richtung "backward". Bestätigen Sie die "stark verkürzte Grünphase" und das Überqueren von Fußgängern bei Rot.
    *   **Verkehrsfluss:** Beurteilen Sie den Rückstau und die Beinahe-Situationen im Kontext des aktuellen Verkehrsaufkommens (Stoßzeit, hoher Verkehr).
    *   **Fehlerbild:** Versuchen Sie, das genaue Fehlerbild zu identifizieren: Ist die Grünphase nur verkürzt, oder fehlt sie komplett? Gibt es andere Auffälligkeiten (z.B. fehlende Gelbphase, Flackern)?
    *   **Konnektivität:** Versuchen Sie, eine Verbindung zum System herzustellen, auch wenn die Konnektivität instabil ist. Prüfen Sie, ob temporäre Verbindungen für eine erste Diagnose möglich sind.

4.  **Dokumentation:**
    *   **Fotos/Videos:** Machen Sie aussagekräftige Fotos oder Videos vom Fehlerbild (verkürzte Grünphase, Rückstau, Fußgänger bei Rot) und der Gesamtsituation.
    *   **Uhrzeit/Dauer:** Notieren Sie präzise Uhrzeiten und die Dauer der beobachteten Phasen.
    *   **Beobachtungen:** Halten Sie alle Beobachtungen schriftlich fest, insbesondere die Auswirkungen auf den Verkehr und die Sicherheit.
    *   **Gerätezustand:** Dokumentieren Sie den Zustand Ihres Technikgeräts (instabile Konnektivität).

5.  **Eskalation:**
    *   **Sofortige Meldung:** Aufgrund des hohen Schweregrads und der Sicherheitskritikalität ist eine sofortige telefonische Meldung an die zuständige Leitstelle/Fachabteilung zwingend erforderlich.
    *   **Informationen:** Geben Sie alle gesammelten Informationen weiter:
        *   OSM-ID n689679362, Koordinaten 47.8492581, 12.0934822, Richtung "backward".
        *   Bestätigung der "stark verkürzten Grünphase" und der sicherheitskritischen Situation.
        *   Aktuelle Beobachtungen zu Rückstau und Beinahe-Situationen.
        *   Hinweis auf die instabile Konnektivität Ihres Geräts, die eine Fernwartung oder detailliertere Diagnose erschweren könnte.
        *   Empfehlung für eine umgehende Entstörung oder manuelle Steuerung/Abschaltung der Anlage, falls die Gefahr nicht anders zu bannen ist.
    *   **Rückmeldung:** Erfragen Sie das weitere Vorgehen und die voraussichtliche Reaktionszeit.

**Annahme:** Da die Konnektivität instabil ist, wird eine Fernanalyse oder -behebung erschwert sein. Eine manuelle Überprüfung und gegebenenfalls eine manuelle Steuerung oder Abschaltung der Anlage durch geschultes Personal vor Ort könnte notwendig werden, um die Sicherheit zu gewährleisten.

---

## C10

- Domaene: SIGNAL

### USER MESSAGE

```
Ampel scheint auf Rot zu „hängen“. Kein Umschalten beobachtet.
```

### CONTEXT (wie vom Judge gesehen)

```json
{
  "incident": {
    "fault_type": "signal_stuck",
    "severity": "high",
    "reported_at": "2026-01-18T04:09:32+01:00",
    "reporter": "internal",
    "photo_description": "Dauerhaft rote Phase erkennbar, kein Phasenwechsel sichtbar. Staubildung an Kreuzung."
  },
  "asset": {
    "asset_osm": "n35664963",
    "longitude": 12.1169259,
    "latitude": 47.8519399
  },
  "device": {
    "connectivity": "online",
    "device_state": "ok"
  },
  "environment": {
    "visibility": "poor_visibility",
    "time_of_day": "day",
    "traffic_exposure": "medium",
    "weather": "storm",
    "noise_level": "medium"
  },
  "_guardrail_notes": [
    "SICHERHEITSHINWEIS: fault_type=signal_stuck / severity=high → Sofortige Absicherung der Kreuzung erforderlich. Bei signal_dark: Kreuzung wie unbeschrankt behandeln. Eskalation an Leitstelle priorisieren."
  ]
}
```

### EXPECTED ELEMENTS

```
(leer -- test_loader schreibt keinen Schluessel expected_elements_short in input.meta, der Judge erhielt hier keinen Inhalt)
```

### MODEL ANSWER

Ein dauerhaft auf Rot stehendes Ampelsignal stellt eine erhebliche Gefahr für die Verkehrssicherheit dar und erfordert umgehendes Handeln. Basierend auf der Meldung, dass die Ampel auf Rot "hängt" und kein Umschalten beobachtet wurde, sowie den Kontextinformationen zur hohen Dringlichkeit und den Umgebungsbedingungen (Sturm, schlechte Sicht), ist folgende Vorgehensweise dringend einzuhalten:

**Schritt-für-Schritt-Checkliste für den Außendienst:**

1.  **Absicherung der Einsatzstelle (Priorität: Sicherheit & Verkehrssicherung)**
    *   **Unverzüglich:** Sichern Sie die Kreuzung gemäß den Unfallverhütungsvorschriften (UVV) und der Straßenverkehrsordnung (StVO) ab.
    *   **Warnsignal:** Schalten Sie das Warnblinklicht Ihres Einsatzfahrzeugs ein und positionieren Sie es so, dass es den ankommenden Verkehr frühzeitig warnt.
    *   **Warneinrichtungen:** Stellen Sie Warnkegel, Warndreiecke oder Blitzleuchten auf, um den Gefahrenbereich deutlich zu kennzeichnen.
    *   **Verkehrsbeobachtung:** Beurteilen Sie die Verkehrssituation. Bei starker Staubildung oder unübersichtlicher Lage ist eine manuelle Verkehrsregelung durch Sie oder die angeforderte Polizei notwendig, bis die Situation entschärft ist.
    *   **Besondere Vorsicht:** Aufgrund der gemeldeten schlechten Sicht und des Sturms ist erhöhte Aufmerksamkeit bei der Absicherung und im weiteren Verlauf geboten.

2.  **Sichtprüfung der Anlage**
    *   **Signalgeber:** Überprüfen Sie alle Signalgeber der betroffenen Ampelanlage. Stehen tatsächlich alle auf Rot, oder gibt es Abweichungen (z.B. einzelne Lampen aus, andere Farben)?
    *   **Äußere Schäden:** Suchen Sie nach offensichtlichen Beschädigungen an den Signalgebern, Masten oder der Verkabelung, die durch den Sturm verursacht worden sein könnten (z.B. lose Kabel, defekte Linsen).
    *   **Steuergerät:** Falls zugänglich, prüfen Sie das Steuergerät auf sichtbare Fehlermeldungen, ungewöhnliche Geräusche oder Gerüche.

3.  **Diagnose und Beobachtung**
    *   **Phasenwechsel:** Bestätigen Sie durch längere Beobachtung, dass tatsächlich kein Phasenwechsel stattfindet. Wie lange ist die Rotphase bereits aktiv?
    *   **Andere Ampeln:** Funktionieren andere Ampelanlagen in der Nähe oder an derselben Kreuzung normal? Dies kann Hinweise auf einen lokalen oder systemweiten Fehler geben.
    *   **Detektoren:** Überprüfen Sie, falls möglich, die Funktion der Fahrzeug- und Fußgängerdetektoren (Induktionsschleifen, Radarsensoren, Taster). Ein dauerhaft belegter Detektor könnte die Ursache für eine hängende Rotphase sein.
    *   **Gerätestatus:** Beachten Sie, dass das Gerät laut System "online" und der Gerätestatus "ok" meldet. Dies deutet darauf hin, dass die Störung möglicherweise nicht durch einen kompletten Ausfall, sondern durch einen Logikfehler, eine Fehlkonfiguration oder ein Problem mit den Sensorinputs verursacht wird.

4.  **Dokumentation**
    *   **Zeitstempel:** Notieren Sie die genaue Uhrzeit Ihrer Ankunft und des Beginns der Absicherungsmaßnahmen.
    *   **Fehlerbeschreibung:** Halten Sie das genaue Fehlerbild fest (z.B. "Alle Signalgeber der Kreuzung [Kreuzungsname/Nummer] dauerhaft auf Rot, kein Phasenwechsel").
    *   **Fotos:** Machen Sie aussagekräftige Fotos von der Ampelanlage, der Verkehrssituation (Staubildung) und Ihrer Absicherung.
    *   **Umgebungsbedingungen:** Dokumentieren Sie die Wetterbedingungen (Sturm, schlechte Sicht) und deren Einfluss auf die Situation.
    *   **Durchgeführte Maßnahmen:** Notieren Sie alle Schritte, die Sie unternommen haben.

5.  **Eskalation (Priorität: Sofortige Meldung)**
    *   **Leitstelle:** Melden Sie den Vorfall **umgehend** an die zuständige Leitstelle oder Verkehrsmanagementzentrale.
    *   **Informationen:** Geben Sie alle gesammelten Informationen weiter:
        *   Genaue Position (asset_osm: n35664963, Längen-/Breitengrad: 12.1169259, 47.8519399).
        *   Fehlerbild ("Ampel hängt auf Rot").
        *   Bestätigung der Absicherung.
        *   Beobachtungen (Sturm, schlechte Sicht, Staubildung).
        *   Information, dass das Gerät online und der Gerätestatus "ok" ist, was auf einen komplexeren Fehler hindeutet.
    *   **Unterstützung:** Fordern Sie bei Bedarf Unterstützung an (z.B. Polizei zur Verkehrsregelung, spezialisierte Techniker für die Fehlerbehebung).
    *   **Anweisungen:** Warten Sie auf weitere Anweisungen der Leitstelle und handeln Sie entsprechend.

**Wichtiger Hinweis:** Eine Ampel, die dauerhaft auf Rot steht, muss wie eine ausgefallene Ampel behandelt werden, bei der die Verkehrsregeln der StVO (Rechts vor Links, Vorfahrtsschilder) gelten. Die Absicherung und schnelle Eskalation sind hier entscheidend, um Unfälle zu vermeiden.

---

## C11

- Domaene: LAMP

### USER MESSAGE

```
Gehäuse beschädigt, mögliche Berührungsgefahr. Bitte absichern.
```

### CONTEXT (wie vom Judge gesehen)

```json
{
  "asset": {
    "asset_osm": "n4470029720",
    "longitude": 12.1326497,
    "latitude": 47.8433336,
    "crs": "EPSG:4326",
    "lit": "yes",
    "name": "Rosenheim, Leitzachstraße"
  },
  "incident": {
    "fault_type": "open_housing",
    "severity": "high",
    "reported_at": "2026-01-18T06:17:02+01:00",
    "reporter": "dispatch",
    "photo_available": true,
    "photo_description": "Tagesaufnahme bei klarem Wetter: Gehäuse deutlich geöffnet, Schrauben fehlen. Innenverkabelung sichtbar freiliegend. Absicherung erforderlich."
  },
  "environment": {
    "time_of_day": "day",
    "weather": "clear",
    "lighting_condition": "normal_visibility",
    "traffic_exposure": "low",
    "noise_level": "medium"
  },
  "device": {
    "device_state": "ok",
    "connectivity": "online"
  }
}
```

### EXPECTED ELEMENTS

```
(leer -- test_loader schreibt keinen Schluessel expected_elements_short in input.meta, der Judge erhielt hier keinen Inhalt)
```

### MODEL ANSWER

Ein beschädigtes Gehäuse mit möglicher Berührungsgefahr erfordert sofortiges Handeln. Hier ist die Schritt-für-Schritt-Checkliste für die Absicherung und weitere Maßnahmen an der Straßenlampe in der Leitzachstraße, Rosenheim:

**1. Absicherung (Priorität: Sicherheit und Verkehrssicherung)**
*   **Gefahrenbereich absperren:** Sofortige und großräumige Absperrung des Bereichs um die Straßenlampe mit geeigneten Mitteln (z.B. Warnkegel, Absperrband, Bauzaun), um Passanten und Verkehrsteilnehmer vor der Berührungsgefahr und herabfallenden Teilen zu schützen.
*   **Warnhinweise anbringen:** Deutliche Warnschilder "Gefahr durch Stromschlag" oder "Betreten verboten" an der Absperrung anbringen.
*   **Stromzufuhr prüfen/unterbrechen:** Wenn gefahrlos möglich und die Zuständigkeit klar ist, die Stromzufuhr zur betroffenen Lampe unterbrechen. Bei Unsicherheit oder fehlender Möglichkeit, die Stromzufuhr zu unterbrechen, ist höchste Vorsicht geboten und der nächste Schritt zu priorisieren.
*   **Verkehrssicherung:** Bei Bedarf (je nach Verkehrsaufkommen und Lage) zusätzliche Verkehrssicherungsmaßnahmen ergreifen und ggf. die Polizei oder Verkehrsleitstelle informieren.

**2. Sichtprüfung (Detaillierte Begutachtung)**
*   **Schadensausmaß:** Das Gehäuse ist deutlich geöffnet, Schrauben fehlen und die Innenverkabelung ist sichtbar freiliegend.
*   **Weitere Schäden:** Prüfen, ob weitere Komponenten (z.B. Leuchtmittel, Mast, Fundament) beschädigt sind oder lose Teile vorhanden sind.
*   **Feuchtigkeit/Nässe:** Kontrolle auf das Eindringen von Feuchtigkeit in das Gehäuse, da dies die elektrische Gefahr zusätzlich erhöht.
*   **Ursache (wenn erkennbar):** Versuch, die mögliche Ursache der Beschädigung zu identifizieren (z.B. Vandalismus, Materialermüdung, Anfahrschaden).

**3. Diagnose/Beobachtung**
*   **Stromflussprüfung:** Falls die Stromzufuhr nicht unterbrochen werden konnte, mit geeignetem, geprüftem Equipment (z.B. Spannungsprüfer) prüfen, ob Spannung an den freiliegenden Teilen anliegt. **Nur durch geschultes Personal!**
*   **Funktion der Lampe:** Obwohl das Gehäuse beschädigt ist, prüfen, ob die Lampe noch leuchtet (was auf eine aktive Stromzufuhr hindeuten würde). Der aktuelle Gerätestatus ist "ok" und "online", was auf eine funktionierende Elektronik hindeutet, aber nicht die mechanische Beschädigung oder die elektrische Gefahr ausschließt.

**4. Dokumentation**
*   **Fotos:** Umfassende Fotos des Schadens aus verschiedenen Perspektiven, inklusive der Absperrung und der Umgebung.
*   **Schadensbeschreibung:** Genaue Beschreibung des Schadens, der freiliegenden Teile, fehlender Schrauben und der durchgeführten Absicherungsmaßnahmen.
*   **Datum/Uhrzeit:** Zeitpunkt der Feststellung und der durchgeführten Maßnahmen.
*   **Beteiligte Personen:** Namen der vor Ort tätigen Personen.
*   **Wetterbedingungen:** Tagesaufnahme bei klarem Wetter.

**5. Eskalation**
*   **Sofortige Meldung:** Unverzügliche Meldung an die zuständige Leitstelle/Einsatzleitung mit allen gesammelten Informationen.
*   **Reparaturauftrag:** Einleitung eines Reparaturauftrags mit höchster Priorität aufgrund der Berührungsgefahr und der hohen Dringlichkeit ("severity: high").
*   **Sicherstellung der Reparatur:** Verbleib vor Ort, bis die Reparatur eingeleitet oder eine dauerhafte Sicherung gewährleistet ist, oder klare Anweisungen zur weiteren Vorgehensweise vorliegen.

---

## C12

- Domaene: SIGNAL

### USER MESSAGE

```
Kurzzeitige Aussetzer/Neustarts vermutet; Verhalten inkonsistent. (Richtung: backward). (Asset-ID: n6887356461)
```

### CONTEXT (wie vom Judge gesehen)

```json
{
  "asset_osm": "n6887356461"
}
```

### EXPECTED ELEMENTS

```
(leer -- test_loader schreibt keinen Schluessel expected_elements_short in input.meta, der Judge erhielt hier keinen Inhalt)
```

### MODEL ANSWER

Okay, hier ist die Schritt-für-Schritt-Checkliste für die gemeldeten inkonsistenten Aussetzer/Neustarts der Ampelanlage (Asset-ID: n6887356461), Richtung rückwärts:

### Checkliste: Ampelanlage – Inkonstantes Verhalten (Asset-ID: n6887356461)

1.  **Absicherung (Priorität: Sicherheit & Verkehrssicherung)**
    *   **Verkehrssicherung:** Unverzüglich geeignete Maßnahmen zur Verkehrssicherung einleiten (z.B. Warnblinkanlage des Einsatzfahrzeugs, Warndreiecke, Warnleuchten).
    *   **Gefahrenbereich:** Sicherstellen, dass der Arbeitsbereich für Personal und Verkehrsteilnehmer gefahrlos ist.
    *   **Meldung:** Bei akuter Gefährdung (z.B. Ampel komplett ausgefallen, Dauerrot/Dauergrün) umgehend die Leitstelle informieren und ggf. Polizei/Verkehrslenkung anfordern.

2.  **Sichtprüfung (Erste Einschätzung)**
    *   **Umgebung:** Gibt es offensichtliche äußere Einflüsse (z.B. Sturmschäden, Vandalismus, Bauarbeiten in der Nähe, lose Kabel)?
    *   **Ampelköpfe:** Sind alle Leuchtmittel intakt? Gibt es sichtbare Beschädigungen an den Ampelköpfen oder deren Aufhängung?
    *   **Schaltkasten:** Ist der Schaltkasten unbeschädigt und verschlossen? Gibt es Anzeichen von Feuchtigkeitseintritt oder Überhitzung (Geruch)?
    *   **Zuleitungen:** Sind die Zuleitungen zur Ampel und zum Schaltkasten unbeschädigt?

3.  **Diagnose/Beobachtung (Fehleranalyse)**
    *   **Fehlerbild:** Das genaue Verhalten der Ampel beobachten. Tritt der Fehler nur in der genannten Richtung ("backward") auf?
    *   **Frequenz:** Wie oft treten die Aussetzer/Neustarts auf? Gibt es ein Muster (z.B. zu bestimmten Tageszeiten, bei bestimmten Schaltvorgängen)?
    *   **Dauer:** Wie lange dauern die Aussetzer an?
    *   **Fehlermeldungen:** Gibt es am Steuergerät im Schaltkasten sichtbare Fehlermeldungen oder Status-LEDs, die auf einen Fehler hinweisen? (Ggf. Handbuch des Steuergeräts konsultieren).
    *   **Spannungsversorgung:** Wenn möglich und sicher, die Spannungsversorgung im Schaltkasten prüfen (z.B. auf Unterspannung oder Schwankungen).

4.  **Dokumentation (Beweissicherung & Nachvollziehbarkeit)**
    *   **Zeitpunkt:** Genaue Uhrzeit der Feststellung und der Beobachtungen.
    *   **Beschreibung:** Detaillierte Beschreibung des Fehlerbildes (was genau passiert, welche Richtung betroffen ist, Frequenz, Dauer).
    *   **Fotos:** Aussagekräftige Fotos von der Situation, dem Schaltkasten (innen/außen), eventuellen Beschädigungen oder Fehlermeldungen.
    *   **Maßnahmen:** Welche Schritte wurden bereits unternommen (Absicherung, Prüfungen)?
    *   **Asset-ID:** Immer die korrekte Asset-ID (n6887356461) angeben.

5.  **Eskalation (Nächste Schritte)**
    *   **Behebung vor Ort:** Wenn die Ursache klar ist (z.B. lose Klemme, defekte Sicherung) und eine sichere Behebung vor Ort möglich ist, diese durchführen und Funktionstest machen.
    *   **Fachpersonal:** Bei komplexen Fehlern, die über die Kompetenz des Außendienstes hinausgehen (z.B. Steuergerätefehler, Verkabelungsprobleme, die nicht sofort ersichtlich sind), umgehend den zuständigen Fachdienst (Elektriker, Ampeltechniker) informieren und die gesammelten Informationen übermitteln.
    *   **Priorität:** Die Dringlichkeit der Eskalation basierend auf der potenziellen Gefährdung des Verkehrs festlegen.

**Annahme:** Die Bezeichnung "Richtung: backward" bezieht sich auf eine spezifische Fahrtrichtung oder einen Signalgeber, der in der Dokumentation der Anlage so benannt ist. Falls unklar, bitte präzisieren.

---

## C13

- Domaene: LAMP

### USER MESSAGE

```
Unregelmäßiges Verhalten (an/aus), Ursache unklar.
```

### CONTEXT (wie vom Judge gesehen)

```json
{
  "incident": {
    "fault_type": "intermittent",
    "severity": "low",
    "reported_at": "2026-01-17T01:08:07+01:00",
    "reporter": "patrol"
  },
  "asset": {
    "asset_osm": "n4449540379",
    "latitude": 47.8772297,
    "longitude": 12.1220096,
    "name": "Langenpfunzen, Römerstraße",
    "lit": "yes"
  },
  "device": {
    "connectivity": "offline",
    "device_state": "ok"
  },
  "environment": {
    "time_of_day": "day",
    "weather": "fog",
    "lighting_condition": "normal_visibility",
    "traffic_exposure": "medium",
    "noise_level": "high"
  },
  "extras": {
    "context_notes": [
      "device.* beschreibt das Techniker-Gerät (App/Smartphone), NICHT das Asset.",
      "connectivity/device_state beeinflusst Vorgehen (z.B. offlinefähig dokumentieren), ist keine Fehlerursache des Assets.",
      "Wenn connectivity=offline/spotty: nutze Offline-Workflow (lokal dokumentieren/Foto lokal speichern) und später synchronisieren; keine Schritte, die Online-Zugriff voraussetzen."
    ]
  }
}
```

### EXPECTED ELEMENTS

```
(leer -- test_loader schreibt keinen Schluessel expected_elements_short in input.meta, der Judge erhielt hier keinen Inhalt)
```

### MODEL ANSWER

Ein unregelmäßiges Schaltverhalten (an/aus) einer Straßenleuchte erfordert eine systematische Vorgehensweise, um die Ursache zu ermitteln und die Verkehrssicherheit zu gewährleisten.

**Checkliste für den Außendienst:**

1.  **Absicherung (Priorität: Sicherheit)**
    *   **Verkehrssicherung:** Unmittelbare Absicherung der Arbeitsstelle gemäß UVV und örtlichen Vorschriften (Warnweste, ggf. Warndreieck/Blitzleuchte aufstellen).
    *   **Gefahrenbeurteilung:** Prüfen, ob eine unmittelbare Gefahr für Passanten oder Verkehrsteilnehmer besteht (z.B. herabhängende Kabel, stark beschädigter Mast). Bei akuter Gefahr sofort großräumig absperren und Vorgesetzte/Notdienst informieren.

2.  **Sichtprüfung (Erste Einschätzung)**
    *   **Leuchte:** Optische Kontrolle der Leuchte auf äußere Beschädigungen (Gehäuse, Glasbruch, lose Teile).
    *   **Mast:** Überprüfung des Mastes auf Risse, Korrosion, Vandalismus oder Anfahrtschäden.
    *   **Kabel/Anschlüsse:** Sichtkontrolle der Zuleitungen und Anschlüsse am Mastfuß auf Beschädigungen, Korrosion oder lose Verbindungen.
    *   **Umgebung:** Prüfen, ob externe Faktoren das Schaltverhalten beeinflussen könnten (z.B. starker Bewuchs, der Sensoren verdeckt; Baustellenaktivitäten; starke Vibrationen).

3.  **Diagnose/Beobachtung (Ursachenforschung)**
    *   **Verhaltensbeobachtung:** Da das Verhalten unregelmäßig ist, die Leuchte über einen längeren Zeitraum beobachten. Notieren Sie, wann sie schaltet (an/aus) und wie lange die jeweiligen Zustände anhalten.
    *   **Tageszeit/Umwelt:** Berücksichtigen Sie, dass es tagsüber ist und Nebel herrscht. Prüfen Sie, ob die Leuchte bei diesen Lichtverhältnissen überhaupt aktiv sein sollte (Helligkeitssensor).
    *   **Reproduktion (vorsichtig):** Falls sicher und ohne Risiko, versuchen Sie, das Verhalten durch leichte äußere Einwirkung (z.B. vorsichtiges Rütteln am Mast) zu reproduzieren, um lose Kontakte auszuschließen.
    *   **Messung (falls möglich):** Wenn geschult und mit passendem Werkzeug ausgestattet, Spannung und Strom am Leuchtenanschluss messen, um elektrische Fehler einzugrenzen.

4.  **Dokumentation (Offline-Workflow beachten)**
    *   **Wichtig:** Ihr Gerät ist offline. Alle Daten müssen lokal gespeichert und später synchronisiert werden.
    *   **Fotos:** Machen Sie aussagekräftige Fotos vom Zustand der Leuchte, des Mastes und der Umgebung.
    *   **Beschreibung:** Notieren Sie detailliert das beobachtete unregelmäßige Verhalten, mögliche Auffälligkeiten und die durchgeführten Prüfschritte.
    *   **Standortdaten:** Bestätigen Sie den Standort (Langenpfunzen, Römerstraße) und die Asset-ID (n4449540379).
    *   **Offline-Speicherung:** Stellen Sie sicher, dass alle erfassten Informationen und Fotos sicher auf Ihrem Gerät gespeichert sind, um sie bei der nächsten Online-Verbindung zu synchronisieren.

5.  **Eskalation (Nächste Schritte)**
    *   **Behebung nicht möglich:** Wenn die Ursache nicht vor Ort behoben werden kann oder spezielle Fachkenntnisse/Werkzeuge erforderlich sind, leiten Sie den Fall mit allen gesammelten Informationen an die zuständige Fachabteilung (z.B. Elektriker, Wartungsteam) weiter.
    *   **Sicherheitsrisiko:** Bei Feststellung eines Sicherheitsrisikos (z.B. Stromschlaggefahr, drohender Mastbruch) sofort die Leuchte außer Betrieb nehmen (falls möglich und sicher), den Bereich absperren und die Notfallkette aktivieren.
    *   **Empfehlung:** Geben Sie eine Empfehlung für die weiteren Schritte ab, basierend auf Ihren Beobachtungen und Diagnosen.

---

## C14

- Domaene: LAMP

### USER MESSAGE

```
Lampe leuchtet gar nicht mehr. Meldung kam über Bürgerhinweis. (Asset-ID: n4427359783)
```

### CONTEXT (wie vom Judge gesehen)

```json
{
  "asset_osm": "n4427359783"
}
```

### EXPECTED ELEMENTS

```
(leer -- test_loader schreibt keinen Schluessel expected_elements_short in input.meta, der Judge erhielt hier keinen Inhalt)
```

### MODEL ANSWER

Okay, hier ist die Schritt-für-Schritt-Checkliste für die defekte Straßenlampe (Asset-ID: n4427359783), basierend auf dem Bürgerhinweis:

**Checkliste: Straßenlampe leuchtet nicht (Asset-ID: n4427359783)**

1.  **Absicherung (Priorität: Sicherheit & Verkehrssicherung)**
    *   Fahrzeug sicher abstellen (Warnblinkanlage, Warnweste anlegen).
    *   Gefahrenbereich um die Lampe absichern (z.B. mit Warnkegeln, Blitzleuchte), besonders wenn sich die Lampe im Verkehrsraum befindet oder eine unmittelbare Gefahr (z.B. herabhängende Teile) besteht.
    *   Auf den fließenden Verkehr und Passanten achten.

2.  **Sichtprüfung (Erste Einschätzung)**
    *   **Lampe selbst:** Ist das Leuchtmittel sichtbar beschädigt (z.B. Glasbruch, fehlende Abdeckung)?
    *   **Mast:** Sind Beschädigungen am Mast erkennbar (z.B. Anfahrtsschäden, Korrosion, Risse)?
    *   **Zuleitung/Anschluss:** Sind sichtbare Beschädigungen an Kabeln oder am Anschlusskasten am Mastfuß vorhanden?
    *   **Umgebung:** Gibt es Anzeichen für Vandalismus oder äußere Einwirkungen (z.B. Baufahrzeuge in der Nähe, umgestürzte Bäume)?
    *   **Schaltkasten/Verteiler (falls zugänglich und sicher):** Sind Sicherungen ausgelöst? (Nur prüfen, wenn dafür autorisiert und geschult!)

3.  **Diagnose/Beobachtung (Fehlerursache eingrenzen)**
    *   **Einzelschaden oder Reihenschaden?** Leuchten benachbarte Lampen? Dies hilft zu klären, ob es sich um einen lokalen Defekt oder ein Problem in der Stromversorgung des gesamten Abschnitts handelt.
    *   **Tageszeit:** Ist die Lampe tagsüber ausgefallen oder leuchtet sie auch nachts nicht? (Bürgerhinweis deutet auf dauerhaften Ausfall hin).
    *   **Geräusche/Gerüche:** Gibt es ungewöhnliche Geräusche (z.B. Brummen) oder Gerüche (z.B. Brandgeruch) im Bereich der Lampe oder des Schaltkastens?

4.  **Dokumentation**
    *   **Fotos:** Machen Sie aussagekräftige Fotos vom Zustand der Lampe, des Mastes und eventueller Beschädigungen oder Auffälligkeiten.
    *   **Notizen:**
        *   Datum, Uhrzeit des Vor-Ort-Termins.
        *   Genaue Position der Lampe (ggf. GPS-Koordinaten, Hausnummer).
        *   Festgestellte Mängel (z.B. "Leuchtmittel defekt", "Kabelbruch", "Sicherung ausgelöst", "keine sichtbare Ursache").
        *   Status benachbarter Lampen.
        *   Angaben zur Verkehrssicherung.
        *   Wetterbedingungen.

5.  **Eskalation**
    *   **Meldung an die zuständige Stelle:** Leiten Sie alle gesammelten Informationen (Asset-ID, Fotos, Notizen) umgehend an die Leitstelle oder den zuständigen Fachbereich weiter.
    *   **Priorisierung:** Wenn eine unmittelbare Gefahr für die Verkehrssicherheit besteht (z.B. herabhängende Teile, Stromschlaggefahr), kennzeichnen Sie dies als dringende Störung.
    *   **Nächste Schritte:** Erfragen Sie die weiteren Anweisungen oder die Beauftragung eines Elektrikers/Spezialisten zur Reparatur.

---

## C15

- Domaene: SIGNAL

### USER MESSAGE

```
Störung tritt sporadisch auf: zeitweise normal, dann Aussetzer.
```

### CONTEXT (wie vom Judge gesehen)

```json
{
  "_unstructured_text": "day | ok | False | patrol | online | high | 2026-01-21T19:27:27+01:00 | 47.8729153 | clear | intermittent | low | high | n48911455 | 12.1106825 | normal_visibility"
}
```

### EXPECTED ELEMENTS

```
(leer -- test_loader schreibt keinen Schluessel expected_elements_short in input.meta, der Judge erhielt hier keinen Inhalt)
```

### MODEL ANSWER

Bei einer sporadisch auftretenden Störung an einer Straßenlampe oder Ampelanlage ist ein strukturiertes Vorgehen entscheidend, um Sicherheit zu gewährleisten und die Ursache zu finden. Hier ist eine Schritt-für-Schritt-Checkliste:

**Checkliste für sporadische Störungen (z.B. Asset n48911455)**

1.  **Absicherung (Sicherheit geht vor!)**
    *   **Verkehrssicherung:** Unmittelbar nach Ankunft die Arbeitsstelle gemäß den Vorschriften absichern (Warnblinkanlage, Warnleuchten, Warndreieck, ggf. Leitkegel aufstellen).
    *   **Persönliche Schutzausrüstung (PSA):** Sicherstellen, dass die gesamte PSA (Warnkleidung, Sicherheitsschuhe, Helm, Handschuhe) korrekt getragen wird.
    *   **Gefahrenbereich:** Den Gefahrenbereich um die Anlage (Mast, Schaltkasten) kennzeichnen und unbefugten Zutritt verhindern.

2.  **Sichtprüfung (Erster Überblick)**
    *   **Umgebung:** Gibt es offensichtliche äußere Beschädigungen am Mast, Leuchtenkopf, Schaltkasten oder der Verkabelung? (z.B. Vandalismus, Anfahrschäden, lose Kabel).
    *   **Leuchtmittel/Optik:** Ist das Leuchtmittel intakt? Sind die Abdeckungen sauber und unbeschädigt? Bei Ampeln: Sind alle Optiken klar und unbeschädigt?
    *   **Schaltkasten:** Ist der Schaltkasten verschlossen und unbeschädigt? Sind Sicherungen sichtbar ausgelöst (falls von außen erkennbar)?
    *   **Umwelteinflüsse:** Gibt es Anzeichen für Wassereintritt, Überhitzung, Insektenbefall oder andere Umwelteinflüsse, die die Funktion beeinträchtigen könnten?

3.  **Diagnose/Beobachtung (Dem Fehler auf der Spur)**
    *   **Verhalten beobachten:** Da die Störung sporadisch auftritt, ist eine längere Beobachtung notwendig.
        *   Wie lange bleibt die Anlage in Betrieb, bevor der Aussetzer kommt?
        *   Wie lange dauert der Aussetzer?
        *   Gibt es Muster (z.B. nur bei bestimmten Wetterbedingungen, Tageszeiten, oder nach dem Einschalten/Umschalten)?
    *   **Schaltvorgänge:** Wenn möglich und sicher, Schaltvorgänge (z.B. Ein-/Ausschalten der Anlage, Umschalten der Ampelphasen) manuell auslösen und das Verhalten protokollieren.
    *   **Spannungsmessung (falls autorisiert und sicher):** Bei Ausfall die Spannung am Leuchtmittel/Ampelmodul und im Schaltkasten prüfen, um festzustellen, ob die Stromversorgung unterbrochen ist oder das Leuchtmittel/Modul selbst defekt ist.
    *   **Wärmeentwicklung:** Auf ungewöhnliche Wärmeentwicklung an Komponenten achten.
    *   **Geräusche/Gerüche:** Ungewöhnliche Geräusche (z.B. Knistern, Brummen) oder Gerüche (z.B. verschmorter Kunststoff) wahrnehmen.

4.  **Dokumentation (Präzise Erfassung)**
    *   **Asset-ID:** n48911455
    *   **Standort:** 47.8729153, 12.1106825
    *   **Datum/Uhrzeit:** Genaue Angabe des Beginns der Beobachtung und des Zeitpunkts der Störung (z.B. 2026-01-21T19:27:27+01:00).
    *   **Fehlerbeschreibung:** Detaillierte Beschreibung des beobachteten Verhaltens ("zeitweise normal, dann Aussetzer").
    *   **Umgebungsbedingungen:** Wetter (klar, normal_visibility), Temperatur, besondere Vorkommnisse.
    *   **Durchgeführte Maßnahmen:** Welche Schritte wurden unternommen (z.B. Sichtprüfung, Beobachtung über X Minuten, Schaltvorgänge)?
    *   **Feststellungen:** Alle Beobachtungen aus Schritt 2 und 3 (z.B. "keine äußeren Schäden", "Ausfall nach 15 Minuten Betrieb für 2 Minuten", "Spannung im Schaltkasten stabil").
    *   **Fotos/Videos:** Aussagekräftige Bilder oder kurze Videos der Störung und der Umgebung anfertigen.

5.  **Eskalation (Nächste Schritte einleiten)**
    *   **Priorität:** Angesichts der "high" Priorität ist schnelles Handeln erforderlich.
    *   **Fachabteilung/Störungsdienst:** Die gesammelten Informationen umgehend an die zuständige Fachabteilung oder den Störungsdienst weiterleiten.
    *   **Empfehlung:** Basierend auf den Beobachtungen eine Empfehlung abgeben (z.B. "Austausch des Vorschaltgeräts empfohlen", "Tiefenprüfung der Verkabelung notwendig", "Beobachtung über längeren Zeitraum durch spezialisiertes Team").
    *   **Verkehrssicherung beibehalten:** Falls die Störung ein Sicherheitsrisiko darstellt (z.B. Ampel komplett ausgefallen), muss die Absicherung aufrechterhalten oder verstärkt werden, bis eine dauerhafte Lösung gefunden ist.

**Wichtiger Hinweis:** Führen Sie nur Arbeiten durch, für die Sie qualifiziert und autorisiert sind. Bei Unsicherheiten oder komplexen Fehlern immer die Eskalationskette einhalten.

---

## C16

- Domaene: SIGNAL

### USER MESSAGE

```
Ampel scheint auf Rot zu „hängen“. Kein Umschalten beobachtet.
```

### CONTEXT (wie vom Judge gesehen)

```json
{
  "_raw_text": "Betroffene Lichtsignalanlage: OSM-ID n35664971, Koordinaten 47.8520758, 12.1171619. Gemeldeter Fehler: feststehendes Signal, Schweregrad hoch. Gemeldet am 2026-01-21T20:54:52+01:00 von Leitstelle. Foto vorhanden. Bildbeschreibung: Dauerhaft rote Phase erkennbar, kein Phasenwechsel sichtbar. Staubildung an Kreuzung. Umgebung: tagsüber, Wetter klar, Sichtweite normal_visibility, Verkehrsaufkommen mittel. Technikgerät des Außendienstmitarbeiters: Konnektivität instabil, Gerätezustand in Ordnung."
}
```

### EXPECTED ELEMENTS

```
(leer -- test_loader schreibt keinen Schluessel expected_elements_short in input.meta, der Judge erhielt hier keinen Inhalt)
```

### MODEL ANSWER

Ein feststehendes Rotsignal ist eine kritische Störung, die sofortiges Handeln erfordert, um die Verkehrssicherheit zu gewährleisten. Hier ist eine Schritt-für-Schritt-Checkliste für den Außendienst:

**Checkliste für Störung an Lichtsignalanlage (OSM-ID n35664971, 47.8520758, 12.1171619)**

**1. Absicherung (Priorität: Sicherheit)**
*   **Verkehrssicherung:** Unverzüglich geeignete Maßnahmen zur Verkehrssicherung einleiten (z.B. Warnblinkanlage des Einsatzfahrzeugs, Warndreieck, Warnleuchten). Bei Bedarf Polizei oder Verkehrsregelung anfordern, insbesondere bei hohem Verkehrsaufkommen und Staubildung.
*   **Persönliche Schutzausrüstung (PSA):** Sicherstellen, dass die vollständige PSA (Warnkleidung, Sicherheitsschuhe) getragen wird.
*   **Standortwahl:** Einsatzfahrzeug sicher und sichtbar abstellen, um den Arbeitsbereich zu schützen und den fließenden Verkehr nicht zusätzlich zu behindern.

**2. Sichtprüfung (Erste Einschätzung)**
*   **Bestätigung der Störung:** Prüfen, ob die gemeldete "dauerhaft rote Phase" und das Ausbleiben des Phasenwechsels (wie im Foto beschrieben) weiterhin bestehen.
*   **Gesamtanlage:** Kurze Sichtprüfung der gesamten Kreuzung auf weitere Auffälligkeiten (z.B. andere defekte Signale, beschädigte Masten, offene Kabelkanäle).
*   **Umgebung:** Beachten, ob externe Faktoren (z.B. Baustellen, Unfälle, extreme Witterung) die Störung beeinflussen könnten. (Aktuell: tagsüber, Wetter klar, Sicht normal, Verkehrsaufkommen mittel).

**3. Diagnose/Beobachtung (Fehlerursache eingrenzen)**
*   **Steuergerät:** Wenn sicher zugänglich, das Steuergerät der Ampelanlage prüfen.
    *   **Statusanzeigen:** Leuchten alle Status-LEDs normal? Gibt es Fehlermeldungen auf dem Display?
    *   **Sicherungen/Schutzschalter:** Sind alle Sicherungen intakt und Schutzschalter eingeschaltet?
    *   **Stromversorgung:** Ist die Stromversorgung vorhanden?
*   **Kabel/Verbindungen:** Sichtprüfung auf offensichtliche Beschädigungen an Kabeln oder Steckverbindungen im Bereich des Steuergeräts und der Signalgeber.
*   **Phasenablauf:** Wenn möglich und sicher, den Phasenablauf über einen längeren Zeitraum beobachten, um das Ausmaß der Störung genau zu erfassen (z.B. ob *alle* Phasen betroffen sind oder nur eine bestimmte Richtung).
*   **Sensorik:** Gibt es Induktionsschleifen oder Kameras, die nicht reagieren könnten?

**4. Dokumentation (Beweissicherung und Informationsgrundlage)**
*   **Fotos/Videos:** Weitere Fotos oder Videos der aktuellen Situation aufnehmen (Gesamtkreuzung, betroffene Signalgeber, Steuergerät-Anzeigen).
*   **Fehlerbeschreibung:** Genaue Beschreibung der Beobachtungen: Welche Signale sind betroffen? Seit wann? Gibt es Geräusche?
*   **Maßnahmen:** Dokumentation der bereits durchgeführten Absicherungs- und Diagnosemaßnahmen.
*   **Gerätezustand:** Notieren, dass die Konnektivität des Technikgeräts instabil ist, aber der Gerätezustand in Ordnung ist. Dies ist wichtig für die Übermittlung der Daten.

**5. Eskalation (Maßnahmen einleiten)**
*   **Leitstelle informieren:** Unverzüglich die Leitstelle über den aktuellen Status, die bestätigte Störung und die eingeleiteten Maßnahmen informieren.
*   **Dringlichkeit:** Aufgrund des hohen Schweregrads und der Staubildung ist eine schnelle Behebung essenziell. Die Leitstelle muss über die Notwendigkeit einer sofortigen Reparatur oder des Einsatzes weiterer Kräfte (z.B. Elektriker, Verkehrsregelung) entscheiden.
*   **Anweisungen abwarten:** Auf weitere Anweisungen der Leitstelle warten, bevor eigenmächtig tiefergehende Reparaturen durchgeführt werden, die über die Erstdiagnose hinausgehen.
*   **Kommunikation:** Regelmäßige Updates an die Leitstelle senden, auch bei instabiler Konnektivität, um den Informationsfluss sicherzustellen.

---

## C17

- Domaene: SIGNAL

### USER MESSAGE

```
Ampel funktioniert aktuell, aber wiederholt Ausfälle gemeldet. (Hauptverkehrszeit / hoher Verkehr).
```

### CONTEXT (wie vom Judge gesehen)

```json
{
  "asset": {
    "asset_osm": "n35664946",
    "longitude": 12.1102703,
    "latitude": 47.8539754,
    "crs": "EPSG:4326",
    "traffic_signals": null,
    "traffic_signals:direction": null,
    "button_operated": null
  },
  "incident": {
    "fault_type": "intermittent",
    "severity": "medium",
    "reported_at": "2026-01-18T00:42:54+01:00",
    "reporter": "patrol",
    "photo_available": false
  },
  "environment": {
    "time_of_day": "rush_hour",
    "weather": "clear",
    "visibility": "normal_visibility",
    "traffic_exposure": "high",
    "noise_level": "high"
  },
  "device": {
    "device_state": "ok",
    "connectivity": "online"
  }
}
```

### EXPECTED ELEMENTS

```
(leer -- test_loader schreibt keinen Schluessel expected_elements_short in input.meta, der Judge erhielt hier keinen Inhalt)
```

### MODEL ANSWER

Hier ist die Schritt-für-Schritt-Checkliste für den Vor-Ort-Einsatz bei einer Ampelanlage mit wiederholten Ausfällen:

**1. Absicherung (Priorität: Sicherheit & Verkehrssicherung)**
*   **Verkehrssicherung:** Unverzüglich geeignete Warnkleidung anlegen. Gefahrenbereich mit Warndreiecken, Blitzleuchten und/oder Warnkegeln absichern, um den fließenden Verkehr und die eigene Sicherheit zu gewährleisten. Bei Bedarf Polizei oder Verkehrslenkung anfordern, insbesondere da es sich um Hauptverkehrszeit und hohes Verkehrsaufkommen handelt.
*   **Persönliche Schutzausrüstung (PSA):** Helm, Sicherheitsschuhe und Handschuhe tragen.

**2. Sichtprüfung (Erste Einschätzung)**
*   **Gesamtzustand:** Allgemeine Sichtprüfung der Ampelanlage (Masten, Leuchten, Kabel).
*   **Offensichtliche Schäden:** Sind Leuchten beschädigt, Kabel lose, Schaltschranktüren offen oder gibt es Anzeichen von Vandalismus/Unfall?
*   **Umgebung:** Gibt es Bauarbeiten, Wasseransammlungen oder andere externe Faktoren, die die Funktion beeinträchtigen könnten?

**3. Diagnose/Beobachtung (Fokus auf intermittierenden Fehler)**
*   **Verhalten beobachten:** Da die Ampel aktuell funktioniert, muss das intermittierende Verhalten beobachtet werden. Dies erfordert Geduld.
*   **Fehlerprotokoll:** Wenn möglich, das Fehlerprotokoll im Schaltschrank auslesen.
*   **Spannungsversorgung:** Überprüfung der Spannungsversorgung im Schaltschrank (Sicherungen, Schutzschalter).
*   **Steuerung:** Funktionieren alle Signalgeber korrekt? Gibt es Auffälligkeiten in den Schaltzyklen (z.B. zu kurze Grünphasen, fehlende Phasen)?
*   **Kabelverbindungen:** Sichtprüfung auf lockere oder korrodierte Kabelverbindungen, insbesondere an den Signalgebern und im Schaltschrank.
*   **Sensoren/Detektoren:** Falls vorhanden, Funktion der Verkehrssensoren (Induktionsschleifen, Radardetektoren) prüfen. Sind diese verschmutzt oder beschädigt?
*   **Umwelteinflüsse:** Beobachten, ob der Ausfall bei bestimmten Bedingungen (z.B. Erschütterungen durch Schwerverkehr, Wind, Sonneneinstrahlung auf Sensoren) auftritt.

**4. Dokumentation (Lückenlose Erfassung)**
*   **Datum/Uhrzeit:** Genaue Angaben zum Zeitpunkt des Einsatzes und der Beobachtungen.
*   **Feststellungen:** Detaillierte Beschreibung aller Beobachtungen (z.B. "Ampel fiel für 30 Sekunden aus, dann normaler Betrieb", "Flackern der Rotphase an Signalgeber X").
*   **Maßnahmen:** Welche Schritte wurden unternommen (z.B. "Sicherungen geprüft, keine Auffälligkeiten").
*   **Fotos:** Falls möglich, Fotos von relevanten Stellen (Schaltschrank, beschädigte Komponenten, Verkehrssituation).
*   **Verkehrssituation:** Notieren des Verkehrsaufkommens und der Auswirkungen des Fehlers.
*   **Gerätezustand:** Bestätigung, dass der Gerätezustand aktuell "ok" und die Konnektivität "online" ist, aber der Fehler "intermittent" auftritt.

**5. Eskalation (Fachgerechte Weiterleitung)**
*   **Sofortige Meldung:** Bei anhaltenden oder kritischen Ausfällen, die die Verkehrssicherheit gefährden, sofort die zuständige Fachabteilung/Leitstelle informieren.
*   **Detaillierte Übergabe:** Alle gesammelten Informationen (Dokumentation) an den nachfolgenden Dienst oder spezialisierten Techniker weitergeben, um eine gezielte Fehlerbehebung zu ermöglichen.
*   **Empfehlung:** Aufgrund der intermittierenden Natur und des hohen Verkehrsaufkommens ist eine tiefgreifendere Diagnose durch einen spezialisierten Techniker mit entsprechender Messtechnik erforderlich. Eine temporäre Verkehrsregelung (z.B. durch Polizei) kann während der Stoßzeiten notwendig sein, bis der Fehler behoben ist.

---

## C18

- Domaene: LAMP

### USER MESSAGE

```
Straßenlampe ist dunkel seit etwa 90 Minuten. Bereich wirkt unsicher. (Asset-ID: n12551286240)
```

### CONTEXT (wie vom Judge gesehen)

```json
{
  "asset_osm": "n12551286240"
}
```

### EXPECTED ELEMENTS

```
(leer -- test_loader schreibt keinen Schluessel expected_elements_short in input.meta, der Judge erhielt hier keinen Inhalt)
```

### MODEL ANSWER

Hier ist die Schritt-für-Schritt-Checkliste für die dunkle Straßenlampe:

1.  **Absicherung:**
    *   **Priorität:** Eigensicherung und Verkehrssicherung.
    *   Sichern Sie den Bereich um die dunkle Straßenlampe ab, insbesondere wenn die Dunkelheit die Verkehrssicherheit beeinträchtigt oder eine Gefahrenquelle darstellt. Nutzen Sie Warnkleidung, Warndreiecke, Blitzleuchten oder andere geeignete Mittel.
    *   Beurteilen Sie, ob eine sofortige Sperrung des Bereichs oder eine Umleitung notwendig ist.

2.  **Sichtprüfung:**
    *   Überprüfen Sie die Lampe und den Mast auf offensichtliche Beschädigungen (z.B. Vandalismus, Sturmschäden, angefahrene Masten, offene Kabel).
    *   Gibt es in der Nähe weitere dunkle Lampen? Dies könnte auf eine größere Störung (z.B. Sicherungsausfall im Verteilerkasten) hindeuten.
    *   Ist die Lampe eventuell nur verschmutzt oder verdeckt (z.B. durch Bewuchs)?

3.  **Diagnose/Beobachtung:**
    *   Hören Sie auf ungewöhnliche Geräusche (z.B. Brummen, Knistern) am Mast oder im Leuchtenkopf.
    *   Gibt es Anzeichen für einen Kurzschluss oder Überhitzung (Brandgeruch)?
    *   Falls gefahrlos möglich und geschult: Überprüfen Sie, ob der Sicherungsautomat im zugehörigen Verteilerkasten ausgelöst hat. **Achtung: Nur durch geschultes Personal!**

4.  **Dokumentation:**
    *   Halten Sie den genauen Standort fest.
    *   Notieren Sie die **Asset-ID: n12551286240**.
    *   Dokumentieren Sie den Zeitpunkt der Feststellung (seit ca. 90 Minuten dunkel).
    *   Beschreiben Sie den Zustand der Lampe und des Umfelds (z.B. "Bereich wirkt unsicher").
    *   Machen Sie Fotos von der Situation und eventuellen Beschädigungen.
    *   Erfassen Sie alle durchgeführten Absicherungsmaßnahmen.

5.  **Eskalation:**
    *   Melden Sie den Vorfall umgehend an die zuständige Leitstelle oder den Bereitschaftsdienst.
    *   Geben Sie alle gesammelten Informationen (Asset-ID, Standort, Beobachtungen, Absicherungsmaßnahmen) präzise weiter.
    *   Fordern Sie bei Bedarf die Entsendung eines Elektrikers oder eines spezialisierten Teams an.
    *   Bleiben Sie vor Ort, bis die Situation sicher ist oder Ablösung eintrifft, falls dies die Anweisung ist.

---

## C19

- Domaene: LAMP

### USER MESSAGE

```
Lampe leuchtet gar nicht mehr. Meldung kam über Routinekontrolle.
```

### CONTEXT (wie vom Judge gesehen)

```json
{
  "_raw_text": "Die Straßenlampe befindet sich am Standort None (OSM-ID: n4939032525, Koordinaten: 47.8553091, 12.1230035). Gemeldeter Fehler: outage, Schweregrad mittel. Gemeldet am 2026-01-21T11:45:31+01:00 von Streife. Kein Foto verfügbar. Umgebung: tagsüber, Wetter klar, Lichtverhältnisse normal_visibility, Verkehrsaufkommen gering. Technikgerät des Außendienstmitarbeiters: Konnektivität online, Gerätezustand in Ordnung."
}
```

### EXPECTED ELEMENTS

```
(leer -- test_loader schreibt keinen Schluessel expected_elements_short in input.meta, der Judge erhielt hier keinen Inhalt)
```

### MODEL ANSWER

Okay, die Straßenlampe am Standort None (OSM-ID: n4939032525, Koordinaten: 47.8553091, 12.1230035) leuchtet nicht mehr. Hier ist die Schritt-für-Schritt-Checkliste für den Außendienst:

**Checkliste: Straßenlampenausfall (Schweregrad mittel)**

1.  **Absicherung (Sicherheit geht vor)**
    *   **Verkehrssicherung:** Bei Bedarf und je nach Standort (auch bei geringem Verkehrsaufkommen) den Arbeitsbereich gemäß UVV und StVO absichern (z.B. Warnblinkanlage, Warnweste, ggf. Warndreieck/Leitkegel).
    *   **Persönliche Schutzausrüstung (PSA):** Sicherstellen, dass die vollständige PSA (Warnweste, Sicherheitsschuhe, ggf. Handschuhe) getragen wird.
    *   **Gefahrenbereich prüfen:** Auf offensichtliche Gefahren wie beschädigte Kabel, offene Verteilerkästen oder instabile Masten achten. Bei unmittelbarer Gefahr: Arbeitsbereich sofort verlassen und Notfallkette einleiten.

2.  **Sichtprüfung (Erste Einschätzung)**
    *   **Mast und Leuchtenkopf:** Auf äußerliche Beschädigungen (Anfahrschäden, Vandalismus, Korrosion, lose Teile) prüfen.
    *   **Zuleitung/Kabel:** Sichtprüfung der sichtbaren Kabel auf Beschädigungen oder Manipulationen.
    *   **Leuchtmittel/Abdeckung:** Ist das Leuchtmittel sichtbar defekt (z.B. zerbrochene Lampe, geschwärzter Kolben)? Ist die Abdeckung intakt oder beschädigt/fehlt sie?
    *   **Umgebung:** Gibt es Anzeichen für Bauarbeiten, Erdarbeiten oder andere Aktivitäten in der Nähe, die die Stromversorgung beeinträchtigt haben könnten?

3.  **Diagnose/Beobachtung (Fehlerursache eingrenzen)**
    *   **Sicherungskasten/Verteiler:** Wenn zugänglich und autorisiert, den Sicherungskasten der Leuchte prüfen. Ist die Sicherung ausgelöst? (Vorsicht: Nur bei entsprechender Qualifikation und unter Beachtung der Sicherheitsvorschriften!)
    *   **Schaltuhr/Steuerung:** Bei Einzelsteuerung: Funktion der Schaltuhr oder des Dämmerungsschalters prüfen.
    *   **Gruppenfehler:** Leuchten in der direkten Umgebung prüfen. Sind weitere Leuchten in der gleichen Gruppe ausgefallen? Dies könnte auf einen Fehler in der Zuleitung oder im Verteiler hindeuten.
    *   **Gerätediagnose:** Falls das Technikgerät des Außendienstmitarbeiters entsprechende Diagnosefunktionen für die Leuchte bietet, diese nutzen.

4.  **Dokumentation (Lückenlose Erfassung)**
    *   **Fehlerbeschreibung:** Genaue Beschreibung des festgestellten Fehlers (z.B. "Lampe komplett dunkel", "Sicherung ausgelöst", "Kabelbruch sichtbar").
    *   **Maßnahmen:** Welche Schritte wurden unternommen (z.B. "Sicherung geprüft", "Sichtprüfung durchgeführt").
    *   **Umgebungsbedingungen:** Bestätigung der gemeldeten Bedingungen (tagsüber, klares Wetter, normale Sicht, geringes Verkehrsaufkommen).
    *   **Fotos:** Auch wenn kein Foto gemeldet wurde, jetzt unbedingt Fotos vom Zustand der Leuchte, eventuellen Beschädigungen und der Umgebung machen.
    *   **GPS-Koordinaten:** Bestätigung der Koordinaten oder Korrektur, falls nötig.
    *   **Zeitstempel:** Genaue Uhrzeit der Feststellung und der durchgeführten Maßnahmen.
    *   **Materialbedarf:** Einschätzung, welche Ersatzteile oder welches Material für die Reparatur benötigt werden könnten.

5.  **Eskalation (Nächste Schritte einleiten)**
    *   **Reparaturauftrag:** Basierend auf der Diagnose einen detaillierten Reparaturauftrag erstellen.
    *   **Fachpersonal:** Wenn der Fehler nicht vor Ort behoben werden kann (z.B. komplexer elektrischer Defekt, Mastbruch), umgehend Fachpersonal (Elektriker, Tiefbau) anfordern.
    *   **Priorisierung:** Da der Schweregrad "mittel" ist, sollte die Reparatur zeitnah erfolgen. Bei Feststellung einer unmittelbaren Gefahr (z.B. offene Elektrik, Mastbruch) ist die Priorität sofort auf "hoch" zu setzen und die Notfallkette zu aktivieren.
    *   **Rückmeldung:** Rückmeldung an die Leitstelle/Verwaltung über den Status und die geplanten weiteren Schritte.

---

## C20

- Domaene: LAMP

### USER MESSAGE

```
Dunkler Abschnitt entlang Schönau; bitte prüfen.
```

### CONTEXT (wie vom Judge gesehen)

```json
{
  "incident": {
    "fault_type": "outage",
    "severity": "medium",
    "reported_at": "2026-01-15T10:17:54+01:00",
    "photo_available": true,
    "photo_description": "Dämmerungsaufnahme bei Regen: gesamter Straßenabschnitt dunkel. Mehrere Masten sichtbar, alle ohne Licht. Kein einzelner Schaden erkennbar.",
    "reporter": "citizen"
  },
  "asset": {
    "asset_osm": "n4446442023",
    "latitude": 47.8227101,
    "longitude": 12.1125581,
    "name": "Schönau",
    "lit": "yes"
  },
  "device": {
    "connectivity": "online",
    "device_state": "low_power_mode"
  },
  "environment": {
    "time_of_day": "dusk",
    "weather": "rain",
    "lighting_condition": "poor_visibility",
    "traffic_exposure": "low",
    "noise_level": "medium"
  },
  "extras": {
    "context_notes": [
      "device.* beschreibt das Techniker-Gerät (App/Smartphone), NICHT das Asset.",
      "connectivity/device_state beeinflusst Vorgehen (z.B. offlinefähig dokumentieren), ist keine Fehlerursache des Assets.",
      "incident.photo_available ist ein Workflow-Hinweis (Foto vorhanden), kein Beweis für eine konkrete Ursache."
    ]
  }
}
```

### EXPECTED ELEMENTS

```
(leer -- test_loader schreibt keinen Schluessel expected_elements_short in input.meta, der Judge erhielt hier keinen Inhalt)
```

### MODEL ANSWER

Ein dunkler Abschnitt entlang der Schönau erfordert eine umgehende Prüfung. Angesichts der Dämmerung, des Regens und der schlechten Sichtverhältnisse ist die Sicherheit oberstes Gebot.

Hier ist die Schritt-für-Schritt-Checkliste für den Vor-Ort-Einsatz:

**1. Absicherung**
*   **Verkehrssicherung:** Unmittelbar nach Ankunft die Einsatzstelle gemäß den Vorschriften der StVO und RSA absichern (Warnblinkanlage, Warnleuchten, Warndreieck, ggf. Leitkegel).
*   **Persönliche Schutzausrüstung (PSA):** Warnkleidung (mind. Klasse 2), Sicherheitsschuhe, ggf. Regenkleidung und Stirnlampe/Taschenlampe verwenden.
*   **Gefahrenanalyse:** Auf weitere Gefahren wie rutschigen Untergrund, herabhängende Äste oder erhöhten Verkehr achten.

**2. Sichtprüfung**
*   **Gesamteindruck:** Den gesamten gemeldeten Abschnitt (Schönau) bei schlechter Sicht auf weitere Auffälligkeiten prüfen.
*   **Masten/Leuchten:** Alle Masten im betroffenen Bereich auf sichtbare Schäden (z.B. angefahrene Masten, offene Leuchtenköpfe, hängende Kabel) untersuchen.
*   **Zuleitungen:** Sichtprüfung der Zuleitungen im Bereich der Masten, sofern zugänglich und sicher.
*   **Umgebung:** Auf Baustellen, Erdarbeiten oder andere Aktivitäten in der Nähe achten, die eine Beschädigung der Infrastruktur verursacht haben könnten.

**3. Diagnose/Beobachtung**
*   **Stromversorgung:**
    *   Wenn möglich und sicher, die Sicherungen im nächstgelegenen Verteilerkasten prüfen.
    *   Gibt es Anzeichen für einen Stromausfall in der gesamten Umgebung oder nur im betroffenen Abschnitt?
*   **Leuchtenfunktion:**
    *   Einzelne Leuchten auf Funktion prüfen, falls eine manuelle Schaltung oder ein Reset möglich ist.
    *   Auffälligkeiten wie Flackern, sehr schwaches Licht oder verzögertes Einschalten notieren.
*   **Steuerung:** Wenn bekannt, den Zustand der Steuerung (z.B. Dämmerungsschalter, Zeitschaltuhr) prüfen.
*   **Widerspruch:** Der Asset-Status "lit: yes" steht im Widerspruch zur Meldung "outage". Dies ist zu verifizieren. Möglicherweise handelt es sich um eine Störung der Steuerung oder eine lokale Unterbrechung, während das System den Asset als funktionsfähig meldet.

**4. Dokumentation**
*   **Fotos:** Detaillierte Fotos der Situation (Gesamtansicht des dunklen Abschnitts, einzelne Masten, eventuelle Schäden) anfertigen. Das bereits vorhandene Foto ist ein guter Ausgangspunkt.
*   **Befunde:** Alle Beobachtungen und Diagnoseschritte präzise im System erfassen.
*   **Standort:** Genaue Positionsdaten des betroffenen Abschnitts und ggf. einzelner beschädigter Masten notieren.
*   **Gerätestatus:** Das Techniker-Gerät ist online, aber im Stromsparmodus. Sicherstellen, dass die Dokumentation vollständig erfasst und synchronisiert wird, bevor der Akku leer ist.

**5. Eskalation**
*   **Sofortige Gefahr:** Bei unmittelbarer Gefahr (z.B. offene Kabel, umsturzgefährdeter Mast) umgehend den Bereitschaftsdienst oder die zuständige Fachabteilung informieren und die Gefahrenstelle absichern.
*   **Umfassender Ausfall:** Wenn der Ausfall einen größeren Bereich betrifft oder die Ursache nicht vor Ort behoben werden kann, die zuständige Fachabteilung für Elektrotechnik/Instandhaltung informieren und die gesammelten Informationen übermitteln.
*   **Priorisierung:** Angesichts der schlechten Sichtverhältnisse und des Regens ist eine schnelle Behebung des Ausfalls wichtig für die Verkehrssicherheit.

---

## C21

- Domaene: LAMP

### USER MESSAGE

```
Straßenlampe ist dunkel seit etwa 20 Minuten. Bereich wirkt unsicher.
```

### CONTEXT (wie vom Judge gesehen)

```json
{
  "asset": {
    "asset_osm": "n12520338291",
    "longitude": 12.1178456,
    "latitude": 47.8505506,
    "crs": "EPSG:4326",
    "lit": null,
    "name": null
  },
  "incident": {
    "fault_type": "outage",
    "severity": "medium",
    "reported_at": "2026-01-21T15:41:46+01:00",
    "reporter": "patrol",
    "photo_available": false
  },
  "environment": {
    "time_of_day": "night",
    "weather": "clear",
    "lighting_condition": "poor_visibility",
    "traffic_exposure": "medium",
    "noise_level": "low"
  },
  "device": {
    "device_state": "low_power_mode",
    "connectivity": "spotty"
  }
}
```

### EXPECTED ELEMENTS

```
(leer -- test_loader schreibt keinen Schluessel expected_elements_short in input.meta, der Judge erhielt hier keinen Inhalt)
```

### MODEL ANSWER

Verstanden. Eine dunkle Straßenlampe, die seit 20 Minuten ausgefallen ist und ein unsicher wirkender Bereich erfordern schnelles und strukturiertes Vorgehen. Hier ist die Checkliste für den Außendienst:

**Checkliste: Ausfall Straßenlampe**

1.  **Absicherung (Priorität: Sicherheit)**
    *   **Verkehrssicherung:** Unverzüglich Warnblinkanlage einschalten, Warnweste anlegen. Bei Bedarf Warndreieck/Blitzleuchte aufstellen, um den Arbeitsbereich abzusichern und andere Verkehrsteilnehmer zu warnen.
    *   **Persönliche Sicherheit:** Achten Sie auf den umgebenden Verkehr und mögliche Gefahrenquellen im Dunkeln. Betreten Sie den Bereich nur, wenn es sicher ist.

2.  **Sichtprüfung (Erste Einschätzung)**
    *   **Umgebung:** Gibt es weitere dunkle Lampen in der Nähe? Sind andere Infrastrukturen (z.B. Ampeln, Verteilerkästen) betroffen?
    *   **Lampe:** Ist die Leuchte physisch beschädigt (Glasbruch, Gehäuseschäden)? Hängen Kabel lose herunter? Gibt es Anzeichen von Vandalismus oder Unfallschäden?
    *   **Stromversorgung:** Sind Sicherungskästen oder Verteiler in der Nähe sichtbar und zugänglich? Gibt es dort offensichtliche Schäden?

3.  **Diagnose/Beobachtung (Fehlerursache eingrenzen)**
    *   **Stromzufuhr:** Prüfen Sie, ob die Lampe komplett stromlos ist oder ob es Anzeichen für eine Teilauslastung gibt (z.B. Flackern, sehr schwaches Leuchten). Der gemeldete "low_power_mode" des Geräts könnte auf eine unzureichende Stromversorgung oder einen internen Defekt hindeuten.
    *   **Konnektivität:** Die "spotty" Konnektivität des Geräts erschwert eine Fernanalyse. Versuchen Sie, eine lokale Verbindung herzustellen, falls die Lampe Smart-Funktionen besitzt.
    *   **Auslöser:** Gab es in der Umgebung kürzlich Bauarbeiten, Erdarbeiten oder andere Ereignisse, die eine Beschädigung der Stromleitung verursacht haben könnten?

4.  **Dokumentation (Beweissicherung & Meldung)**
    *   **Fotos:** Machen Sie aussagekräftige Fotos von der defekten Lampe, der unmittelbaren Umgebung und eventuellen Schäden.
    *   **Details:** Notieren Sie den genauen Standort (Asset-ID: n12520338291, Koordinaten: 47.8505506, 12.1178456), die genaue Uhrzeit des Ausfalls (seit ca. 20 Minuten), Ihre Beobachtungen (z.B. "Bereich wirkt unsicher", "keine sichtbaren Schäden an der Lampe"), und die bereits durchgeführten Maßnahmen.
    *   **System-Update:** Aktualisieren Sie den Status im System mit den neuen Informationen.

5.  **Eskalation (Nächste Schritte einleiten)**
    *   **Gefahr:** Bei unmittelbarer Gefahr (z.B. herabhängende Kabel, offene Verteilerkästen, Unfallgefahr durch Dunkelheit) sofort den Bereitschaftsdienst oder die Feuerwehr informieren.
    *   **Reparatur:** Leiten Sie die Reparatur durch das zuständige Team ein. Geben Sie alle gesammelten Informationen weiter, um eine schnelle Fehlerbehebung zu ermöglichen.
    *   **Beleuchtung:** Falls der Bereich kritisch ist und die Reparatur länger dauert, prüfen Sie die Möglichkeit einer temporären Beleuchtung (z.B. mobile Lichtmasten).

---

## C22

- Domaene: LAMP

### USER MESSAGE

```
Lampe war vorhin aus, ist jetzt wieder an. Sporadischer Fehler.
```

### CONTEXT (wie vom Judge gesehen)

```json
{
  "_unstructured_text": "poor_visibility | storm | Rosenheim, Bahnhof | True | intermittent | 2026-01-19T09:52:16+01:00 | ok | medium | Nachtaufnahme bei Sturm: Laterne aktuell an (nach gemeldetem Ausfall). Mastarm mit Sturmspuren, Schaltbox äußerlich geschlossen. | high | 12.1186732 | night | 47.8512747 | high | offline | citizen | n5718630490 | yes"
}
```

### EXPECTED ELEMENTS

```
(leer -- test_loader schreibt keinen Schluessel expected_elements_short in input.meta, der Judge erhielt hier keinen Inhalt)
```

### MODEL ANSWER

Ein sporadischer Fehler an einer Straßenlampe erfordert eine sorgfältige Vorgehensweise. Hier ist eine Schritt-für-Schritt-Checkliste für den Außendienst, unter Berücksichtigung der gemeldeten Bedingungen (Sturm, schlechte Sicht, Bahnhofsbereich):

### Checkliste: Sporadischer Lampenausfall (ID: n5718630490)

**1. Absicherung (Priorität: Sicherheit & Verkehrssicherung)**
*   **Gefahrenbereich sichern:** Aufgrund der schlechten Sicht, des Sturms und des Standorts am Bahnhof ist eine umfassende Absicherung des Arbeitsbereichs unerlässlich.
    *   Warnblinklicht am Fahrzeug einschalten.
    *   Warnkegel/Warndreiecke in ausreichendem Abstand aufstellen.
    *   Warnwesten tragen.
    *   Bei Bedarf: Zusätzliche Beleuchtung für den Arbeitsbereich sicherstellen.
    *   Besondere Vorsicht im Bereich von Gleisanlagen oder stark frequentierten Bereichen.
*   **Stromversorgung prüfen:** Vor Arbeiten am Mast oder der Schaltbox sicherstellen, dass keine unmittelbare Stromschlaggefahr besteht.

**2. Sichtprüfung (Umfassende Begutachtung)**
*   **Gesamtzustand des Mastes und Mastarms:**
    *   Sichtbare Sturmschäden, Risse, Verformungen oder lose Teile am Mast und Mastarm prüfen (gemeldet: "Mastarm mit Sturmspuren").
    *   Korrosion oder Materialermüdung.
*   **Leuchtenkopf:**
    *   Sitz des Leuchtenkopfes prüfen, ob er fest montiert ist.
    *   Sichtbare Beschädigungen am Gehäuse oder der Abdeckung.
    *   Verschmutzungen, die die Lichtabgabe beeinträchtigen könnten.
*   **Schaltbox/Anschlusskasten:**
    *   Äußerer Zustand der Schaltbox prüfen (gemeldet: "Schaltbox äußerlich geschlossen").
    *   Sichtbare Beschädigungen, offene Klappen oder Manipulationen.
    *   Feuchtigkeitseintritt oder Kondenswasserbildung.
*   **Kabel und Leitungen:**
    *   Sichtbare Beschädigungen, Quetschungen oder blanke Stellen an Zuleitungen und internen Kabeln.
    *   Korrosion an Anschlüssen.
*   **Umgebung:**
    *   Bewuchs, der die Leuchte verdeckt oder beschädigt.
    *   Fremdkörper im Bereich der Leuchte.

**3. Diagnose/Beobachtung (Fokus auf sporadischen Fehler)**
*   **Aktueller Zustand:** Bestätigen, dass die Lampe aktuell leuchtet (gemeldet: "Laterne aktuell an").
*   **Fehlerbild reproduzieren:**
    *   Wenn möglich, versuchen, den Fehler durch Schalten (falls zugänglich) oder Beobachtung über einen längeren Zeitraum zu reproduzieren.
    *   Auf Flackern, Helligkeitsschwankungen oder ungewöhnliche Geräusche achten.
*   **Mögliche Ursachen für sporadischen Fehler:**
    *   Wackelkontakte (Kabel, Klemmen, Sicherungen).
    *   Defekte Vorschaltgeräte/Treiber, die bei Temperaturschwankungen oder Lastwechseln ausfallen.
    *   Feuchtigkeit in der Leuchte oder Schaltbox, die Kurzschlüsse verursacht.
    *   Defekte Dämmerungsschalter oder Zeitschaltuhren.
    *   Überlastung oder Spannungsschwankungen im Netz.
    *   Defekte Leuchtmittel, die kurz vor dem Totalausfall stehen.
*   **Status "offline" prüfen:** Obwohl die Lampe leuchtet, wurde der Status "offline" gemeldet. Dies deutet auf ein Kommunikationsproblem oder einen Fehler in der Steuerung hin.
    *   Kommunikationsmodul prüfen (falls vorhanden).
    *   Verbindung zum zentralen Steuerungssystem prüfen.

**4. Dokumentation (Präzise und vollständig)**
*   **Datum, Uhrzeit und Name des Technikers.**
*   **Genaue Position der Leuchte** (ggf. mit GPS-Koordinaten: 47.8512747, 12.1186732).
*   **Detaillierte Beschreibung der Beobachtungen:**
    *   Was wurde vorgefunden? (z.B. "Lampe leuchtet, Mastarm mit leichten Sturmspuren, Schaltbox geschlossen.")
    *   Welche Tests wurden durchgeführt?
    *   Konnten Fehler reproduziert werden?
    *   Fotos von Auffälligkeiten (Sturmschäden, Anschlüsse, etc.).
*   **Vermutete Ursache(n).**
*   **Durchgeführte Maßnahmen** (z.B. "Klemmen nachgezogen, Sichtprüfung ohne Befund").
*   **Empfehlung für weitere Schritte.**

**5. Eskalation (Bei Bedarf)**
*   **Bei unklarer Ursache oder nicht behebbarer Störung:**
    *   Information an die Leitstelle/Vorgesetzten mit allen Dokumentationsdetails.
    *   Empfehlung für eine detailliertere Fehleranalyse (z.B. Messung von Spannungen/Strömen, Austausch von Komponenten).
*   **Bei Sicherheitsrisiken:**
    *   Wenn der Mast instabil ist oder eine unmittelbare Gefahr besteht, sofort den Bereich absperren und die zuständigen Stellen informieren.
    *   Ggf. Notabschaltung der Stromversorgung veranlassen.

Dieser systematische Ansatz hilft, die Ursache des sporadischen Fehlers zu finden und die Sicherheit zu gewährleisten.

---

## C23

- Domaene: LAMP

### USER MESSAGE

```
Straßenlampe ist dunkel seit etwa 90 Minuten. Bereich wirkt unsicher.
```

### CONTEXT (wie vom Judge gesehen)

```json
{
  "asset": {
    "asset_osm": "n7230270217",
    "longitude": 12.0941951,
    "latitude": 47.8493667,
    "crs": "EPSG:4326",
    "lit": "yes",
    "name": "Rosenheim, Äußere Münchener Straße/Aicherpark"
  },
  "incident": {
    "fault_type": "outage",
    "severity": "high",
    "reported_at": "2026-01-19T01:52:56+01:00",
    "reporter": "patrol",
    "photo_available": true,
    "photo_description": "Aufnahme bei Sturm/Dämmerung: Laterne dunkel, Mast leicht geneigt. Schaltbox-Deckel leicht geöffnet – mögliche Sturmeinwirkung."
  },
  "environment": {
    "time_of_day": "dusk",
    "weather": "storm",
    "lighting_condition": "poor_visibility",
    "traffic_exposure": "high",
    "noise_level": "high"
  },
  "device": {
    "device_state": "low_battery",
    "connectivity": "offline"
  }
}
```

### EXPECTED ELEMENTS

```
(leer -- test_loader schreibt keinen Schluessel expected_elements_short in input.meta, der Judge erhielt hier keinen Inhalt)
```

### MODEL ANSWER

Die dunkle Straßenlampe in der Äußeren Münchener Straße/Aicherpark, Rosenheim, erfordert aufgrund der Umstände (Sturm, schlechte Sicht, geneigter Mast, offener Schaltkasten, hohe Verkehrsdichte) ein schnelles und strukturiertes Vorgehen. Priorität hat die Sicherheit vor Ort.

**Schritt-für-Schritt-Checkliste:**

1.  **Absicherung (Sofortmaßnahmen)**
    *   **Gefahrenbereich absperren:** Aufgrund des leicht geneigten Mastes und des geöffneten Schaltkastens besteht akute Gefahr. Sichern Sie den Bereich großräumig ab, um Passanten und Verkehrsteilnehmer zu schützen.
    *   **Warnhinweise aufstellen:** Platzieren Sie deutlich sichtbare Warnschilder und Blitzleuchten, insbesondere bei schlechter Sicht und hohem Verkehrsaufkommen.
    *   **Verkehrssicherung gewährleisten:** Bei Bedarf den Verkehr umleiten oder reduzieren, um die Sicherheit der Einsatzkräfte und anderer Personen zu gewährleisten.

2.  **Sichtprüfung (Erste Einschätzung)**
    *   **Mastzustand prüfen:** Bestätigen Sie die Neigung des Mastes und suchen Sie nach weiteren strukturellen Schäden (Risse, Verformungen).
    *   **Schaltkasten inspizieren:** Überprüfen Sie den geöffneten Deckel des Schaltkastens. Ist Wasser eingedrungen? Sind Kabel freigelegt oder beschädigt?
    *   **Umgebung beobachten:** Gibt es weitere dunkle Lampen in der Nähe? Sind andere Infrastrukturelemente (Verkehrszeichen, Ampeln) ebenfalls betroffen oder beschädigt?
    *   **Sturmschäden:** Achten Sie auf weitere sturmbedingte Schäden in der unmittelbaren Umgebung, die die Situation verschärfen könnten (herabfallende Äste, lose Gegenstände).

3.  **Diagnose/Beobachtung (Ursachenforschung)**
    *   **Ausfall bestätigen:** Verifizieren Sie, dass die Lampe tatsächlich dunkel ist und nicht nur flackert oder schwach leuchtet.
    *   **Mögliche Ursachen:** Basierend auf der Beschreibung ("outage", "Mast leicht geneigt", "Schaltbox-Deckel leicht geöffnet – mögliche Sturmeinwirkung") sind ein Kurzschluss, eine Beschädigung der Verkabelung oder ein Defekt im Vorschaltgerät/Leuchtmittel durch die Sturmeinwirkung wahrscheinlich.
    *   **Gerätestatus:** Beachten Sie den Gerätestatus "low_battery" und "offline" des meldenden Geräts; dies betrifft die Meldung selbst, nicht die Straßenlampe.

4.  **Dokumentation**
    *   **Fotos machen:** Erstellen Sie detaillierte Fotos von allen Schäden, der Absicherung und der Gesamtsituation.
    *   **Vollständigen Bericht erstellen:** Notieren Sie alle Beobachtungen, die genaue Uhrzeit der Feststellung, die durchgeführten Maßnahmen und die beteiligten Personen.
    *   **Referenzdaten:** Halten Sie die Asset-ID (n7230270217), den Standort (Rosenheim, Äußere Münchener Straße/Aicherpark) und die gemeldeten Details (fault_type: outage, severity: high, reported_at: 2026-01-19T01:52:56+01:00) fest.

5.  **Eskalation (Dringend)**
    *   **Notdienst kontaktieren:** Aufgrund des geneigten Mastes und des geöffneten Schaltkastens besteht eine unmittelbare Gefahr. Informieren Sie umgehend den zuständigen Notdienst für elektrische Anlagen und die Straßenbeleuchtung.
    *   **Polizei/Feuerwehr informieren:** Bei akuter Gefahr für den öffentlichen Verkehr oder die Sicherheit von Personen ist die Polizei oder Feuerwehr zu verständigen, um weitere Absicherungsmaßnahmen zu koordinieren.
    *   **Vorgesetzte informieren:** Melden Sie den Vorfall umgehend an Ihre Vorgesetzten, um weitere Schritte und Ressourcen zu koordinieren.

**Zusätzliche Hinweise:**
*   Betreten Sie den Gefahrenbereich des Mastes oder des Schaltkastens nicht ohne entsprechende Schutzausrüstung und Sicherung durch Fachpersonal.
*   Warten Sie auf das Eintreffen der spezialisierten Einsatzkräfte.

---

## C24

- Domaene: SIGNAL

### USER MESSAGE

```
Kurzzeitige Aussetzer/Neustarts vermutet; Verhalten inkonsistent. (Richtung: backward).
```

### CONTEXT (wie vom Judge gesehen)

```json
{
  "_unstructured_text": "citizen | day | medium | 2026-01-20T04:16:40+01:00 | ok | clear | high | False | 12.1183214 | 47.8585403 | high | online | intermittent | normal_visibility | n12872023045 | backward"
}
```

### EXPECTED ELEMENTS

```
(leer -- test_loader schreibt keinen Schluessel expected_elements_short in input.meta, der Judge erhielt hier keinen Inhalt)
```

### MODEL ANSWER

Ein gemeldeter Fall von kurzzeitigen Aussetzern und Neustarts bei der Anlage `n12872023045` erfordert umgehendes Handeln. Priorität hat die Sicherheit aller Verkehrsteilnehmer und Passanten.

Hier ist die Schritt-für-Schritt-Checkliste für den Außendienst:

### **Checkliste: Inkonstantes Verhalten (Aussetzer/Neustarts) bei Anlage n12872023045**

**1. Absicherung der Gefahrenstelle (Priorität: Sicherheit)**
*   **Verkehrssicherung:** Bei Ampelanlagen oder Straßenlampen, die den Verkehr beeinflussen, sofort geeignete Warnschilder, Warnleuchten und Absperrungen gemäß StVO und internen Sicherheitsrichtlinien aufstellen.
*   **Personenschutz:** Eigenschutz und Schutz Dritter gewährleisten. Persönliche Schutzausrüstung (PSA) tragen.
*   **Meldung an Leitstelle:** Kurze Statusmeldung über die Absicherung und Ankunft am Einsatzort.

**2. Sichtprüfung vor Ort**
*   **Umgebung:** Gibt es offensichtliche externe Einflüsse (z.B. Beschädigungen durch Fahrzeuge, Vandalismus, Bauarbeiten, umgestürzte Bäume, Wasseransammlungen)?
*   **Anlage selbst:**
    *   **Kabel und Anschlüsse:** Sind Kabel sichtbar beschädigt, locker oder korrodiert? Sind die Anschlüsse fest?
    *   **Gehäuse:** Ist das Gehäuse intakt oder gibt es Risse, Öffnungen, die das Eindringen von Feuchtigkeit ermöglichen könnten?
    *   **Leuchtmittel/Optik (bei Lampen):** Ist das Leuchtmittel korrekt eingesetzt? Sind die Optiken sauber und unbeschädigt?
    *   **Steuerung/Schaltkasten (bei Ampeln/komplexen Anlagen):** Sind die Türen des Schaltkastens geschlossen und verriegelt? Gibt es Anzeichen von Überhitzung oder Feuchtigkeit im Bereich des Schaltkastens (nicht öffnen, falls nicht autorisiert)?
*   **Verhalten beobachten:** Das inkonsistente Verhalten (Aussetzer/Neustarts) über einen längeren Zeitraum (mind. 10-15 Minuten) beobachten. Wann treten die Aussetzer auf? Gibt es Muster (z.B. bei Erschütterungen, Wind, bestimmten Schaltvorgängen)?

**3. Diagnose und Beobachtung**
*   **Fehlerbilder:**
    *   **Flimmern/Dimmen:** Tritt dies vor einem Ausfall auf?
    *   **Kompletter Ausfall:** Wie lange dauert der Ausfall? Startet die Anlage von selbst neu?
    *   **Falsche Schaltzustände (bei Ampeln):** Werden falsche Signale angezeigt oder bleiben Signale aus?
    *   **Geräusche/Gerüche:** Gibt es ungewöhnliche Geräusche (Brummen, Knistern) oder Gerüche (Schmorgeruch)?
*   **Spannungsversorgung (falls Messgeräte vorhanden und autorisiert):** Kurzzeitige Spannungsschwankungen oder -ausfälle messen.
*   **Fehlercodes:** Falls die Anlage über eine Diagnoseanzeige verfügt, vorhandene Fehlercodes notieren.

**4. Dokumentation**
*   **Einsatzbericht:**
    *   Datum, Uhrzeit des Eintreffens und der Beobachtung.
    *   Genaue Position (Koordinaten: 12.1183214, 47.8585403).
    *   Anlagen-ID: `n12872023045`.
    *   Detaillierte Beschreibung des beobachteten Verhaltens (Frequenz, Dauer der Aussetzer, Art des Neustarts).
    *   Festgestellte Auffälligkeiten bei der Sichtprüfung (z.B. lockeres Kabel, beschädigtes Gehäuse).
    *   Durchgeführte Absicherungsmaßnahmen.
    *   Wetterbedingungen zum Zeitpunkt der Beobachtung (klar, normal_visibility).
*   **Fotos/Videos:** Aussagekräftige Bilder oder kurze Videos des Fehlerbildes und der Umgebung machen.

**5. Eskalation**
*   **Leitstelle informieren:** Umfassende Rückmeldung an die Leitstelle mit allen gesammelten Informationen und der Einschätzung der Dringlichkeit.
*   **Empfehlung:**
    *   Bei akuter Gefahr für den Verkehr oder Personen: Sofortige Abschaltung der Anlage (falls möglich und sicher) und Anforderung eines spezialisierten Teams zur Reparatur.
    *   Bei weniger kritischen, aber anhaltenden Problemen: Anforderung eines Wartungsteams zur detaillierten Fehleranalyse und Reparatur.
*   **Nächste Schritte:** Klärung der weiteren Vorgehensweise mit der Leitstelle (z.B. Ersatzteile bestellen, Spezialisten anfordern).

**Annahme:** Die Meldung "citizen | day | medium | 2026-01-20T04:16:40+01:00 | ok | clear | high | False | 12.1183214 | 47.8585403 | high | online | intermittent | normal_visibility | n12872023045 | backward" beschreibt den initialen Meldeeingang und die Rahmenbedingungen. Die Priorität ist als "high" eingestuft, was schnelles Handeln erfordert.

---

## C25

- Domaene: LAMP

### USER MESSAGE

```
Flackern tritt vor allem bei Regen auf.
```

### CONTEXT (wie vom Judge gesehen)

```json
{
  "_unstructured_text": "2026-01-19T09:04:59+01:00 | dusk | flicker | low | ok | low | low | False | citizen | 12.0896193 | 47.8457235 | poor_visibility | offline | Rosenheim, Endorfer Au / Krones | rain | n12557351679 | yes"
}
```

### EXPECTED ELEMENTS

```
(leer -- test_loader schreibt keinen Schluessel expected_elements_short in input.meta, der Judge erhielt hier keinen Inhalt)
```

### MODEL ANSWER

Ein flackerndes Licht, besonders bei Regen, deutet auf einen möglichen Kurzschluss oder Feuchtigkeitseintritt hin. Dies erfordert umgehendes Handeln, um die Verkehrssicherheit zu gewährleisten.

Hier ist die Schritt-für-Schritt-Checkliste:

1.  **Absicherung (Sicherheit & Verkehrssicherung)**
    *   **Unmittelbare Gefahrenbeurteilung:** Ist das Flackern so stark, dass es den Verkehr irritiert oder blendet? Besteht die Gefahr eines Ausfalls oder eines Stromschlags?
    *   **Verkehrssicherung:** Falls erforderlich, die Gefahrenstelle absichern (z.B. Warnbake, Warnleuchte aufstellen). Bei starker Beeinträchtigung des Verkehrs oder Gefahr für Passanten umgehend die Polizei oder Feuerwehr informieren.
    *   **Zugang sichern:** Sicherstellen, dass Unbefugte keinen Zugang zur Anlage haben.

2.  **Sichtprüfung (Erste Einschätzung vor Ort)**
    *   **Leuchte:** Zustand der Leuchte prüfen (Risse, Beschädigungen, offene Gehäuse, sichtbare Feuchtigkeit).
    *   **Mast:** Zustand des Mastes prüfen (Korrosion, Beschädigungen, Stabilität).
    *   **Kabel/Anschluss:** Sichtbare Beschädigungen an Kabeln oder am Anschlusskasten am Mastfuß.
    *   **Umgebung:** Gibt es Anzeichen für externe Einflüsse (z.B. Vandalismus, Anfahrschäden, Bewuchs, der die Leuchte berührt)?
    *   **Regen:** Bestätigt sich der Zusammenhang mit Regen? Ist die Leuchte nass?

3.  **Diagnose/Beobachtung (Fehlerursache eingrenzen)**
    *   **Flacker-Muster:** Ist das Flackern konstant, periodisch oder unregelmäßig? Tritt es nur bei Regen auf oder auch bei Trockenheit?
    *   **Intensität:** Wie stark ist das Flackern (low, wie im Bericht angegeben)?
    *   **Weitere Auffälligkeiten:** Gibt es Geräusche (Brummen, Knistern), Gerüche (Schmorgeruch) oder andere visuelle Hinweise (Rauch, Funken)?
    *   **Stromversorgung:** Wenn möglich und sicher, die Spannung am Anschluss messen (nur durch Fachpersonal!).
    *   **Komponentenprüfung:** Wenn sicher zugänglich, die einzelnen Komponenten (Vorschaltgerät, Leuchtmittel, Zünder) auf sichtbare Defekte prüfen.

4.  **Dokumentation**
    *   **Details erfassen:** Alle Beobachtungen aus Schritt 2 und 3 detailliert festhalten.
    *   **Fotos/Videos:** Aussagekräftige Bilder oder kurze Videos des Flackerns und der Umgebung machen.
    *   **Standort:** Genaue Standortdaten (Endorfer Au / Krones, Rosenheim, 12.0896193 | 47.8457235) und die Asset-ID (n12557351679) notieren.
    *   **Zeitstempel:** Datum und Uhrzeit der Beobachtung (19.01.2026, 09:04:59 Uhr) und des aktuellen Status festhalten.
    *   **Meldung:** Die Bürger-Meldung (citizen) mit den Details "poor_visibility", "offline", "rain" und "yes" für Flackern in die Dokumentation aufnehmen.

5.  **Eskalation**
    *   **Fachfirma/Elektriker:** Aufgrund des Zusammenhangs mit Regen und der potenziellen Gefahr durch Feuchtigkeitseintritt ist umgehend eine Fachfirma oder ein qualifizierter Elektriker zu beauftragen.
    *   **Dringlichkeit:** Die Dringlichkeit ist hoch, da Feuchtigkeit in elektrischen Anlagen zu Kurzschlüssen, Ausfällen oder sogar Bränden führen kann.
    *   **Anweisung:** Die Anlage bis zur Reparatur außer Betrieb nehmen, falls eine unmittelbare Gefahr besteht oder die Verkehrssicherheit nicht anders gewährleistet werden kann.
    *   **Status-Update:** Alle relevanten Stellen über den aktuellen Status und die eingeleiteten Maßnahmen informieren.

---

## C26

- Domaene: LAMP

### USER MESSAGE

```
Straßenlampe ist dunkel seit etwa 20 Minuten. Bereich wirkt unsicher.
```

### CONTEXT (wie vom Judge gesehen)

```json
{
  "incident": {
    "fault_type": "outage",
    "severity": "high",
    "reported_at": "2026-01-16T20:06:14+01:00",
    "photo_available": true,
    "photo_description": "Nachtaufnahme: Laterne dunkel, Gewerbegebiet ohne Beleuchtung. Mast intakt, Schaltbox geschlossen. Kein sichtbarer Vandalismus.",
    "reporter": "citizen"
  },
  "asset": {
    "asset_osm": "n4465173757",
    "latitude": 47.8409877,
    "longitude": 12.1236173,
    "name": "Rosenheim, Isarstraße/Gewerbegebiet",
    "lit": "yes"
  },
  "device": {
    "connectivity": "online",
    "device_state": "low_battery"
  },
  "environment": {
    "time_of_day": "night",
    "weather": "clear",
    "lighting_condition": "poor_visibility",
    "traffic_exposure": "high",
    "noise_level": "high"
  },
  "extras": {
    "context_notes": [
      "device.* beschreibt das Techniker-Gerät (App/Smartphone), NICHT das Asset.",
      "connectivity/device_state beeinflusst Vorgehen (z.B. offlinefähig dokumentieren), ist keine Fehlerursache des Assets.",
      "incident.photo_available ist ein Workflow-Hinweis (Foto vorhanden), kein Beweis für eine konkrete Ursache."
    ]
  }
}
```

### EXPECTED ELEMENTS

```
(leer -- test_loader schreibt keinen Schluessel expected_elements_short in input.meta, der Judge erhielt hier keinen Inhalt)
```

### MODEL ANSWER

Hier ist die Schritt-für-Schritt-Checkliste für den Einsatz vor Ort:

**Checkliste Straßenlampe dunkel (Rosenheim, Isarstraße/Gewerbegebiet)**

**1. Absicherung & Eigensicherung**
*   **Verkehrssicherung:** Sofortige Absicherung der Arbeitsstelle gemäß UVV und StVO, insbesondere aufgrund der hohen Verkehrsbelastung und schlechten Sichtverhältnisse bei Nacht. Einsatz von Warnblinklicht, Warnleuchten, Warndreiecken/Leitkegeln.
*   **Persönliche Schutzausrüstung (PSA):** Vollständige PSA anlegen (Warnkleidung, Sicherheitsschuhe, ggf. Helm und Handschuhe).
*   **Umfeldprüfung:** Schnelle Einschätzung des unmittelbaren Bereichs auf weitere Gefahrenquellen (z.B. lose Kabel, beschädigte Infrastruktur).

**2. Sichtprüfung (ohne direkten Kontakt)**
*   **Leuchtmittel/Leuchtenkopf:** Ist das Leuchtmittel sichtbar defekt (z.B. Glasbruch, Verfärbung)? Ist der Leuchtenkopf intakt oder beschädigt?
*   **Mast:** Zustand des Mastes prüfen (Korrosion, Risse, Anfahrtschäden, Stabilität).
*   **Schaltbox/Anschlusskasten:** Optische Prüfung der Schaltbox am Mastfuß (geschlossen, unbeschädigt, keine Manipulationen).
*   **Umgebung:** Funktionieren benachbarte Straßenlampen? Gibt es Anzeichen für Vandalismus oder externe Beschädigungen im Umfeld?
*   **Kabel:** Sind oberirdische Kabel sichtbar beschädigt oder lose?

**3. Diagnose & Beobachtung**
*   **Fehlerbild:** Bestätigung, dass die Lampe vollständig dunkel ist und nicht flackert oder schwach leuchtet.
*   **Stromversorgung (falls sicher zugänglich):** Falls gefahrlos möglich und qualifiziert, eine erste Prüfung der Stromzufuhr am Mastfuß (z.B. mit berührungslosem Spannungsprüfer). **Achtung: Nur durch geschultes Personal!**
*   **Ursachenanalyse:** Basierend auf der Sichtprüfung erste Hypothesen zur Ursache bilden (z.B. Leuchtmittelausfall, Sicherung, Kabelbruch, Vorschaltgerät).

**4. Dokumentation**
*   **Fotos:** Umfassende Fotos der Situation anfertigen (Gesamtansicht, Detailaufnahmen der Lampe, des Mastes, der Schaltbox, der Absicherung).
*   **Standort:** Genaue Lokalisierung und Bestätigung der Asset-ID (n4465173757, Rosenheim, Isarstraße/Gewerbegebiet).
*   **Zeitpunkt:** Genaue Erfassung des Feststellungszeitpunkts und des Beginns der Störung (seit ca. 20 Minuten).
*   **Beobachtungen:** Alle Feststellungen detailliert protokollieren (z.B. "Mast intakt, Schaltbox geschlossen, kein sichtbarer Vandalismus", "keine weiteren Ausfälle im direkten Umfeld").
*   **Maßnahmen:** Dokumentation der getroffenen Absicherungsmaßnahmen.
*   **Gerätezustand:** Hinweis auf den niedrigen Akkustand des Techniker-Geräts beachten und ggf. alternative Dokumentationswege oder schnellen Abschluss der Dokumentation sicherstellen.

**5. Eskalation**
*   **Priorität:** Aufgrund der Dunkelheit im Gewerbegebiet und des Unsicherheitsgefühls des Bürgers ist dies ein Vorfall mit hoher Priorität.
*   **Meldung:** Umgehende Meldung an die zuständige Leitstelle/Fachabteilung mit allen gesammelten Informationen und Fotos.
*   **Folgeauftrag:** Anforderung von spezialisiertem Personal und/oder Material zur Fehlerbehebung (z.B. Elektriker, Hubsteiger für Leuchtmittelwechsel/Reparatur).
*   **Provisorische Maßnahmen:** Falls eine sofortige Reparatur nicht möglich ist, Prüfung von provisorischen Maßnahmen zur Erhöhung der Sicherheit bis zur endgültigen Behebung (z.B. mobile Beleuchtung, zusätzliche Absperrungen, falls erforderlich).

---

## C27

- Domaene: SIGNAL

### USER MESSAGE

```
Signalgeber ohne Funktion; keine Lichtsignale sichtbar. (Hauptverkehrszeit / hoher Verkehr).
```

### CONTEXT (wie vom Judge gesehen)

```json
{
  "incident": {
    "fault_type": "signal_dark",
    "severity": "high",
    "reported_at": "2026-01-16T09:00:51+01:00",
    "reporter": "citizen",
    "photo_description": "Alle Signalphasen dunkel, keine Lichtausgabe sichtbar. Ampelgehäuse äußerlich intakt. Kreuzung ohne Regelung."
  },
  "asset": {
    "asset_osm": "n34576088",
    "longitude": 12.1354183,
    "latitude": 47.8489887
  },
  "device": {
    "connectivity": "offline",
    "device_state": "ok"
  },
  "environment": {
    "visibility": "poor_visibility",
    "time_of_day": "rush_hour",
    "traffic_exposure": "high",
    "weather": "rain",
    "noise_level": "high"
  },
  "_guardrail_notes": [
    "HINWEIS: device.connectivity=offline und device.device_state=ok beziehen sich auf das Technikgerät (Smartphone/Tablet), NICHT auf die Ampelanlage selbst. Offline-Workflow anpassen: Dokumentation lokal, spätere Synchronisation.",
    "SICHERHEITSHINWEIS: fault_type=signal_dark / severity=high → Sofortige Absicherung der Kreuzung erforderlich. Bei signal_dark: Kreuzung wie unbeschrankt behandeln. Eskalation an Leitstelle priorisieren."
  ]
}
```

### EXPECTED ELEMENTS

```
(leer -- test_loader schreibt keinen Schluessel expected_elements_short in input.meta, der Judge erhielt hier keinen Inhalt)
```

### MODEL ANSWER

Die Situation ist kritisch und erfordert sofortiges Handeln. Ein Signalgeber ohne Funktion bei Hauptverkehrszeit, hohem Verkehrsaufkommen und schlechter Sicht stellt eine erhebliche Gefahr dar. Priorität hat die umgehende Sicherung der Kreuzung.

**Vorgehensweise bei "Signalgeber ohne Funktion" (Signal Dark)**

**1. Absicherung der Gefahrenstelle (Priorität: SOFORT!)**
*   **Unmittelbare Gefahrenabwehr:** Die Kreuzung ist als ungesicherter Bereich zu betrachten.
*   **Warnblinklicht:** Eigenes Fahrzeug mit Warnblinklicht gut sichtbar positionieren, um auf die Gefahr aufmerksam zu machen.
*   **Warndreieck/Warnleuchten:** Ausreichend Warndreiecke und/oder Warnleuchten aufstellen, um den fließenden Verkehr frühzeitig zu warnen und die Kreuzung abzusichern.
*   **Verkehrsregelung (falls geschult und sicher):** Bei hohem Verkehrsaufkommen und fehlender Regelung durch die Ampel, wenn möglich und sicher, den Verkehr manuell regeln, bis professionelle Unterstützung eintrifft. Eigensicherung beachten!
*   **Polizei informieren:** Unverzüglich die Polizei über die ausgefallene Ampelanlage und die Gefahrensituation informieren, um Unterstützung bei der Verkehrsregelung anzufordern.

**2. Sichtprüfung (Äußerlich)**
*   **Ampelgehäuse:** Prüfen, ob das Ampelgehäuse äußerlich intakt ist (keine sichtbaren Beschädigungen, Vandalismus, Anfahrspuren). Laut Meldung ist es intakt.
*   **Kabel/Zuleitungen:** Sichtprüfung auf offensichtliche Beschädigungen an Kabeln oder Zuleitungen im sichtbaren Bereich.
*   **Umgebung:** Gibt es Anzeichen für externe Einflüsse (z.B. umgestürzte Bäume, Baufahrzeuge, die Kabel beschädigt haben könnten)?

**3. Diagnose/Beobachtung (Funktion)**
*   **Alle Signalphasen dunkel:** Bestätigen, dass tatsächlich alle Signalphasen des betroffenen Signalgebers dunkel sind und keine Lichtausgabe erfolgt.
*   **Andere Signalgeber:** Funktionieren andere Signalgeber an der gleichen Kreuzung? Dies hilft bei der Eingrenzung des Fehlers (lokaler Defekt vs. zentrale Störung).
*   **Stromversorgung:** Gibt es Anzeichen für einen Stromausfall im Bereich der Kreuzung (z.B. auch Straßenlampen dunkel)?
*   **Witterungseinflüsse:** Regen und schlechte Sicht können die Situation verschärfen. Dies bei der Dokumentation und Eskalation berücksichtigen.

**4. Dokumentation (Lokal speichern!)**
*   **Offline-Workflow:** Da die Konnektivität des Geräts offline ist, alle Informationen sorgfältig lokal erfassen.
*   **Uhrzeit und Datum:** Genaue Uhrzeit der Feststellung und des Beginns der Absicherung.
*   **Standort:** Bestätigung der Koordinaten (Längengrad: 12.1354183, Breitengrad: 47.8489887) und der Asset-ID (n34576088).
*   **Fehlerbeschreibung:** "Signalgeber ohne Funktion, keine Lichtsignale sichtbar. Alle Signalphasen dunkel."
*   **Umgebungsbedingungen:** Hoher Verkehr, Hauptverkehrszeit, schlechte Sicht, Regen, hoher Geräuschpegel.
*   **Durchgeführte Maßnahmen:** Detaillierte Beschreibung der Absicherungsmaßnahmen (Warndreieck, Warnleuchten, ggf. Polizei informiert).
*   **Fotos:** Mehrere Fotos aus verschiedenen Perspektiven machen, die den Zustand der Ampel und die Absicherung dokumentieren.
*   **Reporter-Informationen:** "Bürger gemeldet", "2026-01-16T09:00:51+01:00".

**5. Eskalation (Priorität: SOFORT!)**
*   **Leitstelle/Bereitschaftsdienst:** Unverzüglich die zuständige Leitstelle oder den Bereitschaftsdienst telefonisch kontaktieren.
*   **Dringlichkeit:** Die hohe Dringlichkeit der Störung ("severity: high", "rush_hour", "high traffic", "poor_visibility") klar kommunizieren.
*   **Informationen:** Alle gesammelten Informationen (Standort, Fehlerbild, Umgebungsbedingungen, durchgeführte Absicherungsmaßnahmen) präzise weitergeben.
*   **Anforderung:** Umgehende Entsendung eines Technikers und ggf. Unterstützung bei der Verkehrsregelung anfordern.
*   **Synchronisation:** Sobald wieder Konnektivität besteht, die lokal erfassten Daten und Fotos synchronisieren.

---

## C28

- Domaene: LAMP

### USER MESSAGE

```
Zeitweiser Ausfall gemeldet; aktuell normal. Bitte kontrollieren.
```

### CONTEXT (wie vom Judge gesehen)

```json
{
  "_unstructured_text": "poor_visibility | fog | Rosenheim, Heilig Blut | True | intermittent | 2026-01-18T14:56:09+01:00 | ok | medium | Straßenlaterne im Nebel aufgenommen; Leuchtmittel aktiv, jedoch Mast mit leichten Feuchtigkeitsflecken. Schaltbox äußerlich in Ordnung. | high | 12.116307 | night | 47.8369218 | medium | online | patrol | n1987093602 | yes"
}
```

### EXPECTED ELEMENTS

```
(leer -- test_loader schreibt keinen Schluessel expected_elements_short in input.meta, der Judge erhielt hier keinen Inhalt)
```

### MODEL ANSWER

Bitte führen Sie folgende Schritte zur Überprüfung der Straßenlaterne in Rosenheim, Heilig Blut (ID: n1987093602) durch, die einen zeitweisen Ausfall meldet, aber aktuell in Betrieb ist. Priorität ist hoch, insbesondere wegen der Feuchtigkeitsflecken am Mast.

**Schritt-für-Schritt-Checkliste:**

1.  **Absicherung (Sicherheit & Verkehrssicherung):**
    *   Sichern Sie den Arbeitsbereich gemäß den Vorschriften ab, insbesondere bei schlechter Sicht oder Dunkelheit.
    *   Stellen Sie sicher, dass der Verkehr nicht behindert oder gefährdet wird.
    *   Tragen Sie persönliche Schutzausrüstung (PSA).

2.  **Sichtprüfung:**
    *   Überprüfen Sie den Mast auf weitere Feuchtigkeitsflecken, Korrosion oder Beschädigungen.
    *   Kontrollieren Sie die Schaltbox erneut auf äußere Unversehrtheit und mögliche Anzeichen von Feuchtigkeitseintritt (Kondenswasser, Rostspuren).
    *   Prüfen Sie die Verkabelung im sichtbaren Bereich auf Beschädigungen oder lose Verbindungen.
    *   Begutachten Sie das Leuchtmittel und die Leuchtenabdeckung auf Risse oder Defekte.
    *   Achten Sie auf Anzeichen von Vandalismus oder Fremdeinwirkung.

3.  **Diagnose/Beobachtung:**
    *   Da der Ausfall "intermittent" ist, versuchen Sie, den Fehler zu reproduzieren oder auf spezifische Bedingungen zu achten (z.B. bei Nässe, Wind, bestimmten Schaltzeiten).
    *   Messen Sie, falls möglich und sicher, die Spannung an der Leuchte und in der Schaltbox.
    *   Überprüfen Sie die Sicherungen und Schutzschalter in der Schaltbox.
    *   Beobachten Sie das Schaltverhalten der Laterne über einen längeren Zeitraum, falls dies praktikabel ist.

4.  **Dokumentation:**
    *   Halten Sie alle Feststellungen detailliert fest (Datum, Uhrzeit, genaue Beobachtungen, Messwerte).
    *   Machen Sie Fotos von allen relevanten Bereichen, insbesondere von den Feuchtigkeitsflecken am Mast und dem Zustand der Schaltbox.
    *   Notieren Sie, welche Maßnahmen Sie ergriffen haben.

5.  **Eskalation:**
    *   Basierend auf Ihren Feststellungen entscheiden Sie über die weiteren Schritte.
    *   Bei Anzeichen von Wassereintritt, Korrosion oder elektrischen Defekten, die ein Sicherheitsrisiko darstellen, ist eine sofortige Behebung durch Fachpersonal erforderlich.
    *   Melden Sie den Status und Ihre Empfehlungen umgehend an die zuständige Stelle zur weiteren Veranlassung.

---

## C29

- Domaene: SIGNAL

### USER MESSAGE

```
Ampel funktioniert aktuell, aber wiederholt Ausfälle gemeldet.
```

### CONTEXT (wie vom Judge gesehen)

```json
{
  "_raw_text": "Betroffene Lichtsignalanlage: OSM-ID n2043315, Koordinaten 47.8415331, 12.1224516. Gemeldeter Fehler: sporadischer Ausfall, Schweregrad mittel. Gemeldet am 2026-01-18T17:05:05+01:00 von Leitstelle. Kein Foto verfügbar. Umgebung: nachts, Wetter Sturm, Sichtweite poor_visibility, Verkehrsaufkommen mittel. Technikgerät des Außendienstmitarbeiters: Konnektivität online, Gerätezustand in Ordnung."
}
```

### EXPECTED ELEMENTS

```
(leer -- test_loader schreibt keinen Schluessel expected_elements_short in input.meta, der Judge erhielt hier keinen Inhalt)
```

### MODEL ANSWER

Verstanden. Sporadische Ausfälle einer Lichtsignalanlage bei Sturm und schlechter Sicht erfordern schnelles und sicheres Handeln. Hier ist die Schritt-für-Schritt-Checkliste für den Außendienst:

**Betroffene Lichtsignalanlage:** OSM-ID n2043315, Koordinaten 47.8415331, 12.1224516
**Gemeldeter Fehler:** Sporadischer Ausfall, Schweregrad mittel. Gemeldet am 2026-01-18T17:05:05+01:00.
**Umgebung:** Nachts, Sturm, schlechte Sicht, mittleres Verkehrsaufkommen.

---

### **Checkliste Außendienst: Sporadischer Ampelausfall**

1.  **Absicherung (Priorität: Sicherheit & Verkehrssicherung)**
    *   **Persönliche Sicherheit:** Warnweste, Schutzkleidung, geeignete Beleuchtung (Stirnlampe).
    *   **Verkehrssicherung:**
        *   Unverzüglich Warnblinkanlage des Einsatzfahrzeugs aktivieren.
        *   Warndreiecke und/oder Blitzleuchten gemäß StVO und internen Vorschriften aufstellen.
        *   Bei Bedarf: Absperrungen errichten, um den Arbeitsbereich zu sichern und den Verkehr zu leiten.
        *   Besondere Vorsicht aufgrund von Sturm, schlechter Sicht und Dunkelheit.
    *   **Leitstelle informieren:** Ankunft am Einsatzort bestätigen und Absicherungsmaßnahmen melden.

2.  **Sichtprüfung (Umfassende Inspektion)**
    *   **Gesamtanlage:**
        *   Äußere Beschädigungen an Masten, Signalgebern, Kabeln oder Schaltkästen?
        *   Lose Teile (z.B. durch Sturm)?
        *   Verschmutzungen oder Bewuchs, der die Sichtbarkeit der Signalgeber beeinträchtigt?
    *   **Kabel und Anschlüsse:**
        *   Sichtbare Beschädigungen an Zuleitungen oder Signalkabeln?
        *   Korrosion oder lose Verbindungen an den Schaltkästen oder Signalgebern?
    *   **Umgebung:**
        *   Stehendes Wasser, das in Schaltkästen eindringen könnte?
        *   Baumaterialien oder andere Hindernisse, die die Anlage beeinflussen?

3.  **Diagnose / Beobachtung (Fehlersuche & Verifizierung)**
    *   **Fehlerbild verifizieren:**
        *   Anlage über längeren Zeitraum beobachten, um den sporadischen Ausfall zu bestätigen.
        *   Tritt der Ausfall unter bestimmten Bedingungen auf (z.B. Windböen, Erschütterungen)?
    *   **Schaltkasten:**
        *   Sichtprüfung der Sicherungen und Schutzschalter. Sind alle intakt und eingeschaltet?
        *   Prüfung auf Feuchtigkeit oder Schäden im Schaltkasten.
        *   Kontrolle der Klemmstellen auf festen Sitz.
    *   **Steuerung:**
        *   Statusanzeigen der Steuerungseinheit prüfen (Fehlermeldungen, LEDs).
        *   Systemprotokolle (falls zugänglich) auf Auffälligkeiten oder Fehlereinträge prüfen.
        *   Spannungsversorgung messen (Eingang/Ausgang der Steuerung).
    *   **Signalgeber:**
        *   Funktion aller Signalgeber einzeln prüfen (falls möglich über Testschaltung).
        *   Wackelkontakte an den Lampenfassungen oder LED-Modulen ausschließen.

4.  **Dokumentation (Präzise & Vollständig)**
    *   **Zeitpunkt:** Beginn und Ende der Arbeiten.
    *   **Feststellungen:** Genaue Beschreibung aller beobachteten Auffälligkeiten, Schäden oder Fehlermeldungen.
    *   **Durchgeführte Maßnahmen:** Was wurde geprüft, gemessen, repariert oder ausgetauscht?
    *   **Messwerte:** Alle relevanten Spannungswerte, Stromstärken etc.
    *   **Umgebungsbedingungen:** Bestätigung von Sturm, schlechter Sicht, Nacht.
    *   **Fotos:** Falls möglich und sicher, Fotos von Auffälligkeiten oder Schäden machen (auch wenn kein Foto gemeldet wurde, kann es vor Ort anders sein).
    *   **Protokollierung:** Alle Daten im System des Technikgeräts erfassen.

5.  **Eskalation (Bei Bedarf)**
    *   **Reparatur vor Ort möglich?**
        *   Wenn der Fehler behoben werden konnte: Funktionsprüfung durchführen und Leitstelle informieren.
        *   Anlage weiter beobachten, um die Störungsfreiheit zu bestätigen.
    *   **Reparatur nicht möglich / Komplexer Fehler:**
        *   Leitstelle umgehend über die Situation informieren.
        *   Detaillierte Beschreibung der Diagnoseergebnisse und der benötigten Ressourcen (Spezialwerkzeug, Ersatzteile, weiteres Personal).
        *   Ggf. Entscheidung über temporäre Außerbetriebnahme oder manuelle Regelung der Kreuzung (Polizei/Verkehrsregelung anfordern).
        *   Nächste Schritte mit der Leitstelle abstimmen.

---

**Annahme:** Das Technikgerät ist online und funktionsfähig, was die Dokumentation und Kommunikation erleichtert. Bei anhaltendem Sturm und schlechter Sicht ist die Sicherheit des Personals und der Verkehrsteilnehmer oberstes Gebot.

---

## C30

- Domaene: LAMP

### USER MESSAGE

```
Lampe war vorhin aus, ist jetzt wieder an. Sporadischer Fehler.
```

### CONTEXT (wie vom Judge gesehen)

```json
{
  "_raw_text": "Die Straßenlampe befindet sich am Standort Rosenheim, Bahnhof (OSM-ID: n5718630492, Koordinaten: 47.8511562, 12.1186059). Gemeldeter Fehler: sporadischer Ausfall, Schweregrad niedrig. Gemeldet am 2026-01-21T09:11:43+01:00 von Bürger. Foto vorhanden. Bildbeschreibung: Leuchtmittel optisch intakt, Mastfuß ohne sichtbare Schäden; Schaltbox geschlossen. Kein akuter Handlungsbedarf erkennbar. Umgebung: tagsüber, Wetter klar, Lichtverhältnisse normal_visibility, Verkehrsaufkommen hoch. Technikgerät des Außendienstmitarbeiters: Konnektivität offline, Gerätezustand schwache Batterie."
}
```

### EXPECTED ELEMENTS

```
(leer -- test_loader schreibt keinen Schluessel expected_elements_short in input.meta, der Judge erhielt hier keinen Inhalt)
```

### MODEL ANSWER

Ein sporadischer Ausfall einer Straßenlampe erfordert eine systematische Vorgehensweise, auch wenn der Fehler aktuell nicht sichtbar ist. Priorität hat immer die Sicherheit, insbesondere bei hohem Verkehrsaufkommen.

**Standort:** Rosenheim, Bahnhof (OSM-ID: n5718630492, Koordinaten: 47.8511562, 12.1186059)
**Fehler:** Sporadischer Ausfall (Lampe war aus, jetzt wieder an), gemeldet am 21.01.2026.
**Aktuelle Situation:** Tagsüber, klares Wetter, normale Sicht, hohes Verkehrsaufkommen. Leuchtmittel optisch intakt, Mastfuß ohne sichtbare Schäden, Schaltbox geschlossen.
**Hinweis:** Das Technikgerät des Außendienstmitarbeiters hat offline Konnektivität und schwache Batterie. Dies muss vor Ort behoben werden, um eine ordnungsgemäße Dokumentation und ggf. Diagnose zu ermöglichen.

---

**Schritt-für-Schritt-Checkliste für den Außendienst:**

1.  **Absicherung (Sicherheit geht vor):**
    *   **Verkehrssicherung:** Trotz des aktuell nicht sichtbaren Fehlers und Tageslichts ist bei hohem Verkehrsaufkommen eine angemessene Absicherung der Arbeitsstelle gemäß UVV und StVO unerlässlich, falls Arbeiten am Mast oder der Schaltbox erforderlich werden könnten.
    *   **Persönliche Schutzausrüstung (PSA):** Sicherstellen, dass die vollständige PSA getragen wird.

2.  **Sichtprüfung (Erweiterte Beobachtung):**
    *   **Umfeld:** Erneute, detaillierte Sichtprüfung des Mastes, des Leuchtmittels und der Schaltbox auf äußere Beschädigungen, Korrosion, lose Kabel oder ungewöhnliche Geräusche/Gerüche.
    *   **Leuchtmittel:** Obwohl optisch intakt, auf Verfärbungen, Flackern oder andere Auffälligkeiten achten, die auf einen bevorstehenden Ausfall hindeuten könnten.
    *   **Schaltbox:** Prüfen, ob die Schaltbox tatsächlich fest verschlossen ist und keine Manipulationen erkennbar sind.
    *   **Umgebungseinflüsse:** Gibt es in der Nähe Bäume oder andere Objekte, die bei Wind Kabel bewegen oder Schatten werfen könnten, welche die Sensorik beeinflussen?

3.  **Diagnose/Beobachtung (Fehlersuche bei Sporadik):**
    *   **Gerätezustand:** Unbedingt zuerst die Konnektivität des Technikgeräts herstellen und die Batterie laden oder wechseln. Ohne funktionierendes Gerät ist eine ordnungsgemäße Dokumentation und ggf. Fehleranalyse nicht möglich.
    *   **Schaltzeiten/Sensorik:** Wenn möglich, die Schaltzeiten der Lampe prüfen (Dämmerungsschalter, Zeitschaltuhr). Ein sporadischer Fehler kann auf eine fehlerhafte Sensorik oder eine ungenaue Einstellung hindeuten.
    *   **Wackelkontakt:** Sporadische Fehler sind oft auf Wackelkontakte in der Verkabelung oder im Leuchtmittel selbst zurückzuführen. Eine leichte Bewegung am Mast oder der Schaltbox kann manchmal den Fehler reproduzieren (Vorsicht: nur bei ausgeschalteter Anlage und entsprechender Absicherung).
    *   **Lasttest (falls möglich):** Wenn die Lampe über eine Steuerung verfügt, kann ein manuelles Ein- und Ausschalten über einen längeren Zeitraum helfen, den Fehler zu provozieren.
    *   **Umgebungsdaten:** Notieren, ob es seit der Meldung weitere Beobachtungen gab (z.B. durch andere Kollegen oder Bürger).

4.  **Dokumentation (Lückenlos und Präzise):**
    *   **Alle Beobachtungen:** Jede Feststellung, auch wenn sie unauffällig erscheint, detailliert im System dokumentieren.
    *   **Fotos:** Aktuelle Fotos vom Standort, Mast, Leuchtmittel und der Schaltbox machen.
    *   **Gerätedaten:** Wenn das Technikgerät wieder online ist, alle verfügbaren Daten (z.B. Spannungswerte, Schaltzustände) auslesen und speichern.
    *   **Maßnahmen:** Alle durchgeführten Schritte und Prüfungen festhalten.
    *   **Einschätzung:** Eine Einschätzung zum möglichen Fehlerbild und zur Dringlichkeit abgeben.

5.  **Eskalation (Folgeaktionen definieren):**
    *   **Keine Fehlerursache gefunden:** Wenn trotz aller Prüfungen keine eindeutige Fehlerursache gefunden wird, den Fall als "sporadischer Fehler, nicht reproduzierbar" dokumentieren und eine Wiedervorlage für eine erneute Prüfung bei Dunkelheit oder bei erneuter Fehlermeldung einstellen.
    *   **Verdacht auf Fehler:** Bei Verdacht auf einen spezifischen Fehler (z.B. Wackelkontakt, defekte Sensorik) eine Folgebeauftragung zur detaillierten Fehlerbehebung oder zum Austausch der vermuteten Komponente einleiten.
    *   **Sicherheitsrisiko:** Sollte sich wider Erwarten ein Sicherheitsrisiko ergeben (z.B. offene Kabel, instabiler Mast), sofortige Maßnahmen zur Gefahrenabwehr einleiten und die zuständige Stelle informieren.

---

**Zusammenfassend:** Der Fokus liegt auf einer gründlichen Untersuchung und Dokumentation, um bei einem sporadischen Fehlerbild eine Basis für zukünftige Diagnosen zu schaffen. Die Behebung der Probleme mit dem Technikgerät ist hierbei ein kritischer erster Schritt.

---
