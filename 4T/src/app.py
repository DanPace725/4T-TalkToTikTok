# app.py

import streamlit as st
from video_util import download_video 
from transcription import transcribe_video, correct_transcription

st.title("Video to Audio Transcription")

url = st.text_input("Enter video URL")

if st.button("Transcribe"):
  result = transcribe_video(download_video(url))
  st.write(result)

if st.button("Correct"):
  corrected = correct_transcription(result)
  correct_transcription(result, corrected)

