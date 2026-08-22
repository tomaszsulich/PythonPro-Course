from django.urls import path
from . import views

app_name = "library"

urlpatterns = [
    path("", views.catalog, name="catalog"),
    path("books/<int:book_id>/", views.book_detail, name="book_detail"),
    path("register/", views.register, name="register"),
    path("reserve/<int:copy_id>/", views.reserve, name="reserve"),
    path("my-reservations/", views.my_reservations, name="my_reservations"),
    path("api/books/", views.api_books, name="api_books"),
    path("api/books/<int:book_id>/", views.api_book_detail, name="api_book_detail"),
    path("api/my-reservations/", views.api_my_reservations, name="api_my_reservations"),
]