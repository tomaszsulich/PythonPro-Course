def calculator(a: float, b: float, wybor: str):
    if wybor == "1":
        return a + b
    elif wybor == "2":
        return a - b
    elif wybor == "3":
        return a * b
    elif wybor == "4":
        if b != 0:
            return a / b
        else:
            return "Błąd: nie można dzielić przez zero!"
    else:
        return "Niepoprawny wybór!"

def pobierz_dzialanie() -> None:
    print("Wybierz działanie:")
    print("1 - dodawanie")
    print("2 - odejmowanie")
    print("3 - mnożenie")
    print("4 - dzielenie")

    wybor = input("Twój wybór: ")

    if wybor in {"1", "2", "3", "4"}:
        wynik = calculator(a, b, wybor)
        print("Wynik:", wynik)
    else:
        print("Niepoprawny wybór!")


a = float(input("Podaj pierwszą liczbę: "))
b = float(input("Podaj drugą liczbę: "))
    