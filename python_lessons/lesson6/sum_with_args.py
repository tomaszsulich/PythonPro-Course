# def suma(liczba1, liczba2, liczba3, ...) - bardzo trudne!
def suma(*liczby): # dowolna ilość wartości
    print(liczby, type(liczby))
    
suma(1, 2, 3, 4, 5)