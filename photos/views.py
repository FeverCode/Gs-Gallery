from django.shortcuts import render
from .models import Image

# Create your views here.
def index(request):
    photo = Image.objects.all()
    
    ctx = {'images': photo                                                                                                                                          }
    return render(request, 'index.html', ctx)    
