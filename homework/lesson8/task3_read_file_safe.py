def wczytaj_plik() -> None:
    sciezka = input("Podaj ścieżkę do pliku: ")
    
    try:
        plik = open(sciezka, mode = "r")
        print(f"Plik o nazwie {sciezka} istnieje.")
    except FileNotFoundError:
        print(f"Plik o nazwie {sciezka} nie istnieje.")
    except PermissionError:
        print(f"Brak dostępu do pliku {sciezka}")
    else:
        plik.close()
            

def main():
    while True:
        wczytaj_plik()
        czy_exit = input("Czy chcesz zakończyć program (tak/nie)? ").lower()
        
        if czy_exit not in {"tak", "nie"}:
            print("Wpisz 'tak' lub 'nie'.")
            continue
                
        if czy_exit == "tak":
            break

if __name__ == "__main__":
    main()
    
# WERSJA Z MINIMALNĄ POPRAWKĄ
# def wczytaj_plik() -> None:
#     sciezka = input("Podaj ścieżkę do pliku: ")
    
#     try:
#         with open(sciezka, mode="r") as plik:
#             print(f"Plik o nazwie {sciezka} istnieje.")
#     except FileNotFoundError:
#         print(f"Plik o nazwie {sciezka} nie istnieje.")
#     except PermissionError:
#         print(f"Brak dostępu do pliku {sciezka}")
#     else:
#         plik.close()


# def main():
#     while True:
#         wczytaj_plik()
#         czy_exit = input("Czy chcesz zakończyć program (tak/nie)? ").lower()
        
#         if czy_exit not in {"tak", "nie"}:
#             print("Wpisz 'tak' lub 'nie'.")
#             continue
                
#         if czy_exit == "tak":
#             break
    

# if __name__ == "__main__":
#     main()