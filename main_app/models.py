from django.db import models
from django.contrib.auth.models import User

class Plant(models.Model):
  name = models.CharField(max_length=100)
  type = models.CharField(max_length=100)
  location = models.CharField(max_length=100)
  description = models.TextField(max_length=1000)
  culinary_use = models.TextField(max_length=1000)
  medicinal_use = models.TextField(max_length=1000)
  harvest_season = models.CharField(max_length=250)
  cautions = models.TextField(max_length=250)


class Recipe(models.Model):
  name = models.CharField(max_length=100)
  servings = models.IntegerField()
  preptime = models.CharField(max_length=50)
  cooktime = models.CharField(max_length=50)
  ingredients = models.TextField(max_length=250)
  directions = models.TextField(max_length=1000)
  user = models.ForeignKey(User, on_delete=models.CASCADE)
