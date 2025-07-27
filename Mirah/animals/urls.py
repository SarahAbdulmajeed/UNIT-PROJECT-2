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
    #Ideal Weight 
    path("weights/ideal/all/", views.all_ideal_weight_view, name="all_ideal_weight_view"),
    path("weights/ideal/add/", views.add_ideal_weight_view, name="add_ideal_weight_view"),
    path("weights/ideal/<int:ideal_weight_id>/edit/", views.edit_ideal_weight_view, name="edit_ideal_weight_view"),
    path("weights/ideal/<int:ideal_weight_id>/delete/", views.delete_ideal_weight_view, name="delete_ideal_weight_view"),
    #Vaccine Types
    path("vaccine/type/all/", views.all_vaccine_types_view, name="all_vaccine_types_view"),
    path("vaccine/type/add/", views.add_vaccine_type_view, name="add_vaccine_type_view"),
    path("vaccine/type/<int:vtype_id>/edit/", views.edit_vaccine_type_view, name="edit_vaccine_type_view"),
    path("vaccine/type/<int:vtype_id>/delete/", views.delete_vaccine_type_view, name="delete_vaccine_type_view"),
    #Vaccine Record
    path("vaccine/<int:animal_id>/add/", views.add_vaccine_record_view, name="add_vaccine_record_view"),
    path("vaccine/delete/<int:animal_id>", views.delete_vaccine_record_view, name="delete_vaccine_record_view"),

] 