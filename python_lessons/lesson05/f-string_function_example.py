def wypisz_produkt(produkt: str, koszt: float | int) -> None:
    print(f"{produkt} kosztuje {koszt:.2f}")
    
produkt, koszt = "chleb", 5.125
wypisz_produkt(produkt = produkt, koszt = koszt)