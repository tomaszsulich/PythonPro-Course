dzialanie = input("Podaj dzialanie matematyczne (+, -, *, /): ")
# poprawna odpowiedź: "+", "-", "*", "/"

if dzialanie not in {"+", "-", "*", "/"}:
    print("Niepoprawne działanie!")