# ZMIENNA ISTNIEJE, ALE JESZCZE NIE MA WARTOŚCI
wiek: int = None

imie: str = "pawel" # ZMIENNE MOŻNA HINTOWAĆ, ALE JEST TO BEZ SENSU

imie = "pawel"
wiek = 25
srednia_ocen = [3, 2, 3, 5, 4]
czy_student = True

suma_ocen = 0
licznik = 0

for ocena in srednia_ocen:
    suma_ocen += ocena
    licznik += 1
    
print(srednia_ocen)

# WERSJA PYTHONOWA
oceny = [3, 2, 3, 5, 4]
srednia_ocen = sum(oceny) / len(oceny)

def opisz_zmienna(zmienna):
    return f"{zmienna=}[{type(zmienna.__class__)}]" # WYŚWIETLA BEZ CLASS

for zmienna in (imie, wiek, srednia_ocen, czy_student):
    print(opisz_zmienna(zmienna))
    
student = {
    "imie": imie,
    "wiek": wiek,
    "sr_ocen": srednia_ocen,
    "czy_student": czy_student
    # GDYBYŚMY TU DAWALI oceny, TO PRZY ZMIANIE oceny/student[oceny] DRUGA TEŻ BY SIĘ ZMIENIAŁA
}

# LEPSZE JAK ZALEŻY NA NAZWACH, MOŻEMY OD RAZU WYCIĄGAĆ WART., NIE MUSI BYĆ PRZEZ SŁOWNIK
for key, value in student.items():
    print(key, ":", value)
