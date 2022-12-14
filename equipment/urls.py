from django.urls import path
from . import views

urlpatterns = [
    path('', views.equipment_list, name='equipment_list'),
]