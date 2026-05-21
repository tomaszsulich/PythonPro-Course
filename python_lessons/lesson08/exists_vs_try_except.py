import os
filepath = "nieistniejacyplik.txt"

os.path.exists(filepath)
if os.path.exists(filepath):
    print("plik istnieje")
    open(filepath) # w większości języków tak, w Pythonie wyjątki
else:
    print("plik nie istnieje")