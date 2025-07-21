from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

# Create your views here.
def animals_view(request:HttpRequest):
    return render(request,"animals/animals.html")


#=========[ Animals Type ]=========
def all_types_view(request:HttpRequest):
    return render(request,"animals/types/all.html")

def add_type_view(request:HttpRequest):
    return render(request,"animals/types/add.html")

def edit_type_view(request:HttpRequest, type_id: int):
    return render(request,"animals/types/edit.html")

def delete_type_view(request:HttpRequest, type_id: int):
    return render(request,"animals/types/delete.html")
