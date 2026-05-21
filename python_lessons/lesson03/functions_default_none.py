# JAKBYŚMY CHCIELI DAĆ PUSTĄ LISTĘ W ARGUMENTACH
# NIE DAJEMY PUSTEJ LISTY W PARAMETRZE DOMYŚLNYM, TWORZYMY JĄ W ŚRODKU FUNKCJI
def create_user(name, age, scores = None):
    if scores is None:
        scores = []
    scores.append(99)
    name = name + "200"
    print(scores)
    
name = "pawel"
create_user(name, 20)