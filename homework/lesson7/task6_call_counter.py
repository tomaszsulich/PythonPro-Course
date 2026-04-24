def stworz_licznik():
    i = 0
    
    def licznik():
        nonlocal i
        i += 1
        return i
    
    return licznik

licz = stworz_licznik()

print(licz()) # 1
print(licz()) # 2
print(licz()) # 3

# WERSJA Z KONTROLOWANYM STARTEM
# def stworz_licznik(start = 0):
#     i = start
    
#     def licznik():
#         nonlocal i
#         i += 1
#         return i
    
#     return licznik

# licz = stworz_licznik(5)

# print(licz()) # 6
# print(licz()) # 7