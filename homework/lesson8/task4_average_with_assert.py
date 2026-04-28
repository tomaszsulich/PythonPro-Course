# TROCHĘ NADPROGRAMOWE, BO ASERCJA RZADKO SPOTYKANA
def oblicz_srednia(lista_ocen: list[float | int]) -> float:
    assert len(lista_ocen) > 0, "Lista ocen nie może być pusta."
    
    oceny = [float(o) for o in lista_ocen]
    return sum(oceny) / len(oceny)


def main():
    lista_ocen = [5, 7, 13, 28, 54, 32, 65, 11, 76]
    wynik = oblicz_srednia(lista_ocen)
    
    print(f"Średnia z {lista_ocen} wynosi {wynik:.2f}.")
    print(oblicz_srednia([]))

    
if __name__ == "__main__":
    main()