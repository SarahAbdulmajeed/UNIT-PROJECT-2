from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpRequest, HttpResponse
from .models import AnimalType, Breed, Animal, WeightRecord, IdealWeight, VaccineType, VaccinationRecord
from .forms import AnimalTypeForm, BreedForm, AnimalForm, WeightRecordForm, IdealWeightForm, VaccineTypeForm, VaccinationRecordForm
from .tables import TypeTable, BreedTable ,AnimalTable, WeightRecordTable, IdealWeightTable, VaccineTypeTable, VaccinationRecordTable
from .filters import TypeFilter, BreedFilter, AnimalFilter, IdealWeightFilter, VaccineTypeFilter
from django_tables2 import RequestConfig
from datetime import date
from dateutil.relativedelta import relativedelta



# Create your views here.
def animals_view(request:HttpRequest):
    return render(request,"animals/animals.html")

#=========[ Animal Types ]=========
def all_types_view(request:HttpRequest):
    types = AnimalType.objects.all()
    filter = TypeFilter(request.GET, queryset=types)
    table = TypeTable(filter.qs)
    RequestConfig(request,paginate={"per_page": 10}).configure(table)
    return render(request,"animals/types/all.html",{"table":table, "filter":filter})

def add_type_view(request:HttpRequest):
    if request.method == "POST":
       form = AnimalTypeForm(request.POST)
       if form.is_valid():
           form.save()
           return redirect('animals:all_types_view')
       else:
           print(form.errors)
    else:
        form = AnimalTypeForm()

    return render(request,"animals/types/add.html",{"form":form})

def edit_type_view(request:HttpRequest, type_id: int):
    type = AnimalType.objects.get(id = type_id)
    if request.method == "POST":
        form = AnimalTypeForm(request.POST, instance=type)
        if form.is_valid():
            form.save()
            return redirect("animals:all_types_view")
        else:
            print(form.errors)
    else:
        form = AnimalTypeForm(instance=type)
    return render(request,"animals/types/edit.html", {"form":form, "type":type})

def delete_type_view(request:HttpRequest, type_id: int):
    type = AnimalType.objects.get(pk = type_id)
    type.delete()
    return redirect("animals:all_types_view")


#=========[ Animal Breeds ]=========
def all_breeds_view(request:HttpRequest):
    breeds = Breed.objects.all()
    filter = BreedFilter(request.GET, queryset=breeds)
    table = BreedTable(filter.qs)
    RequestConfig(request,paginate={"per_page": 10}).configure(table)
    return render(request,"animals/breeds/all.html",{"table":table, "filter":filter})

def add_breed_view(request:HttpRequest):
    if request.method == "POST":
        form = BreedForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('animals:all_breeds_view')
        else:
            print(form.errors)
    else:
        form = BreedForm()
    return render(request,"animals/breeds/add.html",{"form":form})

def edit_breed_view(request:HttpRequest, breed_id: int):
    breed = Breed.objects.get(id = breed_id)
    if request.method == "POST":
        form = BreedForm(request.POST, instance=breed)
        if form.is_valid():
            form.save()
            return redirect('animals:all_breeds_view')
        else:
            print(form.errors)
    else:
        form = BreedForm(instance=breed)
    return render(request,"animals/breeds/edit.html", {"form":form, "breed":breed})

def delete_breed_view(request:HttpRequest, breed_id: int):
    breed = Breed.objects.get(pk = breed_id)
    breed.delete()
    return redirect("animals:all_breeds_view")

#=========[ Animal ]=========
def all_animals_view(request:HttpRequest):
    animals = Animal.objects.all()
    filter = AnimalFilter(request.GET, queryset=animals)
    table = AnimalTable(filter.qs)
    RequestConfig(request, paginate={"per_page": 10}).configure(table)
    return render(request, "animals/animal/all_animals.html", {"table": table, "filter":filter})

def add_animal_view(request:HttpRequest):
    if request.method == "POST":
        form = AnimalForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("animals:all_animals_view")
        else:
            print(form.errors)
    else:
        form = AnimalForm()
    return render(request,"animals/animal/add_animal.html",{'form':form})

