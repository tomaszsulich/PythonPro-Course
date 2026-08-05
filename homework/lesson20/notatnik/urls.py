from django.urls import path
from . import views

app_name = "notatnik"

urlpatterns = [
    path("notes/", views.note_list, name="note_list"),
    path("note/<int:note_id>/", views.note_detail, name="note_detail"),
]