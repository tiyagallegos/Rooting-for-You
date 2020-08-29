from django.db import models

# Create your models here.
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

    def __str__(self):
        return self.common_name

    def get_absolute_url(self): 
        return reverse('detail', kwargs={'plant_id': plant.id})

class Pot(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    size = models.CharField(max_length=100)
    color = models.CharField(max_length=20)
    locaation = models.TextField(max_length=250)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('pots_detail', kwargs={'pk': self.id})