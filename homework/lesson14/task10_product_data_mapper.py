from shop_db import get_connection

DEFAULT_PRODUCT_COLUMNS = ("id_produktu", "nazwa_produktu", "cena")
ALLOWED_PRODUCT_COLUMNS = {"id_produktu", "nazwa_produktu", "cena", "id_kategorii", "nazwa_kategorii"}

DATABASE_COLUMNS = {
    "id_produktu", "nazwa_produktu", "cena", "id_kategorii",
    "nazwa_kategorii", "imie", "email", "id_zamowienia",
    "id_klienta", "data_zamowienia", "ilosc"
}

COLUMN_LABELS = {
    "id_produktu": "ID",
    "nazwa_produktu": "Nazwa",
    "cena": "Cena",
    "id_kategorii": "ID kategorii",
    "nazwa_kategorii": "Kategoria"
}


class Produkt:
    """Reprezentuje model produktu mapowany z rekordów relacyjnej bazy danych na obiekty Pythona."""
    def __init__(self, id_produktu: int, nazwa_produktu: str, cena: float, \
                 id_kategorii: int | None = None, nazwa_kategorii: str | None = None) -> None:
        
        self.id_produktu = id_produktu
        self.nazwa_produktu = nazwa_produktu
        self.cena = cena
        self.id_kategorii = id_kategorii
        self.nazwa_kategorii = nazwa_kategorii


# TUTAJ LEPIEJ WYGLĄDAŁOBY NP. get_products, ALE POLECENIE WYMAGAŁO PL
def pobierz_wszystkie_produkty() -> list[Produkt]:
    """Mapuje rekordy produktów z relacyjnej bazy danych na obiekty klasy Produkt."""
    
    all_products_sql = f"""--sql
        SELECT
            p.id_produktu,
            p.nazwa_produktu,
            p.cena,
            k.id_kategorii,
            k.nazwa_kategorii
        FROM Produkty AS p
        JOIN Kategorie AS k
        ON k.id_kategorii = p.id_kategorii
    """
    
    with get_connection() as conn:
        rows = conn.cursor().execute(all_products_sql).fetchall()
        
    return [
        Produkt(id_produktu, nazwa_produktu, cena, id_kategorii, nazwa_kategorii)
        for (id_produktu, nazwa_produktu, cena, id_kategorii, nazwa_kategorii) in rows
    ]
    

def main() -> None:
    kolumny = input(
        "Podaj kolumny do wyświetlenia "
        "(id_produktu, nazwa_produktu, cena, "
        "id_kategorii, nazwa_kategorii):\n"
    ).strip()
        
    if not kolumny:
        kolumny = DEFAULT_PRODUCT_COLUMNS
    else:
        kolumny = tuple(kolumna.strip().lower() for kolumna in kolumny.split(","))
    
    nieistniejace = []
    niedostepne = []
    
    for kolumna in kolumny:
        if kolumna not in DATABASE_COLUMNS:
            nieistniejace.append(kolumna)
        elif kolumna not in ALLOWED_PRODUCT_COLUMNS:
            niedostepne.append(kolumna)
            
    if nieistniejace:
        print("Kolumny nieistniejące w bazie:")
        for kolumna in nieistniejace:
            print(f"- {kolumna}")
            
    if niedostepne:
        print("Kolumny niedostępne dla obiektu Produkt:")
        for kolumna in niedostepne:
            print(f"- {kolumna}")
            
    if nieistniejace or niedostepne:
        return
               
    produkty = pobierz_wszystkie_produkty()
    
    if not produkty:
        print("Nie znaleziono produktów.")
        return
    
    for produkt in produkty:
        opis = []
        
        for kolumna in kolumny:
            wartosc = getattr(produkt, kolumna)
            
            if isinstance(wartosc, float):
                wartosc = f"{wartosc:.2f}"   
            
            opis.append(f"{COLUMN_LABELS[kolumna]}: {wartosc}")
        
        print(", ".join(opis))
                 
       
if __name__ == "__main__":
    main()