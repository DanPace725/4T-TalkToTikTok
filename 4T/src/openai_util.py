# openai_util.py

import openai 
import os

openai.api_key = os.getenv("OPENAI_API_KEY") 

def transcribe_audio(audio_file):
  response = openai.Audio.transcribe(
    file=audio_file, 
    model="whisper-1", 
    response_format="text"
  )
  return response

def correct_transcription(transcription):
  response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo", 
    temperature=0, 
    messages=[
      {"role": "system", "content": f"Correct this transcription:"},
      {"role": "user", "content": transcription}
    ]
  )
  return response['choices'][0]['message']['content']