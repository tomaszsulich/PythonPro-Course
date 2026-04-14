def pobierz_bool(komunikat):
    while True:
        wartosc = int(input(komunikat))
     
        if wartosc in (0, 1):
            return bool(wartosc)
        print("Podano niepoprawne dane!")

a_bool = pobierz_bool("Podaj pierwszą wartość (1 lub 0): ")
b_bool = pobierz_bool("Podaj drugą wartość (1 lub 0): ")

print("AND:", a_bool and b_bool)
print("OR:", a_bool or b_bool)