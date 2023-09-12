# src/video_util.py 

from pyktok import save_tiktok

def download_video(url):
  """Download video from URL using pyktok"""
  
  try:
    save_tiktok(url, True, "data.csv", "chrome")
    return "video_data.mp4" 
  except Exception as e:
    print(f"Failed to download video: {e}")
    return None