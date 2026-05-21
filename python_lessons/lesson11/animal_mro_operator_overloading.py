from abc import ABC

akceptowalne_jedzenie = ...

class Zwierze(ABC):
    
    def zjedz(self, jedzenie: str):
        if jedzenie in self.akceptowalne_jedzenie:
            print("jedz")
        else:
            raise ValueError(self.__class__.__name__+ " nie moze jesc " + jedzenie)
        
    def __str__(self):
        return f"<{self.__class__.__name__}>"
    
    def __repr__(self):
        return self.__str__()
    
    def __add__(self, other: Zwierze):
        if not isinstance(other, Zwierze):
            raise TypeError()
        return PsoZajac(self.masa + other.masa)

class Miesozerca:
    akceptowalne_jedzenie = ("mieso")
    
class Roslinozerca:
    akceptowalne_jedzenie = ("trawa")
          
class Pies(Zwierze, Miesozerca):
    
    def __init__(self, masa = 10):
        self.masa = masa
    
    def daj_glos(self):
        print("hau hau")
        
    # def zjedz(self, jedzenie: str):
    #     if jedzenie in ("mieso", "karma_dla_psa"):
    #         print("jem...")
    #     raise ValueError("pies nie moze jesc", jedzenie)
    
class Zajac(Zwierze, Roslinozerca):
    def __init__(self):
        self.masa = 5
    latki = True

    # def zjedz(self, jedzenie: str):
    #     if jedzenie in ("trawa", "marchew"):
    #         print("jem...")
    #     raise ValueError("zajac nie moze jesc", jedzenie)
    
class PsoZajac(Zajac, Pies):
    
    def __init__(self, masa = 15):
        self.masa = masa

def nakarm_zwierze(zwierze: Zwierze, jedzenie: str):
    zwierze.zjedz(jedzenie)
    
z = Zajac()
nakarm_zwierze(z, "trawa")

p = Pies(10.1)
nakarm_zwierze(p, "mieso")

print(f"Laczna masa psa i zajaca to {p + z} kg.")