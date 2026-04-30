# lista z wartościami <1, 5>
lst = []
for i in range(1, 6):
    lst.append(i)
print("for lst", lst)

# x = "wartosc pod warunkiem" if warunek else "wartosc domyslna"

lst_comp = [i for i in range(1, 6)]
print("lst comp", lst_comp)

lst_comp = [element for element in range(1, 6) if element % 2 == 0] # parzyste
print("lst comp", lst_comp)

# zapis czytelniejszy
lst_comp = [element * element
            for element in range(1, 6)
            if element % 2 == 0]

lst_pow = []
for element in range(1, 6):
    if element % 2 == 0:
        lst_pow.append(element * element)
        
print("el * el", lst_comp)