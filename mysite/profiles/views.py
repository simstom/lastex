from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .models import Profile
from django.core.files.storage import FileSystemStorage

# Create your views here.

def upload(request):
    return render(request,'profiles/upload.html')

def upload_create(request):
    form=Profile()
    form.title=request.POST['title']
    try:
        form.image=request.FILES['image']

    except: #이미지가 없어도 그냥 지나가도록-!
        pass
    form.save()
        
    return redirect('/profiles/profile/')

def profile(request):
    profile=Profile.objects.all()
    # upload = profile.image
    # fss = FileSystemStorage()
    # file = fss.save(upload.name, upload)
    # file_url = fss.url(file)
    file_url = 123457
    return render(request,'profiles/profile.html',{'profile':profile, 'file_url':file_url})



# from .forms import UploadFileForm

# # Imaginary function to handle an uploaded file.
# from somewhere import handle_uploaded_file

# def upload_file(request):
#     if request.method == 'POST':
#         form = UploadFileForm(request.POST, request.FILES)
#         if form.is_valid():
#             handle_uploaded_file(request.FILES['file'])
#             return HttpResponseRedirect('/success/url/')
#     else:
#         form = UploadFileForm()
#     return render(request, 'upload.html', {'form': form})
