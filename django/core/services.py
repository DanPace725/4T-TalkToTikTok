# core/services.py
import openai 
import os


openai.api_key = os.getenv("OPENAI_API_KEY") 

def transcribe_audio(audio_file):
  try:
    with open(audio_file, "rb") as audio_file:
      response = openai.Audio.transcribe(
        file=audio_file, 
        model="whisper-1", 
        response_format="text"
      )
      return response
  except openai.error.OpenAIError as e:
    error_string = (f"Failed to transcribe audio: {e}")
    return error_string

def correct_transcription(transcription):
  try:
    response = openai.ChatCompletion.create(
      model="gpt-3.5-turbo", 
      temperature=0, 
      messages=[
        {"role": "system", "content": f"Correct this transcription, return in markdown format with line breaks:"},
        {"role": "user", "content": transcription}
      ]
    )
    return response['choices'][0]['message']['content']
  except openai.error.OpenAIError as e:
    error_string = (f"Failed to correct transcription: {e}")
    return error_string
