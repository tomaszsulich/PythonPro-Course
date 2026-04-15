tekst = input("Wpisz dowolny tekst, pusty też OK: ")

if bool(tekst):
    print("Wprowadzony tekst to: {tekst}")
else:
    print("Wpisany tekst jest pusty (False)")