def load_breed(request:HttpRequest):
    type_id = request.GET.get("animal_type")
    breeds = Breed.objects.filter(animal_type=type_id)
    return render(request, "animals/animal/breed_options.html", {'breeds': breeds})

def edit_animal_view(request:HttpRequest, animal_id: int):
    animal = Animal.objects.get(pk=animal_id) #كلمي الاستاذ عنها get_object_or_404
    if request.method == "POST":
        form = AnimalForm(request.POST, request.FILES, instance=animal)
        if form.is_valid():
            form.save()
            return redirect("animals:detail_animal_view", animal_id=animal_id)
        else:
            print(form.errors)
    else:
        form = AnimalForm(instance=animal)
    return render(request,"animals/animal/edit_animal.html", {"form":form, "animal":animal})

def delete_animal_view(request:HttpRequest, animal_id: int):
    animal = Animal.objects.get(pk = animal_id)
    animal.delete()
    return redirect("animals:all_animals_view")

def detail_animal_view(request:HttpRequest, animal_id: int):
    animal = Animal.objects.get(pk=animal_id)
    
    #calculate age 
    age_calc = relativedelta(date.today() , animal.birth_date)
    age_format = {"years": age_calc.years, "months": age_calc.months ,"days": age_calc.days}
    

    #fetch weight records 
    weight_record_table = WeightRecordTable(WeightRecord.objects.filter(animal=animal))
    #fetch vaccination records
    vaccination_record_table = VaccinationRecordTable(VaccinationRecord.objects.filter(animal=animal))
    
    #last weight 
    last_weight_obj = WeightRecord.objects.filter(animal=animal).order_by('-date').first()
    last_weight_record = last_weight_obj.weight_kg if last_weight_obj else None #prevent no weight records error 

    #age in days
    age_in_days = (date.today() - animal.birth_date).days

    #check the ideal weight
    weight_status = None
    if last_weight_record is not None:
        ideal = IdealWeight.objects.filter( breed=animal.breed, gender=animal.gender, age_from_days__lte=age_in_days, age_to_days__gte=age_in_days).first()
        if ideal:
            if last_weight_record < ideal.ideal_min_weight:
                weight_status = "underweight"
            elif last_weight_record > ideal.ideal_max_weight:
                weight_status = "overweight"
            else:
                weight_status = "ideal"
    else:
        print("no weight records")

    #check the vaccination records 
    all_required_vaccination = VaccineType.objects.filter(breed=animal.breed, gender=animal.gender)
    current_vaccinations = VaccinationRecord.objects.filter(animal=animal)
    given_vaccine_ids = current_vaccinations.values_list('vaccine_type__id', flat=True)
    missing_vaccinations = all_required_vaccination.exclude(id__in=given_vaccine_ids)

    if not all_required_vaccination.exists():
        vaccination_status = "no_required"
    elif missing_vaccinations.exists():
        vaccination_status = "incomplete"
    else:
        vaccination_status = "complete"


    RequestConfig(request,paginate={"per_page": 3}).configure(weight_record_table)
    RequestConfig(request,paginate={"per_page": 3}).configure(vaccination_record_table)

    return render(request,"animals/animal/detail_animal.html", {"animal":animal, "weightRecordTable":weight_record_table, "vaccinationRecordTable":vaccination_record_table, "age_format":age_format, "last_weight_record":last_weight_record, "age_in_days":age_in_days, "weight_status":weight_status, "vaccination_status": vaccination_status, "missing_vaccinations": missing_vaccinations,})

#=========[ Weight Record ]=========
def add_weight_record_view(request:HttpRequest, animal_id:int):
    animal = get_object_or_404(Animal, id=animal_id)
    if request.method == "POST":
        form = WeightRecordForm(request.POST, request.FILES)
        if form.is_valid():
            weight_record = form.save(commit=False)
            weight_record.animal = animal
            weight_record.save()
            return redirect("animals:detail_animal_view", animal_id=animal.pk)
    else:
        form = WeightRecordForm()

    return render(request, "animals/weight_record/add.html", {"form": form, "animal": animal})

