def analiza_listy(lista: list[int]):
    return min(lista), max(lista), sum(lista)

print(analiza_listy([1, 2, 3, 8, 6, 5, 7]))

# WERSJA ALTERNATYWNA, ALE DŁUŻSZA
# def analiza_listy(lista: list[int]):
#     minimum = min(lista)
#     maximum = max(lista)
#     suma = sum(lista)
#     return minimum, maximum, suma

# print(analiza_listy([1, 2, 3, 8, 6, 5, 7]))