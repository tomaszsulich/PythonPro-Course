import pdb
import sqlite3

DATABASE_NAME = 'todo_raw.db'

def pobierz_zadania():
    """Pobiera wszystkie zadania z bazy danych."""
    qr = """--sql
    SELECT id, opis, zrobione, priorytet FROM zadania
    """
    with sqlite3.connect(DATABASE_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute(qr)
        return cursor.fetchall()
    
def pokaz_zadania():
    """Wyświetla listę wszystkich zadań."""
    zadania = pobierz_zadania()
    if not zadania:
        print("Brak zadań na liście.")
        return
    
    print("\n--- Twoja lista zadań ---")
    for i, (id_, opis, status, prio) in enumerate(zadania):
        pdb.set_trace()
        status = "✓" if status else "✗"
        print(f"[{status}] [ID: {id_}][prio: {prio}]: {opis}")
        print("------------------------\n") 

def dodaj_zadanie(opis: str, priorytet: int):
    """Dodaje nowe zadanie do bazy danych."""
    qr = """--sql
    INSERT INTO zadania (opis, priorytet) VALUES (?, ?)
    """
    with sqlite3.connect(DATABASE_NAME) as conn:
        cursor = conn.cursor()
        # Używamy placeholderów (?), aby zapobiec SQL Injection
        cursor.execute(qr, (opis, priorytet))
        conn.commit()
        
def wyszukaj_zadanie(fragment_opisu: str):
    """Wyszukuje zadania zawierające dany fragment opisu."""
    qr = """--sql
    SELECT id, opis, zrobione, priorytet 
    FROM zadania
    WHERE opis LIKE ?
    """
    with sqlite3.connect(DATABASE_NAME) as conn:
        cursor = conn.cursor()
        # Używamy placeholdera (?) i dodajemy wildcardy (%) do wyszukiwania
        cursor.execute(qr, (f"%{fragment_opisu}%", ))
        return cursor.fetchall()
        
def usun_zadanie(id_zadania: int):
    """Usuwa zadanie o podanym ID z bazy danych."""
    qr = """--sql
        DELETE FROM zadania
        WHERE id = ?
        """
    with sqlite3.connect(DATABASE_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute(qr, (id_zadania,))
        conn.commit()
        
def menu_dodaj_zadanie():
    opis = input("Podaj opis zadania do dodania, ['q' - wyjście]: ").strip()
    prio = input("Podaj priorytet zadania (1-5), [def=1]: ").strip()
    
    if prio == "":
        prio = 1
    else:
        try:
            prio = int(prio)
            if not (1 <= prio <= 5):
                raise ValueError("Wartość priorytetu spoza dozwolonego zakresu.")
        except ValueError:
            print("Podano niepoprawną liczbę.")
    dodaj_zadanie(opis, prio)
    print("Zadanie dodane!")

def menu_usun_zadanie():
    id_ = input("Podaj id zadania do usunięcia, ['q' - wyjście]: ").strip()
    
    if id_.lower() == 'q':
        return
    
    try:
        usun_zadanie(int(id_))
    except ValueError:
        print("Podano niepoprawną liczbę.")