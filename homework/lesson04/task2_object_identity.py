a, b, c = 256, 256, 256
d, e, f = 257, 257, 257

print(f"id(a) = {id(a)}, id(b) = {id(b)}, id(c) = {id(c)}")
print(f"id(d) = {id(d)}, id(e) = {id(e)}, id(f) = {id(f)}")

# dodatkowy tekst pokazujący różnicę w tworzeniu obiektów
x, y, z = int("257"), int("257"), int("257")
print(f"id(x) = {id(x)}, id(y) = {id(y)}, id(z) = {id(z)}")

# Python stosuje optymalizację pamięci dla małych liczb (small integer caching),
# dlatego zmienne o wartości 256 często wskazują na ten sam obiekt.

# Dla większych liczb (np. 257) Python może tworzyć osobne obiekty, ale w niektórych
# przypadkach (np. w jednej linii kodu) może również użyć optymalizacji i przypisać
# ten sam obiekt.

# W przykładzie z int("257") wymuszamy tworzenie nowych obiektów, co pozwala zauważyć
# różnicę w identyfikatorach.