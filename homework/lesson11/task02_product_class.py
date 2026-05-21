class Produkt:
    
    def __init__(self, nazwa: str, cena: float, kategoria: str) -> None:
        self.nazwa = nazwa
        self.cena = cena
        self.kategoria = kategoria
    

def main() -> None:
    produkt1 = Produkt("Laptop", 2999.99, "Elektronika")
    produkt2 = Produkt("Chipsy", 9.99, "Przekąski")
    
    print("Produkt 1:")
    print(f"Nazwa: {produkt1.nazwa}")
    print(f"Cena: {produkt1.cena}")
    print(f"Kategoria: {produkt1.kategoria}")
    
    print("\nProdukt 2:")
    print(f"Nazwa: {produkt2.nazwa}")
    print(f"Cena: {produkt2.cena}")
    print(f"Kategoria: {produkt2.kategoria}")


if __name__ == "__main__":
    main()