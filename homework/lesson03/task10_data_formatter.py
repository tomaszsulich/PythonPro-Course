pelne_imie = input("Podaj swoje imię i nazwisko: ")

pelne_imie_czyste = pelne_imie.strip()
pelne_imie_duze = pelne_imie_czyste.title()
dlugosc = len(pelne_imie_duze)

print(pelne_imie_duze)
print(f"Długość wprowadzonego ciągu jest równa {dlugosc} znaków.")