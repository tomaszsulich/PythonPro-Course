import datetime

class Osoba:
    def __init__(self, imie, rok_urodzenia):
        self.imie = imie
        self.rok_urodzenia = rok_urodzenia
        self.__wyplata = 1000
        
    @property
    def wyplata(self):
        return self.__wyplata
    
    @wyplata.setter
    def wyplata(self, wartosc):
        if wartosc <= self.__wyplata:
            raise ValueError("Nie podoba mi się ta 'Nowa' wypłata!")
        self.__wyplata = wartosc

    @property
    def wiek(self):
        return datetime.date.today().year - self.rok_urodzenia
    
o0 = Osoba("Jaś", 24)
o1 = Osoba.z_roku_urodzenia("Małgosia", 2010)
print("wyplata mal", o1.wyplata)