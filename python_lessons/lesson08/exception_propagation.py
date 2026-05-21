# bardzo głęboka walidacja, np. wiek; bardzo często wykorzystywane
def funkcja():
    raise ValueError("mój komentarz")

def funkcja_nadrzedna():
    return funkcja()

def funkcja_nadnadrzedna():
    try:
        return funkcja_nadrzedna()
    except ValueError:
        print("przechwyciłem go 2 funkcje wyżej")