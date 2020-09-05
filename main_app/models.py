from django.db import models
from django.urls import reverse
from datetime import date
import datetime
from django.contrib.auth.models import User

WATERINGS = (
    ('M', 'Morning Water'),
    ('A', 'Afternoon Water'),
    ('E', 'Evening Water'),
)

FEEDINGS = (
    ('C', 'Compost Tea'),
    ('F', 'Fertilizer'),
    ('S', 'New Soil')
)


# Create your models here.


class Pot(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    size = models.CharField(max_length=100)
    color = models.CharField(max_length=20)
    location = models.TextField(max_length=250)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('pots_detail', kwargs={'pk': self.id})

class Plant(models.Model):
    sci_name = models.CharField(max_length=100)
    common_name = models.CharField(max_length=100)
    genus = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    water = models.TextField(max_length=250)
    sun = models.TextField(max_length=250)
    food = models.TextField(max_length=250)
    toxicity = models.CharField(max_length=100)
    age = models.IntegerField()
    pots = models.ManyToManyField(Pot)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.common_name

    def get_absolute_url(self): 
        return reverse('detail', kwargs={'plant_id': self.id})

    def fed_for_month(self):
        start_date = datetime.datetime.now() - datetime.timedelta(days=30)
        start_date = start_date.date()
        feedings = self.feeding_set.all()
        print(feedings[0].date, start_date)
        return feedings[0].date > start_date
    
    def watered_for_week(self):
        start_date = datetime.datetime.now() - datetime.timedelta(days=7)
        start_date = start_date.date()
        waterings = self.watering_set.all()
        print(waterings[0].date, start_date)
        return waterings[0].date > start_date



        
class Photo(models.Model):
    url = models.CharField(max_length=200)
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE)

    def __str__(self):
        return f"Photo for plant_id: {self.plant_id} @{self.url}"
    #def fed_for_the_month(self):
    #    return self.feeding_set.filter(date=date.today()).count() >= 1

    #def watered_for_week(self):
    #    return self.watering_set.filter(date=date.today()).count() >= 1

class Watering(models.Model):
    date = models.DateField('watering date')
    volume = models.CharField(max_length=15)
    watering = models.CharField(max_length=1, choices=WATERINGS, default=WATERINGS[0][0])
    
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_watering_display()} on {self.date}"
    
    class Meta: 
        ordering = ['-date']

class Feeding(models.Model):
    date = models.DateField('feeding date')
    volume = models.CharField(max_length=15)
    feeding = models.CharField(verbose_name='feeding type', max_length=1, choices=FEEDINGS, default=FEEDINGS[0][0])
    
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_feeding_display()} on {self.date}"
    
    class Meta: 
        ordering = ['-date']