class InvalidPasswordError(Exception):
    """Wyjątek zgłaszany przy niepoprawnym haśle."""
    
def ustaw_haslo(haslo: str) -> None:
    """Sprawdza poprawność hasła."""
    if len(haslo) < 8:
        raise InvalidPasswordError("Hasło musi mieć co najmniej 8 znaków.")
    

def main() -> None:
    haslo = input("Podaj hasło: ")
    
    try:
        ustaw_haslo(haslo)
        print("Hasło zostało ustawione.")
    except InvalidPasswordError as e:
        print(f"Błąd: {e}")
        
        
if __name__ == "__main__":
    main()