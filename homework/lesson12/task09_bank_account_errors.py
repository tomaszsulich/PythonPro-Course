from dataclasses import dataclass

class BrakSrodkowError(Exception):
    """Wyjątek zgłaszany przy próbie wypłaty kwoty większej niż dostępne saldo."""

@dataclass
class KontoBankowe:
    _saldo: float = 0.0
    
    @property
    def saldo(self) -> float:
        return self._saldo
    
    def wplac(self, kwota: float) -> None:
        if kwota < 0:
            raise ValueError("Kwota wpłaty nie może być ujemna!")
        self._saldo += kwota
        
    def wyplac(self, kwota: float) -> None:
        if kwota < 0:
            raise ValueError("Kwota do wypłaty nie może być ujemna!")
        
        if kwota > self._saldo:
            raise BrakSrodkowError("Nie masz wystarczających środków na koncie!")
        
        self._saldo -= kwota
        
        
def main() -> None:
    konto = KontoBankowe()
    print(f"Saldo początkowe: {konto.saldo}")
    
    try:
        konto.wplac(1000)
        print(f"Saldo po wpłacie: {konto.saldo}")
        
        konto.wplac(-50)
        
    except ValueError as e:
        print(f"Błąd wpłaty: {e}")

    try:
        konto.wyplac(-200)
        
    except ValueError as e:
        print(f"Błąd wypłaty: {e}")
        
    except BrakSrodkowError as e:
        print(f"Błąd wypłaty: {e}")
        
    try:
        konto.wyplac(2000)
        print(f"Saldo po wypłacie: {konto.saldo}")
        
    except BrakSrodkowError as e:
        print(f"Błąd wypłaty: {e}")
        

if __name__ == "__main__":
    main()