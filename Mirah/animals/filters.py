import django_filters
from .models import AnimalType, Breed, Animal, IdealWeight

class TypeFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains', label='Search by Name')
    class Meta:
        model = AnimalType 
        fields = ['name',] 

class BreedFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains', label='Search by Name')
    class Meta:
        model = Breed 
        fields = ['name', 'animal_type'] 

class AnimalFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains', label='Search by Name')
    class Meta:
        model = Animal 
        fields = ['name', 'animal_type', 'breed', 'status'] 

class IdealWeightFilter(django_filters.FilterSet):
    class Meta:
        model = IdealWeight 
        fields = ['breed', 'gender', 'age_from_days', 'age_to_days' ,'ideal_min_weight', 'ideal_max_weight'] 
