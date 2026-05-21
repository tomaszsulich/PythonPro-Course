from dataclasses import dataclass, field

@dataclass
class OsobaDc():
    imie: str = field(repr = False, compare = False)
    rok_urodzenia: int
    wyplata: int = field(default = 1000, repr = False, compare = False)
    wydajnosc: float = field(default = 0.5, repr = False, compare = False)
    oceny_pracownika: list = field(default_factory = list)

    @property
    def ratio(self):
        "im wyższe ratio, tym lepiej dla firmy"
        return round(1000 * self.wydajnosc / self.wyplata, 3)
    
stef = OsobaDc("Stefan", 1995)
ala = OsobaDc("Ala", 1995, 1200, wydajnosc = 0.5)
ela = OsobaDc("Ela", 2000, 1650, wydajnosc = 0.75)

print(stef == ala)