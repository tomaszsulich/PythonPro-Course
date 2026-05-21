import datetime

class Osoba:
    def __init__(self, imie, rok_urodzenia, wyplata = 1000, wydajnosc = 0.5):
        self.imie = imie
        self.rok_urodzenia = rok_urodzenia
        self.wyplata = wyplata
        self.wydajnosc = wydajnosc
    
    @property
    def ratio(self):
        "im wyższe ratio, tym lepiej dla firmy"
        return self.wydajnosc / self.wyplata
    
osoba_lst = [Osoba("Adam", 2000),
             Osoba("Jaś", 1999, 1300, 0.6),
             Osoba("Andrzej", 1970, 2000, 0.45)]


from dataclasses import dataclass

@dataclass
class OsobaDc():
    imie: str
    rok_urodzenia: int
    wyplata: float = 1000
    wydajnosc: float = 0.5

    @property
    def ratio(self):
        "im wyższe ratio, tym lepiej dla firmy"
        return round(1000 * self.wydajnosc / self.wyplata, 3)
    
    def __gt__(self, other: OsobaDc):
        return self.ratio > other.ratio
    
    def __eq__(self, other: OsobaDc):
        return self.ratio == other.ratio
    
stef = OsobaDc("Stefan", 1995)
ala = OsobaDc("Ala", 1995, 1200, wydajnosc = 0.5)
ela = OsobaDc("Ela", 2000, 1650, wydajnosc = 0.75)

print(stef > ala)