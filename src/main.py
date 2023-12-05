import streamlit as st
import numpy as np
import pandas as pd
from pydub import AudioSegment
from io import BytesIO

# Titre de l'application
st.title("Uploader un fichier musical")

# Section pour uploader le fichier WAV
uploaded_file = st.file_uploader("Choisissez un fichier WAV", type=["wav"])

# Vérifier si un fichier a été uploadé
if uploaded_file is not None:
    # Lire le fichier audio
    audio = AudioSegment.from_wav(uploaded_file)

    # Afficher les informations sur le fichier audio
    st.write("Informations sur le fichier audio :")
    st.write(f"Durée : {len(audio) / 1000} secondes")
    st.write(f"Nombre de canaux : {audio.channels}")
    st.write(f"Fréquence d'échantillonnage : {audio.frame_rate} Hz")

    # Afficher le graphique du signal audio
    st.write("Graphique du signal audio :")
    st.line_chart(np.array(audio.get_array_of_samples()))