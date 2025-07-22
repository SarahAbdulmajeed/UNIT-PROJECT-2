from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .models import AnimalType, Breed, Animal
from .forms import AnimalTypeForm, BreedForm, AnimalForm
from django_tables2 import RequestConfig
from .tables import TypeTable, BreedTable ,AnimalTable


# Create your views here.
def animals_view(request:HttpRequest):
    return render(request,"animals/animals.html")

#=========[ Animal Types ]=========
def all_types_view(request:HttpRequest):
    types = AnimalType.objects.all()
    table = TypeTable(types)
    RequestConfig(request).configure(table)
    return render(request,"animals/types/all.html",{"table":table})

def add_type_view(request:HttpRequest):
    type_form = AnimalTypeForm()
    if request.method == "POST":
       type_form = AnimalTypeForm(request.POST)
       if type_form.is_valid():
           type_form.save()
           return redirect('animals:all_types_view')
       else:
           print("not valid form")
    return render(request,"animals/types/add.html")

def edit_type_view(request:HttpRequest, type_id: int):
    type = AnimalType.objects.get(id = type_id)
    type_form = AnimalTypeForm(instance=type)
    if request.method == "POST":
        type_form = AnimalTypeForm(request.POST, instance=type)
        if type_form.is_valid():
            type_form.save()
            return redirect("animals:all_types_view")
        else:
           print("not valid form")
    return render(request,"animals/types/edit.html", {"type":type})

def delete_type_view(request:HttpRequest, type_id: int):
    type = AnimalType.objects.get(pk = type_id)
    type.delete()
    return redirect("animals:all_types_view")


#=========[ Animal Breeds ]=========
def all_breeds_view(request:HttpRequest):
    breeds = Breed.objects.all()
    table = BreedTable(breeds)
    RequestConfig(request).configure(table)
    return render(request,"animals/breeds/all.html",{"table":table})

def add_breed_view(request:HttpRequest):
    types = AnimalType.objects.all()
    breed_form = BreedForm()
    if request.method == "POST":
        breed_form = BreedForm(request.POST)
        if breed_form.is_valid():
            breed_form.save()
            return redirect('animals:all_breeds_view')
        else:
            print("invalid form")
    return render(request,"animals/breeds/add.html",{"types":types})

def edit_breed_view(request:HttpRequest, breed_id: int):
    types = AnimalType.objects.all()
    breed = Breed.objects.get(id = breed_id)
    breed_form = BreedForm(instance=breed)
    if request.method == "POST":
        breed_form = BreedForm(request.POST, instance=breed)
        if breed_form.is_valid():
            breed_form.save()
            return redirect('animals:all_breeds_view')
        else:
            print("invalid form")
    return render(request,"animals/breeds/edit.html", {"breed":breed, "types":types})

def delete_breed_view(request:HttpRequest, breed_id: int):
    breed = Breed.objects.get(pk = breed_id)
    breed.delete()
    return redirect("animals:all_breeds_view")


#=========[ Animal ]=========
def all_animals_view(request):
    animals = Animal.objects.all()
    table = AnimalTable(animals)
    RequestConfig(request).configure(table)
    return render(request, "animals/animal/all_animals.html", {"table": table})

def add_animal_view(request:HttpRequest):
    if request.method == "POST":
        form = AnimalForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            print(form.errors)
    else:
        form = AnimalForm()
    return render(request,"animals/animal/add_animal.html",{'form':form})

def load_breed(request:HttpRequest):
    type_id = request.GET.get("animal_type")
    breeds = Breed.objects.filter(animal_type=type_id)
    return render(request, "animals/animal/breed_options.html", {'breeds': breeds})

def edit_animal_view(request:HttpRequest, animal_id: int):
    animal = Animal.objects.get(pk=animal_id)
    if request.method == "POST":
        form = AnimalForm(request.POST, request.FILES, instance=animal)
        if form.is_valid():
            form.save()
            return redirect("animals:all_animals_view")  # غيريها للمكان اللي ترجعين له
        else:
            print(form.errors)
    else:
        form = AnimalForm(instance=animal)
    return render(request,"animals/animal/edit_animal.html", {"form":form, "animal":animal})

def delete_animal_view(request:HttpRequest, animal_id: int):
    animal = Animal.objects.get(pk = animal_id)
    animal.delete()
    return redirect("animals:all_animals_view")

