with open("safe_calculator_dict.py", encoding = "utf8") as f:
    # operacje na pliku
    print(f.readlines(1))
# <= wyszliśmy z wcięcia, program automatycznie zamknął plik

with open("dane.txt", encoding = "utf8", mode = "w") as f:
    print(f.write("moja pierwsza zapisana w pliku linia <3"))
    
with open("dane.txt", encoding = "utf8", mode = "w") as f:
    print(f.write("no i druga moja linia"))