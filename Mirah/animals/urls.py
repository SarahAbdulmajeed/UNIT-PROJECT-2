from . import views
from django.urls import path

app_name = "animals"

urlpatterns = [
    path("", views.animals_view, name="animals_view"),
    path("types/", views.all_types_view, name="all_types_view"),
    path("types/add/", views.add_type_view, name="add_type_view"),
    path("types/<int:type_id>/edit/", views.edit_type_view, name="edit_type_view"),
    path("types/<int:type_id>/delete/", views.delete_type_view, name="delete_type_view"),

] 