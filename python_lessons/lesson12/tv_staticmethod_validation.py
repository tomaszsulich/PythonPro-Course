class Telewizor:
    ZAKRES_GLOSNOSCI = (0, 100)
    
    def __init__(self, marka: str) -> None:
        self.marka = self.testuj_marke(marka)
        self.__kanal = 1
        self.__glosnosc = 10
        self.__wlaczony = False
    
    @staticmethod
    def testuj_marke(nazwa_marki):
        if "!" in nazwa_marki:
            raise ValueError("Zakazany znak w parametrze marka!")
        elif len(nazwa_marki) < 2:
            raise ValueError("Nazwa marki jest za krótka!")
        else:
            print("Nazwa marki poprawna")
            return nazwa_marki
        
    def glosniej(self, wartosc: int):
        print("Podgłośniamy o wartość", wartosc)
        self.__zmien_glosnosc(wartosc)
        
    def ciszej(self, wartosc: int):
        print("Ściszamy o wartość", wartosc)
        self.__zmien_glosnosc(-wartosc)
        
    def on_off(self):
        self.__wlaczony = not self.__wlaczony
        
    def wlacz(self):
        self.__wlaczony = True
        
    def wylacz(self):
        self.__wlaczony = False
        
    def ustaw_kanal(self, nowy_kanal):
        if not self.__wlaczony:
            raise ValueError("Telewizor musi być włączony, aby zmienić kanał.")
        self.__kanal = nowy_kanal

    def info(self):
        print(f"[{"ON" if self.__wlaczony else "OFF"}][{self.__glosnosc=}][{self.__kanal=}]")

    def __zmien_glosnosc(self, wartosc: int):
        if not self.__wlaczony:
            raise ValueError("Telewizor musi być włączony, aby zmienić głośność.")
        if not isinstance(wartosc, int):
            raise TypeError
        m0, m1 = self.ZAKRES_GLOSNOSCI
        if not (m0 <= self.__glosnosc + wartosc <= m1):
            raise ValueError("Przekroczono zakres głośności!")
        print("Zmieniono głośność o", wartosc)
        self.__glosnosc += wartosc
        
t = Telewizor("Okil")
try:
    t2 = Telewizor("Oop")
except ValueError:
    print("Przechwycono wyjątek zgodnie z oczekiwaniami!")
else:
    raise Exception("Nieoczekiwany brak wyjątku")