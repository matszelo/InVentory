from django.db import models
from django.utils.datetime_safe import date


class Kategoria(models.Model):
    nazwa = models.CharField(max_length=50)

    def __str__(self):
        return self.nazwa

    class Meta:
        verbose_name = "Kategoria"
        verbose_name_plural = "Kategorie"

class Producent(models.Model):
    nazwa = models.CharField(max_length=50)

    def __str__(self):
        return self.nazwa

    class Meta:
        verbose_name = "Producent"
        verbose_name_plural = "Producenci"

class Lokalizacja(models.Model):
    nazwa = models.CharField(max_length=50)

    def __str__(self):
        return self.nazwa

    class Meta:
        verbose_name = "Lokalizacja"
        verbose_name_plural = "Lokalizacje"


class Sprzet(models.Model):
    kategoria = models.ForeignKey(Kategoria,on_delete=models.CASCADE, null=True, blank=False)
    producent = models.ForeignKey(Producent, on_delete=models.CASCADE, null=True, blank=False)
    nazwa = models.CharField(max_length=50, null=True, blank=False)
    numer_seryjny = models.CharField(max_length=50, null=True, blank=False)
    numer_inwentarzowy = models.CharField(max_length=6, null=True, blank=False)
    lokalizacja = models.ForeignKey(Lokalizacja, on_delete=models.CASCADE, null=True, blank=False)
    data_utworzenia = models.DateTimeField(default=date.today)
    zdjecie = models.ImageField(null=True, blank=True, upload_to="images/")
    def __str__(self):
        return self.nazwa

    class Meta:
        verbose_name = "Sprzet"
        verbose_name_plural = "Sprzety"


