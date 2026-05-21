NAZWA_PLIKU = "dziennik.txt"

def dziennik(nazwa_pliku: str = NAZWA_PLIKU) -> None:
    while True:
        linia = input("Wpisz tekst: ")
        
        if linia.lower() == "koniec":
            break
        
        with open(NAZWA_PLIKU, "a", encoding = "utf-8") as f:
            f.write(linia + "\n")

           
def main() -> None:            
    dziennik()
    
    
if __name__ == "__main__":
    main()