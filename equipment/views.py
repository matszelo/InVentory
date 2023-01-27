from django.shortcuts import render, redirect
from .models import Sprzet
from .forms import Equipmentform
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.contrib import messages
import csv
from django.http import FileResponse
import io
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter

# Generownie pliku PDF

def equipment_pdf(request):
    buf = io.BytesIO()
    c = canvas.Canvas(buf, pagesize=letter, bottomup=0)
    texttob = c.beginText()
    texttob.setTextOrigin(inch, inch)
    texttob.setFont("Helvetica", 14)

    equipments = Sprzet.objects.all()
    lines = []

    for equipment in equipments:
        lines.append(str(equipment.id))
        lines.append(str(equipment.nazwa))
        lines.append(str(equipment.kategoria))
        lines.append(str(equipment.producent))
        lines.append(str(equipment.numer_seryjny))
        lines.append(str(equipment.numer_inwentarzowy))
        lines.append(str(equipment.lokalizacja))
        lines.append(str(equipment.data_utworzenia))
        lines.append(" ")

    for line in lines:
        texttob.textLine(line)

    c.drawText(texttob)
    c.showPage()
    c.save()
    buf.seek(0)

    return FileResponse(buf, as_attachment=True, filename='Lista_sprzetow.pdf')

# GEnerowanie pliku CSV

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

# Wyszukiwanie sprzętu w bazie

def search_equipment(request):
    if request.method == "POST":
        searched = request.POST['searched']
        equipments = Sprzet.objects.filter(nazwa__icontains=searched) # Filtr wyszukiwania sprzętu po nazwie
        return render(request, 'equipment/search_equipment.html', {'searched': searched, 'equipments': equipments})
    else:
        return render(request, 'equipment/search_equipment.html', {})

# Usuwanie sprzętu z bazy    

def delete_equipment(request, equipment_id):
    equipment = Sprzet.objects.get(pk=equipment_id)
    equipment.delete()
    messages.success(request, "Poprawnie usunięto sprzęt") # Komunikat po usunięciu sprzętu
    return redirect('equipment_list')

# Aktualizowanie danych sprzętu w bazie

def update_equipment(request, equipment_id):
    equipment = Sprzet.objects.get(pk=equipment_id)
    form = Equipmentform(request.POST or None, request.FILES or None, instance=equipment)
    if form.is_valid():
        form.save()
        messages.success(request, "Poprawnie zapisano dane sprzętu") # Komunikat po zaktualizowaniu sprzętu
        return redirect('equipment_list')
    return render(request, 'equipment/update_equipment.html', {'equipment': equipment, 'form': form})

# Wyświetlenie danego sprzętu z bazy

def show_equipment(request, equipment_id):
    equipment = Sprzet.objects.get(pk=equipment_id)
    return render(request, 'equipment/show_equipment.html', {'equipment': equipment})

# Dodanie sprzętu do bazy

def add_equipment(request):
    submitted = False
    if request.method == "POST":
        form = Equipmentform(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Poprawnie dodano nowy sprzęt") # KOmunikat po dodaniu sprzętu
            return redirect('equipment_list')
    else:
        form = Equipmentform
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'equipment/add_equipment.html', {'form': form, 'submitted': submitted})

# Wyświetlenie wszystkich sprzętów w bazie

def all_equipment(request):
    equipment_count = Sprzet.objects.all().count()
    equipment_list = Sprzet.objects.all()
    p = Paginator(Sprzet.objects.all(), 10) # Ograniczenie ilości sprzętu do 10 na jednej stronie
    page = request.GET.get('page')
    equipments = p.get_page(page)
    nums = "a" * equipments.paginator.num_pages # Numeracja stron sprzętu
    return render(request, 'equipment/equipment_list.html',
                  {'equipment_list': equipment_list, 'equipments': equipments, 'nums': nums,
                   'equipment_count': equipment_count})
