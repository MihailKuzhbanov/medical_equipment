from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('about', views.about, name='about'),
    path('equipment', views.equipment, name='equipment'),
    path('add_equipment', views.add_equipment, name='add_equipment')
]
