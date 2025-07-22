import django_tables2 as tables
from .models import AnimalType, Breed, Animal


class TypeTable(tables.Table):
    actions = tables.TemplateColumn(template_name='animals/actions/TypeTable_actions.html', orderable=False)
    class Meta:
        model = AnimalType
        template_name = "django_tables2/table.html"
        fields = ("name",'created_at')

class BreedTable(tables.Table):
    actions = tables.TemplateColumn(template_name='animals/actions/BreedTable_actions.html', orderable=False)
    class Meta:
        model = Breed
        template_name = "django_tables2/table.html"
        fields = ("name",'animal_type','created_at')

class AnimalTable(tables.Table):
    actions = tables.TemplateColumn(template_name='animals/actions/AnimalTable_actions.html', orderable=False)
    class Meta:
        model = Animal
        template_name = "django_tables2/table.html"
        fields = ("name", "animal_type", "breed", "status", "birth_date")
