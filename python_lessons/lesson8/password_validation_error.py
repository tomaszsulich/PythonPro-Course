def wczytaj_plik(sciezka_do_pliku) -> list[list[int]]:
    ...

class BladWalidacjiHaslaError(Exception):
    """Wyjątek zgłaszany, gdy hasło nie spełnia wymagań."""
    pass

def sprawdz_haslo(haslo: str):
    if len(haslo) < 8:
        raise BladWalidacjiHaslaError("Hasło jest za krótkie (minimum 8 znaków).")
    # print([char.isdigit() for char in haslo])
    # Python do niektórych funkcji pozwala wrzucić comprehension bez nawiasów, np. w any, all
    if not any(char.isdigit() for char in haslo):
        raise BladWalidacjiHaslaError("Hasło musi zawierać co najmniej jedną cyfrę.")
    print("Hasło jest poprawne.")
    
sprawdz_haslo("Dizoral1234")