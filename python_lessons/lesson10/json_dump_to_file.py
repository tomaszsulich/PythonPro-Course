import json

uzytkownik = {"imie": "Jakub",
              "wiek": 22}

# zapisanie do pliku
with open("serial_test_file.json", "w") as fp:
    json.dump(uzytkownik, fp)
    
uzytkownik = {"imie": "Jakub",
              "wiek": 22,
              "oceny": [2.5, 1, 5, 6, "x"]}

# bardzo łatwo się zaktualizuje
with open("serial_test_file.json", "w") as fp:
    json.dump(uzytkownik, fp)