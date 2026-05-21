# tuple są niemutowalne (nie można podmieniać wartości), często trochę szybsze
# i bezpieczniejsze, bo nie można ich przypadkowo zmienić
tuple0 = (10, 20, 30)

# słowniki przechowują dane w postaci klucz : wartość
# pozwalają szybko wyszukiwać dane po kluczu
dict0 = {'pn': 20,
         'wt': 21,
         'sr': 22}
print(dict0['wt'])

# get zwraca wartość domyślną (None), jeśli nie znajdzie klucza
# można podać własną wartość domyślną po przecinku
print(dict0.get("cz")) # None
print(dict0.get("cz"), 0) # 0
print(dict0.get("pt", "brak")) # "brak"
