import os
import streamlit as st
from song_analyzer import analyzer

st.title("Musicnalyzer")

st.write("Upload an audio file for source separation.")
uploaded_audio = st.file_uploader("Upload Audio File", type=["mp3", "wav"])

if uploaded_audio is not None:
    st.write("Original")
    st.audio(uploaded_audio, format="audio/wav")
    st.write("Source Separation in Progress...")

    # Create a temporary directory for output
    os.makedirs("out", exist_ok=True)

    # Write the uploaded audio to a temporary file
    with open("music.wav", "wb") as f:
        f.write(uploaded_audio.read())

    # Run the Demucs source separation command
    os.system("python3 -m demucs.separate music.wav -o out")

    # Analyze the separated audio to get the song key
    song_key, song_BPM = analyzer("music.wav")

    st.write("Source Separation Completed!")

    st.write("Separation Results:")
    st.write("Vocals")
    st.audio("./out/htdemucs/music/vocals.wav", format="audio/wav")
    st.write("Bass")
    st.audio("./out/htdemucs/music/bass.wav", format="audio/wav")
    st.write("Drums")
    st.audio("./out/htdemucs/music/drums.wav", format="audio/wav")
    st.write("Others")
    st.audio("./out/htdemucs/music/other.wav", format="audio/wav")

    st.write("Song Key:", song_key)
    st.write("Song Tempo:", song_BPM)
