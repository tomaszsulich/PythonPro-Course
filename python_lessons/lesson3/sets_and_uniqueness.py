set_ = {1, 2, 3, 4, 5, 6} 
set_ = {1, 2, 393, 4, 2892, 5, 6, 7, 8}

print(set_) # zbiór nie trzyma kolejności, ale jest szybki i wykorzystywany, sortuje
# tam, gdzie zależy nam na sprawdzeniu, czy jakiś zbiór informacji zawiera el. sprawdzany
print(7 in set_)

print(list(set([1, 2, 3, 4, 5, 6, 1, 2, 3, 5]))) # pozbywa się duplikatów