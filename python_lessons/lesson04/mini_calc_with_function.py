a = float(input("Podaj pierwszą liczbę: "))
b = float(input("Podaj drugą liczbę: "))

def calculator(a: float | int, b: float | int) -> None:
    result1 = a + b
    result2 = a * b
    result3 = a / b
    result4 = a - b

    print(result1, result2, result3, result4, sep="\n")
    
calculator(a, b)