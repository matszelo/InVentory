from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_equipment, name='equipment_list'),
    path('add_Sprzet', views.add_Sprzet, name='add_Sprzet')
]