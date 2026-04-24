oceny = {"Jan": 4, "Anna": 5, "Piotr": 3, "Kasia": 4}

# sorted, lambda, el. słownika (klucz, wartość) od najwyższej do najniższej wg ocen
oceny_posortowane = sorted(oceny.items(), key = lambda x: x[1], reverse = True)
print(oceny_posortowane)

slownik_posortowany = dict(oceny_posortowane)
print(slownik_posortowany)

# TO SAMO, CO WYŻEJ, ALE MNIEJ PISANIA
# slownik_posortowany = dict(
#     sorted(oceny.items(), key = lambda ocena: ocena[1], reverse = True)
# )

# MOŻEMY ROZPAKOWAĆ SŁOWNIK
# for imie, ocena in oceny_posortowane:
#     print(imie, ocena)