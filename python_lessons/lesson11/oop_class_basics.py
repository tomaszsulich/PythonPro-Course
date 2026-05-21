name = 'Pawel'
wiek = 20

def przywitaj_sie(imie, wiek):
    print(f"hej, jestem {imie}, mam {wiek} lat.")
    
przywitaj_sie(name, wiek)


class User:
    
    def __init__(self, name: str, age: int, status: int = 10):
        self.__status = status
        self.name = name
        self.age = age
        self.__money = 0
        
    def say_hello(self):
        print(f"hej, jestem {self.name}, mam {self.age} lat.")
        
    def add_money(self, new_money: float, from_user: str):
        self.__money += new_money
        print(f"{from_user} dał mi {new_money} zł, teraz mam {self.__money} zł.")
        
class Car:
    carglobal = "x"
    
    def __init__(self, color, brand, x = 0, y = 0):
        self.carglobal = None
        self.color = color
        self.brand = brand
        self.pos = (x, y)
        
    def drive_to(self, x, y):
        self.pos = (x, y)
        print("przemieszczam sie do pozycji", self.pos)
        
    def __repr__(self):
        return f"<Car {self.color} {self.brand} at {self.pos}>"

user0 = User('Pawel', 20)

car0 = Car("black", "audi")
car1 = Car("red", "ferrari")