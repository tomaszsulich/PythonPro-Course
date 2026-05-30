import sqlite3

conn = sqlite3.connect(':memory:')
cursor = conn.cursor()

# Tabela klientów
cursor.execute('''--sql
CREATE TABLE Klienci ( 
    id_klienta INTEGER PRIMARY KEY,
    imie TEXT NOT NULL)''')

cursor.execute("INSERT INTO Klienci (imie) VALUES ('Anna'), ('Piotr'), ('Katarzyna')")

# Tabela zamówień
cursor.execute('''--sql
CREATE TABLE Zamowienia (
    id_zamowienia INTEGER PRIMARY KEY,
    id_klienta INTEGER,
    produkt TEXT NOT NULL,
    FOREIGN KEY (id_klienta) REFERENCES Klienci(id_klienta)
)''')
cursor.execute("INSERT INTO Zamowienia (id_klienta, produkt) VALUES (1, 'Laptop'), (2, 'Myszka'), (1, 'Monitor')")
conn.commit()

# Zapytanie z JOIN
query = '''--sql
SELECT
Klienci.imie,
Zamowienia.produkt
FROM Zamowienia
INNER JOIN Klienci ON Zamowienia.id_klienta = Klienci.id_klienta
'''

cursor.execute(query)
wyniki = cursor.fetchall()

print("Zamówienia klientów:")
for row in wyniki:
    print(f"- Klient: {row[0]}, Produkt: {row[1]}")

conn.close()