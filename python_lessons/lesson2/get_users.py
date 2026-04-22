def pobierz_uzytkownika() -> dict: #informuje o tym, że funkcja zwraca słownik
    dane_uzytkownika = {} # klucz: wartosc
    
    for informacja in ("imie", "wiek", "miasto"):
        dane_uzytkownika[informacja] = input("Wprowadz " + informacja + ": ")
        
    return dane_uzytkownika

users = []
liczba_uzytkownikow = int(input("Podaj liczbe uzytkownikow: "))

if liczba_uzytkownikow <= 0:
    print("Liczba musi byc wieksza od 0.")
else:
    # liczba uzytkownikow = 3
    while liczba_uzytkownikow != 0:
        user = pobierz_uzytkownika()
        users.append(user)
        liczba_uzytkownikow = liczba_uzytkownikow - 1
        
    # while len(users) < 3:
    #   user = pobierz_uzytkownika()
    #   users.append(user)
    
    for i in range(liczba_uzytkownikow):
        user = pobierz_uzytkownika()
        users.append(user)
