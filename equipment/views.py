from django.shortcuts import render, redirect
from .models import Sprzet
from django.http import HttpResponseRedirect
from .forms import Equipmentform

def update_equipment(request, equipment_id):
    equipment = Sprzet.objects.get(pk=equipment_id)
    form = Equipmentform(request.POST or None, instance=equipment)
    if form.is_valid():
        form.save()
        return redirect('equipment_list')
    return render(request, 'equipment/update_equipment.html', {'equipment': equipment, 'form': form})
def show_equipment(request, equipment_id):
    equipment = Sprzet.objects.get(pk=equipment_id)
    return render(request, 'equipment/show_equipment.html', {'equipment': equipment})
def add_equipment(request):
    submitted = False
    if request.method == "POST":
        form = Equipmentform(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('add_equipment?submitted=True')
    else:
        form = Equipmentform
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'equipment/add_equipment.html', {'form': form, 'submitted': submitted})

def all_equipment(request):
    equipment_list = Sprzet.objects.all()
    return render(request, 'equipment/equipment_list.html', {'equipment_list': equipment_list})

