from django.contrib import admin
from .models import Ogloszenie


@admin.register(Ogloszenie)
class OgloszenieAdmin(admin.ModelAdmin):
    list_display = ("tytul", "cena", "data_dodania")
    search_fields = ("tytul", "opis")
    list_filter = ("data_dodania",)
    ordering = ("-data_dodania",)