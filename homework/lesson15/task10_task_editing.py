from sqlalchemy.orm import Session
from sqlalchemy_app.database import get_db
from sqlalchemy_app.models import Zadanie


def pokaz_zadania(db: Session) -> None:
    """Wyświetla listę wszystkich zadań."""
    zadania = db.query(Zadanie).all() # Zamiast SELECT * FROM ...
    
    if not zadania:
        print("Brak zadań na liście.")
        return
    
    print("\n--- Twoja lista zadań ---")
    
    for zadanie in zadania:
        status = "✓" if zadanie.zrobione else "✗"
        print(f"[{status}] ID: {zadanie.id}, Opis: {zadanie.opis}")
        
    print("------------------------\n")


def wyszukaj_zadania(db: Session, fraza: str) -> None:
    """Wyszukuje zadania zawierające określoną frazę."""
    zadania = db.query(Zadanie).filter(Zadanie.opis.contains(fraza)).all()
    
    if not zadania:
        print("Brak zadań zawierających tę frazę.")
        return
    
    print(f"\n--- Zadania zawierające '{fraza}' ---")
    
    for zadanie in zadania:
        status = "✓" if zadanie.zrobione else "✗"
        print(f"[{status}] ID: {zadanie.id}, Opis: {zadanie.opis}")
        
    print("------------------------\n")


def dodaj_zadanie(db: Session, opis: str) -> None:
    """Dodaje nowe zadanie do bazy."""
    nowe_zadanie = Zadanie(opis=opis) # Tworzymy obiekt, a nie piszemy INSERT
    db.add(nowe_zadanie)
    db.commit()
    db.refresh(nowe_zadanie) # Odśwież, aby pobrać ID


def edytuj_zadanie(db: Session, id_zadania: int, nowy_opis: str) -> None:
    """Edytuje opis zadania o podanym ID."""
    zadanie = db.query(Zadanie).filter(Zadanie.id == id_zadania).first()
    
    if zadanie:
        zadanie.opis = nowy_opis # Po prostu zmieniamy atrybut!
        db.commit()
        print("Zadanie zaktualizowane!")
    else:
        print("Nie znaleziono zadania o podanym ID.")


def oznacz_jako_zrobione(db: Session, id_zadania: int) -> None:
    """Oznacza zadanie jako zrobione."""
    zadanie = db.query(Zadanie).filter(Zadanie.id == id_zadania).first() #  Wyszukujemy obiekt
    
    if zadanie:
        zadanie.zrobione = True # Po prostu zmieniamy atrybut!
        db.commit()
        print("Zadanie zaktualizowane!")
    else:
        print("Nie znaleziono zadania o podanym ID.")


def usun_zadanie(db: Session, id_zadania: int) -> None:
    """Usuwa zadanie z bazy."""
    zadanie = db.query(Zadanie).filter(Zadanie.id == id_zadania).first()
    
    if zadanie:
        db.delete(zadanie) # Usuwamy obiekt, a nie piszemy DELETE
        db.commit()
        print("Zadanie usunięte!")
    else:
        print("Nie znaleziono zadania o podanym ID.")
        

def main() -> None:
    db_generator = get_db()
    db_session = next(db_generator)
    
    while True:
        print("Menu (SQLAlchemy):")
        print("1. Pokaż zadania")
        print("2. Dodaj zadanie")
        print("3. Edytuj zadanie")
        print("4. Oznacz zadanie jako zrobione")
        print("5. Wyszukaj po frazie")
        print("6. Usuń zadanie")
        print("7. Wyjdź")
        
        wybor = input("Wybierz opcję: ")

        if wybor == '1':
            pokaz_zadania(db_session)
            
        elif wybor == '2':
            opis = input("Podaj opis zadania: ")
            dodaj_zadanie(db_session, opis)
            print("Zadanie dodane!")
            
        elif wybor == '3':
            try:
                id_zadania = int(input("Podaj ID zadania, które chcesz edytować: "))
                nowy_opis = input("Podaj nowy opis zadania: ")
                edytuj_zadanie(db_session, id_zadania, nowy_opis)
            except ValueError:
                print("Błędne ID. Podaj liczbę.")
                
        elif wybor == '4':
            try:
                id_zadania = int(input("Podaj ID zadania, które chcesz oznaczyć jako zrobione: "))
                oznacz_jako_zrobione(db_session, id_zadania)
            except ValueError:
                print("Błędne ID. Podaj liczbę.")
                
        elif wybor == '5':
            fraza = input("Podaj frazę do wyszukania: ")
            wyszukaj_zadania(db_session, fraza)
        
        elif wybor == '6':
            try:
                id_zadania = int(input("Podaj ID zadania, które chcesz usunąć: "))
                usun_zadanie(db_session, id_zadania)
            except ValueError:
                print("Błędne ID. Podaj liczbę.")
                    
        elif wybor == '7':
            print("Do zobaczenia!")
            db_session.close()
            break
        
        else:
            print("Nieznana opcja, spróbuj ponownie.")
            
            
if __name__ == "__main__":
    main()