from django.shortcuts import render
from .models import Sprzet
from django.http import HttpResponseRedirect
from .forms import Equipmentform

def add_Sprzet(request):
    submitted = False
    if request.method == "POST":
        form = Equipmentform(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('add_Sprzet?submitted=True')
    else:
        form = Equipmentform
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'equipment/add_Sprzet.html', {'form': form, 'submitted': submitted})
def all_equipment(request):
    equipment_list = Sprzet.objects.all()
    return render(request, 'equipment/equipment_list.html', {'equipment_list': equipment_list})

