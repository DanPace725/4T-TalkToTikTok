
---

# 4T-TalkToTikTok

4T-TalkToTikTok is a project that aims to transcribe audio from TikTok videos using the OpenAI Whisper model and then correct the transcriptions using the GPT-3.5-turbo model. It provides a user-friendly interface through Streamlit, allowing users to input a TikTok video URL and get the transcription in real-time.

## Features

- **Video Download**: Download TikTok videos using the provided URL.
- **Audio Extraction**: Convert the downloaded video to audio format for transcription.
- **Transcription**: Transcribe the audio using OpenAI's Whisper model.
- **Correction**: Correct the transcription using the GPT-3.5-turbo model.

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/DanPace725/4T-TalkToTikTok.git
   ```

2. Navigate to the project directory:
   ```
   cd 4T-TalkToTikTok
   ```

3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Set up the OpenAI API key as an environment variable:
   ```
   export OPENAI_API_KEY='your_api_key_here'
   ```

5. Ensure you have `ffmpeg` installed and accessible from the command line. If you're not sure how to do this you can check out this link [here](https://www.geeksforgeeks.org/how-to-install-ffmpeg-on-windows/). 

## Usage

1. Start the Streamlit app:
   ```
   streamlit run /src/app.py
   ```

2. Open the provided link in your browser.

3. Input a TikTok video URL and click on "Transcribe" to get the transcription.

4. Click on "Download Transcript" to download the transcript in Markdown.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

[MIT](https://choosealicense.com/licenses/mit/)

---
