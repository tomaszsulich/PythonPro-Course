# sprawdzenie czy break się wykonał - C++, C# itd.break_
break_ = False

for num in [1, 2, 3, 4, 2038, 20, 20, 272, 27, 27, 201]:
    if num > 2036:
        break_ = True
        break
    
if break_uruchomiony:
    ...
else:
    ... # inna reakcja
    
# sprawdzenie czy break się wykonał - sprawdzenie warunku 2 razy, ale zawsze coś,
# mniej poprawne niż z flagą 
break_ = False

for num in [1, 2, 3, 4, 2038, 20, 20, 272, 27, 27, 201]:
    if num > 2036: # dla 2040 daje False
        break_ = True
        break

break_ = num > 2036

if break_:
    print(True)
else:
    print(False)

# wyświetla True i False - sposób z flagą    
break_ = False

for num in [1, 2, 3, 4, 2038, 20, 20, 272, 27, 27, 201]:
    if num > 2036:
        break_ = True
        break
    
if break_:
    print(True)
else:
    print(False)

# sposób z przypisaniem False do break   
for num in [1, 2, 3, 4, 2038, 20, 20, 272, 27, 27, 201]:
    if num > 2036:
        break_ = True
        break
else:
    break_ = False
    
if break_:
    print("Break")