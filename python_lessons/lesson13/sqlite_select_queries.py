import sqlite3

conn = sqlite3.connect("kurs.db")

c = conn.cursor()
# Pobierz wszystkie kolumny (*) z tabeli 'miasta'
c.execute("SELECT * FROM miasta")

# fetchall() pobiera wszystkie pasujące rekordy
wszystkie_miasta = c.fetchall()
print("Wszystkie miasta w bazie:")

for miasto in wszystkie_miasta:
    print(miasto)

print("\nMiasta z populacją powyżej 700 000:")
# Możemy filtrować wyniki za pomocą klauzuli WHERE
c.execute("SELECT nazwa, populacja FROM miasta WHERE populacja > ?",
(700000,))

# fetchone() pobiera jeden pasujący rekord
miasta_powyzej_700k = c.fetchall()

for miasto in miasta_powyzej_700k:
    print(f" - {miasto[0]}, populacja: {miasto[1]}")
    
conn.close()