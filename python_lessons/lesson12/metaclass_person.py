class MetaOsoba(type):
    
    def __new__(cls, name, bases, dct):
        dct["firma"] = "Januszex"
        print(name, bases)
        print("pre print object")
        obj = super().__new__(cls, name, bases, dct)
        print("print obj", obj)
        return obj

class Osoba(metaclass=MetaOsoba):
    def __init__(self, imie, rok_urodzenia, wyplata = 1000, wydajnosc = 0.5):
        print("init")
        self.imie = imie
        self.rok_urodzenia = rok_urodzenia
        self.wyplata = wyplata
        self.wydajnosc = wydajnosc
    
    @property
    def ratio(self):
        "im wyższe ratio, tym lepiej dla firmy"
        return self.wydajnosc / self.wyplata
    
osoba_lst = [#Osoba("Adam", 2000),
             #Osoba("Jaś", 1999, 1300, 0.6),
             ]
o = Osoba("Andrzej", 1970, 2000, 0.45)