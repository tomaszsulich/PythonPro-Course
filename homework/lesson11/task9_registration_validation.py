class RejestracjaUzytkownika:
    
    def __init__(self, email: str, haslo: str) -> None:
        bledy = []
        
        if "@" not in email:
            bledy.append("Nieprawidłowy adres email. Musi zawierać znak '@'.")

        if len(haslo) < 8:
            bledy.append("Hasło musi mieć co najmniej 8 znaków.")
            
        if bledy:
            raise ValueError(bledy)
        
        self.email = email
        self.haslo = haslo
        
        
def main() -> None:
    print("=== Rejestracja użytkownika: jankowalski@gmail.com ===")
    try:
        uzytkownik1 = RejestracjaUzytkownika("jankowalski@gmail.com", "piesek123")
        print(f"Użytkownik zarejestrowany: {uzytkownik1.email}")
        
    except ValueError as e:
        for blad in e.args[0]:
            print(f"Błąd rejestracji: {blad}")
    
    print("\n=== Rejestracja użytkownika: anna.nowak ===") 
    try:
        uzytkownik2 = RejestracjaUzytkownika("anna.nowak", "kot12345")
        print(f"Użytkownik zarejestrowany: {uzytkownik2.email}")
        
    except ValueError as e:
        for blad in e.args[0]:
            print(f"Błąd rejestracji: {blad}")
    
    print("\n=== Rejestracja użytkownika: piotr.kowalski@gmail.com ===")
    try:
        uzytkownik3 = RejestracjaUzytkownika("piotr.kowalski@gmail.com", "kot")
        print(f"Użytkownik zarejestrowany: {uzytkownik3.email}")
        
    except ValueError as e:
        for blad in e.args[0]:
            print(f"Błąd rejestracji: {blad}")
    
    print("\n=== Rejestracja użytkownika: ewa.nowak ===")
    try:
        uzytkownik4 = RejestracjaUzytkownika("ewa.nowak", "123")
        print(f"Użytkownik zarejestrowany: {uzytkownik4.email}")
        
    except ValueError as e:
        for blad in e.args[0]:
            print(f"Błąd rejestracji: {blad}")
        

if __name__ == "__main__":
    main()