# core/utils.py

# Import necessary modules
from pyktok import save_tiktok
import regex as re
import subprocess


def download_video(url):
  """Download video from URL using pyktok"""
  
  try:
    save_tiktok(url, True, "data.csv", "chrome")
    regex_url = re.findall(r'https://www.tiktok.com/(.*?)\?', url)
    saved_filename = regex_url.replace('/','_') + '.mp4'
    return saved_filename 
  except (subprocess.CalledProcessError, FileNotFoundError) as e:
    error_string = (f"Failed to download video: {e}")
    return error_string
  


def convert_to_audio(video_file, audio_file):
  try:
    cmd = [
    'ffmpeg', '-i', video_file,  
    '-q:a', '0', 
    '-map', 'a', audio_file
    ]

    process = subprocess.run(cmd)
    if process.returncode != 0:
      raise Exception(f"ffmpeg command failed with return code: {process.returncode}")
    return True
  
  except FileNotFoundError as e:
    error_string = (f"File not found: {e}")
    return error_string
  except subprocess.CalledProcessError as e:
    error_string = (f"ffmpeg command failed: {e}")
    return error_string
  except Exception as e:
    error_string = (f"Unexpected error occurred: {e}")
    return error_string
  
  