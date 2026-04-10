while True:
    l0 = float(input("Podaj wartosc pierwszej liczby: "))
    l1 = float(input("Podaj wartosc drugiej liczby: "))
    dzialanie = input("Podaj dzialanie (+, -, *, /): ")
    
    if dzialanie not in {"+", "-", "*", "/"}:
        print("Niepoprawne dzialanie!")
        continue
    
    if dzialanie == "+":
        wynik = l0 + l1
    elif dzialanie == "-":
        wynik = l0 - l1
    elif dzialanie == "*":
        wynik = l0 * l1
    elif dzialanie == "/":
        if l1 == 0:
            print("Nie mozna dzielic przez zero!")
            continue
        wynik = l0 / l1
    print("Wynik: ", wynik)
    
    czy_zakonczyc = input("Czy chcesz zakonczyc program?")
    if czy_zakonczyc == "tak":
        break # natychmiastowe wyjście z pętli