wzrost = int(input("wzrost[cm]: "))
waga = int(input("waga[kg]: "))
bmi = waga / (wzrost * wzrost) # BMI (Body Mass Index) to wskaźnik masy ciała obliczany 
# jako stosunek wagi do kwadratu wzrostu, używany do oceny, czy masa ciała jest prawidłowa.
print(bmi)

# DOPISYWANIE WARTOŚCI BARDZO ŁATWE PRZEZ SŁOWNIK, TAKA TROCHĘ ALTERNATYWA DLA if, elif, else ITD.
{1: 'xxx',
 2: 'xnjsjk'}[2]

# CZASAMI PRZYDATNE JAK CHCEMY COŚ POLICZYĆ NA SZYBKO
{1: print,
 2: ...}

def f_c(): ...
def c_f(): ...

# W TEN SPOSÓB MOŻEMY ŁATWIEJ DOBRAĆ SIĘ DO FUNKCJI, KTÓRĄ CHCEMY ZAMIAST if'a
klucz = input("Podaj sposób przeliczenia: ")
{"f_c": f_c,
 "c_f": c_f}[klucz]