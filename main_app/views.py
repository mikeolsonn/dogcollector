from django.shortcuts import render
from .models import Dog

# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def dogs_index(request):
    dogs = Dog.objects.all()
    return render(request, 'dogs/index.html', {'dogs': dogs})

def dogs_detail(request, dog_id):
    # query the database for a single cat obj
    dog = Dog.objects.get(id=dog_id)
    # return a call to render the detail.html and context dict
    return render(request, 'dogs/detail.html', {'dog': dog})
    