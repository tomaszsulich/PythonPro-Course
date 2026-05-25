import sqlite3

conn = sqlite3.connect('kurs.db')
c = conn.cursor()

nowa_populacja = 540000
miasto_do_aktualizacji = 'Poznań'
c.execute("SELECT * FROM miasta WHERE nazwa = ?", (miasto_do_aktualizacji))
print(c.fetchone())

conn.close()
exit()

c.execute("UPDATE miasta SET populacja = ? WHERE nazwa = ?", (nowa_populacja, miasto_do_aktualizacji))
conn.commit()
print(f"Zaktualizowano populację dla miasta: {miasto_do_aktualizacji}. Zmieniono {c.rowcount} rekordów.")
# Sprawdźmy, czy zmiana została zapisana
c.execute("SELECT * FROM miasta WHERE nazwa = ?", (miasto_do_aktualizacji,))
zaktualizowane_miasto = c.fetchone()