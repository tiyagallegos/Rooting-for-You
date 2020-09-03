from django.shortcuts import render
from .models import Plant, Pot
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .forms import FeedingForm, WateringForm
from django.shortcuts import render, redirect

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def plants_index(request):
    plants = Plant.objects.all()
    return render(request, 'plants/index.html', {'plants': plants})

def plants_detail(request, plant_id):
    plant = Plant.objects.get(id=plant_id)
    pots_plant_doesnt_have = Pot.objects.exclude(id__in = plant.pots.all().values_list('id'))
    print(pots_plant_doesnt_have)
    feeding_form = FeedingForm()
    watering_form = WateringForm()
    return render(request, 'plants/detail.html', {'plant': plant, 'feeding_form': feeding_form, 'watering_form': watering_form, 'pots': pots_plant_doesnt_have})

def add_feeding(request, plant_id):
    form = FeedingForm(request.POST)
    if form.is_valid(): 
        new_feeding = form.save(commit=False)
        new_feeding.plant_id = plant_id
        new_feeding.save()
    return redirect('detail', plant_id=plant_id)


def add_watering(request, plant_id):
    form = WateringForm(request.POST)
    if form.is_valid(): 
        new_watering = form.save(commit=False)
        new_watering.plant_id = plant_id
        new_watering.save()
    return redirect('detail', plant_id=plant_id)

def assoc_pot(request, plant_id, pot_id):
    Plant.objects.get(id=plant_id).pots.add(pot_id)
    return redirect('detail', plant_id=plant_id)

def unassoc_pot(request, plant_id, pot_id):
    Plant.objects.get(id=plant_id).pots.remove(pot_id)
    return redirect('detail', plant_id=plant_id)

class PlantCreate(CreateView):
    model = Plant
    fields = '__all__'
    success_url = '/plants/'

class PlantUpdate(UpdateView):
    model = Plant
    fields = '__all__'
    success_url = '/plants/'
    
class PlantDelete(DeleteView):
    model = Plant
    success_url = '/plants/'

class PotList(ListView):
    model = Pot

class PotDetailView(DetailView):
    model = Pot

class PotCreate(CreateView):
    model = Pot
    fields = '__all__'
    success_url = '/pots/'

class PotUpdate(UpdateView):
    model = Pot
    fields = ['name', 'location', 'description', 'color']
    success_url = '/pots/'

class PotDelete(DeleteView):
    model = Pot
    success_url = '/pots/'