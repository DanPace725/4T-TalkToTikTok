"""
URL configuration for T2TT project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from core import views
from core.views import video_upload



urlpatterns = [
    path('admin/', admin.site.urls),
    path('download/', views.download_and_transcribe_view, name='download_and_transcribe_view'),
    path('', views.home_view, name='home_view'),
    path('success/', views.success_view, name='success'),
    path('error/', views.error_view, name='error'),
    path('transcript/', views.transcript_view, name='transcript'),
    path('download_transcript/<str:filename>/', views.download_transcript_view, name='download_transcript'),
    path('upload/', views.video_upload, name='video_upload'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
