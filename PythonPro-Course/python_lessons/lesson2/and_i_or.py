# AND i OR (bardzo często kluczowe wartości graniczne)
# bardziej Pythonowy sposób, and mniej
# w każdym innym przypadku else, inaczej elif
# można też sprawdzić czy wzrost nie jest od razu spełniony, w ten sposób trochę sobie 
# eliminujemy warunki

wzrost = float(input("Podaj wzrost:"))
czy_opiekun = input("Czy z opiekunem?")
if(czy_opiekun == "tak"):
    czy_opiekun_bool = True
else:
    czy_opiekun_bool = False

if (wzrost < 120):
    print("Nie wchodzisz!")
elif (wzrost >= 160) or czy_opiekun_bool:
    print("Możesz wejść.")
else:
    print("Nie wchodzisz.")

