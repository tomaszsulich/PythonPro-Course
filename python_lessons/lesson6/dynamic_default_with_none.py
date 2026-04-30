def oblicz_pole_prostokata(a, b = None):
    if b is None:
        return a * a # b = a znacznie częstsze
    return a * b

oblicz_pole_prostokata(1, 10)
oblicz_pole_prostokata(1)