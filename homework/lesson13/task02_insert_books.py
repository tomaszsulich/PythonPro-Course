from library_db import get_connection

def dodaj_ksiazki(ksiazki: list[tuple[str, str, int]]) -> None:
    """Dodaje wiele książęk do tabeli ksiazki"""
    with get_connection() as conn:
        c = conn.cursor()
        
        c.executemany("INSERT INTO ksiazki (tytul, autor, rok_wydania) VALUES (?, ?, ?)",
                      ksiazki)
        c.execute("SELECT * FROM ksiazki")
        
        ksiazki_w_bazie = c.fetchall()
        print("Książki w bazie:")
        for ksiazka in ksiazki_w_bazie:
            print(ksiazka)
        

def main() -> None:
    ksiazki_do_dodania = [
            ("Tango z rożnem", "Iwona Banach", 2023),
            ("Krzyk", "Tokuro Nukui", 1993),
            ("W mroku płytkich kłamstw", "Ginny Myers Sain", 2022)
        ]
    dodaj_ksiazki(ksiazki_do_dodania)
    
    
if __name__ == "__main__":
    main()