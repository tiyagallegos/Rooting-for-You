from django.shortcuts import render


class Plant: 
    def __init__(self, sci_name, common_name, genus, description, water, sun, food, toxicity, age):
        self.sci_name = sci_name
        self.common_name = common_name
        self.genus =  genus
        self.description = description
        self.water = water
        self.sun = sun
        self.food = food
        self.toxicity = toxicity
        self.age = age

plants = [
    Plant('Calathea crotalifera S. Watson', 'rattlesnake plant', 'calathea', 'yellow at top looks like tail of snake', '1-2 weeks', 
    'bright indirect sunlight', 'spring, summer, and fall', 'safe for humans, dogs, and cats', 9)
]



# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def plants_index(request):
    return render(request, 'plants/index.html', {'plants': plants})