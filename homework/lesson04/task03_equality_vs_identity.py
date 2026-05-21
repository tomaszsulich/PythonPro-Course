lista1 = [1, 1]
lista2 = [1, 1]

print(f"Czy lista1 i lista2 mają tę samą wartość? {lista1 == lista2}")
print(f"Czy lista1 i lista2 to ten sam obiekt? {lista1 is lista2}")

# Operator '==' porównuje wartości obiektów (czy zawartość jest taka sama).
# Operator 'is' porównuje tożsamość obiektów (czy to dokładnie ten sam obiekt w pamięci).

# W tym przypadku listy mają tę samą wartość (== True), 
# ale są różnymi obiektami w pamięci (is False).

# Kolekcje (np. listy) nie współdzielone w pamięci tak jak małe liczby,
# dlatego każda lista tworzona jest jako nowy obiekt.