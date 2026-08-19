import csv

CSV_FILE = "produkty.csv"

def zsumuj_ceny() -> float:
    try:
        with open(CSV_FILE, "r", encoding = "utf-8") as f:
            reader = csv.DictReader(f, delimiter = ";")
            return sum(float(wiersz["cena"]) for wiersz in reader)

    except FileNotFoundError:
        print("Plik nie istnieje.")
        return 0.0
            

def main() -> None:
    print(f"Suma cen: {zsumuj_ceny()}")
    
    
if __name__ == "__main__":
    main()