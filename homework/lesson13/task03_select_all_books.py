from library_db import get_connection

def zwroc_ksiazki() -> list[tuple[str, str, int]]:
    """Zwraca wszystkie książki zapisane w bazie danych"""
    with get_connection() as conn:
        c = conn.cursor()
        c.execute("SELECT * FROM ksiazki")
        return c.fetchall()

 
def main() -> None:
    ksiazki = zwroc_ksiazki()
    
    for ksiazka in ksiazki:
        print(ksiazka)

   
if __name__ == "__main__":
    main()