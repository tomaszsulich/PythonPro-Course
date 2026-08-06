from django.urls import path

from .views import (
    category_view,
    home_view,
)


urlpatterns = [
    path("", home_view, name="home"),
    path(
        "category/<int:category_id>/",
        category_view,
        name="category",
    ),
]