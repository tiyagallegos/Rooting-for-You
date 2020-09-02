from django.forms import ModelForm
from .models import Feeding, Watering

class FeedingForm(ModelForm):
    class Meta: 
        model = Feeding
        fields = ['date', 'volume', 'watering']

class WateringForm(ModelForm):
    class Meta: 
        model = Watering
        fields = ['date', 'volume', 'feeding']