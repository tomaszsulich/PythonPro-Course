def testuj_marke(nazwa_marki):
        if "!" in nazwa_marki:
            raise ValueError("Zakazany znak w parametrze marka!")
        elif len(nazwa_marki) < 2:
            raise ValueError("Nazwa marki jest za krótka!")
        else:
            print("Nazwa marki poprawna")
            return nazwa_marki