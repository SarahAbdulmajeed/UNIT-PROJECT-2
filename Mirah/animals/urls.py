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


] 