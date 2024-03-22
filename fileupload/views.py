from django.shortcuts import render, redirect
from .forms import FileUploadForm
from .models import FileUpload

def fileUpload(request):
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        aud = request.FILES["audiofile"]
        fileupload = FileUpload(
            title=title,
            content=content,
            audiofile=aud,
        )
        fileupload.save()
        return redirect('fileupload')
    else:
        fileuploadForm = FileUploadForm
        context = {
            'fileuploadForm': fileuploadForm,
        }
        return render(request, 'fileupload/file_upload.html', context)
    #return render(request, 'fileupload/file_upload.html', {})

