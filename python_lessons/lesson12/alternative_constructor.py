import datetime

class Osoba:
    def __init__(self, imie, wiek):
        self.imie = imie
        self.wiek = wiek

    @classmethod
    def z_roku_urodzenia(cls, imie, rok_urodzenia):
        """
        Alternatywny konstruktor.
        'cls' to referencja do klasy Osoba.
        """
        aktualny_rok = datetime.date.today().year
        wiek = aktualny_rok - rok_urodzenia
        # Zwracamy nową instancję klasy
        return cls(imie, wiek)
    
# o0 = Osoba("Jaś", 24)
o1 = Osoba.z_roku_urodzenia("Małgosia", 2020)