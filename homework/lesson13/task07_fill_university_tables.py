from students_db import get_connection

def dodaj_studentow(studenci: list[tuple[str, str]]) -> None:
    """Zapisuje listę studentów w bazie uczelnia.db"""
    with get_connection() as conn:
        c = conn.cursor()
        
        c.executemany("INSERT INTO studenci (imie, nazwisko) VALUES (?, ?)", studenci)
        c.execute("SELECT * FROM studenci")
        
        studenci_w_bazie = c.fetchall()
        print("Studenci w bazie:")
        for student in studenci_w_bazie:
            print(student)
            
def dodaj_audytoria(audytoria: list[tuple[str, int]]) -> None:
    """Zapisuje listę audytoriów w bazie uczelnia.db"""
    with get_connection() as conn:
        c = conn.cursor()
        
        c.executemany("INSERT INTO audytoria (nazwa_budynku, numer_sali) VALUES (?, ?)", 
                      audytoria)
        c.execute("SELECT * FROM audytoria")
        
        audytoria_w_bazie = c.fetchall()
        print("\nAudytoria w bazie:")
        for audytorium in audytoria_w_bazie:
            print(audytorium)
        

def main() -> None:
    studenci_do_dodania = [
            ("Jan", "Kowalski"),
            ("Zofia", "Kucięba"),
            ("Patrycja", "Mucha"),
            ("Rafał", "Porajski"),
            ("Zuzanna", "Karciarska"),
            ("Patryk", "Sułtan"),
            ("Nikodem", "Wieszcz"),
            ("Zuzanna", "Waligórska"),
            ("Michał", "Wiśniewski"),
            ("Joanna", "Zapobierajska"),
            ("Karol", "Mikołajewski"),
            ("Olaf", "Lubaszenko"),
            ("Cezary", "Bałwochwalski"),
            ("Roch", "Janowski"),
            ("Anna", "Wiosnarska")
        ]
    dodaj_studentow(studenci_do_dodania)
    
    audytoria_do_dodania = [
        ("Wydział Matematyczno-Przyrodniczy. Szkoła Nauk Ścisłych", 1245),
        ("Wydział Psychologii Tradingu", 1703),
        ("Studium Wychowania Fizycznego", 10),
        ("Studium Języków Obcych", 32),
        ("Wydział Prawa i Administracji", 16),
        ("Wydział Nauk Humanistrycznych", 1134)
        ]
    dodaj_audytoria(audytoria_do_dodania)
    
    
if __name__ == "__main__":
    main()