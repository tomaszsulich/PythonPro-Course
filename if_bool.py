# if czy_zakonczono_pomyslnie is True (is, bo kwestia optymalizacji Pythona)
# is porównuje czy to te same zmienne, nie ta sama wartość (NIE, TO NIE JEST TO SAMO 
# WBREW POZOROM), is porównuje tożsamość obiektu
# dla True/False można używać is, bo są singletonami
# do porównania wartości zwykle używa się ==
# is porównuje czy to są te same obiekty
# funkcja id zwraca identyfikator zmiennej, komórkę w pamięci (dwie różne zmienne, 
# identyfikatory te same, bardzo często kwestia optymalizacji pamięci Pythona)


czy_zakonczono_pomyslnie = True

if czy_zakonczono_pomyslnie:
    print("Gratulacje! Ten element programu działa!")
else:
    print("Próbuj dalej.")
    
print(id(czy_zakonczono_pomyslnie))

a = 10 # wartości != 0 są traktowane jako True w warunkach if
b = True

print(id(a))
print(id(b))
print(a is b)