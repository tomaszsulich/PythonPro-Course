# listy służą do tego, aby mieć historię i dzięki temu łatwiej ją zanalizować
# w listach, indeksach liczymy od 0, LISTY ELASTYCZNE ALE LICZY SIĘ W NICH KOLEJNOŚĆ
pomiary_temp = [10, 12, 13, 15, 16, 15, 12]
pomiary_temp = [10, 12, 13, 15, 16, 15, 12, 10.2, "zimno"]
pomiary_temp.append("cieplo") # dodaje coś na koniec listy
pomiary_temp.insert(2, "wstawione") # na wybrane miejsce wstawia daną wartość

# listy możemy łączyć np. sumowaniem
lista_laczona = [10, 20, 30] + [40, 50, 60]
pomiary_temp[5:18] # od której wartości zaczynamy to ją też uwzględnia, ostatniej już nie

# lista od 0 do 23
pomiary_temp = list(range(24))
print("pelna_lista", pomiary_temp)
print("sublista", pomiary_temp[5:18])

# możemy ściągnąć pewien element, od razu go usuwając 


# listy są niejako domyślne przy zbiorach danych, możemy w nich dowolnie podmienić wartość
list = [1, 2, 3]
print(list)
list[0] = [10, 20, 30]
print(list)

# alternatywny sposób tworzenia listy, ale zdecydowanie mniej zalecany
lista1 = ()
