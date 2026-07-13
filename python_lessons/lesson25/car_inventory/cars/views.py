from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.
from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.contrib import messages

def register(request):
    # Sprawdzamy, czy metoda żądania to POST (wysyłka formularza)
    if request.method == 'POST':
        # Tworzymy instancję formularza z danymi z żądania
        form = CustomUserCreationForm(request.POST)
        # Sprawdzamy, czy formularz jest poprawny
        if form.is_valid():
            form.save() # Zapisujemy użytkownika w bazie danych
            username = form.cleaned_data.get('username')
            # Wyświetlamy komunikat o sukcesie
            messages.success(request, f'Konto dla {username} zostało utworzone! Możesz się teraz zalogować.')
            return redirect('login') # Przekierowujemy na stronę logowania
    else:
        # Jeśli metoda to GET, tworzymy pusty formularz
        form = CustomUserCreationForm()
    
    # Renderujemy szablon z formularzem
    return render(request, 'users/register.html', {'form': form})

def home(request):
    return render(request, 'index.html')

@login_required
def profile(request):
    return render(request, 'users/profile.html')