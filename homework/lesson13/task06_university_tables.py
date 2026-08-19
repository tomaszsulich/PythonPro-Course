from students_db import get_connection

def stworz_tab_studenci() -> None:
    """Tworzy tabelę studentów w bazie danych."""
    with get_connection() as conn:
        c = conn.cursor()
        
        c.execute("""CREATE TABLE IF NOT EXISTS studenci (
        id_studenta INTEGER PRIMARY KEY,
        imie TEXT NOT NULL,
        nazwisko TEXT NOT NULL)""")
        
        print("Tabela 'studenci' jest gotowa do użycia.")
        
def stworz_tab_audytoria() -> None:
    """Tworzy tabelę audytoriów w bazie danych."""
    with get_connection() as conn:
        c = conn.cursor()
        
        c.execute("""CREATE TABLE IF NOT EXISTS audytoria (
        id_audytorium INTEGER PRIMARY KEY,
        nazwa_budynku TEXT NOT NULL,
        numer_sali INTEGER)""")
        
        print("Tabela 'audytoria' jest gotowa do użycia.")
    

if __name__ == "__main__":
    stworz_tab_studenci()
    stworz_tab_audytoria()