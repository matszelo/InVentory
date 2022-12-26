from django.contrib import admin
from .models import Sprzet, Kategoria, Producent, Lokalizacja
from django.contrib.auth.models import Group

admin.site.unregister(Group)
admin.site.register(Sprzet)
admin.site.register(Kategoria)
admin.site.register(Producent)
admin.site.register(Lokalizacja)



