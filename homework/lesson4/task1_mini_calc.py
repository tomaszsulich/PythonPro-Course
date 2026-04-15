def calculator(a: float | int, b: float | int) -> None:
    dodaj = a + b
    odejmij = a - b
    pomnoz = a * b
    
    print(dodaj, odejmij, pomnoz, sep = "\n")
    
    if b != 0:
        print(a / b)
    else:
        print("Nie można dzielić przez zero!")


def main():
    a = float(input("Podaj pierwszą liczbę: "))
    b = float(input("Podaj drugą liczbę: "))
    calculator(a, b)


if __name__ == "__main__":
    main()