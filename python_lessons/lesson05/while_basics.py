i = 0
while i < 10:
    print(i)
    i += 1
    
i = 0
while True:
    print(i)
    if i > 9:
        print("break dla i=", i)
        break
    i += 1

# przykład pętli bez efektu widocznego na zewnątrz
i = 0
while i < 10:
    i += 1