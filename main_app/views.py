from django.shortcuts import render
from .models import Plant, Pot, Photo
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .forms import FeedingForm, WateringForm
from django.shortcuts import render, redirect
import uuid
import boto3
from botocore.exceptions import ClientError
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

S3_BASE_URL = "https://rootingforyou.s3.amazonaws.com/"
BUCKET = "rootingforyou"

def signup(request):
    error_message = ''
    if request.method == 'POST':
        #creae a user form object that includes data from the browser
        form = UserCreationForm(request.POST)
        if form.is_valid():
            #adding user to db
            user = form.save()
            login(request, user)
            return redirect('index')
        else: 
            error_message = 'Invalid sign up, try again!'
            #either bad POT request or a GET reqeust so just render the empty form
    form = UserCreationForm()
    context = { 'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)

@login_required
def add_photo(request, plant_id):
    photo_file = request.FILES.get('photo-file', None)
    if photo_file: 
        s3 = boto3.client('s3')
        key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
        try: 
            s3.upload_fileobj(photo_file, BUCKET, key)
            url = f"{S3_BASE_URL}{key}"
            photo = Photo(url=url, plant_id=plant_id)
            photo.save()
        except ClientError as e:
            print(e)
    return redirect('detail', plant_id=plant_id)

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

@login_required
def plants_index(request):
    plants = Plant.objects.filter(user=request.user)
    return render(request, 'plants/index.html', {'plants': plants})

@login_required
def plants_detail(request, plant_id):
    plant = Plant.objects.get(id=plant_id)
    pots_plant_doesnt_have = Pot.objects.exclude(id__in = plant.pots.all().values_list('id'))
    feeding_form = FeedingForm()
    watering_form = WateringForm()
    return render(request, 'plants/detail.html', {'plant': plant, 'feeding_form': feeding_form, 'watering_form': watering_form, 'pots': pots_plant_doesnt_have})

@login_required
def add_feeding(request, plant_id):
    form = FeedingForm(request.POST)
    if form.is_valid(): 
        new_feeding = form.save(commit=False)
        new_feeding.plant_id = plant_id
        new_feeding.save()
    return redirect('detail', plant_id=plant_id)

@login_required
def add_watering(request, plant_id):
    form = WateringForm(request.POST)
    if form.is_valid(): 
        new_watering = form.save(commit=False)
        new_watering.plant_id = plant_id
        new_watering.save()
    return redirect('detail', plant_id=plant_id)

@login_required
def assoc_pot(request, plant_id, pot_id):
    Plant.objects.get(id=plant_id).pots.add(pot_id)
    return redirect('detail', plant_id=plant_id)

@login_required
def unassoc_pot(request, plant_id, pot_id):
    Plant.objects.get(id=plant_id).pots.remove(pot_id)
    return redirect('detail', plant_id=plant_id)

class PlantCreate(LoginRequiredMixin, CreateView):
    model = Plant
    fields = ['sci_name','common_name','genus','description', 'water', 'sun', 'food', 'toxicity', 'age']
    
    def form_valid(self, form):
    # Assign the logged in user (self.request.user)
        form.instance.user = self.request.user  # form.instance is the cat
    # Let the CreateView do its job as usual
        return super().form_valid(form)

class PlantUpdate(LoginRequiredMixin, UpdateView):
    model = Plant
    fields = ['sci_name','common_name','genus','description', 'water', 'sun', 'food', 'toxicity', 'age']
    success_url = '/plants/'
    
class PlantDelete(LoginRequiredMixin, DeleteView):
    model = Plant
    success_url = '/plants/'

class PotList(LoginRequiredMixin, ListView):
    model = Pot
    def get_queryset(self):
        return Pot.objects.filter(user=self.request.user)

class PotDetailView(LoginRequiredMixin, DetailView):
    model = Pot

class PotCreate(LoginRequiredMixin, CreateView):
    model = Pot
    fields = ['name', 'location', 'description', 'color']
    def form_valid(self, form):
        #currently logged in user: self.reqeust. user
        form.instance.user = self.request.user
        #super() calls createviews verion of form_valid which allows us to use createview other funcitonality
        #is creating the cat in the db and redirecting
        return super().form_valid(form)

class PotUpdate(LoginRequiredMixin, UpdateView):
    model = Pot
    fields = ['name', 'location', 'description', 'color']
    success_url = '/pots/'

class PotDelete(LoginRequiredMixin, DeleteView):
    model = Pot
    success_url = '/pots/'