from django.core.exceptions import ValidationError
from django.db import models as m

# Create your models here.

class Category(m.Model):
    name = m.CharField(max_length=30)
    
class Author(m.Model):
    name = m.CharField(max_length=100)
                       # validators=[validate_even])
    # age = m.IntegerField()
    email = m.EmailField()
    
class Post(m.Model):
    # każdy post ma jednego autora, autor ma wiele postów
    title = m.CharField()
    author = m.ForeignKey("Author", 
                          on_delete=m.CASCADE,
                          related_name="posts")
    category = m.ForeignKey(Category, on_delete=m.CASCADE, null=True)