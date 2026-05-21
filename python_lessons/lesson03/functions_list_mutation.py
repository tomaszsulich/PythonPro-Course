scores = [20, 20, 10, 1, 2]

def create_user(name, age, scores):
    scores.append(99)
    name = name + "200"
    ...
    
name = "pawel"
print(scores)
create_user(name, 20, scores)
print(scores)

