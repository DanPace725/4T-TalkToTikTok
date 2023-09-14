
---

# Setting Up and Running the 4T-TalkToTikTok Streamlit App

## Introduction

4T-TalkToTikTok is a Streamlit app designed to transcribe audio from TikTok videos using the OpenAI Whisper model and then correct the transcriptions using the GPT-3.5-turbo model.

## Prerequisites

1. **Python**: Ensure you have Python (version 3.6 or newer) installed. You can download it from [Python's official website](https://www.python.org/downloads/).

2. **pip**: Ensure you have pip installed. It usually comes with Python.

3. **Git** (optional): If you're planning to clone the repository.

## Installation Steps

1. **Clone the Repository** (optional):
   If you have Git installed, you can clone the repository:
   ```bash
   git clone https://github.com/DanPace725/4T-TalkToTikTok.git
   cd 4T-TalkToTikTok
   ```

2. **Set Up a Virtual Environment** (recommended):
   It's a good practice to set up a virtual environment for your projects to avoid potential conflicts between dependencies.
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use: venv\Scripts\activate
   ```

3. **Install Required Libraries**:
   Install the necessary libraries using pip:
   ```bash
   pip install streamlit openai pyktok
   ```

4. **Set Up OpenAI API Key**:
   You'll need an API key from OpenAI to use the transcription and correction services. Once you have the key:
   ```bash
   export OPENAI_API_KEY='your_api_key_here'  # On Windows, use: set OPENAI_API_KEY=your_api_key_here
   ```

5. **Ensure `ffmpeg` is Installed**:
   The app uses `ffmpeg` to convert video to audio. Ensure it's installed and accessible from the command line. You can download it from the [official website](https://ffmpeg.org/download.html).

## Running the App

1. **Navigate to the App Directory**:
   Ensure you're in the directory containing `app.py`.

2. **Run the Streamlit App**:
   ```bash
   streamlit run app.py
   ```

3. **Access the App**:
   Once you run the command, Streamlit will provide a local URL (usually `http://localhost:8501/`). Open this URL in your web browser.

4. **Use the App**:
   - Enter a TikTok video URL in the provided input field.
   - Click the "Transcribe" button.
   - The app will download the video, transcribe the audio, correct the transcription, and display the corrected transcription.
   - You can also download the transcription using the "Download Transcript" button.

## Troubleshooting

1. **Failed to Download Video**: Ensure the provided TikTok URL is valid and accessible.
2. **Failed to Transcribe Audio**: Check your OpenAI API key and ensure you have access to the Whisper and GPT-3.5-turbo models.
3. **Dependencies Issues**: If you encounter any issues related to dependencies, ensure you've activated your virtual environment and installed all required libraries.

---

