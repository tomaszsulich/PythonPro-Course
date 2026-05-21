def zsumuj_slowa() -> None:
    while True:
        nazwa_pliku = input("Podaj nazwę pliku: ")
        
        try:
            with open(nazwa_pliku, "r", encoding = "utf-8") as f:
                liczba_slow = sum(len(linia.split()) for linia in f)
                
                if liczba_slow == 0:
                    print("Plik jest pusty.")
                    
                print(f"Liczba słów: {liczba_slow}")
                break
            
        except FileNotFoundError:
            print("Podany plik nie istnieje.")
            

def main() -> None:
    zsumuj_slowa()
    
    
if __name__ == "__main__":
    main()