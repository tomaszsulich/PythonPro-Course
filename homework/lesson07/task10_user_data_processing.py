uzytkownicy = [
    {"imie": "Jan", "wiek": 30, "aktywny": True},
    {"imie": "Anna", "wiek": 17, "aktywny": False},
    {"imie": "Piotr", "wiek": 25, "aktywny": True}
]

aktywni_pelnoletni = [u["imie"].upper() for u in uzytkownicy if u["aktywny"] \
                      and u["wiek"] >= 18]
print(aktywni_pelnoletni)

# WERSJA Z MAP I FILTER
# aktywni_pelnoletni = list(
#     map(lambda u: u["imie"].upper(),
#         filter(lambda u: u["aktywny"] and u["wiek"] >= 18, uzytkownicy))
# )