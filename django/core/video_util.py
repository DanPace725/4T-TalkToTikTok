# src/video_util.py 

""" from pyktok import save_tiktok
import regex as re


def download_video(url):
  # Download video from URL using pyktok
  
  try:
    save_tiktok(url, True, "metadata.csv", "chrome")
    regex_url = re.findall(r'https://www.tiktok.com/(.*?)\?', url)[0]
    saved_filename = regex_url.replace('/','_') + '.mp4'
    return saved_filename 
  except Exception as e:
    error_string = (f"Failed to download video: {e}")
    return error_string
"""