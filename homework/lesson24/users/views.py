from django.contrib import messages
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import redirect, render

from .forms import CustomUserCreationForm


@login_required
def home(request):
    return render(
        request,
        "home.html",
    )


@login_required
def profile(request):
    return render(
        request,
        "users/profile.html",
    )


def register(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()

            login(
                request,
                user,
            )

            messages.success(
                request,
                f"Konto dla {user.username} zostało utworzone! "
                "Zostałeś automatycznie zalogowany.",
            )

            return redirect("home")
    else:
        form = CustomUserCreationForm()

    return render(
        request,
        "users/register.html",
        {"form": form},
    )


@staff_member_required
def user_list(request):
    users = User.objects.all()

    return render(
        request,
        "users/user_list.html",
        {"users": users},
    )