from django.shortcuts import render
from .models import Category
# Create your views here.

def get_category(request):
    id_ = request.GET.get("q")
    cat = Category.objects.get(id=id_)
    return render(request, "category.html", {"category": cat})