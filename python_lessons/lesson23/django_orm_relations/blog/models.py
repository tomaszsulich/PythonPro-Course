from django.core.exceptions import ValidationError
from django.shortcuts import render
from django.db import models as m

# Create your models here.

class Category(m.Model):
    name = m.CharField()
    
def validate_even(value):
    # walidacja jednego pola
    if value % 2 != 0:
        raise ValidationError("Musi być parzyste")

# Category.objects.create(name="Nazwa kategorii")

# c = Category(name="Nazwa kategorii")
# c.save() - razem z powyższą metodą dla każdej osobnej kategorii osobny rekord

# Category.objects.bulk_create() - wykonuje wiele wpisów naraz
# Category.objects.get() - ZAWSZE ZWRACA TYLKO JEDEN WYNIK, INACZEJ BŁĄD!

class Author(m.Model):
    name = m.CharField(max_length=100)
                       # validators=[validate_even])
    # age = m.IntegerField()
    email = m.EmailField()
    
    # def clean(self):
    #     ...
    
    # def save(self):
    #     self.email = self.email.lower
    #     super().save()

class Post(m.Model):
    # każdy post ma jednego autora, autor ma wiele postów
    title = m.CharField()
    author = m.ForeignKey("Author", 
                          on_delete=m.CASCADE,
                          related_name="posts")
    
# a = Author(name="Radek", age=22, email="zsjjoljljjjjlghjgjhgjTFGfvjgkgk@xzx.com")
# p = Post(a)

# a.save()