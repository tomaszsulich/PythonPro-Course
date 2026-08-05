# ogloszenia/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path("info/", views.info, name="info"),
    path("rules/", views.rules, name="rules"),
    path("user/<str:username>/", views.user_profile, name="user_profile"),
    path("products/", views.product_list, name="product_list"),
    path("products/add/", views.add_product, name="add_product"),
    path(
        "category/<int:category_id>/",
        views.products_by_category,
        name="products_by_category",
    ),
]