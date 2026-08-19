class Pracownik:
    
    def __init__(self, imie: str, stawka_godzinowa: float) -> None:
        self.imie = imie
        self.stawka_godzinowa = stawka_godzinowa
        
    def oblicz_pensje(self, liczba_godzin: int) -> float:
        return self.stawka_godzinowa * liczba_godzin
    
class Programista(Pracownik):
    
    def __init__(self, imie: str, stawka_godzinowa: float, jezyki_programowania: list[str]) -> None:
        super().__init__(imie, stawka_godzinowa)
        self.jezyki_programowania: list = jezyki_programowania
        

def main() -> None:
    programista = Programista("Jan", 50.0, ["Python", "Java", "C++"])
    liczba_godzin = 160
    pensja = programista.oblicz_pensje(liczba_godzin)
    print(f"Programista {programista.imie} zarobi {pensja} zł za {liczba_godzin} godzin pracy.")
    

if __name__ == "__main__":
    main()