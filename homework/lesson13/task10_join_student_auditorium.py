from students_db import get_connection

def znajdz_sale_studenta(nazwisko: str) -> list[tuple[str, str, str, int]]:
    """Zwraca audytoria przypisane do studenta o podanym nazwisku."""
    if not isinstance(nazwisko, str):
        raise TypeError("Nazwisko studenta musi być stringiem!")
    
    with get_connection() as conn:
        c = conn.cursor()
        
        c.execute("""
            SELECT s.imie, s.nazwisko, a.nazwa_budynku, a.numer_sali
            FROM studenci AS s
            JOIN przypisania AS p
            ON s.id_studenta = p.id_studenta
            JOIN audytoria AS a
            ON p.id_audytorium = a.id_audytorium
            WHERE s.nazwisko = ?
        """, (nazwisko,))
        
        return c.fetchall()


def main() -> None:
    nazwisko = input("Podaj nazwisko studenta: ")
    
    if not nazwisko.strip():
        print("Musisz podać nazwisko!")
        return
    
    sala_studenta = znajdz_sale_studenta(nazwisko.strip())
    
    if not sala_studenta:
        print("Nie znaleziono studenta lub przypisanego audytorium!")
        return
    
    for imie, nazwisko, nazwa_budynku, numer_sali in sala_studenta:
        print(f"Student {imie} {nazwisko} znajduje się w budynku {nazwa_budynku}, sala {numer_sali}.")
    

if __name__ == "__main__":
    main()