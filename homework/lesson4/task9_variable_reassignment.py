x = 10
print(f"Początkowa wartość x ma identyfikator: {id(x)}.")
x = x + 1
print(f"Po zmianie x mamy id(x) = {id(x)}.")

# Tak, identyfikator x się zmienił, ponieważ zmienna ta została nadpisana.
# Oznacza to, że po wykonaniu operacji x = x + 1 w pamięci został stworzony nowy obiekt
# (liczba 11), a zmienna x zaczęła wskazywać na ten nowy obiekt. Poprzedni obiekt (10)
# pozostaje bez zmian.

# ROZWIĄZANIE OD PAWŁA
# x = 10
# print(f"id(x) = {id(x)}")
# x += 1  # x = x + 1
# print(f"id(x) = {id(x)}")
# # id sie zmienilo, bo x jest niemutowalny, czyli nie da się go zmienić.
# # aby dokonać zmian, python musi stworzyć w pamięci nową liczbę, która jest wynikiem dzialania