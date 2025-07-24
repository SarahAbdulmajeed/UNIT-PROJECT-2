from django import forms
from .models import AnimalType, Breed, Animal, WeightRecord, IdealWeight
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

        # animal type & breed
        if "animal_type" in self.data:
            try:
                type_id = int(self.data.get("animal_type"))
                self.fields["breed"].queryset = Breed.objects.filter(animal_type=type_id)
            except (ValueError, TypeError):
                self.fields["breed"].queryset = Breed.objects.none()
        elif self.instance.pk: #important for edit 
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

class IdealWeightForm(forms.ModelForm):
    class Meta:
        model = IdealWeight
        fields = ["breed","age_from_days","age_to_days","ideal_min_weight","ideal_max_weight","gender"]

    #min weight not negative
    def clean_ideal_min_weight(self):
        value = self.cleaned_data.get('ideal_min_weight')
        if value is not None and value <= 0:
            raise forms.ValidationError("Minimum weight must be greater than zero.")
        return value
    
    #max not negative
    def clean_ideal_max_weight(self):
        value = self.cleaned_data.get('ideal_max_weight')
        if value is not None and value <= 0:
            raise forms.ValidationError("Maximum weight must be greater than zero.")
        return value
    
    # min days not negative
    def clean_age_from_days(self):
        value = self.cleaned_data.get('age_from_days')
        if value is not None and value < 0:
            raise forms.ValidationError("Minimum age (in days) must be zero or greater.")
        return value
    
    #min age < max age
    def clean_age_range(self):
        cleaned_data = super().clean()
        min_days = cleaned_data.get('age_from_days')
        max_days = cleaned_data.get('age_to_days')

        if min_days is not None and max_days is not None:
            if min_days >= max_days:
                raise forms.ValidationError("Maximum age must be greater than minimum age.")

    #min weight < max weight
    def clean_weight_range(self):
        
        cleaned_data = super().clean()
        ideal_min_weight = cleaned_data.get('ideal_min_weight')
        ideal_max_weight = cleaned_data.get('ideal_max_weight')

        if ideal_min_weight is not None and ideal_max_weight is not None:
            if ideal_min_weight >= ideal_max_weight:
                raise forms.ValidationError("Maximum weight must be greater than minimum weight.")

    #not overlapping      
    def clean_overlapping(self):
        cleaned_data = super().clean()
        min_days = cleaned_data.get('min_days')
        max_days = cleaned_data.get('max_days')
        breed = cleaned_data.get('breed')
        gender = cleaned_data.get('gender')

        if min_days is not None and max_days is not None and breed and gender:
            overlapping = IdealWeight.objects.filter(
                breed=breed,
                gender=gender
            ).exclude(pk=self.instance.pk).filter(
                min_days__lte=max_days,
                max_days__gte=min_days
            )

            if overlapping.exists():
                raise forms.ValidationError("There is already an overlapping age range for this breed and gender.")