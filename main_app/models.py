from django.db import models

# Create your models here.
class Plant(models.Model):
    sci_name = models.CharField(max_length=100)
    common_name = models.CharField(max_length=100)
    water = models.TextField(max_length=250)
    sun = models.TextField(max_length=250)
    food = models.TextField(max_length=250)
    toxicity = models.CharField(max_length=100)
    age = models.ImageField()

    def __str__(self):
        return self.name

