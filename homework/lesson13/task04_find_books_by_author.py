from library_db import get_connection

def zwroc_ksiazki_autora(autor: str) -> list[tuple[str, str, int]]:
    """Zwraca wszystkie książki podanego autora."""
    if not isinstance(autor, str):
        raise TypeError("Autor musi być stringiem!")
    with get_connection() as conn:
        c = conn.cursor()
        c.execute("SELECT * FROM ksiazki WHERE autor = ?", (autor,))
        return c.fetchall()


def main() -> None:
    autor = input("Podaj autora: ")
    
    if not autor.strip():
        print("Musisz podać autora!")
        return
    
    ksiazki_fav_autora = zwroc_ksiazki_autora(autor)
    
    if not ksiazki_fav_autora:
        print("Nie znaleziono książek tego autora!")
        return
    
    for ksiazka in ksiazki_fav_autora:
        print(ksiazka)
    

if __name__ == "__main__":
    main()