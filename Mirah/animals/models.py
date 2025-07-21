from django.db import models

class AnimalType(models.Model):
    name = models.CharField(max_length=1024, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

class Breed(models.Model):
    name = models.CharField(max_length=1024)
    animal_type = models.ForeignKey(AnimalType, on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
