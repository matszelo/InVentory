from django import forms
from django.forms import ModelForm
from .models import Sprzet

class Equipmentform(ModelForm):
    class Meta:
        model = Sprzet
        fields = "__all__"