# Zadanie wykonane przy okazji dwóch poprzednich.

# W SQLAlchemy każdy rekord jest obiektem klasy Zadanie, dlatego możemy odwoływać się
# do kolumn przez atrybuty (zadanie.id, zadanie.opis) zamiast przez indeksy.

# Sqlite3 zwraca rekord jako krotkę, dlatego dostęp do danych odbywa się przez indeksy
# odpowiadające kolejności kolumn w zapytaniu SELECT.