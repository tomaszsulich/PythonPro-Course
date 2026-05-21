class MetaOsoba(type):
    singletons = {}
    def __call__(cls, name, bases, dct):
        print("new")
        if name in cls.singletons:
            # print("cokolwiek")
            # print(cls.singletons)
            # print("zwracam istniejącą instancję")
            return cls.singletons[name]
        else:
            obj = super().__new__(cls, name, bases, dct)
            cls.singletons[name] = obj
            return obj

class Osoba(metaclass=MetaOsoba):
    def __init__(self, imie, rok_urodzenia, wyplata = 1000, wydajnosc = 0.5):
        self.imie = imie
        self.rok_urodzenia = rok_urodzenia
        self.wyplata = wyplata
        self.wydajnosc = wydajnosc
    
    @property
    def ratio(self):
        "im wyższe ratio, tym lepiej dla firmy"
        return self.wydajnosc / self.wyplata
    
# o = Osoba("Andrzej", 1970, 2000, 0.45)
# o2 = Osoba("Adam", 1986)