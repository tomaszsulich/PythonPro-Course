from django.urls import path
from . import views

urlpatterns = [
    # ... inne ścieżki
    path('register/', views.register, name='register'),
    path('', views.home, name='home'),
    path('profile/', views.profile, name='profile')
]