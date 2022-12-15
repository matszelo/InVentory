from django.shortcuts import render
from .models import Sprzet

def all_equipment(request):
    equipment_list = Sprzet.objects.all()
    return render(request, 'equipment/equipment_list.html', {'equipment_list': equipment_list})
