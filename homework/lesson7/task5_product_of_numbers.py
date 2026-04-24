from functools import reduce
liczby = [1, 2, 3, 4, 5]

iloczyn = reduce(lambda akumulator, element: akumulator * element, liczby)
print(f"Iloczyn liczb {liczby} = {iloczyn}")