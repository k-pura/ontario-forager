from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('index/', views.index, name='index'),
    path('plant/<str:plant_type>/', views.sort, name= 'sort'),
    path('recipes/', views.recipes, name='recipes'),
    path('login/', views.login_user, name='login'),
    path('accounts/signup/', views.signup, name='signup'),
    path('addrecipe/new', views.recipe_new, name='newrecipe'),
    path('recipe_add', views.recipe_create, name='create'),
]