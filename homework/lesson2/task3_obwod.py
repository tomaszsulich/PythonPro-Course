def pobierz_dodatnia_liczbe(komunikat):
    while True:
        wartosc = float(input(komunikat))
        if wartosc > 0:
            return wartosc
        print("Wartość musi być większa od zera.")

dlugosc = pobierz_dodatnia_liczbe("Podaj długość prostokata: ")
szerokosc = pobierz_dodatnia_liczbe("Podaj szerokość prostokata: ")

obwod = 2 * (dlugosc + szerokosc)

print(f"Obwód tego prostokata wynosi {obwod}.")

# WERSJA PODSTAWOWA - OD PAWŁA
# dlugosc = float(input("Podaj długość: "))
# szerokosc = float(input("Podaj szerokość: "))

# obwod = 2 * (dlugosc + szerokosc)

# print("Obwód prostokąta wynosi:", obwod)
