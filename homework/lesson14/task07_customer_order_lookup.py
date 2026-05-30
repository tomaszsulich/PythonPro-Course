from shop_db import get_connection

def get_products_ordered_by_customer(customer_name: str = "Anna Nowak") -> list[tuple[str]]:
    """Odtwarza listę produktów zamówionych przez klienta na podstawie relacji między tabelami"""
    
    customer_ordered_products_sql = """--sql
        SELECT p.nazwa_produktu
        FROM produkty as p
        JOIN zamowienia_produkty as zp
        ON zp.id_produktu = p.id_produktu
        JOIN zamowienia as z
        ON z.id_zamowienia = zp.id_zamowienia
        JOIN klienci as k
        ON k.id_klienta = z.id_klienta
        WHERE LOWER(k.imie) = LOWER(?)
        ORDER BY p.nazwa_produktu
    """
    with get_connection() as conn:
        return conn.cursor().execute(customer_ordered_products_sql, (customer_name,)).fetchall()
    
def get_customer_display_name(customer_name: str) -> str | None:
    """Zwraca nazwę klienta w formacie zapisanym w bazie danych"""
    
    customer_display_name_sql = """--sql
    SELECT imie FROM Klienci
    WHERE imie IS NOT NULL
    AND TRIM(imie) != ''
    AND LOWER(imie) = LOWER(?)
    """
    with get_connection() as conn:
        result = conn.cursor().execute(customer_display_name_sql, (customer_name,)).fetchone()
    
        if result is None:
            return None
        return result[0]

    
def main() -> None:
    customer_name = input("Podaj imię klienta (domyślnie 'Anna Nowak'): ").strip()
    
    if not customer_name:
        customer_name = "Anna Nowak"
    customer_display_name = get_customer_display_name(customer_name)
        
    if customer_display_name is None:
        print(f"Nie znaleziono klienta {customer_name}!")
        return
    
    produkty = get_products_ordered_by_customer(customer_display_name)
    
    if not produkty:
        print(f"Nie znaleziono produktów przypisanych do klienta {customer_display_name}.")
        return

    nazwy_produktow = [produkt[0] for produkt in produkty]
    print(f"Produkty zamówione przez klienta {customer_display_name}:\n", nazwy_produktow)
    
    
if __name__ == "__main__":
    main()