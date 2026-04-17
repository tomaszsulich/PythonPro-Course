sekret = 42

while True:
    liczba = float(input("Podaj liczbę: "))
    if liczba == sekret:
        print("Gratulacje! Odgadłeś moją liczbę!")
        break
    print("Niestety, nie myślę o tej liczbie...")
    
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
#         print("Moja liczba jest większa.")
#     else:
#         print("Moja liczba jest mniejsza.")
    
#     print("Niestety, nie myślę o tej liczbie...")