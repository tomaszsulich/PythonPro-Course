from shop_db import get_connection
from task06_dynamic_query_builder import display_query_results

ALLOWED_SORT_COLUMNS = {"kategoria", "liczba_produktow"}
ALLOWED_SORT_DIRECTIONS = {"ASC", "DESC"}

def generate_category_product_report(sort_by: str = "liczba_produktow",
                                     sort_direction: str = "DESC") -> list[tuple[str, int]]:
    """Generuje raport liczby produktów przypisanych do poszczególnych kategorii."""
    
    category_inventory_summary_sql = f"""--sql
        SELECT k.nazwa_kategorii AS kategoria, COUNT(p.id_produktu) AS liczba_produktow
        FROM kategorie AS k
        JOIN produkty AS p
        ON p.id_kategorii = k.id_kategorii
        GROUP BY p.id_kategorii, k.nazwa_kategorii
        ORDER BY {sort_by} {sort_direction}
    """
    
    with get_connection() as conn:
        return conn.cursor().execute(category_inventory_summary_sql).fetchall()
    
    
def main() -> None:
    kolumna_sortujaca = input("Podaj kolumnę sortowania (kategoria, liczba_produktow): ").strip()
    kolumna_sortujaca = kolumna_sortujaca.lower()
    
    if not kolumna_sortujaca:
        kolumna_sortujaca = "liczba_produktow"
    
    if kolumna_sortujaca not in ALLOWED_SORT_COLUMNS:
        print(f"Kolumna sortowania '{kolumna_sortujaca}' nie jest dostępna w tym raporcie!")
        return
        
    kierunek_sortowania = input("Podaj kierunek sortowania (ASC/DESC): ").strip().upper()
    
    if not kierunek_sortowania:
        kierunek_sortowania = "DESC"
        
    if kierunek_sortowania not in ALLOWED_SORT_DIRECTIONS:
        print(f"Kierunek sortowania '{kierunek_sortowania}' nie jest obsługiwany!")
        return
    
    kolumny_do_wyswietlenia = ("kategoria", "liczba_produktow")
    
    try:
        raport = generate_category_product_report(kolumna_sortujaca, kierunek_sortowania)
    
        if not raport:
            print("Raport nie zawiera żadnych rekordów!")
        else:
            display_query_results(kolumny_do_wyswietlenia, raport)
    except Exception as e:
        print(f"Wystąpił błąd podczas generowania raportu: {e}")
        
        
if __name__ == "__main__":
    main()