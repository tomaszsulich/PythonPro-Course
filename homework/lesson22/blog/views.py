from django.db.models import Q
from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, render

from .models import Category, Post


def home_view(request: HttpRequest) -> HttpResponse:
    query = request.GET.get("q", "").strip()

    posts = Post.objects.order_by("-publication_date")

    if query:
        posts = posts.filter(
            Q(title__icontains=query)
            | Q(content__icontains=query)
        )

    posts = posts[:5]

    return render(
        request,
        "blog/home.html",
        {
            "posts": posts,
            "query": query,
        },
    )


def category_view(request: HttpRequest, category_id: int) -> HttpResponse:
    category = get_object_or_404(
        Category,
        pk=category_id,
    )

    posts = Post.objects.filter(
        category=category,
    )

    return render(
        request,
        "blog/category.html",
        {
            "category": category,
            "posts": posts,
        },
    )