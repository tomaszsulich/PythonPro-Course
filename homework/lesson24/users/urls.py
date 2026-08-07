from django.urls import path

from .views import home, profile, register, user_list


urlpatterns = [
    path("", home, name="home"),
    path("profile/", profile, name="profile"),
    path("register/", register, name="register"),
    path(
        "users/",
        user_list,
        name="user_list",
    ),
]