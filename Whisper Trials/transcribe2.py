import streamlit as st
import openai
import os
import pyktok as pyk
import subprocess



# Set up OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")
main_path = "E:/Coding/4T/Whisper Trials/"
# Streamlit UI
st.title("Video URL to Audio Transcription with OpenAI")
video_url = st.text_input("Enter the TikTok video URL:")

def transcribe_audio_with_whisper(file_path):
    """
    Transcribes an audio file using OpenAI's Whisper API.

    Args:
    - file_path (str): Path to the audio file to be transcribed.

    Returns:
    - str: Transcribed text.
    """
    with open(file_path, "rb") as audio_file:
        response = openai.Audio.transcribe(
            file=audio_file,
            model="whisper-1",
            response_format="text"
        )
        
    return response


def download_video(url):
    try:
        pyk.save_tiktok(url, True, 'video_data.csv','chrome')
        video_filename = url.replace('/','_') + '.mp4'
        return video_filename
    except Exception as e:
        print(f"Failed to download the video due to {str(e)}")
        return False

  
def convert_mp4_to_mp3(input_file, output_file):
    """
    Convert an MP4 file to MP3 using ffmpeg.

    Parameters:
    - input_file (str): Path to the input MP4 file.
    - output_file (str): Path to the output MP3 file.

    
    """
    command = [
        'ffmpeg',
        '-i', input_file,
        '-q:a', '0',  # Best quality audio
        '-map', 'a',
        output_file
    ]

    process = subprocess.run(command)
    return process.returncode == 0  # Return True if successful, False otherwise

if video_url:
    with st.spinner("Downloading video..."):
        video_filename = download_video(video_url)

    
    if video_filename:
        with st.spinner("Converting video to audio..."):
            success_convert = convert_mp4_to_mp3(video_filename, "temp_audio.mp3")
        
        if success_convert:
            st.write(video_filename)
            with st.spinner("Transcribing audio..."):
                transcription = transcribe_audio_with_whisper("temp_audio.mp3")
            st.subheader("Transcription:")
            st.write(transcription)
        else:
            st.error("Failed to convert video to audio.")
    else:
        st.error("Failed to download the video.")

    # Optional: Correct the transcription using GPT-3.5-turbo
    if st.button("Correct Transcription"):
        with st.spinner("Correcting transcription..."):
            prompt = f"Correct the following transcription: {transcription}"
            response = openai.ChatCompletion.create(model="gpt-3.5-turbo", 
            temperature=0,
            messages=[
                {
                    "role": "system",
                    "content": prompt
                },
                {
                    "role": "user",
                    "content": transcription
                }
            ]
        )
            corrected_transcription = response['choices'][0]['message']['content']
        st.subheader("Corrected Transcription:")
        st.write(corrected_transcription)
