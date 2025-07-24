from django.db import models

class AnimalType(models.Model):
    name = models.CharField(max_length=1024, unique=True) #unique so the name cannot be duplicate
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name

class Breed(models.Model):
    name = models.CharField(max_length=1024)
    animal_type = models.ForeignKey(AnimalType, on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name
    
class WeightRecord(models.Model):
    animal = models.ForeignKey("Animal", on_delete=models.CASCADE)
    weight_kg = models.DecimalField(max_digits=5, decimal_places=2)
    date = models.DateField()
    image = models.ImageField(upload_to="weights/", blank=True, null=True)
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

class IdealWeight(models.Model):
    class GenderChoices(models.TextChoices):
        MALE = "M", "Male"
        FEMALE = "F", "Female"

    breed = models.ForeignKey('Breed', on_delete=models.PROTECT)
    age_from_days = models.PositiveIntegerField()
    age_to_days = models.PositiveIntegerField()
    ideal_min_weight = models.DecimalField(max_digits=5, decimal_places=2)
    ideal_max_weight = models.DecimalField(max_digits=5, decimal_places=2)
    gender = models.CharField(max_length=1, choices=GenderChoices.choices)


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
