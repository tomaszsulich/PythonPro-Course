def mierz_czas(func: callable):
    def wrapper(*args, **kwargs):
        # funkcjonalność przed wywołaniem docelowej funkcji
        wynik = func(*args, **kwargs) # wywołanie oryginalnej funkcji
        # funkcjonalność po wywołaniu docelowej funkcji
        return wynik
    return wrapper

@mierz_czas
def funkcja_coreowa(): # funkcja wykonująca istotną rzecz
    ...
    
funkcja_coreowa_udekorowana = mierz_czas(funkcja_coreowa) # dużo czytelniejsze, ale wszyscy
# korzystają z małpy