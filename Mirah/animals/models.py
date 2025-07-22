from django.db import models

class AnimalType(models.Model):
    name = models.CharField(max_length=1024, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name

class Breed(models.Model):
    name = models.CharField(max_length=1024)
    animal_type = models.ForeignKey(AnimalType, on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name

class Animal(models.Model):
    class GenderChoices(models.TextChoices):
        MALE = "M", "Male"
        FEMALE = "F", "Female"

    class StatusChoices(models.TextChoices):
        ACTIVE = "active", "Active"
        SOLD = "sold", "Sold"
        DEAD = "dead", "Dead"

    name = models.CharField(max_length=1024)
    animal_type = models.ForeignKey('AnimalType', on_delete=models.PROTECT)
    breed = models.ForeignKey('Breed', on_delete=models.PROTECT)
    gender = models.CharField(max_length=1, choices=GenderChoices.choices)
    birth_date = models.DateField()
    notes = models.TextField(blank=True)
    image = models.ImageField(upload_to='images/', default="images/default.png")
    status = models.CharField(max_length=20, choices=StatusChoices.choices, default=StatusChoices.ACTIVE)
    created_at = models.DateTimeField(auto_now_add=True)
