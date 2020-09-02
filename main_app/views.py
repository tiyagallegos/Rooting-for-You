from django.shortcuts import render
from .models import Plant, Pot
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .forms import FeedingForm, WateringForm

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
    feeding_form = FeedingForm()
    watering_form = WateringForm()
    return render(request, 'plants/detail.html', {'plant': plant, 'feeding_form': feeding_form, 'watering_form': watering_form})

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