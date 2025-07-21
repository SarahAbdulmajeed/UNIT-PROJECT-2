from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .models import AnimalType
from .forms import AnimalTypeForm

# Create your views here.
def animals_view(request:HttpRequest):
    return render(request,"animals/animals.html")


#=========[ Animals Type ]=========
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
