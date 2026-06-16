# Drifteffekt und Bewegung der Boxen beim Zoomen

## Fehlerbeschreibung
Beim Zoomen bewegten sich die Inhalte des Boxplots in y-Richtung mit, 
anstatt vergrößert zu werden und ragten über den clip-path hinaus.
Anstatt sie also vergrößert darzustellen, drifteten sie aus dem Render-Bereich hinaus.

## Ursache
+ Versuch, `transform = "scale(k, 1)"` auf die *gesamte* Containergruppe des Inhaltes
  (`gContent`) anzuwenden
+ D3 liefert jedoch bei jedem Scroll-Event (das bei diesem Projekt zum Zoomen genutzt wird)
schon eine neue Transformationsmatrix, weshalb sich die *manuell transformierten y-Werte auf
diese aufaddierten* und so eine *kumulative Verschiebung* auslösten. Die Inhalte rutschten damit
bei jedem Scroll-Event weiter weg in y-Richtung von ihrer Ursprungsposition.

+ insgesamt:
  + `transform.y`-Offset
  + weiteres Problem: falsch gewählter *Ursprung der Skalierung*:
  Auswahl des *Mittelpunkts der Werte-Gruppe `gContent`, anstatt Nutzung
  des Ursprungs des Plot-Bereiches*

```js
gContent.attr("transform",
    `translate(${margin.left}, ${transform.y + yNull}) scale(1, ${k}) translate(0, ${-yNull})`
);
```

Die Kombination aus `translate(..., transform.y + yNull) und scale(1, k)` führt dazu, dass die Translation (Verschiebung) mit der Skalierung k interagiert 
und sich bei jedem Zoom-Event "aufschaukelt".

## Fehlerbehebung
+ Änderung der Datenstruktur in `renderChart()`:
  + einzelnes Ansteuern der Elemente durch die `zoomInChart()`- Funktion
  durch Binden der Werte (Quartile, Whisker-Grenzen) an die entsprechenden DOMs
  ```js
  svg_group.append("rect").attr("class", "element box-rect")
    .datum({ q1: q1, q3: q3 }) // Box
  
  // ...
  
  svg_group.append("line").attr("class", "element whisker-vert")
    .datum({ y1: whiskerMin, y2: whiskerMax }) // Whisker-Linien
  ```
  
+ Änderung des Zooms in `zoomInChart()`:
  + Attributupdates der einzelnen Elemente, anstatt Anwendung einer 
  Gesamttransformation

  ```js
  gContent.selectAll(".whisker-vert")
      .attr("y1", d => newY(d.y1))
      .attr("y2", d => newY(d.y2)); // einzelnes Verschieben der y-Werte für genaue Transformation
      
  gContent.selectAll(".box-rect")
      .attr("y", d => newY(d.q3))
      .attr("height", d => Math.abs(newY(d.q1) - newY(d.q3)));
  ```
  
## Fazit

| Aspekt            | Bug                                                        | Fix                                                                                  |
|-------------------|------------------------------------------------------------|--------------------------------------------------------------------------------------|
| **Ansatz**        | Transformation der gesamten Gruppe (`scale`)               | Manuelle Aktualisierung der Koordinaten der einzelnen Elemente                       |
| **Fehlerursache** | kumulativer Translation-Offset (doppelte y-Transformation) | absolute Neuberechnung der einzelnen Koordinaten -> keine doppelten Transformationen |
| **Präzision**     | hering (Rundungsfehler bei Skalierung)                     | hoch (direkte Skalen-Abfrage)                                                        |
| **Resultat**      | Diagramm "wandert"                                         | Diagramm bleibt fixiert und Zoom wird korrekt ausgeführt                             |

