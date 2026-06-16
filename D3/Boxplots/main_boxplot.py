import streamlit as st
import json
import os
import config
import utils

# ========== Konfigurationsvariablen ==========
# Pfade
json_path = config.JSON_PATH
html_path = config.HTML_PATH
config_path = config.CONFIG_PATH
# Chart-Parameter
chart_height = config.CHART_HEIGHT

# ========== Einlesen der Daten ==========
final_html = utils.generate_boxplot(json_path, html_path, config_path)

# ========== Rendern der Seite ==========

st.title("Boxplots mit D3.js")
st.markdown("<br><br>", unsafe_allow_html=True) # Abstandshalter durch Leerzeilen

# Rendern
st.iframe(final_html, height=chart_height)