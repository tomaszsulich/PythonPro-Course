class WiekNiepoprawnyError(Exception):
    """Wyjątek zgłaszany, gdy użytkownik ma mniej niż 18 lat."""
    pass


def rejestruj_uzytkownika(wiek: int) -> str:
    if wiek < 18:
        raise WiekNiepoprawnyError("Masz mniej niż 18 lat.")
    print("Masz co najmniej 18 lat.")


def main():
    while True:
        try:
            wiek = int(input("Podaj wiek: "))
            rejestruj_uzytkownika(wiek)
            
        except ValueError:
            print("WIEK MUSI BYĆ LICZBĄ!")
        except WiekNiepoprawnyError as e:
            print(f"Błąd walidacji: {e}")
            
        else:
            print("Rejestracja zakończona sukcesem!")
            
        finally:
            print("Kolejna próba...\n")
            
        while True:
            czy_exit = input("Czy chcesz zakończyć program (tak/nie)? ").lower()
            
            if czy_exit in {"tak", "nie"}:
                break
            print("Wpisz 'tak' lub 'nie'.")
                
        if czy_exit == "tak":
            break
        

if __name__ == "__main__":
    main()