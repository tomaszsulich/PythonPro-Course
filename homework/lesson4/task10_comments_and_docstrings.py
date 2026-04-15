def oblicz_pole_prostokata(a: float | int, b: float | int) -> float:
    # Tutaj dodaj docstring
    """
    Oblicza pole prostokąta na podstawie długości jego boków.
    
    Args:
        a (float | int): długość pierwszego boku
        b (float | int): długość drugiego boku
        
    Returns:
        float: pole prostokąta
    """

    # Tutaj dodaj komentarz
    # pole to wynik mnożenia boków przez siebie wzajemnie
    pole = a * b

    # Tutaj dodaj komentarz
    # wynik mnozenia zostaje zwrocony
    return pole


bok_a = 10
bok_b = 20
wynik = oblicz_pole_prostokata(bok_a, bok_b)
print(f"Pole prostokąta o bokach {bok_a} i {bok_b} wynosi {wynik}.")