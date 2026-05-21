samogloski = "aeiouy"
zdanie = input("Podaj zdanie: ")

for litera in zdanie:
    if litera.lower() not in samogloski:
        continue
    print(litera)