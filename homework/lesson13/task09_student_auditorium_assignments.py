from students_db import get_connection

def dodaj_przypisania() -> None:
    """Łączy studentów z audytoriami w tabeli przypisań."""
    with get_connection() as conn:
        c = conn.cursor()
        
        c.execute("SELECT id_studenta FROM studenci")
        studenci = c.fetchall()
        
        c.execute("SELECT id_audytorium FROM audytoria")
        audytoria = c.fetchall()
        
        przypisania = []
        
        for index, (id_studenta, ) in enumerate(studenci):
            id_audytorium = audytoria[index % len(audytoria)][0]
            przypisania.append((id_studenta, id_audytorium))
            
        c.executemany("INSERT INTO przypisania (id_studenta, id_audytorium) VALUES (?, ?)",
                      przypisania)
        
        c.execute("SELECT * FROM przypisania")
        
        przypisania_w_bazie = c.fetchall()
        
        for id_przypisania, id_studenta, id_audytorium in przypisania_w_bazie:
            print(
                f"Przypisanie {id_przypisania}: ",
                f"student {id_studenta} -> audytorium {id_audytorium}"
            )
            
            
if __name__ == "__main__":
    dodaj_przypisania()