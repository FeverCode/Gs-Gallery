from django.shortcuts import render
from .models import Image

# Create your views here.
def index(request):
    
    # imports photos and save it in database
    photo = Image.objects.all()
    # adding context
    ctx = {'images': photo}
    return render(request, 'index.html', ctx)

def showlist(request):
    return render(request, 'showlist.html')
