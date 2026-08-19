from shop_db import get_connection
from task01_count_products import ALLOWED_TABLES

DATABASE_COLUMNS = {"id_kategorii", "nazwa_kategorii", "id_klienta", "imie", "email", "cena",
                    "id_produktu", "nazwa_produktu", "id_kategorii", "id_zamowienia",
                    "id_klienta", "data_zamowienia", "ilosc", ...}

TABLE_NAME_MAP = {table.lower(): table for table in ALLOWED_TABLES}

ALLOWED_COLUMNS_BY_TABLE = {
    "Produkty": {"id_produktu", "nazwa_produktu", "cena", "id_kategorii"},
    "Kategorie": {"id_kategorii", "nazwa_kategorii"},
    "Klienci": {"id_klienta", "imie", "email"},
    "Zamowienia": {"id_zamowienia", "id_klienta", "data_zamowienia"},
    "Zamowienia_Produkty": {"id_zamowienia", "id_produktu", "ilosc"},
}

COLUMN_NAME_MAP_BY_TABLE = {
    table: {column.lower(): column for column in columns}
    for table, columns in ALLOWED_COLUMNS_BY_TABLE.items()
}

ALLOWED_NUMERIC_COLUMNS_BY_TABLE = {
    "Produkty": {"cena"}, 
    "Zamowienia_Produkty": {"ilosc"}
}

NUMERIC_COLUMN_NAME_MAP_BY_TABLE = {
    table: {column.lower(): column for column in columns}
    for table, columns in ALLOWED_NUMERIC_COLUMNS_BY_TABLE.items()
}


def validate_columns_for_table(columns: tuple[str, ...], table_name: str) -> bool:
    """
    Rozróżnia kolumny nieistniejące w bazie od kolumn niedostępnych 
    w kontekście wybranej tabeli.
    """
    
    missing_columns = []
    disallowed_columns = []
    
    for column in columns:
        if column not in DATABASE_COLUMNS:
            missing_columns.append(column)
        elif column not in ALLOWED_COLUMNS_BY_TABLE[table_name]:
            disallowed_columns.append(column)
        
    if missing_columns:
        print("Kolumny nieistniejące w bazie:")
        
        for column in missing_columns:
            print(f"- {column}")
            
    if disallowed_columns:
        print(f"Kolumny niedostępne dla tabeli '{table_name}':")
        
        for column in disallowed_columns:
            print(f"- {column}")
    
    return not missing_columns and not disallowed_columns

def get_records_above_average(table_name: str = "Produkty", \
                              columns: tuple[str, ...] = ("nazwa_produktu", "cena"), \
                              comparison_column: str = "cena") -> list[tuple]:
    """
    Zwraca rekordy z wybranej tabeli, których wartość wskazanej kolumny jest wyższa
    od średniej wartości tej kolumny.
    """
    
    if table_name not in ALLOWED_TABLES:
        raise ValueError(f"Tabela '{table_name}' nie jest dozwolona!")
    
    allowed_columns = ALLOWED_COLUMNS_BY_TABLE[table_name]
    
    for column in columns:
        if column not in allowed_columns:
            raise ValueError(f"Kolumna '{column}' nie istnieje w tabeli '{table_name}'!")
    
    allowed_numeric_columns = ALLOWED_NUMERIC_COLUMNS_BY_TABLE.get(table_name, set())
    
    if comparison_column not in allowed_numeric_columns:
        raise ValueError(
            f"Kolumna '{comparison_column}' nie może być użyta do liczenia średniej w tabeli '{table_name}'!"
        )
    
    selected_columns = ", ".join(columns)
    
    above_average_records_sql = f"""--sql
        SELECT {selected_columns} FROM {table_name}
        WHERE {comparison_column} > (SELECT AVG({comparison_column}) FROM {table_name})
    """
    
    with get_connection() as conn:
        return conn.cursor().execute(above_average_records_sql).fetchall()
    
def display_query_results(columns: tuple[str, ...], results: list[tuple]) -> None:
    """Wyświetla wyniki zapytania w formie prostej tabeli tekstowej."""
    
    widths = []
    
    for index, column in enumerate(columns):
        max_value_width = max(
            len(f"{row[index]:.2f}")
            if isinstance(row[index], float)
            else len(str(row[index]))
            for row in results)
        
        width = max(len(column), max_value_width)
        widths.append(width)
    
    separator = "+"
    
    for width in widths:
        separator += "-" * (width + 2) + "+"
    print(separator)
    
    header = "|"
    
    for column, width in zip(columns, widths):
        header += f" {column.center(width)} |"
        
    print(header)
    print(separator)
    
    for row in results:
        row_text = "|"
        
        for value, width in zip(row, widths):
            if isinstance(value, float):
                value = f"{value:.2f}"
            else:
                value = str(value)
            row_text += f" {value.center(width)} |"
            
        print(row_text)
        print(separator)

 
def main() -> None:
    tabela = input(f"Podaj nazwę tabeli do zapytania {ALLOWED_TABLES}:\n").strip()
    
    if not tabela:
        tabela = "Produkty"
    else:
        tabela = TABLE_NAME_MAP.get(tabela.lower())
    
    if tabela is None:
        print(f"Podana tabela nie istnieje lub nie jest dozwolona!")
        return
        
    kolumny = input("Podaj kolumny do wyświetlenia (oddzielone przecinkami):\n").strip()
    
    if not kolumny:
        kolumny = ("nazwa_produktu", "cena")
    else:
        kolumny_wejsciowe = tuple(
            kolumna.strip().lower()
            for kolumna in kolumny.split(",")
        )
        
        if not validate_columns_for_table(kolumny_wejsciowe, tabela):
            return 
        
        mapowanie_kolumn = COLUMN_NAME_MAP_BY_TABLE[tabela]
        
        kolumny = tuple(
            mapowanie_kolumn.get(kolumna.strip().lower())
            for kolumna in kolumny.split(",")
        )
    
    kolumna_porownujaca = input("Podaj kolumnę, po której chcesz liczyć średnią: ").strip().lower()
    
    if not kolumna_porownujaca:
        kolumna_porownujaca = "cena"
    
    if kolumna_porownujaca not in DATABASE_COLUMNS:
        print("Podana kolumna nie istnieje!")
        return
    
    if kolumna_porownujaca not in ALLOWED_COLUMNS_BY_TABLE[tabela]:
        print("Podana kolumna nie jest dostępna dla wybranej tabeli!")
        return
        
    if kolumna_porownujaca not in ALLOWED_NUMERIC_COLUMNS_BY_TABLE.get(tabela, set()):
        print("Nie możesz liczyć średniej po tej kolumnie!")
        return
    
    try:
        wyniki = get_records_above_average(tabela, kolumny, kolumna_porownujaca)
        
        if not wyniki:
            print(f"Nie znaleziono rekordów spełniających warunek.")
            return
    
        print("Rekordy spełniające warunek:")
        display_query_results(kolumny, wyniki)
        
    except ValueError as e:
        print(e)
        
        
if __name__ == "__main__":
    main()