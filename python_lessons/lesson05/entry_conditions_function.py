def czy_wchodzi(wzrost, z_opiekunem):
    if wzrost >= 160 or (z_opiekunem and wzrost >= 120):
        print("Możesz wejść.")
    print("Nie możesz wejść.")
    
czy_wchodzi(119, False)
czy_wchodzi(119, True)
czy_wchodzi(120, False)
czy_wchodzi(120, True)
...

z_opiekunem = True
wzrost = 120

if not z_opiekunem and wzrost < 120:
    print("Idź po rodzica.")
    
def czy_wchodzi(wzrost, z_opiekunem):
    if not (z_opiekunem and wzrost < 120):
        print("Idź po rodzica.")
    elif wzrost >= 160 or (z_opiekunem and wzrost >=120):
        print("Możesz wejść.")
        
if czy_wchodzi(wzrost, z_opiekunem):
    print("Idź po rodzica.")
    
if 10 in {1, 2, 3, 4, 5, 6}:
    print("10 jest w zbiorze.")
else:
    print("10 nie jest w zbiorze.")
    
if 10 not in {1, 2, 3, 4, 5, 6}:
    print("10 nie jest w zbiorze.")
else:
    print("10 jest w zbiorze.")
    
x, y, z = 1, 2, 3

x = y = z = 3