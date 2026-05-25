import sqlite3

def stworz_tab_ksiazki():
    with sqlite3.connect("biblioteka.db") as conn:
        c = conn.cursor()
        res = c.execute('''CREATE TABLE ksiazki (
        id_ksiazka INTEGER PRIMARY KEY,
        tytul TEXT NOT NULL,
        autor TEXT NOT NULL,
        rok_wydania INTEGER)''')
        # Zatwierdzamy zmiany w bazie danych
        conn.commit()
        print("Tabela 'książki' została utworzona.")

def dodaj_ksiazki(ksiazki: list[tuple[str, str, int]]):
    with sqlite3.connect("biblioteka.db") as conn:
        c = conn.cursor()
        c.executemany("INSERT INTO ksiazki (tytul, autor, rok_wydania) VALUES (?, ?, ?)",
                      ksiazki)
        conn.commit()
        
def zwroc_ksiazki():
    with sqlite3.connect("biblioteka.db") as conn:
        c = conn.cursor()
        c.execute("select * from ksiazki")
        return c.fetchall()
    
def zwroc_ksiazki_autora(autor: str):
    with sqlite3.connect("biblioteka.db") as conn:
        c = conn.cursor()
        c.execute("select * from ksiazki where autor = ?", (autor,))
        return c.fetchall()
    
def zaktualizuj_rok(autor, tytul, nowy_rok):
    with sqlite3.connect('biblioteka.db') as conn:
        c = conn.cursor()
        c.execute("""UPDATE ksiazki
                  SET rok_wydania = ?
                  WHERE autor = ? and tytul = ?""",
                  (nowy_rok, autor, tytul))
        conn.commit()
        print(c.execute("select * from ksiazki where autor = ? and tytul =  ?",
                        (autor, tytul)).fetchall())
    

if __name__ == "__main__":
    # print(zwroc_ksiazki(), zwroc_ksiazki_autora("autor2"))
    zaktualizuj_rok("autor1", "ksiazka1", 2026)