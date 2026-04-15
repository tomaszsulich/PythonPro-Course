tekst = input("Wpisz dowolny tekst, pusty też OK: ")

if bool(tekst):
    print(f"Wprowadzony tekst to: {tekst}")
else:
    print("Wpisany tekst jest pusty (False).")