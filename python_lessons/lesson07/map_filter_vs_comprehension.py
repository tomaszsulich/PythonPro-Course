lst = [1, 2, 3, 4, 5, 6]

listed_map = list(map(lambda x: x * x, lst))

pow_comp = [i * i for i in lst]

def filter_cond(x):
    return x > 3

print(lst)
filtered_list_func = filter(filter_cond, lst) # warunek skomplikowany, wiersz - kilka kolumn
filtered_list_lamb = filter(lambda x: x > 3, lst)

# tworzę listę liczb większych od 3
filtered_list_comp = [i for i in lst if i > 3]

print(list(filtered_list_func))