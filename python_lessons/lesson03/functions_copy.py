scores = [20, 20, 10, 1, 2]

# KOPIOWANIE LIST - OCHRONA ORYGINAŁU, KONTROLA MUTOWALNOŚCI
def create_user(name, age, scores = None):
    if scores is None:
        scores = []
    scores_c = scores.copy()
    scores_c.append(99)
    print(scores_c)
    
name = "pawel"
print(scores)
create_user(name, 20, scores)
print(scores)