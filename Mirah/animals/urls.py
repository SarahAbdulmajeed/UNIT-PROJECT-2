from . import views
from django.urls import path

app_name = "animals"

urlpatterns = [
    path("", views.animals_view, name="animals_view"),
    #Type
    path("types/all/", views.all_types_view, name="all_types_view"),
    path("types/add/", views.add_type_view, name="add_type_view"),
    path("types/<int:type_id>/edit/", views.edit_type_view, name="edit_type_view"),
    path("types/<int:type_id>/delete/", views.delete_type_view, name="delete_type_view"),
    #Breed
    path("breeds/all/", views.all_breeds_view, name="all_breeds_view"),
    path("breeds/add/", views.add_breed_view, name="add_breed_view"),
    path("breeds/<int:breed_id>/edit/", views.edit_breed_view, name="edit_breed_view"),
    path("breeds/<int:breed_id>/delete/", views.delete_breed_view, name="delete_breed_view"),
    #Animal
    path("all/", views.all_animals_view, name="all_animals_view"),
    path("add/", views.add_animal_view, name="add_animal_view"),
    path("load_breed/", views.load_breed, name="load_breed"),
    path("<int:animal_id>/edit/", views.edit_animal_view, name="edit_animal_view"),
    path("<int:animal_id>/delete/", views.delete_animal_view, name="delete_animal_view"),
    path("<int:animal_id>/details/", views.detail_animal_view, name="detail_animal_view"),
    #Weight Record
    path("weights/<int:animal_id>/add/", views.add_weight_record_view, name="add_weight_record_view"),
    path("weights/delete/<int:weight_id>", views.delete_weight_record_view, name="delete_weight_record_view"),
] 