from django.urls import path
from .views import get_category

urlpatterns = [
    path("<int:q>", get_category, name="get-cat")
]