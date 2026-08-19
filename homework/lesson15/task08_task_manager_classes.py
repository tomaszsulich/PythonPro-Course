import sqlite3
from task01_app_raw_sql import pokaz_zadania


class TaskManagerRaw:
    """Udostępnia operacje CRUD na zadaniach przechowywanych w relacyjnej bazie danych SQLite."""
    
    def __init__(self, database: str = "todo_raw.db") -> None:
        self.database_name = database
        self.init_db()
        
    def init_db(self) -> None:
        """Inicjalizuje bazę danych i tworzy tabelę, jeśli nie istnieje."""
        with sqlite3.connect(self.database_name) as conn:
            cursor = conn.cursor()
            
            # Używamy IF NOT EXISTS, aby uniknąć błędu przy ponownym uruchomieniu
            cursor.execute("""--sql
            CREATE TABLE IF NOT EXISTS zadania (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            opis TEXT NOT NULL,
            zrobione BOOLEAN NOT NULL DEFAULT 0 CHECK (zrobione IN (0, 1)),
            priorytet INTEGER DEFAULT 1
            )""")
            
            conn.commit()
            
    def dodaj_zadanie(self, opis: str, priorytet: int = 1) -> None:
        """Dodaje nowe zadanie do bazy danych."""
        with sqlite3.connect(self.database_name) as conn:
            cursor = conn.cursor()
            
            # Używamy placeholderów (?), aby zapobiec SQL Injection
            cursor.execute(
                "INSERT INTO zadania (opis, priorytet) VALUES (?, ?)", 
                (opis, priorytet)
            )
            
            conn.commit()
            
    def pobierz_zadania(self) -> list[tuple]:
        """Pobiera wszystkie zadania z bazy danych."""
        with sqlite3.connect(self.database_name) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT id, opis, zrobione, priorytet FROM zadania")
            return cursor.fetchall()
        
    def wyszukaj_zadania(self, fraza: str) -> list[tuple]:
        """Wyszukuje zadania zawierające określoną frazę."""
        with sqlite3.connect(self.database_name) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT id, opis, zrobione, priorytet FROM zadania WHERE opis LIKE ?", (f"%{fraza}%",))
            return cursor.fetchall()
        
    def pokaz_zadania(self, zadania: list[tuple]) -> None:
        """Wyświetla listę zadań w czytelny sposób."""
        if not zadania:
            print("Brak zadań na liście.")
            return
        
        print("\n--- Twoja lista zadań ---")
        
        for zadanie in zadania:
            status = "✓" if zadanie[2] else "✗"
            print(f"[{status}] ID: {zadanie[0]}, Opis: {zadanie[1]}, Priorytet: {zadanie[3]}")
        print("------------------------\n")
        
    def oznacz_jako_zrobione(self, id_zadania: int) -> None:
        """Oznacza zadanie o podanym ID jako zrobione."""
        with sqlite3.connect(self.database_name) as conn:
            cursor = conn.cursor()
            
            cursor.execute(
                "UPDATE zadania SET zrobione = ? WHERE id = ?", 
                (True, id_zadania)
            )
            
            conn.commit()
            
    def usun_zadanie(self, id_zadania: int) -> None:
        """Usuwa zadanie o podanym ID z bazy danych."""
        with sqlite3.connect(self.database_name) as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM zadania WHERE id = ?", 
            (id_zadania,))
            conn.commit()
            
            
def main() -> None:
    manager = TaskManagerRaw()
    
    while True:
        print("Menu:")
        print("1. Pokaż zadania")
        print("2. Dodaj zadanie")
        print("3. Oznacz zadanie jako zrobione")
        print("4. Usuń zadanie")
        print("5. Wyszukaj po frazie")
        print("6. Wyjdź")
        
        wybor = input("Wybierz opcję: ")
        
        if wybor == '1':
            pokaz_zadania(manager.pobierz_zadania())
        elif wybor == '2':
            opis = input("Podaj opis zadania: ")
            manager.dodaj_zadanie(opis)
            print("Zadanie dodane!")
            
        elif wybor == '3':
            try:
                id_zadania = int(input("Podaj ID zadania do oznaczenia: "))
                manager.oznacz_jako_zrobione(id_zadania)
                print("Zadanie zaktualizowane!")
            except ValueError:
                print("Błędne ID. Podaj liczbę.")
                
        elif wybor == '4':
            try:
                id_zadania = int(input("Podaj ID zadania do usunięcia: "))
                manager.usun_zadanie(id_zadania)
                print("Zadanie usunięte!")
            except ValueError:
                print("Błędne ID. Podaj liczbę.")
                
        elif wybor == '5':
            fraza = input("Podaj frazę do wyszukania: ")
            pokaz_zadania(manager.wyszukaj_zadania(fraza))
            
        elif wybor == '6':
            print("Do zobaczenia!")
            break
        else:
            print("Nieprawidłowy wybór. Spróbuj ponownie.")
            

if __name__ == "__main__":
    main()