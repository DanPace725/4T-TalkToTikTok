import streamlit as st
import openai
import os



openai.api_key = os.getenv("OPENAI_API_KEY")


# Note: you need to be using OpenAI Python v0.27.0 for the code below to work


def transcribe_audio(file):
    transcript = openai.Audio.transcribe("whisper-1", file)
    return transcript['text']

 

system_prompt = "You are a helpful assistant. Your task is to correct any spelling discrepancies in the transcribed text. Only add necessary punctuation such as periods, commas, and capitalization, and use only the context provided. Add a list of relevant keywords at the end of the response."

def corrected_transcript(temperature, system_prompt, transcript_text):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        temperature=temperature,
        messages=[
            {
                "role": "system",
                "content": system_prompt
            },
            {
                "role": "user",
                "content": transcript_text
            }
        ]
    )
    response_message = response['choices'][0]['message']['content']
    return response


st.title('Video Transcription')


uploaded_file = st.file_uploader("Choose an audio file", type="mp3")
if uploaded_file is not None:
    transcript = transcribe_audio(uploaded_file)
    st.write('Transcript:', transcript)

    system_prompt = "You are a helpful assistant. Your task is to correct any spelling discrepancies in the transcribed text. Only add necessary punctuation such as periods, commas, and capitalization, and use only the context provided."
    corrected_text = corrected_transcript(0, system_prompt, transcript)
    st.write('Corrected Transcript:', corrected_text)

