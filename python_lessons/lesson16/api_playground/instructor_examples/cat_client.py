import requests as rqts

ENDPOINT = "http://127.0.0.1:8000/cats"

def get_cats():
    rqts.get(ENDPOINT)
    
def create_cat(id: int, name: str, age: int, color: str):
    data = {"id": id,
            "name": name,
            "age": age,
            "color": color}
    rqts.post(ENDPOINT, json = data)
    
def patch_cat(id: int, 
              name: str = None, 
              age: int = None, 
              color: str = None):
    if {name, age, color} == {None}:
        raise ValueError("przynajmniej jeden parametr musi być przekazany!")
    data = {"name": name,
            "age": age,
            "color": color}
    
    rqts.patch(ENDPOINT + f"/{id}",
                    json = {k:v
                        for k, v in data.items()
                        if v is not None})
    
print(get_cats().json())