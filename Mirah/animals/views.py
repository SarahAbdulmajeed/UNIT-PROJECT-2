from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .models import AnimalType, Breed
from .forms import AnimalTypeForm, BreedForm

# Create your views here.
def animals_view(request:HttpRequest):
    return render(request,"animals/animals.html")


#=========[ Animal Types ]=========
def all_types_view(request:HttpRequest):
    types = AnimalType.objects.all()
    return render(request,"animals/types/all.html",{"types":types})

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
    return render(request,"animals/breeds/all.html",{"breeds":breeds})

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
