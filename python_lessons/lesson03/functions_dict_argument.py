# FUNKCJA MAŁO UNIWERSALNA, MUSIMY GDZIEŚ TAM SŁOWNIK STWORZYĆ
user_dict = {"name": "tomek", "age": 22}

def create_user(user):
    print(user["name"], user["age"])
    
create_user(user_dict) # Z LISTAMI I ZE SŁOWNIKAMI TRZEBA UWAŻAĆ