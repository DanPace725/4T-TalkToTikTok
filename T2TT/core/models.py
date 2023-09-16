from django.db import models

# Create your models here.
from django.db import models

class VideoTranscription(models.Model):
    video_url = models.URLField(unique=True)  # The URL from which the video was downloaded
    video_file = models.FileField(upload_to='videos/')  # Directory 'videos' inside MEDIA_ROOT
    audio_file = models.FileField(upload_to='audio/')  # Directory 'audio' inside MEDIA_ROOT
    transcription_text = models.TextField(blank=True, null=True)
    downloaded_at = models.DateTimeField(auto_now_add=True)
    transcribed_at = models.DateTimeField(blank=True, null=True)  # Timestamp when the transcription was completed
