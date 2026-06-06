from database_raw import pobierz_zadania, init_db, dodaj_zadanie, oznacz_jako_zrobione
# import database_raw as db - sposób zależy od ilości funkcji

def pokaz_zadania():
    """Wyświetla listę wszystkich zadań."""
    zadania = pobierz_zadania()
    if not zadania:
        print("Brak zadań na liście.")
        return
    
    print("\n--- Twoja lista zadań ---")
    for zadanie in zadania:
        status = "✓" if zadanie[2] else "✗"
        print(f"[{status}] ID: {zadanie[0]}, Opis: {zadanie[1]}")
        print("------------------------\n")
 
   
def main():
    # db.init_db()
    init_db() # Upewnij się, że baza i tabela istnieją
    
    while True:
        print("Menu:")
        print("1. Pokaż zadania")
        print("2. Dodaj zadanie")
        print("3. Oznacz zadanie jako zrobione")
        print("4. Wyjdź")
        wybor = input("Wybierz opcję: ")
        
        if wybor == '1':
            pokaz_zadania()
        elif wybor == '2':
            opis = input("Podaj opis zadania: ")
            dodaj_zadanie(opis)
            print("Zadanie dodane!")
            
        elif wybor == '3':
            try:
                id_zadania = int(input("Podaj ID zadania do oznaczenia: "))
                oznacz_jako_zrobione(id_zadania)
                print("Zadanie zaktualizowane!")
            except ValueError:
                print("Błędne ID. Podaj liczbę.")
                
        elif wybor == '4':
            print("Do zobaczenia!")
            break
        else:
            print("Nieznana opcja, spróbuj ponownie.")

           
if __name__ == "__main__":
    main()