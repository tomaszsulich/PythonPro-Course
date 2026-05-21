sekret = 42

while True:
    liczba = int(input("Podaj liczbę z zakresu 0-100: "))
    
    if liczba == sekret:
        print("Gratulacje! Odgadłeś moją liczbę!")
        break
    elif liczba < sekret:
        print("Za mało!")
    else:
        print("Za dużo!")
    
# WERSJA Z CAŁKOWICIE RANDOMOWYMI LICZBAMI
# from random import random

# sekret = round(random(), 2)

# while True:
#     liczba = round(float(input("Podaj liczbę (0-1, 2 miejsca po przecinku): ").replace(",", ".")), 2)
    
#     if not (0 <= liczba <= 1):
#         print("Podaj liczbę z zakresu 0–1!")
#         continue
    
#     if liczba == sekret:
#         print(f"Gratulacje! Odgadłeś moją liczbę! Było to {sekret}.")
#         break
#     elif liczba < sekret:
#         print("Za mało!")
#     else:
#         print("Za dużo!")