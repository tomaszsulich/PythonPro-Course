from dataclasses import dataclass

class Wektor2D:
    
    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y
        
    def __add__(self, other: Wektor2D) -> Wektor2D:
        if not isinstance(other, (Wektor2D, tuple)):
            raise TypeError
        return __class__(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other: Wektor2D) -> Wektor2D:
        if not isinstance(other, (Wektor2D, tuple)):
            raise TypeError
        return __class__(self.x - other.x, self.y - other.y)
    
    def __eq__(self, other: Wektor2D) -> bool:
        return all(self.x == other.x, self.y == other.y)
    
@dataclass
class Wektor2Ddc:
    x: float
    y: float
    
    def __add__(self, other: Wektor2Ddc) -> Wektor2Ddc:
        if not isinstance(other, (Wektor2Ddc, tuple)):
            raise TypeError
        return __class__(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other: Wektor2Ddc) -> Wektor2Ddc:
        if not isinstance(other, (Wektor2Ddc, tuple)):
            raise TypeError
        return __class__(self.x - other.x, self.y - other.y)
    
    
def main():
    w = Wektor2D(1, 2) + Wektor2D(3, 4)
    
    
if __name__ == "__main__":
    main()