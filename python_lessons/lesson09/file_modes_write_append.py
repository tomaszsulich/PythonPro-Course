with open("dane.txt", encoding = "utf8", mode = "w") as f:
    print(f.write("moja pierwsza zapisana w pliku linia <3"))
    
with open("dane.txt", encoding = "utf8", mode = "w") as f:
    print(f.write("no i druga moja linia"))
    
with open("dane.txt", encoding = "utf8", mode = "a") as f:
    # tworzy znak nowej linii na końcu, bardziej poprawne by było na początku
    print(f.write("no i druga moja prawdziwa linia\n"))