# core/views.py
import os
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.files import File
from .models import VideoTranscription
from .utils import download_video, convert_to_audio
from .services import transcribe_audio

def download_and_transcribe_view(request):
    if request.method == 'POST':
        video_url = request.POST.get('video_url')
        
        # Download the video
        video_filename = download_video(video_url)
        if not video_filename:
            return render(request, 'error.html', {'error': 'Failed to download video'})
        
        # Convert video to audio
        audio_filename = f"{video_filename}_audio.mp3"

        success = convert_to_audio(video_filename, audio_filename)  # Assuming this function returns the audio filename
        if not success:
            return render(request, 'download.html', {'error': 'Failed to convert video to audio.'})
        # Transcribe the audio
        transcription = transcribe_audio(audio_filename)
        if not transcription:
            return render(request, 'download.html', {'error': 'Failed to transcribe audio.'})
        # Write the transcription to a markdown file
        transcripts_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "transcripts")
        md_filename = os.path.join(transcripts_dir, f"{os.path.basename(audio_filename)}.md")
        with open(md_filename, 'w') as md_file:
            md_file.write(transcription)
        
        # Save the results in the model
        video_transcription = VideoTranscription.objects.create(
            video_url=video_url,
            video_file=video_filename,
            transcription_text=transcription
        )
        
        # Redirect to the transcript page instead of success page
        return redirect('transcript')

    return render(request, 'download.html')

def display_transcription_view(request, video_transcription_id):
    video_transcription = VideoTranscription.objects.get(pk=video_transcription_id)
    context = {
        'video_transcription': video_transcription
    }
    return render(request, 'display_transcription_template.html', context)



def download_transcript_view(request):
    latest_transcript = VideoTranscription.objects.latest('downloaded_at')
    md_filename = f"{latest_transcript.video_file}_transcript.md"
    
    with open(md_filename, 'r') as f:
        file_data = f.read()
    
    response = HttpResponse(file_data, content_type='text/markdown')
    response['Content-Disposition'] = f'attachment; filename="{md_filename}"'
    
    return response


def home_view(request):
    return render(request, 'home.html')

def success_view(request):
    return render(request, 'success.html')

def error_view(request):
    return render(request, 'error.html')

def transcript_view(request):
    latest_transcript = VideoTranscription.objects.latest('downloaded_at')
    context = {
        'transcript': latest_transcript
    }
    return render(request, 'transcript.html', context)