def stworz_profil(imie, **dane_dodatkowe):
    profil = {"imię": imie}
    
    for klucz, wartosc in dane_dodatkowe.items():
        profil[klucz] = wartosc
        
    return profil

def wyswietl_profil(profil):
    for klucz, wartosc in profil.items():
        print(f"{klucz}: {wartosc}")
    print()

profil1 = stworz_profil("Anna", wiek = 45, miasto = "Łódź", uczelnia = "UKSW")
profil2 = stworz_profil("Wojtek", wiek = 32, plec = "mężczyzna", uczelnia = "SGGW", miasto = "Warszawa")

wyswietl_profil(profil1)
wyswietl_profil(profil2)

# WERSJA Z ROZPAKOWYWANIEM SŁOWNIKA ZAMIAST PĘTLI FOR W FUNKCJI stworz_profil
# def stworz_profil(imie, **dane_dodatkowe):
#     return {"imię": imie, **dane_dodatkowe}

# def wyswietl_profil(profil):
#     for klucz, wartosc in profil.items():
#         print(f"{klucz}: {wartosc}")
#     print()

# profil1 = stworz_profil("Anna", wiek = 45, miasto = "Łódź", uczelnia = "UKSW")
# profil2 = stworz_profil("Wojtek", wiek = 32, plec = "mężczyzna", uczelnia = "SGGW", miasto = "Warszawa")

# wyswietl_profil(profil1)
# wyswietl_profil(profil2)