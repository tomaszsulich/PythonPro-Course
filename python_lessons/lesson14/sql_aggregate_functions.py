import sqlite3

conn = sqlite3.connect(':memory:')
cursor = conn.cursor()

cursor.execute('''--sql
CREATE TABLE Produkty (
id INTEGER PRIMARY KEY,
nazwa TEXT NOT NULL,
cena REAL NOT NULL,
ilosc_magazyn INT NOT NULL
)''')

produkty = [
('Laptop', 4500.00, 10),
('Myszka', 150.00, 150),
('Klawiatura', 250.00, 70),
('Monitor', 1200.00, 30),
('Słuchawki', 350.00, 90)
]

cursor.executemany('INSERT INTO Produkty (nazwa, cena, ilosc_magazyn) VALUES (?, ?, ?)', produkty)
conn.commit()

# Zapytanie używające funkcji agregujących
query = '''--sql
SELECT
COUNT(id) as liczba_produktow,
AVG(cena) as srednia_cena,
SUM(ilosc_magazyn) as laczna_ilosc_w_magazynie,
MIN(cena) as najnizsza_cena,
MAX(cena) as najwyzsza_cena
FROM Produkty'''

cursor.execute(query)
wynik = cursor.fetchone() # Zwraca jeden wiersz z wynikami

print(f"Liczba wszystkich produktów: {wynik[0]}")
print(f"Średnia cena produktu: {wynik[1]:.2f} zł")
print(f"Łączna ilość sztuk w magazynie: {wynik[2]}")
print(f"Najniższa cena: {wynik[3]:.2f} zł")
print(f"Najwyższa cena: {wynik[4]:.2f} zł")

conn.close()