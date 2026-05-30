from shop_db import get_connection

def get_total_value(category: str = "Elektronika") -> tuple[str, float] | None:
    """Zwraca łączną wartość produktów z określonej kategorii"""
    
    total_value_sql = """--sql
        SELECT k.nazwa_kategorii, SUM(p.cena)
        FROM produkty as p
        JOIN kategorie as k
        ON p.id_kategorii = k.id_kategorii
        WHERE LOWER(TRIM(k.nazwa_kategorii)) = LOWER(TRIM(?))
    """
    with get_connection() as conn:
        result = conn.cursor().execute(total_value_sql, (category,)).fetchone()
        
        if result is None or result[1] is None:
            return None
        return result
    

def main() -> None:
    kategoria = input(f"Podaj nazwę kategorii do obliczenia łącznej wartości produktów: ").strip()
    if not kategoria:
        kategoria = "Elektronika"

    wynik = get_total_value(kategoria)
    
    if wynik is None:
        print(f"Kategoria '{kategoria}' nie istnieje lub nie zawiera żadnych produktów.")
    else:
        kategoria, wartosc_produktow = wynik
        print(f"Łączna wartość produktów z kategorii '{kategoria}' wynosi {wartosc_produktow:.2f}.")
        

if __name__ == "__main__":
    main()