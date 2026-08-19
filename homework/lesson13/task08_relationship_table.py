from students_db import get_connection

def stworz_tab_przypisania() -> None:
    """Tworzy tabelę relacji między studentami i audytoriami."""
    with get_connection() as conn:
        c = conn.cursor()
        
        c.execute("""CREATE TABLE IF NOT EXISTS przypisania (
        id_przypisania INTEGER PRIMARY KEY,
        id_studenta INTEGER,
        id_audytorium INTEGER,
        
        FOREIGN KEY (id_studenta) 
            REFERENCES studenci(id_studenta)
            ON UPDATE CASCADE
            ON DELETE RESTRICT,
            
        FOREIGN KEY (id_audytorium) 
            REFERENCES audytoria(id_audytorium)
            ON UPDATE CASCADE
            ON DELETE RESTRICT)""")
        
        print("Tabela 'przypisania' jest gotowa do użycia.")


if __name__ == "__main__":
    stworz_tab_przypisania()