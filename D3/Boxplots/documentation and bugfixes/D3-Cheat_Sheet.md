# Cheat sheet für die Js D3-Bibliothek 

> D3-Dokumentation:
> https://d3js.org/getting-started

## Zeichnen von SVG-Objekten und -Gruppen

## Einrichten von Diagrammen

1. Angabe der Dimensionen und Margins
```js
  const width = 640;
  const height = 400;
  const marginTop = 20;
  const marginRight = 20;
  const marginBottom = 30;
  const marginLeft = 40;
```

2. Achsenskalierung
    1. x-Achse
```js
  const x = d3.scaleUtc()
     // statisch
    .domain([<Minimalwert>, <Maximalwert>]) // Definitionsbereich (x-Werte)
    .range([marginLeft, width - marginRight]); // Länge der x-Achse; ACHTUNG: margin mit einrechnen!
```

```js
    // oder dynamisch 
    .domain([d3.min(data, d => d.value), d3.max(data, d => d.value)]) // Definitionsbereich (x-Werte)
    .range([marginLeft, width - marginRight]); // Länge der x-Achse; ACHTUNG: margin mit einrechnen!
```


---

   2. y-Achse (analog zur x-Achse)
```js
  const y = d3.scaleLinear()
      .domain([0, 100])
      .range([height - marginBottom, marginTop]);
```

---

   3. Erstellen des SVG-Containers, in dem alle SVG-Objekte angezeigt werden

```js
const svg = d3.create("svg")
      .attr("width", width)
      .attr("height", height);
```

---

4. Hinzufügen der Achsen zum SVG-Container, damit sie gerendert werden können

```js
svg.append("g")
     .attr("transform", `translate(0,${height - marginBottom})`)
     .call(d3.axisBottom(x));

svg.append("g")
    .attr("transform", `translate(${marginLeft},0)`)
    .call(d3.axisLeft(y));
```

---

5. Rückgabe des SVG-Objektes, wenn das Rendern in einer Funktion/Methode passiert

```js
return svg.node();
```

## Transformation

## Anwendungsbeispiel anhand von Boxplots