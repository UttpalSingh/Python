#Notes
# self give access or context to use value or function of class to another variable 
# Inheritance

class car:
    def __init__(self,brand,model): # __init__ = constructor
        self.brand = brand
        self.model = model
    def fullName(self):
        return f"{self.brand} {self.model}"

mycar = car("Toyota","fortuner")
# print(mycar.brand)
# print(mycar.model)
# print(mycar.fullName())

new_car = car("Tata","safari")
# print(new_car.brand)

#Inheritance
# Inheritance is an Object-Oriented Programming (OOP) concept in which one class (child/derived class) acquires the properties and methods of another class (parent/base class).
class electricCar(car):
    def __init__(self,brand,model,battery_size):
        super().__init__(brand,model)
        self.battery_size = battery_size
        
ev_car = electricCar("Tesla","Model S","100kWH")
print(ev_car.brand)
print(ev_car.model)
print(ev_car.battery_size)
print(ev_car.fullName())

#Encapsulation
# Encapsulation is an Object-Oriented Programming (OOP) concept that means wrapping data (variables) and methods (functions) into a single unit (class) and restricting direct access to some data.

