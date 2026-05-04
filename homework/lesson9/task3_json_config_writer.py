import json

CONFIG_FILE = "config.json"

def zapisz_konfiguracje(konfiguracja: dict) -> None:
    with open(CONFIG_FILE, "w", encoding = "utf-8") as f:
        json.dump(konfiguracja, f, indent = 4, ensure_ascii = False)


def main() -> None:
    konfiguracja = {
        "uzytkownik": "admin",
        "motyw": "ciemny",
        "rozdzielczosc": [1920, 1080]
    }
    
    zapisz_konfiguracje(konfiguracja)

        
if __name__ == "__main__":
    main()