# core/views.py

from django.shortcuts import render, redirect
from .models import VideoTranscription
from .utils import download_video, convert_to_audio
from .services import transcribe_audio

def download_and_transcribe_view(request):
    if request.method == 'POST':
        video_url = request.POST.get('video_url')
        
        # Download the video
        video_filename = download_video(video_url)
        
        # Convert video to audio
        audio_filename = f"{video_filename}_audio.mp3"
        audio_file = convert_to_audio(video_filename, audio_filename)  # Assuming this function returns the audio filename
        
        # Transcribe the audio
        transcription = transcribe_audio(audio_file)
        
        # Save the results in the model
        video_transcription = VideoTranscription.objects.create(
            video_url=video_url,
            video_file=video_filename,
            transcription_text=transcription
        )
        
        # Redirect to a success page or display the transcription (based on your design)
        return redirect('success_page_or_other_view_name')

    return render(request, 'download.html')

def display_transcription_view(request, video_transcription_id):
    video_transcription = VideoTranscription.objects.get(pk=video_transcription_id)
    context = {
        'video_transcription': video_transcription
    }
    return render(request, 'display_transcription_template.html', context)

# core/views.py

def home_view(request):
    return render(request, 'home.html')
