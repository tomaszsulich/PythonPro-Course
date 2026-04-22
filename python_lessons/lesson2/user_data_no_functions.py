# zapytaj kolejno uzytkownika o imie, wiek i miasto
# przechowaj odpowiedzi w slowniku
# wypelnij danymi ze slownika zdanie
# A więc, masz na imię [Imie], masz [Wiek] lat i mieszkasz w mieście [Miasto]

# for informacja in ("imie", "wiek", "miasto"):
#    dane_uzytkownika[informacja] = input(f"Wprowadz {informacja}" + ": ")

# print(dane_uzytkownika)
# print(
#   f"A więc, masz na imię {dane_uzytkownika['imie']}", "
#    "masz {dane_uzytkownika['wiek] lat}"
#    "i mieszkasz w mieście {dane_uzytkownika['miasto]}."   
# )

# ALBO

# zmiana polecenia w kolejnych obrotach pętli
dane_uzytkownika = {}

for informacja in ("imie", "wiek", "miasto"):
   dane_uzytkownika[informacja] = input("Wprowadz " + informacja + ": ")

print(dane_uzytkownika)
print(
    f"A więc, masz na imię {dane_uzytkownika['imie']}, "
    f"masz {dane_uzytkownika['wiek']} lat "
    f"i mieszkasz w mieście {dane_uzytkownika['miasto']}."
)
