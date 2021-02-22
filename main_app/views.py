from django.shortcuts import render

from django.http import HttpResponse

class Dog:
    def __init__(self, name, breed, description, age):
        self.name = name
        self.breed = breed
        self.description = description
        self.age = age

dogs = [
    Dog('Otto', 'Bichon', 'frisky little marshmallow', 7),
    Dog('Zeus', 'Puggle', 'good boy', 10),
    Dog('Martha', 'Yellow Lab', 'the most loyal', 5),
]

# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def dogs_index(request):
    return render(request, 'dogs/index.html', {'dogs': dogs})