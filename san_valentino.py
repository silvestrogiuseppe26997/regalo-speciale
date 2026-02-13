import streamlit as st
from streamlit_lottie import st_lottie
import requests
import time

# Configurazione pagina
st.set_page_config(page_title="Per Te", page_icon="❤️")

# Funzione per caricare animazioni carine
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_heart = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_02p3ps9h.json") # Cuore che vola

# --- INTERFACCIA ---
st.title("Hai un messaggio speciale... 💌")

if "button_clicked" not in st.session_state:
    st.session_state.button_clicked = False

def click_button():
    st.session_state.button_clicked = True

# Bottone iniziale
if not st.session_state.button_clicked:
    st.write("Clicca sul cuore per farlo volare")
    st.button("Premi qui ❤️", on_click=click_button)
else:
    # Mostra l'animazione del cuore/palloncino
    st_lottie(lottie_heart, height=300, key="coding")
    
    # Messaggio che appare gradualmente
    placeholder = st.empty()
    full_text = "Sei una cosa speciale per me. Ogni giorno con te è un regalo. ❤️"
    
    displayed_text = ""
    for char in full_text:
        displayed_text += char
        placeholder.subheader(displayed_text)
        time.sleep(0.1) # Effetto scrittura a macchina
    
    st.balloons() # Effetto festa final