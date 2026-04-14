def pobierz_uzytkownika() -> dict: #informuje o tym, że funkcja zwraca słownik
    dane_uzytkownika = {} # klucz: wartosc
    
    for informacja in ("imie", "wiek", "miasto"):
        dane_uzytkownika[informacja] = input("Wprowadz " + informacja + ": ")
        
    return dane_uzytkownika

def pobierz_n_uzytkownikow(ilosc_uzytkownikow):
    users = []
    for _ in range(ilosc_uzytkownikow): # _ gdy nie używamy zmiennej
        user = pobierz_uzytkownika()
        users.append(user)
    return users

liczba_uzytkownikow = int(input("Podaj liczbe uzytkownikow: "))
if liczba_uzytkownikow <= 0:
    print("Liczba musi byc wieksza od 0.")
else:
    # users dostępne po zakończeniu programu w trybie interaktywnym
    users = pobierz_n_uzytkownikow(liczba_uzytkownikow)
    print(users) 