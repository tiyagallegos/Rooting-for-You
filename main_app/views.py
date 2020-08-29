from django.shortcuts import render
from .models import Plant, Pot
from django.views.generic.edit import CreateView, UpdateView, DeleteView

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
    return render(request, 'plants/detail.html', {'plant': plant})

class PlantCreate(CreateView):
    model = Plant
    fields = '__all__'
    success_url = '/plants/'

class PlantUpdate(UpdateView):
    model = Plant
    fields = '__all__'

class PlantDelete(DeleteView):
    model = Plant
    success_url = '/plants/'

def pots_index(request):
    pots = Pot.objects.all()
    return render(request, 'pots/pot_index.html', {'pots': pots})

def pots_detail(request, pot_id):
    pot = Pot.objects.get(id=pot_id)
    return render(request, 'pots/pot_detail.html', {'pot': pot})

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