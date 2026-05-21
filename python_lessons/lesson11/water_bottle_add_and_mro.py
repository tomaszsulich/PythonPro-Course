class ButelkaWody:
    
    def __init__(self, pojemnosc = 1.5, ile_wody: float = None):
        if ile_wody is not None and ile_wody > pojemnosc:
            raise ValueError("nie mozna nalac wiecej wody niz pojemnosc butelki")
        if ile_wody is None:
            ile_wody = pojemnosc
            
    def __add__(self, other):
        if self.ile_wody + other.ile_wody > max(self.pojemnosc, other.pojemnosc):
            return []
        
class Butelka1_5l(ButelkaWody):
    def __init__(self, ile_wody: float = None):
        super().__init__(1.5, ile_wody)
        
class Butelka5l(ButelkaWody):
    def __init__(self, ile_wody: float = None):
        super().__init__(5, ile_wody)
        
# Butelka1_5l()

# Przykład "problemu diamentu"
class A:
    def kim_jestem(self):
        print("Jestem z klasy A")
    
class B(A):
    ...
    # def kim_jestem(self):
    #     print("Jestem z klasy B")

class C(A):
    ...
    # def kim_jestem(self):
    #     print("Jestem z klasy C")

# Klasa D dziedziczy po B i C. Po której z nich powinna odziedziczyć metodę 'kim_jestem'?
class D(B, C):
    pass

# Tworzymy obiekt klasy D
d = D()
d.kim_jestem() # >> Jestem z klasy B

class MyCls():
    ...