from sqlalchemy.orm import Session
from sqlalchemy_app.database import get_db
from sqlalchemy_app.models import Zadanie, Tag


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

 
def dodaj_tag_do_zadania(db: Session, id_zadania: int, nazwa_tagu: str) -> None:
    """Dodaje tag do wskazanego zadania."""
    zadanie = db.query(Zadanie).filter(Zadanie.id == id_zadania).first()
    
    if not zadanie:
        print("Nie znaleziono zadania o podanym ID.")
        return
    
    tag = db.query(Tag).filter(Tag.nazwa == nazwa_tagu).first()
    
    if tag is None:
        tag = Tag(nazwa=nazwa_tagu)
        db.add(tag)
            
    zadanie.tagi.append(tag)
    db.commit()
    
    print(f"Tag '{nazwa_tagu}' dodany do zadania ID {id_zadania}.")


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
        print("3. Oznacz zadanie jako zrobione")
        print("4. Usuń zadanie")
        print("5. Wyszukaj po frazie")
        print("6. Dodaj tag do zadania")
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
                id_zadania = int(input("Podaj ID zadania do oznaczenia: "))
                oznacz_jako_zrobione(db_session, id_zadania)
            except ValueError:
                print("Błędne ID. Podaj liczbę.")
                
        elif wybor == '4':
            try:
                id_zadania = int(input("Podaj ID zadania do usunięcia: "))
                usun_zadanie(db_session, id_zadania)
            except ValueError:
                print("Błędne ID. Podaj liczbę.")
                
        elif wybor == '5':
            fraza = input("Podaj frazę do wyszukania: ")
            wyszukaj_zadania(db_session, fraza)
            
        elif wybor == '6':
            try:
                id_zadania = int(input("Podaj ID zadania, do którego chcesz dodać tag: "))
                nazwa_tagu = input("Podaj nazwę tagu: ").strip()
                
                if not nazwa_tagu:
                    print("Nazwa tagu nie może być pusta.")
                    continue
                
                dodaj_tag_do_zadania(db_session, id_zadania, nazwa_tagu)
                
            except ValueError:
                print("Błędne ID. Podaj liczbę.")
                
        elif wybor == '7':
            print("Do zobaczenia!")
            db_session.close()
            break
            
            
if __name__ == "__main__":
    main()