for i in range(3):
    print(i)
    
for i in range(1, 3):
    print(i)
    
owoce = ["jabłko", "banan", "wiśnia"]
range(10) # => [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

for i in owoce:
    print(i)

# w tym przypadku pętla for przejdzie po wszystkich znakach, elementach stringa  
for i in "pawel":
    print(i)
    
for i in range(len(owoce)): # range(3) => 0, 1, 2
    owoce[i]

# powyższa wersja for została zastąpiona przez tą, bo częściej się z niej korzystało
for i in owoce: # range(3) => 0, 1, 2
    i
    
for owoc in owoce: # range(3) => 0, 1, 2
    owoc
    
for idx, owoc in enumerate(owoce): # range(3) => 0, 1, 2
    print(idx, owoc)

# zwróci nam tuplę
for para_wartosci in enumerate(owoce): # range(3) => 0, 1, 2
    print(para_wartosci)
    
# rozpakuje nam parę wartości
for para_wartosci in enumerate(owoce): # range(3) => 0, 1, 2
    idx, owoc = para_wartosci
    print(para_wartosci)

# modyfikujemy tak, aby zaczynać od jedynki
for idx, owoc in enumerate(owoce, 1): # range(3) => 0, 1, 2
    print(str(idx) + ".", owoc) # f-string też by zadziałał, ale to krótsze i szybsze
    
    print(f"{idx}.", owoc)