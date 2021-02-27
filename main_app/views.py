from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Dog
from .forms import FeedingForm

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
    # create instance of the feedingform
    feeding_form = FeedingForm()
    return render(request,
        'dogs/detail.html',
        { 'dog': dog, 'feeding_form': feeding_form }
    )
    # return a call to render the detail.html and context dict
    return render(request, 'dogs/detail.html', {'dog': dog})

class DogCreate(CreateView):
    model = Dog
    fields = '__all__'
    # success_url = '/dogs/'

class DogUpdate(UpdateView):
    model = Dog
    fields = ['breed', 'description', 'age']

class DogDelete(DeleteView):
    model = Dog
    success_url = '/dogs/'