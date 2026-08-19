class MetaWalidujMetody(type):
    """Metaklasa sprawdzająca obecność docstringów w metodach klasy."""

    def __new__(cls, name: str, bases: tuple, dct: dict):
        metody_bez_docstringa = []
        
        for nazwa_metody, obiekt in dct.items():
            if nazwa_metody.startswith("__"):
                continue

            if callable(obiekt) and obiekt.__doc__ is None:
                metody_bez_docstringa.append(nazwa_metody)

        if metody_bez_docstringa:
            komunikat = "Metody wymagające docstringa:\n"
            
            for metoda in metody_bez_docstringa:
                komunikat += f"- {metoda}\n"
            raise TypeError(komunikat)

        return super().__new__(cls, name, bases, dct)


def main() -> None:
    try:
        class GeneratorRaportow(metaclass=MetaWalidujMetody):

            def wczytaj_dane(self) -> None:
                """Wczytuje dane do raportu."""
                pass

            def generuj_pdf(self) -> None:
                """Generuje raport PDF."""
                pass

            def wyslij_mailem(self) -> None:
                pass

            def eksportuj_csv(self) -> None:
                pass
            
            def __str__(self) -> str:
                return "GeneratorRaportow"

    except TypeError as e:
        print(f"Błąd:\n")
        print(e)


if __name__ == "__main__":
    main()