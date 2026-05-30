# ----- KOD STARTOWY DO ZADAŃ -----
import sqlite3
from shop_db import get_connection

def przygotuj_baze() -> None:
    """Tworzy i wypełnia bazę danych na potrzeby zadań"""
    conn = sqlite3.connect('sklep.db') # Tworzy plik sklep.db
    cursor = conn.cursor()
    
    # Usunięcie tabel, jeśli istnieją, dla czystego startu
    cursor.execute("DROP TABLE IF EXISTS Zamowienia_Produkty")
    cursor.execute("DROP TABLE IF EXISTS Zamowienia")
    cursor.execute("DROP TABLE IF EXISTS Produkty")
    cursor.execute("DROP TABLE IF EXISTS Kategorie")
    cursor.execute("DROP TABLE IF EXISTS Klienci")
    
    # Tworzenie tabel
    cursor.execute('''--sql
    CREATE TABLE Kategorie (
        id_kategorii INTEGER PRIMARY KEY,
        nazwa_kategorii TEXT UNIQUE NOT NULL)''')
    
    cursor.execute('''--sql
    CREATE TABLE Produkty (
        id_produktu INTEGER PRIMARY KEY,
        nazwa_produktu TEXT NOT NULL,
        cena REAL NOT NULL,
        id_kategorii INTEGER,
        FOREIGN KEY (id_kategorii) REFERENCES Kategorie(id_kategorii))''')
    
    cursor.execute('''--sql
    CREATE TABLE Klienci (
        id_klienta INTEGER PRIMARY KEY,
        imie TEXT NOT NULL,
        email TEXT UNIQUE NOT NULL)''')
    
    cursor.execute('''--sql
    CREATE TABLE Zamowienia (
        id_zamowienia INTEGER PRIMARY KEY,
        id_klienta INTEGER,
        data_zamowienia DATE,
        FOREIGN KEY (id_klienta) REFERENCES Klienci(id_klienta))''')
    
    cursor.execute('''--sql
    CREATE TABLE Zamowienia_Produkty (
        id_zamowienia INTEGER,
        id_produktu INTEGER,
        ilosc INTEGER NOT NULL,
        PRIMARY KEY (id_zamowienia, id_produktu),
        FOREIGN KEY (id_zamowienia) REFERENCES Zamowienia(id_zamowienia),
        FOREIGN KEY (id_produktu) REFERENCES Produkty(id_produktu))''')
    
# Wstawianie danych
    kategorie = [('Elektronika',), ('Książki',), ('Dom i ogród',)]
    
    klienci = [
        ('Anna Nowak', 'anna.n@example.com'), 
        ('Jan Kowalski', 'jan.k@example.com'), 
        ('Zofia Wiśniewska', 'zofia.w@example.com')]
    
    produkty = [
        ('Laptop Pro', 5200.00, 1), ('Smartfon X', 2500.00, 1),
        ('Python dla każdego', 89.99, 2), ('Wzorce projektowe', 120.50, 2),
        ('Kosiarka elektryczna', 750.00, 3), ('Zestaw narzędzi', 300.00, 3),
        ('Słuchawki bezprzewodowe', 450.00, 1)]
    
    zamowienia = [(1, '2023-10-01'), (2, '2023-10-02'), (1, '2023-10-05')]
    zamowienia_produkty = [(1, 1, 1), (1, 7, 1), (2, 3, 2), (3, 5, 1)]
    
    cursor.executemany("INSERT INTO Kategorie (nazwa_kategorii) VALUES (?)", kategorie)
    cursor.executemany("INSERT INTO Klienci (imie, email) VALUES (?,?)", klienci)
    cursor.executemany("INSERT INTO Produkty (nazwa_produktu, cena, id_kategorii) VALUES (?,?,?)", 
                       produkty)
    cursor.executemany("INSERT INTO Zamowienia (id_klienta, data_zamowienia) VALUES (?,?)", 
                       zamowienia)
    cursor.executemany("INSERT INTO Zamowienia_Produkty (id_zamowienia, id_produktu, ilosc) VALUES (?,?,?)", 
                       zamowienia_produkty)
    
    conn.commit()
    conn.close()
    print("Baza 'sklep.db' została przygotowana.")
    
# Wywołaj funkcję, aby stworzyć bazę przed rozpoczęciem pracy
przygotuj_baze()

# ZADANIE 1
def count_products() -> int:
    """Zlicza liczbę produktów w tabeli Produkty"""
    count_products_sql = """--sql
        SELECT COUNT(*)
        FROM Produkty
    """
    with get_connection() as conn:
        c = conn.cursor()
        return c.execute(count_products_sql).fetchone()[0]

# ZADANIE 3    
def get_electronics_total_value() -> float:
    """Zwraca łączną wartość produktów z kategorii Elektronika"""
    electronics_total_value_sql = """--sql
        SELECT SUM(p.cena)
        FROM produkty as p
        JOIN kategorie as k
        ON p.id_kategorii = k.id_kategorii
        WHERE k.nazwa_kategorii = 'Elektronika'
    """
    with get_connection() as conn:
        return conn.cursor().execute(electronics_total_value_sql).fetchone()[0]

# ZADANIE 7    
def get_customer_products(customer_name: str = "Anna Nowak") -> list[tuple[str]]:
    """Zwraca nazwy produktów zamówionych przez wybranego klienta"""
    customer_products_sql = """--sql
        SELECT p.nazwa_produktu
        FROM produkty as p
        JOIN zamowienia_produkty as zp
        ON zp.id_produktu = p.id_produktu
        JOIN zamowienia as z
        ON z.id_zamowienia = zp.id_zamowienia
        JOIN klienci as k
        ON k.id_klienta = z.id_klienta
        WHERE k.imie = ?
    """
    with get_connection() as conn:
        return conn.cursor().execute(customer_products_sql, (customer_name,)).fetchall()
    
  
def main():
    liczba_produktow = count_products()
    print(f"W tabeli Produkty znajduje się {liczba_produktow} pozycji.")
    
    wartosc_produktow_elektronika = get_electronics_total_value()
    print(f"Łączna wartość produktów z kategorii 'Elektronika' wynosi {wartosc_produktow_elektronika:.2f} PLN.")
    
    customer_name = input("Podaj imię klienta (domyślnie 'Anna Nowak'): ").strip()
    
    if not customer_name:
        customer_name = "Anna Nowak"
    
    produkty = get_customer_products(customer_name)
    
    if not produkty:
        print(f"Nie znaleziono produktów dla klienta '{customer_name}'.")
        return

    nazwy_produktow = [produkt[0] for produkt in produkty]
    print(f"{customer_name} kupił(a) " + ", ".join(nazwy_produktow) + ".")


if __name__ == "__main__":
    main()