from django.shortcuts import render
from django.http import HttpResponse
from .models import Plant
# Define the home view

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def index(request):
    plants =Plant.objects.all()
    return render(request, 'index.html', {'plants': plants})

def plant(request, plant_id):
    plant = Plant.objects.get(id= plant_id)
    return render(request, 'plant.html', {'plant': plant})