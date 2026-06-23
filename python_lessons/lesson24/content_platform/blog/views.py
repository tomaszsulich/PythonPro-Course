from django.shortcuts import render
from .models import Post
# Create your views here.


def get_category(request, category_id):
    
    posts = Post.objects.filter(category_id=category_id)
    
    return render(request, "posts.html", {"posts": posts,
                                          "author": posts[0].category})

# zad 3.
# Zmodyfikuj widok strony głównej tak, aby wyświetlał tylko 5 najnowszych postów.
# Użyj order_by() i "krojenia" (slicing) QuerySetu. (proste)
def get_posts(request, head=5):
    # slicing od razu włączamy do zapytania SQL
    posts = Post.objects.all().order_by("-pub_dat")[:head]
    return render(request, "posts.html", {"posts": posts})

def get_posts_by_category(request, category_id):
    posts = Post.objects.filter(category_id=category_id)
    return render(request, "posts.html", {"posts": posts})

def search_posts(request):
    phrase = request.GET.get("q", "").strip()
    posts = Post.objects.none()
    if phrase:
        posts = Post.objects.filter(title__icontains=phrase)
    return render(request, "search.html", {"posts": posts})