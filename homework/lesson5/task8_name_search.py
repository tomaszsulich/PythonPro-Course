imiona = ["Anna", "Jan", "Piotr", "Kasia"]
szukane = input("Podaj imię: ").lower()

for imie in imiona:
    if imie.lower() == szukane:
        print("Znaleziono!")
        break
else:
    print("Nie znaleziono imienia na liście.")