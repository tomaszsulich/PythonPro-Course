from shop_db import get_connection

ALLOWED_TABLES = {"Kategorie", "Produkty", "Klienci", "Zamowienia", "Zamowienia_Produkty"}
TABLE_NAME_MAP = {table.lower(): table for table in ALLOWED_TABLES}

def count_records(table_name: str = "Produkty") -> int:
    """Zlicza liczbę rekordów w określonej tabeli."""
    
    # UWAGA: Nazwa tabeli jest składana przez f-string.
    # Należy upewnić się, że tabela jest dozwolona, aby uniknąć SQL Injection.
    
    if table_name not in ALLOWED_TABLES:
        raise ValueError(f"Tabela '{table_name}' nie jest dozwolona!")

    count_records_sql = f"""--sql
        SELECT COUNT(*)
        FROM {table_name}
    """
    
    with get_connection() as conn:
        c = conn.cursor()
        return c.execute(count_records_sql).fetchone()[0]
    

def main() -> None:
    tabela_input = input(f"Podaj nazwę tabeli do zliczenia rekordów {ALLOWED_TABLES}: \n").strip()
    
    if not tabela_input:
        tabela = "Produkty"
    else:
        tabela = TABLE_NAME_MAP.get(tabela_input.lower())
    
    if tabela is None:
        print(f"Tabela '{tabela_input}' nie istnieje lub nie jest dozwolona!")
        return

    liczba_rekordow = count_records(tabela)
    print(f"W tabeli '{tabela}' znajduje się {liczba_rekordow} pozycji.")        

        
if __name__ == "__main__":
    main()