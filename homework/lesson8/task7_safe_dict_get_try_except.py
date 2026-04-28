def pobierz_wartosc(slownik: dict[str, object], klucz: str) -> object | None:
    return slownik.get(klucz)

def pobierz_wartosc_try(slownik: dict[str, object], klucz: str) -> object | None:
    try:
        return slownik[klucz]
    except KeyError:
        return None

    
def main():
    slownik = {"imie": "Tomek"}
    
    print(pobierz_wartosc(slownik, "imie"))
    print(pobierz_wartosc(slownik, "wiek"))
    
    print(pobierz_wartosc_try(slownik, "imie"))
    print(pobierz_wartosc_try(slownik, "wiek"))
    
       
if __name__ == "__main__":
    main()