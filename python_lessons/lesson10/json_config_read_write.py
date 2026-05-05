import json

CONFIG_FILE = "config.json"

konfiguracja = {"uzytkownik": "admin", 
                "motyw": "ciemny", 
                "rozdzielczosc": [1920, 1080]}

with open(CONFIG_FILE, "w", encoding = "utf8") as fp:
    json.dump(konfiguracja, fp)
    
with open(CONFIG_FILE, encoding = "utf8") as fp:
    wczytana_konf = json.load(fp)
print(f"Witaj, {wczytana_konf['uzytkownik']}! Twój motyw to {wczytana_konf['motyw']}.")