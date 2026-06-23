from django.core.exceptions import ValidationError
from django.db import models as m

# Create your models here.

class Tag(m.Model):
    name = m.CharField(max_length=35)
    
class Category(m.Model):
    name = m.CharField(max_length=30)
    
    def __str__(self):
        return self.name
    
class Author(m.Model):
    name = m.CharField(max_length=100)
    email = m.EmailField()
    
    def __str__(self):
        return f"<{self.name} {self.email}>"
    
class Post(m.Model):
    # każdy post ma jednego autora, autor ma wiele postów
    title = m.CharField()
    author = m.ForeignKey("Author", 
                          on_delete=m.CASCADE,
                          related_name="posts")
    category = m.ForeignKey(Category, on_delete=m.CASCADE, null=True)
    tags = m.ManyToManyField(Tag)
    pub_dat = m.DateTimeField(auto_now_add=True)