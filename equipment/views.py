from django.shortcuts import render

def equipment_list(request):
    return render(request, 'equipment/equipment_list.html', {})
