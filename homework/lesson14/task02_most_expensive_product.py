from shop_db import get_connection

def get_most_expensive_product() -> tuple[str, float] | None:
    """Zwraca nazwę i cenę najdroższego produktu."""

    most_expensive_product_sql = """--sql
        SELECT nazwa_produktu, cena
        FROM Produkty
        WHERE cena = (SELECT MAX(cena) FROM Produkty)
    """
    
    # RÓWNOWAŻNIE MOŻNA UŻYĆ ORDER BY i LIMIT 1:
    # most_expensive_product_sql = """--sql
    #     SELECT nazwa_produktu, cena
    #     FROM Produkty
    #     ORDER BY cena DESC
    #     LIMIT 1
    # """
        
    with get_connection() as conn:
        c = conn.cursor()
        return c.execute(most_expensive_product_sql).fetchone()


def main() -> None:
    produkt = get_most_expensive_product()
    
    if produkt is None:
        print("Nie znaleziono produktów.")
    else:
        nazwa_produktu, cena = produkt
        print(f"Najdroższym produktem jest {nazwa_produktu} o cenie {cena:.2f}.")


if __name__ == "__main__":
    main()