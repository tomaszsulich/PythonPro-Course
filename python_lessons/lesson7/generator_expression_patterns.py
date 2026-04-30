tpl_comp = (i for i in range(5))
print(tpl_comp, type(tpl_comp)) # schemat działania, danych bardzo dużo, prawie nic nie waży
# lazy wczytywanie przez generatory

for i in tpl_comp:
    print(i)