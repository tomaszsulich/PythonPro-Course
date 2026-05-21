class Film:
    
    def __init__(self, tytul: str, rezyser: str, rok_produkcji: int) -> None:
        self.tytul = tytul
        self.rezyser = rezyser
        self.rok_produkcji = rok_produkcji
        
    def informacje(self) -> str:
        return f'"{self.tytul}" ({self.rok_produkcji}), reżyseria: {self.rezyser}.'
    
    def __str__(self) -> str:
        return self.informacje()

 
def main() -> None:
    film1 = Film("100 dni do matury", "Mikołaj Piszczan", 2025)
    film2 = Film("Pieprzyć Mickiewicza 3", "Sara Bustamante-Drozdek", 2026)
    
    print(film1)
    print(film2)

    
if __name__ == "__main__":
    main()