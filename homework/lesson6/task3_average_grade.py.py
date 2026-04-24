def oblicz_srednia(*args):
    if len(args) == 0:
        return 0
    
    return sum(args) / len(args)
   
print(f"{oblicz_srednia(1, 2, 3):.2f}")
print(f"{oblicz_srednia(5, 4, 2, 3, 1, 6, 2):.2f}")
print(f"{oblicz_srednia():.2f}")