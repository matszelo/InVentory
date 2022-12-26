from django.shortcuts import render, redirect
from .models import Sprzet
from .forms import Equipmentform
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect

def search_equipment(request):
    if request.method == "POST":
        searched = request.POST['searched']
        equipments = Sprzet.objects.filter(nazwa__contains=searched)
        return render(request, 'equipment/search_equipment.html', {'searched':searched, 'equipments':equipments})
    else:
        return render(request, 'equipment/search_equipment.html', {})

def delete_equipment(request, equipment_id):
    equipment = Sprzet.objects.get(pk=equipment_id)
    equipment.delete()
    return redirect('equipment_list')
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
        form = Equipmentform(request.POST, request.FILES)
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
    p = Paginator(Sprzet.objects.all(), 10)
    page = request.GET.get('page')
    equipments = p.get_page(page)
    nums = "a" * equipments.paginator.num_pages
    return render(request, 'equipment/equipment_list.html', {'equipment_list': equipment_list, 'equipments': equipments, 'nums': nums})

