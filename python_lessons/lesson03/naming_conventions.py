# snake_case
user_name = "pawel"
user_password = "*******"

# PascalCase/CamelCase - dla klas
# zazwyczaj jedna pusta linia po instrukcji z wcięciem, przy definiowaniu funkcji
# automatycznie dwie

_0 = "18769" # NIEZALECANE, ZMIENNA POWINNA BYĆ SAMOOPISUJĄCA SIĘ, WIELKOŚĆ LITER WAŻNA

wiek = 10
wiek = "dziesięć" # WIEK MOŻE BYĆ STRINGIEM, PRZEZ TO PYTHON JEST TROCHĘ WOLNIEJSZY

# OBEJŚCIE SŁÓW KLUCZOWYCH, BO INACZEJ NADPISUJEMY FUNKCJĘ I JESTEŚMY W DUPIE
# CHOCIAŻ NIE POWINNO SIĘ TEGO ROBIĆ, BO MOŻE SIĘ MYLIĆ
print_ = 10
# print = 10
# print(wiek) - wywali, że print nie jest int

# STRING JEST W DUŻEJ MIERZE TRAKTOWANY TAK JAK LISTA
# JAK ZMIENNE MAJĄ OZNACZAĆ COŚ KONKRETNEGO, TO ZACZYNAMY JE OD is, has ITD., PODKREŚLAMY WAR.
czy_dorosly = False