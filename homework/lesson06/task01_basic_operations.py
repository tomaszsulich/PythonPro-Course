def kalkulator(a: float | int, b: float | int, operacja: str) -> float | int | None:
    if operacja == "+":
        return a + b
    elif operacja == "-":
        return a - b
    elif operacja == "*":
        return a * b
    elif operacja == "/":
        if b == 0:
            return None
        return a / b
    else:
        print("Niepoprawne działanie!")
        return None
        
def pobierz_liczbe():
    return float(input("Podaj liczbę: ").replace(",", "."))
    
a = pobierz_liczbe()
b = pobierz_liczbe()
operacja = input("Podaj operację (+, -, *, /): ")

wynik = kalkulator(a, b, operacja)

if wynik is None:
    print("Nie można wykonać działania.")
else:
    print(f"{a} {operacja} {b} = {wynik}")