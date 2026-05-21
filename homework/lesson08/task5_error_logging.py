def pobierz_liczbe() -> float:
    return float(input("Podaj liczbę: ").replace(",", "."))
        
def kalkulator() -> None:
    while True:
        log = open("log.txt", mode = "a", encoding = "utf-8")
        
        try:
            log = open("log.txt", mode = "a", encoding = "utf-8")
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
        
        except ValueError as e:
            log.write(f"ValueError: {e}\n")
            print("WPROWADZONE DANE MUSZĄ BYĆ LICZBAMI!")
        except ZeroDivisionError as e:
            log.write(f"ZeroDivisionError: {e}\n")
            print("NIE WOLNO DZIELIĆ PRZEZ ZERO!")
            
        else:
            print(f"{a} {operacja} {b} = {wynik}")
            
        finally:
            log.close()
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