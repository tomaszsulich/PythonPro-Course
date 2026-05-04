import json

CONFIG_FILE = "config.json"

def wczytaj_konfiguracje() -> dict:
    with open(CONFIG_FILE, encoding = "utf-8") as f:
        return json.load(f)


def main() -> None:
    dane = wczytaj_konfiguracje()
    print(f"Witaj, {dane['uzytkownik']}! Twój motyw to {dane['motyw']}.")
    
    
if __name__ == "__main__":
    main()