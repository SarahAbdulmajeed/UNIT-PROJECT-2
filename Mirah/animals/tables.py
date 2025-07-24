import django_tables2 as tables
from .models import AnimalType, Breed, Animal, WeightRecord, IdealWeight

class TypeTable(tables.Table):
    actions = tables.TemplateColumn(template_name='animals/actions/TypeTable_actions.html', orderable=False)
    class Meta:
        model = AnimalType
        template_name = "django_tables2/table.html"
        fields = ("name",)

class BreedTable(tables.Table):
    actions = tables.TemplateColumn(template_name='animals/actions/BreedTable_actions.html', orderable=False)
    class Meta:
        model = Breed
        template_name = "django_tables2/table.html"
        fields = ("name",'animal_type')

class AnimalTable(tables.Table):
    actions = tables.TemplateColumn(template_name='animals/actions/AnimalTable_actions.html', orderable=False)
    class Meta:
        model = Animal
        template_name = "django_tables2/table.html"
        fields = ("name", "animal_type", "breed", "status", "birth_date")

class WeightRecordTable(tables.Table):
    actions = tables.TemplateColumn(template_name='animals/actions/WeightRecordTable_actions.html', orderable=False)
    class Meta:
        model = WeightRecord
        template_name = "django_tables2/table.html"
        fields = ("weight_kg","date","notes","image")


class IdealWeightTable(tables.Table):
    actions = tables.TemplateColumn(template_name='animals/actions/IdealWeightTable_actions.html', orderable=False)
    class Meta:
        model = IdealWeight
        template_name = "django_tables2/table.html"
        fields = ("breed","age_from_days","age_to_days","ideal_min_weight","ideal_max_weight","gender")
