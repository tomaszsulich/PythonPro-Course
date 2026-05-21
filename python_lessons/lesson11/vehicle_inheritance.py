class Vehicle:
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
        return f"<Vehicle {self.color} {self.brand} at {self.pos}>"
    

class Car(Vehicle):
    def __repr__(self):
        return f"<Car {self.color} {self.brand} at {self.pos}>"
    

class Car(Vehicle):
    def __repr__(self):
        return super().__repr__().replace("Vehicle", "Car", 1)
car0 = Car("black", "audi")
print(car0)