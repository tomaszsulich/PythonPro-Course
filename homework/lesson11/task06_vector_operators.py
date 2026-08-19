class Wektor2D:
    """Reprezentuje wektor w przestrzeni 2D."""
    
    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y
        
    def __add__(self, other) -> "Wektor2D":
        if isinstance(other, Wektor2D):
            return Wektor2D(self.x + other.x, self.y + other.y)
        return NotImplemented
    
    def __sub__(self, other) -> "Wektor2D":
        if isinstance(other, Wektor2D):
            return Wektor2D(self.x - other.x, self.y - other.y)
        return NotImplemented
    
    def __eq__(self, other) -> bool:
        if isinstance(other, Wektor2D):
            return self.x == other.x and self.y == other.y
        return NotImplemented
    
    def __str__(self) -> str:
        return f"<{self.x}, {self.y}>"
    
    
def main() -> None:
    wektor1 = Wektor2D(2, 3)
    wektor2 = Wektor2D(4, 5)
    
    suma = wektor1 + wektor2
    roznica = wektor1 - wektor2
    
    print(f"Suma: {wektor1} + {wektor2} = {suma}")
    print(f"Różnica: {wektor1} - {wektor2} = {roznica}")
    print(f"Czy wektory są równe? {'Tak' if wektor1 == wektor2 else 'Nie'}")
    
    
if __name__ == "__main__":
    main()