def delete_weight_record_view(request:HttpRequest, weight_id:int):
    weight_record = get_object_or_404(WeightRecord, id=weight_id)
    animal_id = weight_record.animal.id
    weight_record.delete()
    return redirect("animals:detail_animal_view", animal_id=animal_id)

#=========[ Ideal Weight ]=========
def all_ideal_weight_view(request:HttpRequest):
    ideal_weight = IdealWeight.objects.all()
    filter = IdealWeightFilter(request.GET, queryset=ideal_weight)
    table = IdealWeightTable(filter.qs)
    RequestConfig(request).configure(table)
    return render(request, "animals/ideal_weight/all.html",{"table":table, "filter":filter})

def add_ideal_weight_view(request:HttpRequest):
    if request.method == "POST":
        form = IdealWeightForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("animals:all_ideal_weight_view")
        else:
            print(form.errors)
    else:
        form = IdealWeightForm()
    return render(request, "animals/ideal_weight/add.html",{"form":form})

def edit_ideal_weight_view(request:HttpRequest, ideal_weight_id:int):
    ideal_weight_range = IdealWeight.objects.get(pk=ideal_weight_id)
    if request.method == "POST":
        form = IdealWeightForm(request.POST, instance=ideal_weight_range)
        if form.is_valid():
            form.save()
            return redirect('animals:all_ideal_weight_view')
        else:
            print(form.errors)
    else:
        form = IdealWeightForm(instance=ideal_weight_range)
    return render(request,"animals/ideal_weight/edit.html", {"form":form, "ideal_weight_range":ideal_weight_range})

def delete_ideal_weight_view(request:HttpRequest, ideal_weight_id:int):
    ideal_weight = IdealWeight.objects.get(pk=ideal_weight_id)
    ideal_weight.delete()
    return redirect("animals:all_ideal_weight_view")

#=========[ Vaccine Types ]=========
def all_vaccine_types_view(request:HttpRequest):
    types = VaccineType.objects.all()
    filter = VaccineTypeFilter(request.GET, queryset=types)
    table = VaccineTypeTable(filter.qs)
    return render(request,"animals/vaccine_types/all.html",{"table":table, "filter":filter})

def add_vaccine_type_view(request:HttpRequest):
    if request.method == "POST":
       form = VaccineTypeForm(request.POST)
       if form.is_valid():
           form.save()
           return redirect('animals:all_vaccine_types_view')
       else:
           print(form.errors)
    else:
        form = VaccineTypeForm()
    return render(request,"animals/vaccine_types/add.html",{"form":form})

def edit_vaccine_type_view(request:HttpRequest, vtype_id:int):
    type = VaccineType.objects.get(pk=vtype_id)
    if request.method == "POST":
        form = VaccineTypeForm(request.POST, instance=type)
        if form.is_valid():
            form.save()
            return redirect('animals:all_vaccine_types_view')
        else:
            print(form.errors)
    else:
        form = VaccineTypeForm(instance=type)
    return render(request,"animals/vaccine_types/edit.html",{"form":form, "type":type})

def delete_vaccine_type_view(request:HttpRequest, vtype_id:int):
    vaccine_type = VaccineType.objects.get(pk = vtype_id)
    vaccine_type.delete()
    return redirect("animals:all_vaccine_types_view")

#=========[ Vaccine Records ]=========
def add_vaccine_record_view(request:HttpRequest, animal_id:int):
    animal = get_object_or_404(Animal, id=animal_id)
    if request.method == "POST":
        form = VaccinationRecordForm(request.POST, request.FILES)
        if form.is_valid():
            vaccination_record = form.save(commit=False)
            vaccination_record.animal = animal
            vaccination_record.save()
            return redirect("animals:detail_animal_view", animal_id=animal.pk)
    else:
        form = VaccinationRecordForm()

    return render(request, "animals/vaccination_record/add.html", {"form": form, "animal": animal})

def delete_vaccine_record_view(request:HttpRequest, animal_id:int):
    vaccination_record = get_object_or_404(VaccinationRecord, id=animal_id)
    animal_id = vaccination_record.animal.id
    vaccination_record.delete()
    return redirect("animals:detail_animal_view", animal_id=animal_id)
