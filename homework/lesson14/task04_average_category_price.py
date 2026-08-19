from shop_db import get_connection

def get_average_category_price(category: str = "Książki") -> tuple[str, float] | None:
    """Oblicza średnią cenę produktów z określonej kategorii."""

    average_category_price_sql = """--sql
        SELECT k.nazwa_kategorii, AVG(p.cena)
        FROM produkty as p
        JOIN kategorie as k
        ON p.id_kategorii = k.id_kategorii
        WHERE LOWER(TRIM(k.nazwa_kategorii)) = LOWER(TRIM(?))
    """
    
    with get_connection() as conn:
        c = conn.cursor()
        result = c.execute(average_category_price_sql, (category,)).fetchone()
    
    if result is None or result[1] is None:
        return None
    return result
    

def main() -> None:
    kategoria = input(f"Podaj nazwę kategorii do obliczenia średniej ceny produktów: ").strip()
    
    if not kategoria:
        kategoria = "Książki"
        
    wynik = get_average_category_price(kategoria)
    
    if wynik is None:
        print(f"Kategoria '{kategoria}' nie istnieje lub nie zawiera żadnych produktów.")
    else:
        kategoria, srednia_cena = wynik
        print(f"Średnia cena produktów z kategorii '{kategoria}' wynosi {srednia_cena:.2f}.")
        
        
if __name__ == "__main__":
    main()