from abc import ABC, abstractmethod


class Zwierze(ABC):
    
    @abstractmethod
    def daj_glos(self):
        raise NotImplementedError()
    
    @abstractmethod
    def zjedz(self, jedzenie: str):
        ...
        
class Pies(Zwierze):
    
    def daj_glos(self):
        print("hau hau")
        
    def zjedz(self, jedzenie: str):
        if jedzenie in ("mieso", "karma_dla_psa"):
            print("jem...")
        raise ValueError("pies nie moze jesc", jedzenie)
    
class Zajac(Zwierze):
    def zjedz(self, jedzenie: str):
        if jedzenie in ("trawa", "marchew"):
            print("jem...")
        raise ValueError("zajac nie moze jesc", jedzenie)

def nakarm_zwierze(zwierze: Zwierze, jedzenie: str):
    zwierze.zjedz(jedzenie)
    
z = Zajac()
nakarm_zwierze(z, "marchew")

p = Pies()
nakarm_zwierze(p, "trawa")