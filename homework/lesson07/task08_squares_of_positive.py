liczby = [-5, 2, 8, -1, 0, 10]

# filter do wybrania tylko liczb dodatnich, map obliczenie ich kwadratów, jedna linijka
dodatnie_kwadraty = list(map(lambda x: x ** 2, filter(lambda x: x > 0, liczby)))
print(dodatnie_kwadraty)