
# Dokumentation des D3-Boxplot-Projektes

|             |                                                     |
|:-----------:|:---------------------------------------------------:|
| **Version** |                        0.0.1                        |
| **Status**  | funktionsfähig unter Verwendung von Testdatensätzen |
|  **Autor**  |                    Nico Seidler                     |


## Kurzbeschreibung
Das Ziel des Projektes besteht darin, 
+ *in der Testphase*: Daten selbst zu generieren
+ *später*: exportierte Daten im json-Format einzulesen
+ die eingelesenen Daten zu verarbeiten und
+ als Boxplot visuell aufzubereiten.

## Technische Umsetzung, Voraussetzungen, Installation und Ausführung
### Technische Umsetzung
Im Projekt wird die klassische `Python-Streamlit-Bibliothek` als Plattform genutzt, um den finalen Boxplot anzuzeigen.
Datenverarbeitung und Erstellung des Boxplots finden jedoch vollständig außerhalb der Python-Welt statt und werden
mittels der JavaScript-Bibliothek `D3` realisiert.
Der Aufbau des Projekts inklusive des Datenflusses kann dem verlinkten [Sequenzdiagramm](#Allgemeiner-Programmablauf-als-Sequenzdiagramm) entnommen werden.

### Installation und Ausführung
Folgende Module werden für die Lauffähigkeit der Anwendung benötigt und sind in der `requirements.txt` vermerkt:
+ `streamlit==1.58.0`
+ `Jinja2==3.1.6`
+ `pandas==3.0.3`
+ `numpy==2.4.6`

Zur *Installation* der benötigten Pakete muss der Befehl `pip install -r requirements.txt` genutzt werden.
Mit `streamlit run main_boxplot.py` wird die App automatisch gestartet und 
öffnet sich in einem entsprechenden Browserfenster.

+ *In der Testversion kann bei Bedarf auch ein neuer Satz an Testdaten mittels `python data.py` generiert werden.*

## Allgemeiner Programmablauf als Sequenzdiagramm
```mermaid
sequenceDiagram
    
    %% data.py
    box green Daten
    participant data
    %% testdaten.json
    participant testdaten
    end
    
    title Programmblauf
    box red main.py
    participant main as main_boxplot.py
    end
    
    %% Funktionen in utils.py
    box blue utils (Hilfsfunktionen)
    participant generate_boxplot
    participant read_json
    participant read_config_js
    participant read_html_template
    participant inject_data_into_html
    end
    
    
    %% Ablauf
    note over data, testdaten: Die Datengenerierung ist <br> vom Erstellen und <br> Anzeigen des Boxplots unabhängig.
    activate data
    data -->> +testdaten: generiert Testdaten
    deactivate data
    
    note over generate_boxplot: Orchestrierungsfunktion
    activate main
    testdaten -->> main: Testdaten stehen für main für Verarbeitung zur Verfügung
    main -->> +generate_boxplot: übergibt Pfad zur json-Datei, Pfad zum html-template, Pfad zur config.js - Datei
    generate_boxplot -->> +read_json: liest Daten aus den in der json vorhandenen Gruppen aus
    read_json ->> generate_boxplot: übergibt extrahierte Daten in einer Liste von dictionaries der Form Liste = [...,{<Gruppenname> : <Werte>},...]
    deactivate read_json
    
    generate_boxplot -->> +read_config_js: übergibt Pfad zur config.js - Datei
    read_config_js ->> generate_boxplot: Rückgabe des Inhalts der config.js - Datei als Config-Template in einem String
    deactivate read_config_js
    
    generate_boxplot -->> +read_html_template: übergibt Pfad zum HTML-Template
    read_html_template ->> generate_boxplot: Rückgabe der HTML-Syntax in einem String mit eingebetteter Variable für die Daten und Referenzen zur config.js
    deactivate read_html_template
    
    generate_boxplot -->> +inject_data_into_html: übergibt Daten in der Liste von dicts, HTML-Template als Einbettungsort, Config-Template zur Konfiguration des HTML-Templates
    inject_data_into_html ->> generate_boxplot: Rückgabe des HTML-Codes als f-String mit integrierten Daten und Konfiguration darin
    deactivate inject_data_into_html
    
    generate_boxplot ->> main: übergibt injiziertes HTML
    deactivate generate_boxplot
    
    note over main: rendert den Boxplot via Streamlit
```
