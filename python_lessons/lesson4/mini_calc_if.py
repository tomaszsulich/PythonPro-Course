a = float(input("Podaj pierwszą liczbę: "))
b = float(input("Podaj drugą liczbę: "))

print("Wybierz działanie: ")
print("1 - dodawanie")
print("2 - odejmowanie")
print("3 - mnożenie")
print("4 - dzielenie")

wybor = input("Twój wybór: ")

if wybor == 1:
    print("Wynik: ", a + b)
elif wybor == 2:
    print("Wynik: ", a - b)
elif wybor == 3:
    print("Wynik: ", a * b)
elif wybor == 4:
    if b != 0:
        print("Wynik: ", a / b)
    else:
        print("Błąd: nie można dzielić przez zero!")
else:
    print("Niepoprawny wybór!")