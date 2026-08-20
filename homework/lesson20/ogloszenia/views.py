from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render

from .forms import ProductForm
from .models import Product


def info(request: HttpRequest):
    return HttpResponse("Informacje o stronie")


def rules(request: HttpRequest):
    return HttpResponse("Regulamin")


def user_profile(request: HttpRequest, username: str):
    return HttpResponse(f"Witaj na profilu, {username}!")


def product_list(request: HttpRequest) -> HttpResponse:
    products = Product.objects.all()

    return render(
        request,
        "ogloszenia/product_list.html",
        {"products": products},
    )


def add_product(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = ProductForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("product_list")
    else:
        form = ProductForm()

    return render(
        request,
        "ogloszenia/product_form.html",
        {"form": form},
    )


def products_by_category(request: HttpRequest, category_id: int) -> HttpResponse:
    products = Product.objects.filter(category_id=category_id)

    return render(
        request,
        "ogloszenia/product_list.html",
        {"products": products},
    )