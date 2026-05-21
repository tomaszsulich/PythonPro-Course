class Telewizor:
    
    def __init__(self) -> None:
        self.__glosnosc = 10
        
    def podglosnij(self, wartosc):
        self.__glosnosc += wartosc
        print("Podgłośniono o", wartosc, f"teraz {self.__glosnosc}")
        
t = Telewizor()
t.podglosnij(10)
Telewizor.podglosnij(t, 10)