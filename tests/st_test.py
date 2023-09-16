import requests
import re
import os
import streamlit as st

def get_video_id(url):
    return re.search(r'tiktok.com/@\w+/video/(\d+)', url).group(1)

def get_video_no_watermark(video_id):
    api_url = f'https://api.tiktokv.com/aweme/v1/aweme/detail/?aweme_id={video_id}'
    res = requests.get(api_url)

    # Check if the response was successful
    if res.status_code != 200:
        raise Exception(f"API request failed with status code {res.status_code}: {res.text}")

    # Check for an empty response
    if not res.text.strip():
        raise Exception("The API returned an empty response.")

    # Safe JSON parsing
    try:
        data = res.json()
    except ValueError:
        raise Exception(f"Failed to parse JSON from response: {res.text}")

    return data['aweme_details'][0]['video']['play_addr']['url_list'][0]

def download_video(url, filename):
    res = requests.get(url)
    with open(filename,'wb') as f:
        f.write(res.content)
    
st.title("TikTok Video Downloader")

video_url = st.text_input("Enter the video URL:")

if st.button("Download"):
    try:
        video_id = get_video_id(video_url)
        download_url = get_video_no_watermark(video_id)
        download_video(download_url, 'video.mp4')
        st.success("Video downloaded successfully!")
    except Exception as e:
        st.error(f"Download failed: {e}")
