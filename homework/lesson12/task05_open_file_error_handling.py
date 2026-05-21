def otworz_plik() -> None:
    """Próbuje otworzyć i odczytać plik tekstowy."""
    
    try:
        with open("nieistniejacy.txt", "r") as plik:
            zawartosc = plik.read()
            print(zawartosc)
            
    except FileNotFoundError:
        print("Błąd: Plik nie istnieje!")


def main() -> None:
    otworz_plik()


if __name__ == "__main__":
    main()