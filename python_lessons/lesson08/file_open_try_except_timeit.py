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
def sprobuj_wczytac_plik(filepath):
    try:
        begfileload = time.time()
        res = open(filepath)
        print(f"plik istnieje, czas wczytywania, {time.time()-begfileload:.5f}")
        return res
    except FileNotFoundError:
        print("plik nie istnieje")
        return None
    
    # zbliżone czasy wczytywania