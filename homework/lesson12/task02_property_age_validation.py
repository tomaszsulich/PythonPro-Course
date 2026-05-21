class Uzytkownik:
    """Reprezentuje użytkownika z walidowanym wiekiem"""
    
    def __init__(self, wiek: int) -> None:
        self._wiek = wiek

    @property
    def wiek(self) -> int:
        return self._wiek
    
    @wiek.setter
    def wiek(self, nowy_wiek: int) -> None:
        if 0 <= nowy_wiek <= 120:
            self._wiek = nowy_wiek
        else:
            raise ValueError('wiek musi być liczbą z zakresu od 0 do 120!')