from django.shortcuts import render
from .models import Post
# Create your views here.


def get_category(request, category_id):
    
    posts = Post.objects.filter(category_id=category_id)
    
    return render(request, "posts.html", {"posts": posts,
                                          "author": posts[0].category})