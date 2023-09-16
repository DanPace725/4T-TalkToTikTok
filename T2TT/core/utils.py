# core/utils.py

# Import necessary modules
from pyktok import save_tiktok
import regex as re
import subprocess


def download_video(url):
  """Download video from URL using pyktok"""
  
  try:
    save_tiktok(url, True, "data.csv", "chrome")
    regex_url = re.findall(r'https://www.tiktok.com/(.*?)\?', url)[0]
    saved_filename = regex_url.replace('/','_') + '.mp4'
    return saved_filename 
  except Exception as e:
    error_string = (f"Failed to download video: {e}")
    return error_string
  


def convert_to_audio(video_file, audio_file):
    cmd = [
    'ffmpeg', '-i', video_file,  
    '-q:a', '0', 
    '-map', 'a', audio_file
    ]

    process = subprocess.run(cmd)
    return process.returncode == 0