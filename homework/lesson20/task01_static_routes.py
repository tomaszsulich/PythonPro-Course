# ogloszenia/views.py
from django.http import HttpRequest, HttpResponse


def info(request: HttpRequest):
    return HttpResponse("Informacje o stronie")


def rules(request: HttpRequest):
    return HttpResponse("Regulamin")


# ogloszenia/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path("info/", views.info, name="info"),
    path("rules/", views.rules, name="rules"),
]


# mojastrona/urls.py
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("ogloszenia.urls")),
]