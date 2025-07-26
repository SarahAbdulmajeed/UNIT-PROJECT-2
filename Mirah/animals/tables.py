import django_tables2 as tables
from .models import AnimalType, Breed, Animal, WeightRecord, IdealWeight

class TypeTable(tables.Table):
    actions = tables.TemplateColumn(template_name='animals/actions/TypesTable_actions.html', orderable=False)
    class Meta:
        model = AnimalType
        template_name = "django_tables2/table.html"
        fields = ("name",)
        attrs = {"class": "custom-django-table"}


class BreedTable(tables.Table):
    actions = tables.TemplateColumn(template_name='animals/actions/BreedsTable_actions.html', orderable=False)
    class Meta:
        model = Breed
        template_name = "django_tables2/table.html"
        fields = ("name",'animal_type')
        attrs = {"class": "custom-django-table"}

class AnimalTable(tables.Table):
    actions = tables.TemplateColumn(template_name='animals/actions/AnimalsTable_actions.html', orderable=False)
    class Meta:
        model = Animal
        template_name = "django_tables2/table.html"
        fields = ("name", "animal_type", "breed", "status", "birth_date")
        attrs = {"class": "custom-django-table"}

class WeightRecordTable(tables.Table):
    actions = tables.TemplateColumn(template_name='animals/actions/WeightRecordsTable_actions.html', orderable=False)
    class Meta:
        model = WeightRecord
        template_name = "django_tables2/table.html"
        fields = ("weight_kg","date","notes","image")
        attrs = {"class": "custom-django-table"}

class IdealWeightTable(tables.Table):
    actions = tables.TemplateColumn(template_name='animals/actions/IdealWeightsTable_actions.html', orderable=False)
    class Meta:
        model = IdealWeight
        template_name = "django_tables2/table.html"
        fields = ("breed","age_from_days","age_to_days","ideal_min_weight","ideal_max_weight","gender")
        attrs = {"class": "custom-django-table"}
