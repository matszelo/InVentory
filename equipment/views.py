from django.shortcuts import render, redirect
from .models import Sprzet
from .forms import Equipmentform
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.contrib import messages
import csv


def equipment_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=equipment.csv'
    writer = csv.writer(response)
    equipments = Sprzet.objects.all()
    writer.writerow(['ID', 'Nazwa', 'Kategoria', 'Producent', 'Numer seryjny', 'Numer inwentarzowy', 'Lokalizacja',
                     'Data utworzenia'])

    for equipment in equipments:
        writer.writerow(
            [equipment.id, equipment.nazwa, equipment.kategoria, equipment.producent, equipment.numer_seryjny,
             equipment.numer_inwentarzowy, equipment.lokalizacja, equipment.data_utworzenia])

    return response


def search_equipment(request):
    if request.method == "POST":
        searched = request.POST['searched']
        equipments = Sprzet.objects.filter(nazwa__contains=searched)
        return render(request, 'equipment/search_equipment.html', {'searched': searched, 'equipments': equipments})
    else:
        return render(request, 'equipment/search_equipment.html', {})


def delete_equipment(request, equipment_id):
    equipment = Sprzet.objects.get(pk=equipment_id)
    equipment.delete()
    messages.success(request, "Poprawnie usunięto sprzęt")
    return redirect('equipment_list')


def update_equipment(request, equipment_id):
    equipment = Sprzet.objects.get(pk=equipment_id)
    form = Equipmentform(request.POST or None, request.FILES or None, instance=equipment)
    if form.is_valid():
        form.save()
        messages.success(request, "Poprawnie zapisano dane sprzętu")
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
            messages.success(request, "Poprawnie dodano nowy sprzęt")
            return redirect('equipment_list')
    else:
        form = Equipmentform
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'equipment/add_equipment.html', {'form': form, 'submitted': submitted})


def all_equipment(request):
    equipment_count = Sprzet.objects.all().count()
    equipment_list = Sprzet.objects.all()
    p = Paginator(Sprzet.objects.all(), 10)
    page = request.GET.get('page')
    equipments = p.get_page(page)
    nums = "a" * equipments.paginator.num_pages
    return render(request, 'equipment/equipment_list.html',
                  {'equipment_list': equipment_list, 'equipments': equipments, 'nums': nums,
                   'equipment_count': equipment_count})
