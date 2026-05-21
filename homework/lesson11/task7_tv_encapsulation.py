class Telewizor:
    """Prosty model telewizora z enkapsulacją kanału i głośności"""
    
    def __init__(self, kanal: int = 1, glosnosc: int = 10, wlaczony: bool = False) -> None:
        self.__kanal = kanal
        self.__glosnosc = glosnosc
        self.__wlaczony = wlaczony
        
    def wlacz(self) -> None:
        self.__wlaczony = True
        
    def wylacz(self) -> None:
        self.__wlaczony = False
        
    def zmien_kanal(self, numer: int) -> None:
        if self.__wlaczony:
            self.__kanal = numer
        else:
            print("Telewizor jest wyłączony. Nie można zmienić kanału.")
    
    def ustaw_glosnosc(self, wartosc: int) -> None:
        if not self.__wlaczony:
            print("Telewizor jest wyłączony.")
        
        elif 0 <= wartosc <= 100:
            self.__glosnosc = wartosc
            
        else:
            print("Głośność musi być w zakresie od 0 do 100.")
            
    def glosniej(self) -> int:
        if not self.__wlaczony:
            print("Telewizor jest wyłączony. Nie można zwiększyć głośności.")
        
        elif self.__glosnosc < 100:
            self.__glosnosc += 1
            
        else:
            print("Głośność jest już ustawiona na maksimum.")
        
        return self.__glosnosc
    
    def ciszej(self) -> int:
        if not self.__wlaczony:
            print("Telewizor jest wyłączony. Nie można zmniejszyć głośności.")
        
        elif self.__glosnosc > 0:
            self.__glosnosc -= 1
            
        else:
            print("Głośność jest już ustawiona na minimum.")
        
        return self.__glosnosc
    
    def info(self) -> str:
        """Zwraca informacje o stanie telewizora"""
        status = "włączony" if self.__wlaczony else "wyłączony"
        return f"Telewizor jest {status}. Kanał: {self.__kanal}, Głośność: {self.__glosnosc}"
    
    def __str__(self) -> str:
        return self.info()

    
def main() -> None:
    tv = Telewizor()
    print(tv)
    
    print("\n--- Próba zmiany kanału przy wyłączonym TV ---")
    tv.zmien_kanal(5)
    print(tv)
    
    print("\n--- Próba ustawienia zbyt dużej głośności ---")
    tv.wlacz()
    tv.ustaw_glosnosc(150)
    print(tv)
    
    
if __name__ == "__main__":
    main()