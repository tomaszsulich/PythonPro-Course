with open("dane.txt", encoding = "utf8", mode = "r") as f:
    for line in f:
        print(line, end = "")
    # f.readlines() <- listę linii: list[str], równoważne z f.read().split("\n")
    # f.read() <- cały plik jako str: str
    
with open("dane.txt", encoding = "utf8", mode = "r") as f:
    calytext = f.read()
    # umożliwia drugi raz wyświetlenie tego samego w pliku
    f.seek(0)
    calytext2 = f.read()
    
print(calytext, "mój sep", calytext2, sep = "\n")