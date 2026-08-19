def main() -> None:
    """Uruchamia prosty kalkulator z obsługą wyjątków."""
    
    while True:
        liczba1 = input("Podaj pierwszą liczbę: ")
        liczba2 = input("Podaj drugą liczbę: ")
        operacja = input("Podaj operację (+, -, *, /): ").strip()

        try:
            liczba1 = float(liczba1)
            liczba2 = float(liczba2)

            operacje = {
                "+": lambda a, b: a + b,
                "-": lambda a, b: a - b,
                "*": lambda a, b: a * b,
                "/": lambda a, b: a / b
            }

            if operacja not in operacje:
                print("Nieznana operacja.")
                continue

            wynik = operacje[operacja](liczba1, liczba2)

        except ValueError:
            print("Podane wartości muszą być liczbami.")

        except ZeroDivisionError:
            print("Nie można dzielić przez zero.")

        else:
            print(f"Wynik: {wynik}")

        finally:
            print("Koniec obliczeń.\n")
            
            
if __name__ == "__main__":
    main()