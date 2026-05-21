def wczytaj_plik():
    sciezka = input("Podaj ścieżkę do pliku: ")
    try:
        plik = open(sciezka, mode = 'r')
        print("plik istnieje")
    except FileNotFoundError:
        print(f"plik o nazwie {sciezka} nie istnieje")
    except PermissionError:
        print(f"brak dostępu do pliku {sciezka}")
    else:
        plik.close()

        
wczytaj_plik()