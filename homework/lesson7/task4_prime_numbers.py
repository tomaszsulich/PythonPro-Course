def czy_pierwsza(n: int):
    startidx = 2
    if n % 2 == 1:
        startidx = 3
    for dzielnik in range(startidx, int(n/2) + 1): # doklejamy wartość środkową
        if n % dzielnik == 0:
            return False
    return True

print(list(filter(czy_pierwsza, range(2, 31))))