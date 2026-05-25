import sqlite3

conn = sqlite3.connect("kurs.db")
c = conn.cursor()

# Sposób 1: Bezpieczne wstawianie danych za pomocą symboli zastępczych (?)
c.execute("INSERT INTO miasta (nazwa, populacja) VALUES (?, ?)",
('Warszawa', 1794166))
c.execute("INSERT INTO miasta (nazwa, populacja) VALUES (?, ?)", ('Kraków',
779996))

# Sposób 2: Wstawianie wielu rekordów naraz
miasta_do_dodania = [
('Łódź', 679941),
('Wrocław', 642869),
('Poznań', 534813)
]
c.executemany("INSERT INTO miasta (nazwa, populacja) VALUES (?, ?)",
miasta_do_dodania)
conn.commit()

print(f"Dodano {c.rowcount} rekordy do tabeli 'miasta'.")
conn.close()