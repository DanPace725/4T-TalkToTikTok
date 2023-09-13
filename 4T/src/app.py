# app.py

import streamlit as st
from video_util import download_video
from transcription import transcribe_video, correct_transcription

st.title("Video to Audio Transcription")

url = st.text_input("Enter video URL")

if st.button("Transcribe"):
    with st.spinner("Downloading video..."):
        video_filename = download_video(url)

    if video_filename:
        with st.spinner("Transcribing..."):
            transcription = transcribe_video(video_filename)

        if transcription:
            with st.spinner("Correcting Transcription..."):
                corrected_trans = correct_transcription(transcription)

            st.subheader("Transcription:")
            st.write(corrected_trans)
            with open("transcript.md", "w") as f:
                f.write(corrected_trans)

            st.download_button(
                label="Download Transcript",
                data=corrected_trans,
                file_name=video_filename + "_transcript.md",
                mime="text/markdown",
            )
        else:
            st.error("Failed to transcribe audio")
    else:
        st.error("Failed to download video.")


