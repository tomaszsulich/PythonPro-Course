import sqlite3

def zadanie8():
    qr = """--sql
    SELECT k.nazwa_kategorii as kategoria, COUNT(p.id_produktu)
    FROM kategorie as k
    JOIN produkty as p
    ON p.id_kategorii = k.id_kategorii
    GROUP BY p.id_kategorii
    """
    
    with sqlite3.connect("sklep.db") as conn:
        return conn.cursor().execute(qr).fetchall()


if __name__ == "__main__":
    for wiersz in zadanie8():
        print(wiersz)