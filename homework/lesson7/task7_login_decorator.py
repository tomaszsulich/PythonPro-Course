def loguj(funkcja):
    def wrapper():
        print(f"Uruchamiam funkcję {funkcja.__name__}...")
        funkcja()
        print(f"Zakończono funkcję {funkcja.__name__}.")
    return wrapper

@loguj
def przywitaj():
    print("Cześć!")
    
przywitaj()

# WERSJA UNIWERSALNA
# def loguj(funkcja):
#     def wrapper(*args, **kwargs):
#         print(f"Uruchamiam funkcję {funkcja.__name__}...")
#         wynik = funkcja(*args, **kwargs)
#         print(f"Zakończono funkcję {funkcja.__name__}.")
#         return wynik
#     return wrapper

# @loguj
# def przywitaj():
#     print("Cześć!")