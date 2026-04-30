def funkcja_zewnetrzna():
    def funkcja_wewnetrzna():
        return 12
    
    return funkcja_wewnetrzna


wynik = funkcja_zewnetrzna()
print("wynikiem", wynik.__name__, "return wyniku", wynik())