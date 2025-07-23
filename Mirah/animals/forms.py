from django import forms
from .models import AnimalType, Breed, Animal, WeightRecord
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Row, Column
from django.urls import reverse_lazy
import datetime


class AnimalTypeForm(forms.ModelForm):
    class Meta:
        model = AnimalType
        fields = "__all__"


class BreedForm(forms.ModelForm):
    class Meta:
        model = Breed
        fields = "__all__"

#https://www.youtube.com/watch?v=UCl5O-XVChk&ab_channel=PrettyPrinted
class AnimalForm(forms.ModelForm):
    class Meta:
        model = Animal
        fields = [
            'name',
            'animal_type',
            'breed',
            'gender',
            'birth_date',
            'notes',
            'image',
            'status'
        ]
        widgets = {
            'birth_date': forms.DateInput(attrs={'type': 'date'}),
            'animal_type': forms.Select(attrs={
                'hx-get': reverse_lazy('animals:load_breed'),
                'hx-target': '#id_breed',
            })
        }


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if "animal_type" in self.data:
            try:
                type_id = int(self.data.get("animal_type"))
                self.fields["breed"].queryset = Breed.objects.filter(animal_type=type_id)
            except (ValueError, TypeError):
                self.fields["breed"].queryset = Breed.objects.none()
        elif self.instance.pk:
            self.fields["breed"].queryset = Breed.objects.filter(animal_type=self.instance.animal_type)
        else:
            self.fields["breed"].queryset = Breed.objects.none()

class WeightRecordForm(forms.ModelForm):
    class Meta:
        model = WeightRecord
        fields = [
            'weight_kg',
            'date',
            'image',
            'notes',
            ]
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }

    def clean_date(self):
        date = self.cleaned_data["date"]
        if date > datetime.date.today():
            raise forms.ValidationError("Weight date cannot be in the future.")
        return date

    def clean_weight_kg(self):
        weight = self.cleaned_data["weight_kg"]
        if weight <= 0:
            raise forms.ValidationError("Weight must be greater than zero.")
        return weight


