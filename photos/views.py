from email.mime import image
from multiprocessing import context
from django.views.generic import TemplateView, ListView
from django.shortcuts import render

from photos.models import Category, Image, Location

# Create your views here.
def index(request):
     images = Image.objects.all()
     category = Category.objects.all()
     locations = Location.get_location()

     if 'location' in request.GET and request.GET['location']:
        name = request.GET.get('location')
        images = Image.view_location(name)

     elif 'category' in request.GET and request.GET['category']:
        cat = request.GET.get('Category')
        images = Image.view_category(cat)

        return render(request, 'index.html', {"name": name, "images": images, "cat": cat})
     return render(request, "index.html", {'images': images, 'locations': locations, 'category': category})


def location_img(request, location):
    images = Image.filter_by_location(location)
    return render(request, 'location.html', {'location_img': images})

    

def SearchResults(request):
    if 'image' in request.GET and request.GET["image"]:
        search_term = request.GET.get("image")
        searched_images = Image.search_image(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"images": searched_images})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})
