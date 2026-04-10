def pobierz_dodatnia_liczbe(komunikat):
    while True:
        wartosc = float(input(komunikat))
        if wartosc > 0:
            return wartosc
        print("Wartosc musi byc wieksza od zera.")

dlugosc = pobierz_dodatnia_liczbe("Podaj długość prostokata: ")
szerokosc = pobierz_dodatnia_liczbe("Podaj szerokość prostokata: ")

obwod = 2 * (dlugosc + szerokosc)

print(f"Obwód tego prostokata wynosi {obwod}.")