wiek = int(input("Podaj swój wiek (w latach, jako liczba całkowita): "))

if wiek < 0:
    print("Wiek nie może być ujemny!")
elif wiek <= 1:
    print("Niemowlę.")
elif wiek <= 12:
    print("Dziecko.")
elif wiek <= 17:
    print("Nastolatek.")
elif wiek <= 64:
    print("Dorosły.")
else:
    print("Senior.")