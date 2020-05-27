from django.shortcuts import render,redirect
import datetime as dt
from django.http  import HttpResponse,Http404
from django.db.models.base import ObjectDoesNotExist
from .models import PhotoImage

# from PIL import ImageGrab
# Create your views here.

def welcome(request):
    
    return render(request, 'home.html')

def allphotos(request):
    photos=PhotoImage.objects.all()
    return render(request, 'pics.html', {"photos":photos})

def search_results(request):

    if 'photo' in request.GET and request.GET["photo"]:
        category = request.GET.get("photo")
        searched_photos = PhotoImage.search_by_category(category)
        message = f"{category}"

        return render(request, 'all-pictures/search.html',{"message":message,"photos": searched_photos})

    else:
        message = "You haven't searched for any term"
        return render(request, 'all-pictures/search.html',{"message":message})

def photo(request,photo_id):
    try:
        photo = PhotoImage.objects.get(id = photo_id)
    except ObjectDoesNotExist:
        raise Http404()
    return render(request,"all-pictures/photo.html", {"photo":photo})

def copy(request,photo_image):
#    img = ImageGrab.grabclipboard()
#    return img
    try:
        
        copiedurl = PhotoImage.copy_photo(image = photo_image)
        
    except ObjectDoesNotExist:
        raise Http404()
    return render(request,"copy.html", {"copy":copiedurl})