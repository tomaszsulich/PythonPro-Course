import csv

dane_csv = [["Imię", "Wiek", "Miasto"],
            ["Anna", 25, "Gdańsk"],
            ["Piotr", 32, "Kraków"]]

# --- Zapis do pliku CSV --
with open("dane.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f, delimiter=';') # Możemy zmienić separator
    writer.writerows(dane_csv)
    

sep = ";"
with open("dane.csv", "w", encoding="utf-8") as fp:
    stringed_data = ("\n".join(sep.join(str(cell) for cell in row))
                    for row in dane_csv)
    fp.write(stringed_data)