from shop_db import get_connection
from task06_dynamic_query_builder import display_query_results

# TUTAJ LEPIEJ WYGLĄDAŁOBY NP. find_products_in_category, ALE POLECENIE WYMAGAŁO PL
def znajdz_produkty_w_kategorii(nazwa_kategorii: str = "Elektronika") -> list[tuple[str, float]]:
    """Wyszukuje produkty należące do wskazanej kategorii niezależnie od wielkości liter"""
    
    category_products_sql = """--sql
        SELECT p.nazwa_produktu, p.cena
        FROM produkty AS p
        JOIN kategorie AS k
        ON k.id_kategorii = p.id_kategorii
        WHERE LOWER(TRIM(k.nazwa_kategorii)) = LOWER(TRIM(?))
        ORDER BY p.nazwa_produktu
    """
    with get_connection() as conn:
        return conn.cursor().execute(category_products_sql,(nazwa_kategorii,)).fetchall()

def get_category_display_name(category: str) -> str | None:
    """Zwraca nazwę kategorii w formacie zapisanym w bazie danych"""
    
    category_display_name_sql = """--sql
    SELECT nazwa_kategorii FROM Kategorie
    WHERE nazwa_kategorii IS NOT NULL
    AND TRIM(nazwa_kategorii) != ''
    AND LOWER(nazwa_kategorii) = LOWER(?)
    """
    with get_connection() as conn:
        result = conn.cursor().execute(category_display_name_sql, (category,)).fetchone()
    
        if result is None:
            return None
        return result[0]
    
    
def main() -> None:
    kategoria = input("Podaj kategorię, w której chcesz znaleźć produkty: ").strip()
    if not kategoria:
        kategoria = "Elektronika"
    
    produkty = znajdz_produkty_w_kategorii(kategoria)
    
    if not produkty:
        print("Nie znaleziono produktów dla podanej kategorii.")
        return
    
    kategoria = get_category_display_name(kategoria)
    kolumny = ("nazwa_produktu", "cena")
    
    print(f"\nKategoria: {kategoria}")
    print(f"Liczba produktów: {len(produkty)}\n")
    
    display_query_results(kolumny, produkty)
    

if __name__ == "__main__":
    main()