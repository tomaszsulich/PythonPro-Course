str_ = "kotek"
lst_ = list(str_) # lista ma więcej funkcji niż string

print(id(str_), id(str_[:-1])) # jakkolwiek modyfikujemy stringa, to się zmienia adres
# str_[1] = "x" - do listy bez problemu byśmy przypisali

lst_2 = lst_[:] # podstring, ale ponieważ to jest to samo, Python nie tworzy new object

lst_ = list(str_)
lst_[1] = "x"
print(lst_)

str_ = str(lst_)
print(str_) # lista jest przyjemna i elastyczna, na wiele pozwala