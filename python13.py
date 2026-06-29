#Notes
# self give access or context to use value or function of class to another variable 
# Inheritance
# Encapsulation
# Polymorphism

class car:
    def __init__(self,brand,model): # __init__ = constructor
        self.__brand = brand
        self.model = model
    def fullName(self):
        return f"{self.brand} {self.model}"

mycar = car("Toyota","fortuner")
# print(mycar.model)
# print(mycar.fullName())

new_car = car("Tata","safari")
# print(new_car.model)

#Inheritance
# Inheritance is an Object-Oriented Programming (OOP) concept in which one class (child/derived class) acquires the properties and methods of another class (parent/base class).
class electricCar(car):
    def __init__(self,brand,model,battery_size):
        super().__init__(brand,model)
        self.battery_size = battery_size
        
ev_car = electricCar("Tesla","Model S","100kWH")
# print(ev_car.model)
# print(ev_car.battery_size)
# print(ev_car.fullName())

#Encapsulation
# Encapsulation is an Object-Oriented Programming (OOP) concept that means wrapping data (variables) and methods (functions) into a single unit (class) and restricting direct access to some data.
# print(ev_car.brand) #object has no attribute 'brand'
# print(mycar.brand) #object has no attribute 'brand'

#Polymorphism [eg:gender]
#Polymorphism is the ability of a single interface, method, or function to perform different actions depending on the object or data it is used with.

class studentMale:
    def __init__(self,name,id):
        self.name = name
        self.id = id
    def showDetail(self):
        return f"{self.name} {self.id}"
    def gender(self):
        return "Male"
    
s1 = studentMale("VIGI",43)
# print(s1.gender())

class studentFemale(studentMale):
    def __init__(self, name, id):
        super().__init__(name, id)
    def gender(self):
        return "Female"
    @staticmethod
    def general_descp():
        return "ALl the students of two genders are good in studey"

s2 = studentFemale("Siri",42)
# print(s2.gender())

#Static method
print(studentFemale.general_descp()) 