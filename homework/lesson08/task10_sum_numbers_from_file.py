def sumuj_liczby_z_pliku() -> None:
    nazwa = input("Podaj nazwę pliku: ")
    suma = 0

    try:
        with open(nazwa, mode="r") as plik:
            for linia in plik:
                try:
                    liczba = float(linia.strip())
                    suma += liczba
                except ValueError:
                    # ignorujemy błędne linie
                    continue
                
    except FileNotFoundError:
        print(f"Plik o nazwie {nazwa} nie istnieje.")
        
    finally:
        print(f"Suma liczb z pliku: {suma}")
        
        
def main():
    while True:
        sumuj_liczby_z_pliku()
        while True:
            czy_exit = input("Czy chcesz zakończyć program (tak/nie)? ").lower()
        
            if czy_exit in {"tak", "nie"}:
                break
            print("Wpisz 'tak' lub 'nie'.")
                
        if czy_exit == "tak":
            break
    
    
if __name__ == "__main__":
    main()