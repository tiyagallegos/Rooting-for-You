from django.forms import ModelForm
from .models import Feeding, Watering

class FeedingForm(ModelForm):
    class Meta: 
        model = Feeding
        fields = ['date', 'volume', 'feeding']

class WateringForm(ModelForm):
    class Meta: 
        model = Watering
        fields = ['date', 'volume', 'watering']
    def __init__(self, *args, **kwargs):
        super(WateringForm, self).__init__(*args, **kwargs)
        self.fields['date'].widget.attrs.update({
            'id': 'water-id'
        })
