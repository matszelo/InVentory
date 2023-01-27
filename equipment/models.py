from django.db import models
from django.utils import timezone
import qrcode
from io import BytesIO
from django.core.files import File
from PIL import Image

# Utworzenie w bazie modelu o nazwie "Kategoria"

class Kategoria(models.Model):
    nazwa = models.CharField(max_length=50)

    def __str__(self):
        return self.nazwa

# Dodanie poprawnych końcówek  

    class Meta:
        verbose_name = "Kategoria"
        verbose_name_plural = "Kategorie"

# Utworzenie w bazie modelu o nazwie "Producent"        

class Producent(models.Model):
    nazwa = models.CharField(max_length=50)

    def __str__(self):
        return self.nazwa

# Dodanie poprawnych końcówek    
    
    class Meta:
        verbose_name = "Producent"
        verbose_name_plural = "Producenci"

# Utworzenie w bazie modelu o nazwie "Lokalizacja"        

class Lokalizacja(models.Model):
    nazwa = models.CharField(max_length=50)

    def __str__(self):
        return self.nazwa

# Dodanie poprawnych końcówek    
    
    class Meta:
        verbose_name = "Lokalizacja"
        verbose_name_plural = "Lokalizacje"

# Utworzenie w bazie modelu o nazwie "Sprzęt"        

class Sprzet(models.Model):
    kategoria = models.ForeignKey(Kategoria, on_delete=models.CASCADE, null=True, blank=False)
    producent = models.ForeignKey(Producent, on_delete=models.CASCADE, null=True, blank=False)
    nazwa = models.CharField(max_length=50, null=True, blank=False)
    numer_seryjny = models.CharField(max_length=50, null=True, blank=False)
    numer_inwentarzowy = models.CharField(max_length=6, null=True, blank=False)
    lokalizacja = models.ForeignKey(Lokalizacja, on_delete=models.CASCADE, null=True, blank=False)
    data_utworzenia = models.DateTimeField(default=timezone.now)
    zdjecie = models.ImageField(null=True, blank=True, upload_to="images/")
    QR_code = models.ImageField(blank=True, upload_to='QR_code/')

    def __str__(self):
        return self.nazwa
    
# Generowanie kodu QR po dodaniu nowego sprzętu do bazy     

    def save(self, *args, **kwargs):
        qr_image = qrcode.make(self.numer_inwentarzowy)
        qr_offset = Image.new('RGB', (310, 310), 'white')
        qr_offset.paste(qr_image)
        files_name = f'QR_code-{self.nazwa}.png'
        stream = BytesIO()
        qr_offset.save(stream, 'PNG')
        self.QR_code.save(files_name, File(stream), save=False)
        qr_offset.close()
        super().save(*args, **kwargs)

# Dodanie poprawnych końcówek         
        
    class Meta:
        verbose_name = "Sprzet"
        verbose_name_plural = "Sprzety"
