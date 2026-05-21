from abc import ABC, abstractmethod


class Zwierze(ABC):
    akceptowalne_jedzenie = ...
    
    def zjedz(self, jedzenie: str):
        if jedzenie in self.akceptowalne_jedzenie:
            print("jedz")
        else:
            raise ValueError(self.__class__.__name__+ " nie moze jesc " + jedzenie)
            
class Miesozerca:
    akceptowalne_jedzenie = ("mieso")
    
class Roslinozerca:
    akceptowalne_jedzenie = ("trawa")
          
class Pies(Zwierze, Miesozerca):
    akceptowalne_jedzenie = ("mieso", "karma")
    
    def daj_glos(self):
        print("hau hau")
        
    # def zjedz(self, jedzenie: str):
    #     if jedzenie in ("mieso", "karma_dla_psa"):
    #         print("jem...")
    #     raise ValueError("pies nie moze jesc", jedzenie)
    
class Zajac(Zwierze, Roslinozerca):
    akceptowalne_jedzenie = ("trawa", "marchew")
    
    # def zjedz(self, jedzenie: str):
    #     if jedzenie in ("trawa", "marchew"):
    #         print("jem...")
    #     raise ValueError("zajac nie moze jesc", jedzenie)

def nakarm_zwierze(zwierze: Zwierze, jedzenie: str):
    zwierze.zjedz(jedzenie)
    
z = Zajac()
nakarm_zwierze(z, "trawa")

p = Pies()
nakarm_zwierze(p, "mieso")