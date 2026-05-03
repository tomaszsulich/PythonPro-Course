linie = ["linia1", "linia2", "linia3"]

with open("dane.txt", encoding = "utf8", mode = "w") as f:
    # dba o Entery niejako za nas
    print(f.write("\n".join(linie)))






linie = [10, 11, 12]

with open("dane.txt", encoding = "utf8", mode = "w") as f:
    # tuple comprehension
    print(f.write("\n".join(str(l) for l in linie)))
    # zmapowanie wartości na string
    print(f.write("\n".join(map(str, linie))))