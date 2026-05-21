class BladPrzetwarzaniaDanychError(Exception):
    pass


def przetworz_dane(dane: dict) -> str:
    try:
        # przykład: oczekujemy klucza "imie"
        return dane["imie"]
        
    except KeyError as e:
        brakujacy_klucz = e.args[0]
        
        # logowanie
        with open("log.txt", mode = "a", encoding = "utf-8") as log:
            log.write(f"KeyError: brak klucza '{brakujacy_klucz}'\n")
        
        # rzucenie nowego wyjątku
        raise BladPrzetwarzaniaDanychError(
            f"Brak klucza: {brakujacy_klucz}"
        )
        
        
def main():
    try:
        przetworz_dane({"nazwisko": "Kowalski"})
    except BladPrzetwarzaniaDanychError as e:
        print(f"Błąd przetwarzania: {e}")
        
        
if __name__ == "__main__":
    main()