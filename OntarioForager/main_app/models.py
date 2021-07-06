from django.db import models

class Plant(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    culinary_use = models.TextField(max_length=250)
    medicinal_use = models.TextField(max_length=250)
    harvest_season = models.CharField(max_length=250)
    cautions = models.TextField(max_length=250)
