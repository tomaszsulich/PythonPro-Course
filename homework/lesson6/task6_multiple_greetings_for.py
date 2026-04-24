def wielokrotne_powitanie(imie: str, ilosc: int) -> None:
    for _ in range(ilosc):
        print(f"Cześć, {imie}!")
    
wielokrotne_powitanie("Kasia", 5)