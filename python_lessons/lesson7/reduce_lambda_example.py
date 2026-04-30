from functools import reduce

liczby = [1, 2, 3, 4, 5, 6]

print(
    reduce(
        lambda akumulator, element: akumulator + element, liczby
    )
)