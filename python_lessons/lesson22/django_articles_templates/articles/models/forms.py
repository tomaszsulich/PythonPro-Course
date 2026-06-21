from django import forms
from . import Article


# formularz tworzony automatycznie przez Django na podstawie modelu Article
class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'content'] # pola widoczne w formularzu
