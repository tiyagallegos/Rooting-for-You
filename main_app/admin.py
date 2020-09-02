from django.contrib import admin
from .models import Plant, Feeding, Watering
# Register your models here.

admin.site.register(Plant)
admin.site.register(Feeding)
admin.site.register(Watering)