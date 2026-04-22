# funkcja sterowana flagami bool — wykonuje pierwszy spełniony warunek
# 
def wypisz_argumenty(arg1 = False, arg2 = False, arg3 = False, arg4 = False):
    if arg1:
        ... # placeholder - program coś tam robi
    elif arg2:
        print(arg2)
    elif arg3:
        ...
    elif arg4:
        ...
        
wypisz_argumenty(arg2 = True) # ustaw parametr arg2 na True (przekazanie argumentu nazwą,
# czyli nic innego jak keywoard argument, tj. kwarg)

osoba = {"imie": "Robert",
         "wzrost": 179,
         "adres": ...,
         "praca": "praca Roberta"}
print(osoba)

# słowniki są dynamiczne - można dodawać nowe klucze po utworzeniu
# dodanie wartości tylko przez klucz
osoba["czy_ma_psa"] = False

# metoda pop() usuwa element (m. in. w listach oraz słownikach) i zwraca jego wartość
zwrocona_wartosc = osoba.pop("wzrost")
print(osoba)

print(zwrocona_wartosc)
