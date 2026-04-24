POZIOM_DOSTEPU = "user"

def zmien():
    POZIOM_DOSTEPU = "admin"
    print("W funkcji: ", POZIOM_DOSTEPU)
    
print("Przed funkcją: ", POZIOM_DOSTEPU)
zmien()
print("Po funkcji: ", POZIOM_DOSTEPU)