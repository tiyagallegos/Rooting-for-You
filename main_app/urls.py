from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('plants/', views.plants_index, name='index'),
    path('plants/<int:plant_id>/', views.plants_detail, name='detail'),
    path('plants/create/', views.PlantCreate.as_view(), name='plants_create'),
    path('plants/<int:pk>/update/', views.PlantUpdate.as_view(), name='plants_update'),
    path('plants/<int:pk>/delete/', views.PlantDelete.as_view(), name='plants_delete'),

    path('pots/', views.pots_index, name='pot_index'),
    path('pots/<int:pot_id>/', views.pots_detail, name='pot_detail'),
    path('pots/create/', views.PotCreate.as_view(), name='pots_create'),
    path('pots/<int:pk>/update/', views.PotUpdate.as_view(), name='pots_update'),
    path('pots/<int:pk>/delete/', views.PotDelete.as_view(), name='pots_delete'),
]