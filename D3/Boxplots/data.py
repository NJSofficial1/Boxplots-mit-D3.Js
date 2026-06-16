import numpy as np
import json

# ---------- Generieren der Daten ----------  

# normalverteilte Daten  
d_normalverteilt = np.random.normal(50, 10, 1000).tolist()

# Daten mit enormen Ausreißern
d_ausreisser = [1, 2 ] + np.random.normal(30, 5, 50).tolist() + [120, 130]
# manuelles Hinzufügen noch größerer Ausreißer
d_ausreisser.extend([100, 200, 300])

# ---------- Export der Daten als JSON ----------

# Erstellen der Struktur für mehrere Boxplots
datensammlung = {
    "gruppen": [
        { "name": "Normalverteilt", "werte": d_normalverteilt },
        { "name": "Ausreißer", "werte": d_ausreisser }
    ]
}

# Erstellen der .json-Datei
with open("static/testdaten.json", "w") as f:
    # Nimm mein Python-Objekt `datensammlung` und schreibe es serialisiert in f
    json.dump(datensammlung, f)