klucze = "imie, miejscowosc, wiek".split(",")
wartosci = ("radek", "zywiec", 17)
dict_comp = {k:v for k, v in zip(klucze, wartosci)} # jednoczesna iteracja - klucze i wart.
print(dict_comp)

klucze = "imie, miejscowosc, wiek, miejscowosc urodzenia".split(",")
wartosci = ("radek", "zywiec", 17, None)
dict_comp = {k:v for k, v in zip(klucze, wartosci) if v} # jednoczesna iteracja - klucze i wart.
print(dict_comp)

klucze = "imie, miejscowosc, wiek, miejscowosc urodzenia, medale olimpijskie".split(",")
wartosci = ("radek", "zywiec", 17, None, 0)
dict_comp = {k:v for k, v in zip(klucze, wartosci) if v is not None} # jednoczesna iteracja - klucze i wart.
print(dict_comp)

# potęgi liczb od 1 do 10, kluczem liczba, wartością potęga
pow_dict = {i: i * i for i in range(1, 11)} # dla zbioru (bez "i:") kolejność nieistotna
print(pow_dict)

pow_dict = {i: i * i for i in range(1, 11) if i * i >= 50} # dla zbioru (bez "i:") kolejność nieistotna
print(pow_dict)

pow_dict = {i: x for i in range(1, 11) if (x := i * i) >= 50} # ma poprawiać czytelność
print(pow_dict)