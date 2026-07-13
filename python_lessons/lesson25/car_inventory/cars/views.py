from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.contrib import messages

from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.models import User
from django.contrib.auth import login as auth_login


def register(request):
    # Sprawdzamy, czy metoda żądania to POST (wysyłka formularza)
    if request.method == 'POST':
        # Tworzymy instancję formularza z danymi z żądania
        form = CustomUserCreationForm(request.POST)
        # Sprawdzamy, czy formularz jest poprawny
        if form.is_valid():
            user = form.save() # Zapisujemy użytkownika w bazie danych
            username = form.cleaned_data.get('username')
            # Wyświetlamy komunikat o sukcesie
            auth_login(request, user)
            messages.success(
                request, 
                f'Konto dla {username} zostało utworzone! Możesz się teraz zalogować.'
            )
            return redirect('login') # Przekierowujemy na stronę logowania
    else:
        # Jeśli metoda to GET, tworzymy pusty formularz
        form = CustomUserCreationForm()
    
    # Renderujemy szablon z formularzem
    return render(request, 'users/register.html', {'form': form})


def logout_view(request):
    return render(request, 'users/logout.html')


@login_required
def home(request):
    return render(request, 'index.html')


@login_required
def profile(request):
    return render(request, 'users/profile.html')


@staff_member_required
def user_list(request):
    users = User.objects.all()
    return render(request, 'user_list.html', {'users': users})