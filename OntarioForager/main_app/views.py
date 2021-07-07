from django.shortcuts import render
from django.http import HttpResponse
from .models import Plant
from .models import Recipe
# Define the home view

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def index(request):
    plants =Plant.objects.all()
    return render(request, 'index.html', {'plants': plants})

def sort(request, plant_type):
    types = Plant.objects.filter(type= plant_type)
    return render(request, 'sort.html', {'plants': types, 'title': plant_type})

def recipes(request):
    recipes = Recipe.objects.all()
    return render(request, 'recipes.html', {'recipes': recipes})