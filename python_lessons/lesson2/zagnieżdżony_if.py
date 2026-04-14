# jeśli w każdym warunku mamy wspólną zmienną, to możemy zagnieździć if'a

wzrost = float(input("Podaj wzrost: "))

if wzrost < 120:
    print("Nie wchodzisz!")
elif wzrost < 160:
    czy_opiekun_bool = input("Czy z opiekunem? ")
    if czy_opiekun_bool == "tak":
        print("Możesz wejść.")
    else:
        print("Nie wchodzisz.")
else:
    print("Możesz wejść.")