class Trojkat:
    
    def __init__(self, a, h):
        self.a = a
        self.h = h
        
    def pole(self):
        return self.a * self.h / 2
    
t = Trojkat(5,3)



class Uczen:
    
    def __init__(self, imie, klasa, oceny = None):
        self.imie = imie
        self.klasa = klasa
        if oceny is None:
            oceny = []
        self.oceny = oceny
        
    def wylicz_srednia(self):
        return sum(self.oceny) / len(self.oceny)
        
uczen1 = Uczen("Wojtek", "3a", [1, 2, 5])
uczen2 = Uczen("Ania", "2b", [3, 2, 5])