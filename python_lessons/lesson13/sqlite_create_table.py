import sqlite3


conn = sqlite3.connect("kurs.db")

c = conn.cursor()
# Analiza zapytania CREATE TABLE :
# INSERT INTO – Wstawianie danych
# Teraz, gdy mamy tabelę, wstawmy do niej kilka rekordów.
# Polecenie execute() wykonuje zapytanie SQL
# Używamy potrójnych cudzysłowów dla czytelności wieloliniowych zapytań
res = c.execute('''
CREATE TABLE if not exists miasta (
id_miasta INTEGER PRIMARY KEY,
nazwa TEXT NOT NULL,
populacja INTEGER)''')
# Zatwierdzamy zmiany w bazie danych
conn.commit()

print("Tabela 'miasta' została utworzona.")
conn.close()