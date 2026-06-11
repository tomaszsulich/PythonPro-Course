import psycopg2
from flask import Flask
import json
from auth import HOST, PORT, DATABASE, USER, PWD

app = Flask(__name__)

# Funkcja do nawiązywania połączenia z bazą danych
def get_db_connection():
    conn = psycopg2.connect(
        host=HOST,
        database=DATABASE,
        user=USER,
        password=PWD
    )
    return conn

@app.route('/users')
def list_users():
    conn = get_db_connection()
    # Tworzymy kursor, który pozwala wykonywać polecenia SQL
    cur = conn.cursor()
    # Wykonujemy zapytanie SQL
    cur.execute('SELECT * FROM users;')
    # Pobieramy wszystkie wyniki
    users = cur.fetchall()
    # Zamykamy kursor i połączenie
    cur.close()
    conn.close()
    # Zwracamy wyniki (na razie w prostej formie)
    return str(users)

if __name__ == '__main__':
    app.run(debug=True)