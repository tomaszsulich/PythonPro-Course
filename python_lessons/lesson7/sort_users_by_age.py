users_dict = [
    {"imie": "pawel", "wiek": 27, "plec": 1, "miejscowosc": "bialystok"},
    {"imie": "malwina", "wiek": 22, "plec": 0, "miejscowosc": "wroclaw"},
    {"imie": "ezekiel", "wiek": 30, "plec": 1, "miejscowosc": "bielsko-biala"}
]

sorted_users = sorted(users_dict, key = lambda user: user["wiek"])
for u in sorted_users:
    print(u["imie"], u["wiek"])