wiek = 18
czy_posiada_pj = True

if wiek >= 18 and czy_posiada_pj:
    print("Może prowadzić.")
    
wzrost = 119
z_opiekunem = True

if wzrost >= 160 or (z_opiekunem and wzrost >= 120):
    print("Możesz wejść.")
    
wzrost = 119
z_opiekunem = False

if wzrost >= 160 or (z_opiekunem and wzrost >= 120):
    print("Możesz wejść.")
    
wzrost = 120
z_opiekunem = True

if wzrost >= 160 or (z_opiekunem and wzrost >= 120):
    print("Możesz wejść.")
    
wzrost = 160
z_opiekunem = False

if wzrost >= 160 or (z_opiekunem and wzrost >= 120):
    print("Możesz wejść.")