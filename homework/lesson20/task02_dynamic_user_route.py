# ogloszenia/views.py
from django.http import HttpResponse


def info(request):
    return HttpResponse("Informacje o stronie")


def rules(request):
    return HttpResponse("Regulamin")


def user_profile(request, username):
    return HttpResponse(f"Witaj na profilu, {username}!")


# ogloszenia/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path("info/", views.info, name="info"),
    path("rules/", views.rules, name="rules"),
    path("user/<str:username>/", views.user_profile, name="user_profile"),
]