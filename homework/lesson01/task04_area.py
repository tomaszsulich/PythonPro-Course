# float nie wysypie programu, najczęściej stosowane w programach okienkowych
# możemy od razu zmapować zmienną, ale możemy też w osobnym kroku
length = float(input("Podaj dlugosc prostokata: ").replace(",", "."))
# replace podmienia wartości
width = float(input("Podaj szerokosc prostokata: ").replace(",", "."))

area = length * width
print(f"Pole twojego prostokata wynosi {area}.")