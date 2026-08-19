from dataclasses import dataclass

@dataclass
class Film:
    """Reprezentuje film wraz z podstawowymi informacjami."""
    
    tytul: str
    rezyser: str
    rok_produkcji: int
    
    def __str__(self) -> str:
        return (
            f"Tytuł: {self.tytul}\n"
            f"Rok produkcji: {self.rok_produkcji}\n"
            f"Reżyser: {self.rezyser}"
        )

def main() -> None:
    film1 = Film("Incepcja", "Christopher Nolan", 2010)
    film2 = Film("Titanic", "James Cameron", 1997)
    
    print(film1)
    print("-" * 40)
    print(film2)
    
    
if __name__ == "__main__":
    main()