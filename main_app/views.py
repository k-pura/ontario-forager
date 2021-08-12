from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Plant
from .models import Recipe
from django.contrib.auth import login
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

def login_user(request):
    return render(request, 'registration/login.html')

def recipe_new(request):
    return render(request, 'addrecipe/new.html')

def recipe_create(request):
    recipe = Recipe.objects.create(
        name = request.POST['name'],
        servings =request.POST['servings'],
        preptime = request.POST['preptime'],
        cooktime = request.POST['cooktime'],
        ingredients = request.POST['ingredients'],
        directions = request.POST['directions'],
    )
    return redirect(f'/recipes/{recipe.id}')

def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        print(form.errors)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
        else:
            error_message = 'Invalid sign up - try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)