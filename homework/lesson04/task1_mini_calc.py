def calculator(a: float | int, b: float | int) -> None:
    dodaj = a + b
    odejmij = a - b
    pomnoz = a * b
    
    if b == 0:
        podziel = "Nie można dzielić przez zero!"
    else:
        podziel = a / b
    
    print(dodaj, odejmij, pomnoz, podziel, sep = "\n")


def main():
    a = float(input("Podaj pierwszą liczbę: "))
    b = float(input("Podaj drugą liczbę: "))
    calculator(a, b)


if __name__ == "__main__":
    main()