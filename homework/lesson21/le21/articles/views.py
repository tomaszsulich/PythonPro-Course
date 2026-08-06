from datetime import timedelta
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone

from .forms import ArticleForm
from .models import Article, Category


def article_create(request):
    form = ArticleForm()

    if request.method == "POST":
        form = ArticleForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("article-create")

    return render(
        request,
        "articles/article_form.html",
        {"form": form},
    )


def article_list_view(request):
    articles = Article.objects.filter(
        is_published=True,
    ).order_by("-pub_date")

    query = request.GET.get("q")

    if query:
        articles = articles.filter(title__icontains=query)

    three_days_ago = timezone.now() - timedelta(days=3)

    return render(
        request,
        "articles/article_list.html",
        {
            "articles": articles,
            "query": query,
            "three_days_ago": three_days_ago,
        },
    )


def category_list_view(request):
    categories = Category.objects.all()

    return render(
        request,
        "articles/category_list.html",
        {"categories": categories},
    )


def category_detail_view(request, pk):
    category = get_object_or_404(Category, pk=pk)

    return render(
        request,
        "articles/category_detail.html",
        {"category": category},
    )