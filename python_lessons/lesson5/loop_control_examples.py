owoce = ["jabłko", "banan", "wiśnia"]
for idx, owoc in enumerate(owoce, 1):
    if owoc == "banan":
        break
    
# i traktowane jako zmienna, i "pętlowe" nadpisane
owoce = ["jabłko", "banan", "wiśnia"]
i = 20
for i, owoc in enumerate(owoce, 1):
    if owoc == "banan":
        break
    
def skomplikowane_obliczenia(numer): ...

for num in [1, 2, 3, 4, 20, 20, 272, 27, 27, 201, 2038]:
    if num % 2 == 0:
        skomplikowane_obliczenia(num)
        
for num in [1, 2, 3, 4, 20, 20, 272, 27, 27, 201, 2038]:
    if num % 2 != 0:
        continue
    skomplikowane_obliczenia(num)
    
for num in [1, 2, 3, 4, 20, 20, 272, 27, 27, 201, 2038]:
    if not (num % 2 == 0):
        continue
    skomplikowane_obliczenia(num)
else:
    print("else się wykonał")
    
for num in [1, 2, 3, 4, 20, 20, 272, 27, 27, 201, 2038]:
    if not (num % 2 == 0):
        continue
    print(num)
    skomplikowane_obliczenia(num)
else:
    print("else się wykonał")

# wyprintuje wszystkie liczby w pętli, napotyka ostatni element, który spełnia ten warunek,
# więc program wychodzi z pętli
for num in [1, 2, 3, 4, 20, 20, 272, 27, 27, 201, 2038]:
    if num > 2036:
        break
    print(num)
    skomplikowane_obliczenia(num)
else:
    print("else się wykonał")
    
# jak znajdziemy to czego szukamy (liczy się pierwsza wartość!), to reszta nas nie obchodzi
for num in [1, 2, 3, 4, 2038, 20, 20, 272, 27, 27, 201]:
    if num > 2036:
        break
    print(num)
    skomplikowane_obliczenia(num)
else:
    print("else się wykonał")
    
# w tym przypadku dla tej jednej liczby cały pozostały kod (tj. print(num) itd.) się nie wykona
for num in [1, 2, 3, 4, 2038, 20, 20, 272, 27, 27, 201]:
    if num > 2036:
        continue
    print(num)
    skomplikowane_obliczenia(num)
else:
    print("else się wykonał")
    
def skomplikowane_obliczenia(numer):
    print("Wywołano skomplikowane_obliczenia dla ", numer)
    
for num in [1, 2, 3, 4, 2038, 20, 20, 272, 27, 27, 201]:
    if num > 2036:
        continue
    print(num)
    skomplikowane_obliczenia(num)
else:
    print("else się wykonał")

for num in [1, 2, 3, 4, 2038, 20, 20, 272, 27, 27, 201]:
    if num <= 2036:
        print(num)
        skomplikowane_obliczenia(num)
else:
    print("else się wykonał")

for num in [1, 2, 3, 4, 2038, 20, 20, 272, 27, 27, 201]:
    if num <= 2036:
        print(num)
        skomplikowane_obliczenia(num)
        
        if num > 20:
            ...
        else:
            ...
            # coś innego
else:
    print("else się wykonał")
    
for num in [1, 2, 3, 4, 2038, 20, 20, 272, 27, 27, 201]:
    if num > 2036:
        continue
    
    print(num)
    skomplikowane_obliczenia(num)
    
    if num > 20:
        ...
    else:
        ...
        # coś innego
else:
    print("else się wykonał")