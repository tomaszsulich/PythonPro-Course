l0 = float(input("Podaj wartosc pierwszej liczby: "))
l1 = float(input("Podaj wartosc drugiej liczby: "))

dzialanie = input("Podaj działanie (+, -, *, /): ")

if dzialanie not in {"+", "-", "*", "/"}:
    print("Niepoprawne działanie!")

elif dzialanie == "+":
    wynik = l0 + l1
    print("Wynik:", wynik)

elif dzialanie == "-":
    wynik = l0 - l1
    print("Wynik:", wynik)

elif dzialanie == "*":
    wynik = l0 * l1
    print("Wynik:", wynik)

elif dzialanie == "/":
    if l1 == 0:
        print("Nie można dzielić przez zero!")
    else:
        wynik = l0 / l1
        print("Wynik:", wynik)