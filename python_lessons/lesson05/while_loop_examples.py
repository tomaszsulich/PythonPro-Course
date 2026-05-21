licznik = 0
while licznik < 3:
    print(f"Pętla while, iteracja: {licznik}")
    licznik += 1 # kluczowy krok - modyfikacja licznika
    
while licznik <= 3:
    print(f"Pętla while, iteracja: {licznik}")
    licznik += 1 # kluczowy krok - modyfikacja licznika
    
# przykład z pętlą while, for mniej intuicyjny
def pobierz_napiecie() -> float: ...

while napiecie >= 4.15: # 2.5V <= pusta, 4.15 <= pełna
    napiecie = pobierz_napiecie()
# przerywanie ładowania

# UWAGA! MUSIMY WCZEŚNIEJ ZDEFINIOWAĆ ZMIENNĄ!
def pobierz_napiecie() -> float: ...

napiecie = 3.5
while napiecie >= 4.15: # 2.5V <= pusta, 4.15 <= pełna
    napiecie = pobierz_napiecie()
# przerywanie ładowania

# DRUGI SPOSÓB
def pobierz_napiecie() -> float:
    # mierzy napięcie na baterii
    return ...

napiecie = pobierz_napiecie()
while napiecie >= 4.15: # 2.5V <= pusta, 4.15 <= pełna
    napiecie = pobierz_napiecie()
print("bateria naładowana")
# przerywanie ładowania

def pobierz_napiecie() -> float:
    # mierzy napięcie na baterii
    return ...

# PRZYKŁAD
napiecia = [3.8, 3.9, 4, 4.1, 4.2] 
licznik = 0

# zerowy obrót pętli
napiecie = napiecia[licznik]
licznik += 1

while napiecie <= 4.15: # 2.5V <= pusta, 4.15 <= pełna
    napiecie = napiecia[licznik]
    print("mierzone napięcie", napiecie)
    licznik += 1
    
print("bateria naładowana", licznik)
# przerywanie ładowania

# PRZEDSTAWIENIE REALNEJ SYTUACJI, W KTÓREJ MOŻEMY SKORZYSTAĆ Z WHILE
def pobierz_napiecie(): ...


napiecie = pobierz_napiecie()

while napiecie <= 4.15:
    napiecie = pobierz_napiecie()
    
print("bateria naładowana")