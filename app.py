import streamlit as st
import streamlit.components.v1 as components

# Configuración de la página para que use todo el ancho
st.set_page_config(layout="wide", page_title="Dashboard LATAM 2026")

# Leer el contenido de tu archivo HTML
with open("dashboardPS.html", "r", encoding="utf-8") as f:
    html_content = f.read()

# Renderizar el HTML
# Ajusta el 'height' según lo necesite tu dashboard para evitar scroll interno innecesario
components.html(html_content, height=1200, scrolling=True)