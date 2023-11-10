# core/views.py

import os
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.files import File
from django.http import HttpResponseRedirect
from .models import VideoTranscription
from .utils import download_video, convert_to_audio
from .services import transcribe_audio
from .forms import VideoForm
from django.http import JsonResponse
from django.urls import reverse



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



def download_transcript_view(request, filename):
    latest_transcript = VideoTranscription.objects.latest('downloaded_at')
    
    # Get the current directory
    current_dir = os.path.dirname(os.path.abspath(__file__))
    # Get the parent directory (django)
    parent_dir = os.path.dirname(current_dir)
    # Construct the path to the media directory
    media_dir = os.path.join(parent_dir, "media")
    
    # Remove the .mp3 from the filename and any directory paths
    base_filename = os.path.basename(latest_transcript.video_file.path).replace('.mp3', '').split('/')[-1]
    base_filename = base_filename.replace('.mp4', '')
    md_filename = os.path.join(media_dir, f"{base_filename}_transcript.md")
    
    with open(md_filename, 'r') as f:
        file_data = f.read()
    
    response = HttpResponse(file_data, content_type='text/markdown')
    response['Content-Disposition'] = f'attachment; filename="{os.path.basename(md_filename)}"'
    
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
def video_upload(request):
    if request.method == 'POST':
        form = VideoForm(request.POST, request.FILES)
        if form.is_valid():
            video = form.save()
            video_filename = video.video.path

            # Convert video to audio
            audio_filename = f"{video_filename.replace('.mp4', '')}.mp3"
            success = convert_to_audio(video_filename, audio_filename)
            if not success:
                return render(request, 'upload.html', {'form': form, 'error': 'Failed to convert video to audio.'})

            # Transcribe the audio
            transcription = transcribe_audio(audio_filename)
            if not transcription:
                return render(request, 'upload.html', {'form': form, 'error': 'Failed to transcribe audio.'})
           
          # Get the current directory
            current_dir = os.path.dirname(os.path.abspath(__file__))
            # Get the parent directory (django)
            parent_dir = os.path.dirname(current_dir)
            # Construct the path to the media directory
            media_dir = os.path.join(parent_dir, "media")

            # Check if the directory exists, if not, create it
            os.makedirs(media_dir, exist_ok=True)

            # Remove the .mp3 from the filename
            base_filename = os.path.basename(audio_filename).replace('.mp3', '').split('/')[-1]
            md_filename = os.path.join(media_dir, f"{base_filename}_transcript.md")

            with open(md_filename, 'w') as md_file:
                md_file.write(transcription)

            # Save the results in the model
            video.audio_file = audio_filename
            video.transcription_text = transcription
            video.save()

            # Create a VideoTranscription object
            video_transcription = VideoTranscription.objects.create(
                video_url=video.video.url,
                video_file=video_filename,
                transcription_text=transcription
            )

            # Redirect to the transcript page instead of success page
            context = {
                'transcript': video_transcription
            }
            return JsonResponse({'redirect': reverse('transcript')})

    else:
        form = VideoForm()

    return render(request, 'upload.html', {'form': form})