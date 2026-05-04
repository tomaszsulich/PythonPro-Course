import csv

CSV_FILE = "produkty.csv"

def zapisz_produkty(produkty: list[dict]) -> None:
    with open(CSV_FILE, "w", newline = "", encoding = "utf-8") as f:
        fieldnames = produkty[0].keys()
        writer = csv.DictWriter(f, fieldnames = fieldnames, delimiter = ";")
        
        writer.writeheader()
        writer.writerows(produkty)


def main() -> None:
    produkty = [
        {"nazwa": "Mleko", "cena": 3.50},
        {"nazwa": "Chleb", "cena": 4.20}
    ]
    
    zapisz_produkty(produkty)


if __name__ == "__main__":
    main()