import random

from faker import Faker


fake = Faker("pl_PL")


sentences = [
    "Programista analizuje wyniki projektu.",
    "Student czyta ciekawą książkę.",
    "Turysta odwiedza piękne miasto.",
    "Kucharz przygotowuje nowy przepis.",
    "Lekarz analizuje nowy raport.",
    "Nauczyciel sprawdza kolejne zadanie.",
    "Dziennikarz pisze interesujący artykuł.",
    "Sportowiec wybiera nowy sprzęt sportowy.",
    "Programista poznaje nowe technologie.",
    "Student przygotowuje ważne dokumenty.",
]


random.shuffle(sentences)


print("=== Losowe polskie imiona i nazwiska ===")

for _ in range(10):
    print(fake.name())


print("\n=== Losowe zdania ===")

for sentence in sentences:
    print(sentence)


# WYNIK Z KONSOLI
# === Losowe polskie imiona i nazwiska ===
# Hubert Madziar
# Julianna Bork
# Paweł Szoka
# pani Ewelina Ubysz
# Klara Hankiewicz
# Miłosz Heleniak
# pan Patryk Tadeusiak
# pani Bianka Fronczyk
# Olgierd Szpyra
# Artur Stąpor

# === Losowe zdania ===
# Nauczyciel sprawdza kolejne zadanie.
# Dziennikarz pisze interesujący artykuł.
# Student przygotowuje ważne dokumenty.
# Sportowiec wybiera nowy sprzęt sportowy.
# Lekarz analizuje nowy raport.
# Turysta odwiedza piękne miasto.
# Programista poznaje nowe technologie.
# Programista analizuje wyniki projektu.
# Kucharz przygotowuje nowy przepis.
# Student czyta ciekawą książkę.