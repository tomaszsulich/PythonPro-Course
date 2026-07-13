from django.contrib.auth.models import User
from django.db import models


class Dealer(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nazwa dealera")
    address = models.TextField(verbose_name="Adres")
    
    class Meta:
        verbose_name = "Dealer"
        verbose_name_plural = "Dealerzy"
        
    def __str__(self):
        
        return self.name
    
    
class Car(models.Model):
    dealer = models.ForeignKey(Dealer,
                               on_delete=models.CASCADE,
                               related_name='cars',
                               null=True,
                               blank=True,
                               verbose_name="Dealer")
    brand = models.CharField(max_length=50, verbose_name="Marka")
    model = models.CharField(max_length=50, verbose_name="Model")
    year = models.IntegerField(verbose_name="Rok produkcji")
    price = models.DecimalField(max_digits=10,
                                decimal_places=2,
                                verbose_name="Cena")
    description = models.TextField(verbose_name="Opis")
    photo = models.ImageField(upload_to='cars/', verbose_name="Zdjęcie")
    owner_website = models.URLField(blank=True,
                                    null=True,
                                    verbose_name="Strona właściciela")
    is_available = models.BooleanField(default=True, verbose_name="Dostępny")
    
    class Meta:
        verbose_name = "Samochód"
        verbose_name_plural = "Samochody"
        
    def __str__(self):
        return f"{self.brand} {self.model}"