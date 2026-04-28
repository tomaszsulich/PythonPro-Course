class BladWalidacjiError(Exception):
    pass


def sprawdz_haslo(haslo: str) -> list[str]:
    bledy = []
    
    ma_wielka = False
    ma_cyfre = False
    
    for znak in haslo:
        if znak.isupper():
            ma_wielka = True
        if znak.isdigit():
            ma_cyfre = True
        
    if len(haslo) < 8:
        bledy.append("Hasło musi mieć co najmniej 8 znaków.")
    if not ma_wielka:
        bledy.append("Hasło musi zawierać co najmniej jedną wielką literę.")
    if not ma_cyfre:
        bledy.append("Hasło musi zawierać co najmniej jedną cyfrę.")
        
    if bledy:
        raise BladWalidacjiError(bledy)
    
    return bledy


def main():
    while True:
        haslo = input("Podaj hasło: ")
        
        try:
            sprawdz_haslo(haslo)
            print("Hasło jest poprawne!")
            
        except BladWalidacjiError as e:
            print("Błędy walidacji:")
            for blad in e.args[0]:
                print(f"- {blad}")
        
        while True:        
            czy_exit = input("Czy chcesz zakończyć (tak/nie)? ").lower()
        
            if czy_exit in {"tak", "nie"}:
                break
            print("Wpisz 'tak' lub 'nie'.")
            
        if czy_exit == "tak":
            break
            
            
if __name__ == "__main__":
    main()