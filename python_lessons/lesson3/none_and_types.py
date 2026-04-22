def some_():
    3 * 2
print(some_()) # zwraca None

if not some_():
    print("None jest jak False.")
    
if some_() is None: # porównuje czy to są te same obiekty
    print("None jest jak False.")
    
print(type(10))

x = None
print(type(x))

print(x, float(x), str(float(x)))