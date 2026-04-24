def silnia(n: int) -> int:
    if n == 0:
        return 1
    else:
        return n * silnia(n-1)

n = int(input("Jakiej liczby chcesz policzyć silnię? "))
print(f"{n}! = {silnia(n)}")