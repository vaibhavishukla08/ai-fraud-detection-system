import streamlit as st
from backend.voice_detector import analyze_audio

st.header("🎙️ Deepfake Voice Scam Detection")

audio_file = st.file_uploader("Upload voice recording", type=["wav", "mp3"])

if audio_file and st.button("Analyze Voice"):
    result = analyze_audio(audio_file)

    st.metric("Fake Probability", result["fake_probability"])
    st.write(result["explanation"])
