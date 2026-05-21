def opis_ksiazki(tytul, autor, rok_wydania = 2024):
    return f"Książka '{tytul}' została napisana przez {autor} i wydana w roku {rok_wydania}."

# test z argumentami pozycyjnymi
print(opis_ksiazki("Wesele", "Stanisław Wyspiański", 1900))

# test z argumentami nazwanymi
print(opis_ksiazki(tytul = "Wesele", autor = "Stanisław Wyspiański", rok_wydania = 1900))

# domyślny argument
print(opis_ksiazki("Dolina cieni", "Remigiusz Mróz"))