def power2(x):
    return x * x

lst = [1, 2, 3, 4, 5, 6]
pow_comp = [i * i for i in lst]

print(map(power2, lst))

for i in map(power2, lst):
    print(i) # musimy stworzyć funkcję! + list comprehension szybsze
    
# lambda = funkcja niema, "w miejscu", musi przyjmować jakiś argument, na szybko tworzymy 
# funkcję potrzebną tylko w tym jednym miejscu, nigdzie nie zapisywana
for i in map(lambda x: x * x, lst):
    print(i)