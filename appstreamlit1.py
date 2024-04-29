
import streamlit as st
from pytube import YouTube
import os

def download_youtube_audio(url):
    try:
        # Utilise le dossier Téléchargements de l'utilisateur
        destination = os.path.join(os.path.expanduser('~'), 'Downloads')
        
        video = YouTube(url)
        audio = video.streams.filter(only_audio=True, file_extension='mp4').first()
        default_filename = audio.default_filename
        final_path = os.path.join(destination, default_filename)
        audio.download(output_path=destination)
        return f"Téléchargement terminé ! Fichier sauvegardé sous : {final_path}"
    except Exception as e:
        return f"Erreur : {e}"

# Interface utilisateur
st.title("Extracteur d'audio YouTube")
video_link = st.text_input("Entrez l'URL de la vidéo YouTube :", "https://youtu.be/your_video_id")

if st.button("Télécharger l'audio"):
    result = download_youtube_audio(video_link)
    st.success(result)
