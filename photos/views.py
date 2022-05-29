from django.views.generic import TemplateView, ListView
from django.shortcuts import render

from photos.models import Category, Image

# Create your views here.
def index(request):
    
    # imports photos and save it in database
    photo = Image.objects.all()
    # adding context
    ctx = {'images': photo}
    return render(request, 'index.html', ctx)

def SearchResults(request):
    if 'image' in request.GET and request.GET["image"]:
        search_term = request.GET.get("image")
        searched_images = Image.search_image(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"images": searched_images})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})
