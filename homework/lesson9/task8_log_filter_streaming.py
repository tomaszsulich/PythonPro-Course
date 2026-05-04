from pathlib import Path

INPUT_FILE = Path("lesson9/log.txt")
OUTPUT_FILE = Path("wyniki_wyszukiwania.txt")

def filtruj_logi(sciezka_we: Path, sciezka_wy: Path, keyword: str) -> int:
    znalezione = 0
    
    with open(sciezka_we, "r", encoding = "utf8") as infile, \
        open(sciezka_wy, "w", encoding = "utf8") as outfile:
            
            # jedno przejście po pliku, bo "Wyobraź sobie"
            for line in infile:
                if keyword in line:
                    # jeden open na plik wynikowy - nie otwieramy go 1000 razy
                    outfile.write(line)
                    znalezione += 1
                    
    return znalezione


def main() -> None:
    keyword = input("Podaj słowo-klucz do wyszukania w logach: ").strip()
    
    if not keyword:
        print("Nie podano słowa kluczowego!")
        return
    
    liczba = filtruj_logi(INPUT_FILE, OUTPUT_FILE, keyword)
    
    print(f"Znaleziono {liczba} pasujących linii.")
    print(f"Wynik zapisano w: {OUTPUT_FILE}.")
    
    
if __name__ == "__main__":
    main()