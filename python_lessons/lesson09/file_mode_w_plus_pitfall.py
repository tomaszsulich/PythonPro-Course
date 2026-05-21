with open("dane.txt", encoding = "utf8", mode = "w+") as f:
    calytext = f.read()
    calytext2 = f.read()
    # wczytał plik, wyczyścił i dupa
    
print(calytext, calytext2, sep = "\n")