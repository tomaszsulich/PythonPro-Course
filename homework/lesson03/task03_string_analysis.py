napis = " Python jest super! "

napis_poprawny = napis.strip()
print(napis_poprawny)

napis_małe = napis_poprawny.lower()
print(napis_małe)

napis_zamienione = napis_małe.replace("super", "świetny")
print(napis_zamienione)

napis_znak = napis_zamienione[4]
print(f"Znak pod indeksem 4 brzmi '{napis_znak}'.")