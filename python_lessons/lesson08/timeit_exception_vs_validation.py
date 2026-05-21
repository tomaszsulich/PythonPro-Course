import os
import time
filepath = "nieist.txt"

def timeit(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        res = func(*args, **kwargs)
        end = time.time()
        print(f"czas operacji {end - start:.5f}")
        return res
    return wrapper

@timeit
def sprobuj_zmapowac(mapujz):
    try:
        int("mapujz")
    except ValueError:
        print("nie udało się zmapować na int")
        return None
    
@timeit
def zmapuj_jezeli(mapujz: str):
    for char in mapujz:
        if not char.isdigit():
            return None
    return int(mapujz)
    
sprobuj_zmapowac("test.txt")
sprobuj_zmapowac("100")
sprobuj_zmapowac("290")
sprobuj_zmapowac("290282762789928")
sprobuj_zmapowac("29092827629928")
sprobuj_zmapowac("t")
zmapuj_jezeli("9857676557884889939202029498484")
zmapuj_jezeli("tekst")