from django.shortcuts import render
from .froms import imageform
from .models import imageuploader

def get_image(request):
    if request.method=="POST":
        form=imageform(request.POST,request.FILES)
        if form.is_valid():
            form.save()
    form=imageform()
    im=imageuploader.objects.all()
    return render(request,'image.html',{"from":form,"image":im})
