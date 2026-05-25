import sqlite3

DB_NAME = "biblioteka.db"

def get_connection():
    return sqlite3.connect(DB_NAME)