class Instrument:
    """Bazowa klasa instrumentów muzycznych"""
    
    def graj(self) -> str:
        """Zwraca sposób wydawania dźwięku przez instrument"""
        return "Wydaje dźwięk."

class Strunowy(Instrument):
    def graj(self) -> str:
        return super().graj() + " [Szarpnięcie struny]"

class Dety(Instrument):
    def graj(self) -> str:
        return super().graj() + " [Zadęcie w ustnik]"

class Gitara(Strunowy):
    def graj(self) -> str:
        return super().graj() + " [Akord G-dur]"

class Trabka(Dety):
    def graj(self) -> str:
        return super().graj() + " [Sygnał trąbki]"
    

def main() -> None:
    gitara = Gitara()
    trabka = Trabka()
    
    print("=== Gitara ===")
    print(gitara.graj())
    
    print("\n=== Trąbka ===")
    print(trabka.graj())
    
    
if __name__ == "__main__":
    main()