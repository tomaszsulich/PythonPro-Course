def bezpieczne_dzielenie(a: float, b: float) -> float | None:
    """Zwraca wynik dzielenia dwóch liczb lub None przy dzieleniu przez zero."""
    
    try:
        return a / b
    
    except ZeroDivisionError:
        print("Błąd: Dzielenie przez zero!")
        return None


def main() -> None:
        a = float(input("Podaj pierwszą liczbę: "))
        b = float(input("Podaj drugą liczbę: "))
        
        wynik = bezpieczne_dzielenie(a, b)
        
        if wynik is not None:
            print(f"Wynik dzielenia {a} przez {b} to: {wynik}")
        

if __name__ == "__main__":
    main()