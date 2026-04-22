kursy = {"USD": 4.0, "EUR": 4.3}

while True:
    kwota = float(input("Podaj kwotę, którą chcesz wymienić (PLN): ").replace(",", "."))
    if kwota < 0:
        print("Kwota musi być większa bądź równa zero!")
        continue
    waluta = input("Podaj walutę, na którą chcesz ją wymienić: ").upper()
    
    if waluta in kursy:
        kwota /= kursy[waluta]
    else:
        print("Nie obsługujemy takiej waluty!")
        continue        
    print(f"Otrzymujesz {kwota:.2f} {waluta}.")
    
    while True:
        czy_kontynuowac = input("Czy chcesz kontynuować (tak/nie)? ").lower()
    
        if czy_kontynuowac == "nie":
            break
        elif czy_kontynuowac == "tak":
            break
        else:
            print("Podaj poprawną odpowiedź (tak/nie).")
    
    if czy_kontynuowac == "nie":
        break