a, b, c = 256, 256, 256
d, e, f = 257, 257, 257

print(id(a), id(b), id(c))
print(id(d), id(e), id(f))

# dodatkowy tekst pokazujący różnicę w tworzeniu obiektów
x, y, z = int("257"), int("257"), int("257")
print(id(x), id(y), id(z))

# Python stosuje optymalizację pamięci dla małych liczb (small integer caching),
# dlatego zmienne o wartości 256 często wskazują na ten sam obiekt.

# Dla większych liczb (np. 257) Python może tworzyć osobne obiekty, ale w niektórych
# przypadkach (np. w jednej linii kodu) może również użyć optymalizacji i przypisać
# ten sam obiekt.

# W przykładzie z int("257") wymuszamy tworzenie nowych obiektów, co pozwala zauważyć
# różnicę w identyfikatorach.