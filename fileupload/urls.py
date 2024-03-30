from django.urls import path
from . import views

urlpatterns = [
<<<<<<< HEAD
    #path('', views.fileUpload, name='fileUpload'),
    path('whisper', views.upload_and_transcribe, name='upload_and_transcribe'),
    path('clova', views.upload_and_clovatranscribe, name='upload_and_clovatranscribe'),
=======
    path('', views.fileUpload, name='fileupload'),
>>>>>>> parent of 1e8c662 (whisper api on app)
]