def powtorz(n):
    def dekorator(funkcja):
        def wrapper():
            for _ in range(n):
                funkcja()
        return wrapper
    return dekorator

@powtorz(3)
def przywitaj():
    print("Cześć!")
    
przywitaj()

# WERSJA UNIWERSALNA
# def powtorz(n):
#     def dekorator(funkcja):
#         def wrapper(*args, **kwargs):
#             for _ in range(n):
#                 funkcja(*args, **kwargs)
#         return wrapper
#     return dekorator

# @powtorz(3)
# def przywitaj():
#     print("Cześć!")
    
# przywitaj()