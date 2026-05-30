import sqlite3

# Utworzenie połączenia z bazą danych w pamięci
conn = sqlite3.connect(':memory:')
cursor = conn.cursor()

# Utworzenie tabeli i dodanie danych
cursor.execute('''--sql
CREATE TABLE Produkty (
    id INTEGER PRIMARY KEY,
    nazwa TEXT NOT NULL,
    cena REAL NOT NULL
)''')

produkty = [
('Laptop', 4500.00),
('Myszka', 150.00),
('Klawiatura', 250.00),
('Monitor', 1200.00),
('Słuchawki', 350.00)
]

cursor.executemany('INSERT INTO Produkty (nazwa, cena) VALUES (?, ?)', produkty)
conn.commit()

# Zapytanie z podzapytaniem
# Zapytanie główne: SELECT * FROM Produkty WHERE cena > (...)
# Podzapytanie: (SELECT AVG(cena) FROM Produkty)
query = '''--sql
SELECT nazwa, cena
FROM Produkty
WHERE cena > (SELECT AVG(cena) FROM Produkty)
'''

cursor.execute(query)
wyniki = cursor.fetchall()

print("Produkty droższe niż średnia:")
for row in wyniki:
    print(f"- {row[0]}: {row[1]:.2f} zł") # Laptop, Monitor
    
conn.close()