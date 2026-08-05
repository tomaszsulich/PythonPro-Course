# ogloszenia/models.py
from django.db import models


class Ogloszenie(models.Model):
    tytul = models.CharField(max_length=100)
    opis = models.TextField()
    cena = models.DecimalField(max_digits=8, decimal_places=2)
    data_dodania = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-data_dodania"]
        verbose_name = "Ogłoszenie"
        verbose_name_plural = "Ogłoszenia"