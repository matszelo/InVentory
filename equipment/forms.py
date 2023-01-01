from django import forms
from django.forms import ModelForm
from .models import Sprzet


class Equipmentform(ModelForm):
    class Meta:
        model = Sprzet
        fields = (
            'kategoria', 'producent', 'nazwa', 'numer_seryjny', 'numer_inwentarzowy', 'lokalizacja',
            'zdjecie')
        labels = {
            'kategoria': 'Kategoria',
            'producent': 'Producent',
            'nazwa': 'Nazwa',
            'numer_seryjny': 'Numer seryjny',
            'numer_inwentarzowy': 'Numer inwentarzowy',
            'lokalizacja': 'Lokalizacja',
            'zdjecie': '',
        }
        widgets = {
            'kategoria': forms.Select(attrs={'class': 'form-select', 'placeholder': 'Kategoria'}),
            'producent': forms.Select(attrs={'class': 'form-select', 'placeholder': 'Producent'}),
            'nazwa': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nazwa'}),
            'numer_seryjny': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Numer seryjny'}),
            'numer_inwentarzowy': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Numer inwentarzowy'}),
            'lokalizacja': forms.Select(attrs={'class': 'form-select', 'placeholder': 'Lokalizacja'}),
        }
