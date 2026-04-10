def pobierz_uzytkownika() -> dict: #informuje o tym, że funkcja zwraca słownik
    dane_uzytkownika = {} # klucz: wartosc
    
    for informacja in ("imie", "wiek", "miasto"):
        dane_uzytkownika[informacja] = input("Wprowadź " + informacja + ": ")
        
    return dane_uzytkownika

users = []
liczba_uzytkownikow = int(input("Podaj liczbę użytkowników: "))

if liczba_uzytkownikow <= 0:
    print("Liczba musi być większa od 0.")
else:
    for i in range(liczba_uzytkownikow):
        user = pobierz_uzytkownika()
        users.append(user)
        
print("\nPodsumowanie użytkowników:")

for user in users:
    wiek = int(user['wiek'])
    
    if wiek == 1:
        lata = "rok"
    elif 2 <= wiek % 10 <= 4 and not 12 <= wiek % 100 <= 14:
        lata = "lata"
    else:
        lata = "lat"
    
    print(
    f"A więc, masz na imię {user['imie']}, "
    f"masz {wiek} {lata} "
    f"i mieszkasz w mieście {user['miasto']}."
)