def jakas_funkcja(a, lst = []):
    print(id([lst]))
    
jakas_funkcja(1)
jakas_funkcja(2) # IDENTYCZNE ID CO WYŻEJ!

def jakas_funkcja(a, lst = None):
    if lst is None:
        lst = []
    print(id(lst), lst)
    
lst0 = jakas_funkcja(1)
lst1 = jakas_funkcja(2) # TO SAMO CO WYŻEJ! CZYŚCI PAMIĘĆ I NADPISUJE TO SAMO MIEJSCE.

def jakas_funkcja(a, lst = None):
    if lst is None:
        lst = []
    print(id(lst), lst)
    return lst
    
lst0 = jakas_funkcja(1)
lst1 = jakas_funkcja(2) # W TYM PRZYPADKU JUŻ DAJE RÓŻNE LISTY