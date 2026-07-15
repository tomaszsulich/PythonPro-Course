from rest_framework import serializers
from .models import Product, Note, Author, Book


class ProductSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Product
        fields = "__all__"
        
        
class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = "__all__"
        
    def validate_title(self, value):
        if len(value) < 5:
            raise serializers.ValidationError("Tytuł musi mieć min. 5 znaków.")
        return value
    
    def validate(self, data):
        if len(data['title']) > len(data['content']):
            raise serializers.ValidationError("content musi być dłuższy od tytułu!")
            
        return data
    

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'name']
        
        
class BookSerializer(serializers.ModelSerializer):
    # Pole tylko do odczytu: wyświetla nazwę (nie wymaga source, jeśli używamy kropki)
    author_name = serializers.CharField(source='author.name', read_only=True)
    
    # Pole do zapisu: używa nazwy pola z modelu 'author', więc source nie jest potrzebne
    author = serializers.PrimaryKeyRelatedField(queryset=Author.objects.all())
    
    class Meta:
        model = Book
        fields = ['id', 'title', 'publication_year', 'author', 'author_name']