class Punkt:
    """Reprezentuje punkt w przestrzeni 2D"""
    
    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y

    def __str__(self) -> str:
        return f"({self.x}, {self.y})"
    
    def odleglosc_od_zera(self) -> float:
        """Zwraca odległość punktu od środka układu współrzędnych"""
        return (self.x ** 2 + self.y ** 2) ** 0.5
    

def main() -> None:
    punkt = Punkt(3.5, 10)
    
    print(f"Współrzędne punktu: {punkt}")
    print(f"Odległość od środka układu wynosi: {punkt.odleglosc_od_zera():.2f}.")
    

if __name__ == "__main__":
    main()