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

    def __str__(self):
        return self.tytul


class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Kategoria"
        verbose_name_plural = "Kategorie"

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="products",
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.name