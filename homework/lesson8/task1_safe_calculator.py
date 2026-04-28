def pobierz_liczbe() -> float:
    while True:
        try:
            return float(input("Podaj liczbę: ").replace(",", "."))
        except ValueError:
            print("WPROWADZONE DANE MUSZĄ BYĆ LICZBAMI!")
        
def kalkulator() -> None:
    while True:
        try:
            a = pobierz_liczbe()
            b = pobierz_liczbe()
            operacja = input("Podaj operację (+, -, *, /): ")
            
            if operacja == "+":
                wynik = a + b
            elif operacja == "-":
                wynik = a - b
            elif operacja == "*":
                wynik = a * b
            elif operacja == "/": 
                wynik = a / b
            else:
                print("Niepoprawne działanie!")
                continue
        
        except ValueError:
            print("WPROWADZONE DANE MUSZĄ BYĆ LICZBAMI!")
        except ZeroDivisionError:
            print("NIE WOLNO DZIELIĆ PRZEZ ZERO!")
            
        else:
            print(f"{a} {operacja} {b} = {wynik}")
            
        finally:
            print("Kolejna operacja...")
        
        while True:
            czy_exit = input("Czy chcesz zakończyć program (tak/nie)? ").lower()
        
            if czy_exit in {"tak", "nie"}:
                break
            print("Wpisz 'tak' lub 'nie'.")
                
        if czy_exit == "tak":
            break


def main():    
    kalkulator()
        
        
if __name__ == "__main__":
    main()