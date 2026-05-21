class Figura:
    """Klasa bazowa dla różnych figur geometrycznych"""
    
    def oblicz_pole(self) -> float:
        pass
    
class Kwadrat(Figura):
    
    def __init__(self, bok: float) -> None:
        self.bok = bok
        
    def oblicz_pole(self) -> float:
        return self.bok ** 2
    
class Kolo(Figura):
    
    def __init__(self, promien: float) -> None:
        self.promien = promien
        
    def oblicz_pole(self) -> float:
        return 3.14159 * self.promien ** 2
    

def main() -> None:
    lista_figur = [Kwadrat(4), Kolo(3)]
    
    for figura in lista_figur:
        print(f"{figura.__class__.__name__}: {figura.oblicz_pole():.2f}")
        
        
if __name__ == "__main__":
    main()