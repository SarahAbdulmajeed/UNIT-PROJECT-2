from django import forms
from .models import AnimalType, Breed

class AnimalTypeForm(forms.ModelForm):
    class Meta:
        model = AnimalType
        fields = "__all__"


class BreedForm(forms.ModelForm):
    class Meta:
        model = Breed
        fields = "__all__"