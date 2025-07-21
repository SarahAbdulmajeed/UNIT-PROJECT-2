from django import forms
from .models import AnimalType

class AnimalTypeForm(forms.ModelForm):
    class Meta:
        model = AnimalType
        fields = "__all__"