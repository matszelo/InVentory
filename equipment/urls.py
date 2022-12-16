from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_equipment, name='equipment_list'),
    path('add_equipment', views.add_equipment, name='add_equipment'),
    path('show_equipment/<equipment_id>', views.show_equipment, name='show_equipment'),
    path('update_equipment/<equipment_id>', views.update_equipment, name='update_equipment'),
]