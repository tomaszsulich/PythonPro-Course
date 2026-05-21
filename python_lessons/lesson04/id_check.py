# id są wszędzie takie same, wg prowadzącego nie powinny być, ale po co Python ma śmiecić xD
a, b, c = 256, 256, 256
print(id(a), id(b), id(c))

x, y, z = 257, 257, 257
print(id(x), id(y), id(z))

x, y, z = int("257"), int("257"), int("257") # w tym przypadku daje inny adres w pamięci
print(id(x), id(y), id(z))

# można to też było zrobić z pętlą for i tuplą, tj. for var in (a, b, c)