class KalkulatorWalut:
    
    @staticmethod
    def usd_na_pln(kwota_usd: float, kurs_usd_pln: float = 4.0) -> float:
        """Przelicza dolary amerykańskie na złotówki."""
        if kwota_usd < 0:
            raise ValueError("Kwota w dolarach nie może być ujemna.")
        return round(kwota_usd * kurs_usd_pln, 2)
    

def main() -> None:
    kwota_usd = 1000
    wynik = KalkulatorWalut.usd_na_pln(kwota_usd)
    print(f"{kwota_usd} USD to {wynik} PLN")
    

if __name__ == "__main__":
    main()