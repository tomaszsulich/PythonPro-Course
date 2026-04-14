rasy = ["Elf", "Krasnolud", "Człowiek"]
klasy = ["Wojownik", "Mag", "Łotr"]

while True:
    rasa = input(f"Wybierz rasę {rasy}: ")
    if rasa in rasy:
        break
    print("Niepoprawna rasa!")
    
while True:
    klasa = input(f"Wybierz klasę {klasy}: ")
    if klasa in klasy:
        break
    print("Niepoprawna klasa!")
    
print(f"Stworzono postać: {rasa} {klasa}")

# WERSJA PODSTAWOWA - OD PAWŁA
# rasa = input("Podaj rasę: ")
# klasa = input("Podaj klasę: ")

# print("Stworzono postać:", rasa, klasa)