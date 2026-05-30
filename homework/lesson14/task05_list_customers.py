from shop_db import get_connection

DEFAULT_CUSTOMER_COLUMNS = ("imie", "email")
ALLOWED_CUSTOMER_COLUMNS = {"imie", "email"}

def get_customers(columns: tuple[str, str] = DEFAULT_CUSTOMER_COLUMNS) -> list[tuple[str, str]]:
    """Pobiera listę klientów wraz z ich adresami e-mail"""
    selected_columns = ", ".join(columns)
    
    customers_sql = f"""--sql
        SELECT {selected_columns} FROM klienci
    """
    with get_connection() as conn:
        return conn.cursor().execute(customers_sql).fetchall()
    
    
def main() -> None:
    kolejnosc_kolumn = input(
        "Wprowadź kolejność kolumn do wyświetlania (imie, email albo email, imie): "
    ).strip()
    
    if not kolejnosc_kolumn:
        kolejnosc_kolumn = DEFAULT_CUSTOMER_COLUMNS
    else:
        kolejnosc_kolumn = tuple(
            kolumna.strip().lower() for kolumna in kolejnosc_kolumn.split(",")
        )
    
    if len(kolejnosc_kolumn) != 2:
        print("Podaj dokładnie dwie kolumny: imie i email.")
        return
    
    bledne_kolumny = [kolumna for kolumna in kolejnosc_kolumn
                      if kolumna not in ALLOWED_CUSTOMER_COLUMNS]
    
    if bledne_kolumny:
        print(f"Niedozwolone kolumny: {', '.join(bledne_kolumny)}")
        return
    
    if set(kolejnosc_kolumn) != ALLOWED_CUSTOMER_COLUMNS:
        print("Dozwolone są tylko układy: imie, email albo email, imie.")
        return
    
    klienci = get_customers(kolejnosc_kolumn)
    
    if not klienci:
        print("\nBrak klientów w bazie danych.")
        return
    
    print("\nLista klientów:")
    for klient in klienci:
        print(" - ".join(klient))
        
        
if __name__ == "__main__":
    main()