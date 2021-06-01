from django.shortcuts import render, redirect
from .models import Photo

# Create your views here.


def gallery(request):
    photos = Photo.objects.all()
  
    context = {'photos': photos}
    return render(request, 'photos/gallery.html', context)


def viewPhoto(request, pk):
    photo = Photo.objects.get(id=pk)
    return render(request, 'photos/photo.html', {'photo': photo})


def addPhoto(request):


    if request.method == 'POST':
        data = request.POST
        images = request.FILES.getlist('images')

        for image in images:
            photo = Photo.objects.create(
                description=data['description'],
                image=image,
            )

        return redirect('gallery')

    return render(request, 'photos/upload.html')

def delPhoto(request, pk):
    photo = Photo.objects.get(id=pk)
    photo.delete()
    return redirect('gallery')