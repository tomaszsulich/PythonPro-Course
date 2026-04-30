users_dict = [
    {"imie": "pawel", "wiek": 27, "plec": 1, "miejscowosc": "bialystok"},
    {"imie": "malwina", "wiek": 22, "plec": 0, "miejscowosc": "bielsko-biala"},
    {"imie": "ezekiel", "wiek": 30, "plec": 1, "miejscowosc": "wroclaw"}
]

sorted_users = sorted(users_dict, key = lambda user: len(user["miejscowosc"]))
for u in sorted_users:
    print(u["imie"], u["wiek"])

def users_order(user: dict):
    return user["miejscowosc"]

# porównuje kolejne literki przez ord
sorted_users = sorted(users_dict, key = users_order, reverse=True)
sorted_users = sorted(users_dict, key = lambda user: user["miejscowosc"], reverse=True)
for u in sorted_users:
    print(u["imie"], u["wiek"])