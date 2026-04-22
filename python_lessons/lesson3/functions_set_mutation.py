scores = [20, 20, 10, 1, 2]
scores = set(scores) # ZBIÓR TEŻ JEST MUTOWALNY, CZYLI MOŻLIWY DO ZMIANY "W MIEJSCU"    

def create_user(name, age, scores):
    scores.add(99)
    name = name + "200"
    
name = "pawel"
print(scores)
create_user(name, 20, scores)
print(scores)