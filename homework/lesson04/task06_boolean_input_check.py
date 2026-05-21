tekst = input("Wpisz dowolny tekst, pusty też OK: ")

# bool tak naprawdę jest tu zbędny, ponieważ pusty string = False, niepusty = True
if bool(tekst):
    print(f"Wprowadzony tekst to: {tekst}")
else:
    print("Wpisany tekst jest pusty (False).")