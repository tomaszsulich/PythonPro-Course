import json

def wczytaj_zadania() -> list[str]:
    try:
        with open("zadania.json", encoding = "utf-8") as f:
            return json.load(f)
        
    except FileNotFoundError:
        return []
    
def zapisz_zadania(zadania: list[str]) -> None:
    with open("zadania.json", "w", encoding = "utf-8") as f:
        json.dump(zadania, f, indent = 4, ensure_ascii = False)

def task_manager() -> None:
    zadania = wczytaj_zadania()
    
    while True:
        print("\n1. Dodaj zadanie.")
        print("2. Wyświetl zadania.")
        print("3. Zapisz i zakończ.")
        
        wybor = input("Wybierz opcję: ")
        
        if wybor == "1":
            nowe_zadanie = input("Dodaj nowe zadanie: ")
            zadania.append(nowe_zadanie)
            
        elif wybor == "2":
            if zadania:
                for i, zadanie in enumerate(zadania, 1):
                    print(f"{i}. {zadanie}")
            else:
                print("Brak zadań.")
                
        elif wybor == "3":
            zapisz_zadania(zadania)
            print("Zapisano zadania.")
            break
        
        else:
            print("Niepoprawna opcja.")
    

def main():
    task_manager()
    
    
if __name__ == "__main__":
    main()