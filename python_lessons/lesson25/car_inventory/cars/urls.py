from django.urls import path
from . import views

# user urls
urlpatterns = [
    # ... inne ścieżki
    path('cars/', views.register, name='register'),
    path('addcar', views.home, name='home'),
    path('profile/', views.profile, name='profile')
]