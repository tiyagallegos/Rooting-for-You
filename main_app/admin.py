from django.contrib import admin
from .models import Plant, Feeding, Watering, Pot, Photo
# Register your models here.

admin.site.register(Plant)
admin.site.register(Feeding)
admin.site.register(Watering)
admin.site.register(Pot)
admin.site.register(Photo)