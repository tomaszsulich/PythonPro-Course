class Instrument:
    """Bazowa klasa instrumentów muzycznych"""
    
    def graj(self) -> str:
        raise NotImplementedError

class Strunowy(Instrument):
    def graj(self) -> str:
        return f"Wydaje dźwięk w reakcji na szarpnięcie struny."

class Dety(Instrument):
    ...

class Gitara(Strunowy):
    def graj(self) -> str:
        return "Gitara w" + super().graj()[:-1].replace("Wydaje", "wydaje", 1) + " palcem."

class Skrzypce(Strunowy):
    def graj(self) -> str:
        return "Skrzypce " + super().graj()[:-1].replace("Wydaje", "wydają", 1) + " smyczkiem."
    

def main() -> None:
    i = Instrument()
    s = Strunowy()
    g = Gitara()
    s_ = Skrzypce()
    
    print("=== Gitara ===")
    print(g.graj())
    
    print("\n=== Skrzypce ===")
    print(s_.graj())
    
    
if __name__ == "__main__":
    main()