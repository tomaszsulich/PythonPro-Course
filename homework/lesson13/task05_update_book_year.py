from library_db import get_connection

def zaktualizuj_rok(autor: str, tytul: str, nowy_rok: int) -> None:
    """Zmienia rok wydania książki i wyświetla zaktualizowany rekord"""
    with get_connection() as conn:
        c = conn.cursor()
        
        c.execute("""UPDATE ksiazki
                  SET rok_wydania = ?
                  WHERE autor = ? and tytul = ?""",
                  (nowy_rok, autor, tytul))
        
        zaktualizowana_ksiazka = c.execute(
            "SELECT * FROM ksiazki WHERE autor = ? AND tytul = ?",
            (autor, tytul)
        ).fetchall()
        
        print(zaktualizowana_ksiazka)
        

def main() -> None:
    zaktualizuj_rok("Tokuro Nukui", "Krzyk", 2015)
    

if __name__ == "__main__":
    main()