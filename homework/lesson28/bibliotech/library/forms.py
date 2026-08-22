from django.contrib.auth.forms import AuthenticationForm, UserCreationForm


class LoginForm(AuthenticationForm):
    """Formularz logowania dopasowany wizualnie do BiblioTech."""
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.fields["username"].label = "Nazwa użytkownika"
        self.fields["password"].label = "Hasło"

        for field in self.fields.values():
            field.widget.attrs["class"] = "form-control"


class RegisterForm(UserCreationForm):
    """Formularz rejestracji z krótkimi, czytelnymi opisami pól."""
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.fields["username"].label = "Nazwa użytkownika"
        
        self.fields["username"].help_text = (
            "Do 150 znaków. Litery, cyfry oraz znaki @ . + - _"
        )
        
        self.fields["password1"].label = "Hasło"
        
        self.fields["password1"].help_text = (
            "Minimum 8 znaków; hasło nie powinno być zbyt proste ani podobne "
            "do nazwy użytkownika."
        )
        
        self.fields["password2"].label = "Powtórz hasło"
        self.fields["password2"].help_text = "Wpisz ponownie to samo hasło."

        for field in self.fields.values():
            field.widget.attrs["class"] = "form-control"