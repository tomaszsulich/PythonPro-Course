from library_db import get_connection

def stworz_tab_ksiazki() -> None:
    with get_connection() as conn:
        c = conn.cursor()
        
        c.execute("""CREATE TABLE IF NOT EXISTS ksiazki (
        id_ksiazka INTEGER PRIMARY KEY,
        tytul TEXT NOT NULL,
        autor TEXT NOT NULL,
        rok_wydania INTEGER)""")
        
        # Przy użyciu "with sqlite3.connect(...)" commit często wykonuje się automatycznie.
        # W praktyce jawny commit bywa pomijany, ale tutaj zostawiamy go dla czytelności.
        conn.commit()
        print("Tabela 'książki' jest gotowa do użycia.")
    

if __name__ == "__main__":
    stworz_tab_ksiazki()