kursy = {"USD": 4.0, "EUR": 4.3}

while True:
    kwota = float(input("Podaj kwotę, którą chcesz wymienić (PLN): "))
    waluta = input("Podaj walutę, na którą chcesz ją wymienić: ").upper()
    
    if waluta == "USD":
        kwota /= kursy["USD"]
    elif waluta == "EUR":
        kwota /= kursy["EUR"]
    else:
        print("Nie obsługujemy takiej waluty!")
        kwota = None
        
    if kwota is not None:
        print(f"Otrzymujesz {kwota:.2f} {waluta}.")
    
    czy_kontynuowac = input("Czy chcesz kontynuować (tak/nie)? ").lower()
    
    if czy_kontynuowac == "nie":
        break
    elif czy_kontynuowac == "tak":
        continue
    else:
        print("Podaj poprawną odpowiedź (tak/nie).")
    