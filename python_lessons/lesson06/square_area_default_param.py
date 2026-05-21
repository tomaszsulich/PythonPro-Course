def pole_kwadratu(a=1):
    print(f"pole kwadratu o boku {a} = {a * a}")
    # return None
    
bok = float(input("Podaj bok kwadratu: "))
pk = pole_kwadratu(a = bok) # dużo parametrów, nie wszystkie obowiązkowe

print(pk)