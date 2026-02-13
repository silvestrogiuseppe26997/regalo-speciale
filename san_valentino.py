import streamlit as st
from streamlit_lottie import st_lottie
import requests
import time

# Configurazione pagina
st.set_page_config(page_title="Per Te", page_icon="❤️")

def load_lottieurl(url):
    try:
        r = requests.get(url)
        if r.status_code != 200:
            return None
        return r.json()
    except:
        return None

# Nuovo link super stabile
lottie_heart = load_lottieurl("https://lottie.host/85ed354c-1660-4966-ba09-90696a09148d/7YfB34e3W7.json")

st.title("Hai un messaggio speciale... 💌")

if "button_clicked" not in st.session_state:
    st.session_state.button_clicked = False

if not st.session_state.button_clicked:
    st.write("Clicca sul cuore per farlo volare")
    if st.button("Premi qui ❤️"):
        st.session_state.button_clicked = True
        st.rerun()

if st.session_state.button_clicked:
    # Se l'animazione è carica la mostra, altrimenti mostra un'emoji grande
    if lottie_heart:
        st_lottie(lottie_heart, height=300, key="coding")
    else:
        st.write("# ❤️🎈")
    
    placeholder = st.empty()
    full_text = "Sei una cosa speciale per me. Ogni giorno con te è un regalo. ❤️"
    
    displayed_text = ""
    for char in full_text:
        displayed_text += char
        placeholder.subheader(displayed_text)
        time.sleep(0.1)
    
    st.balloons()
