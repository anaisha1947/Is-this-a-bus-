#Write a Python program to implement Inheritance by creating 
# a Parent Class Vehicle with a constructor that has details like name, 
# maximum speed, and mileage. Then, create a Child Class Bus that 
# inherits Class Vehicle. 
# Finally, showcase Inheritance to display the details of the 
# Vehicle Bus named - School Volvo.
class Vehicles:
    def __init__(self,name,max_speed,mileage):
        self.name = name
        self.max_speed = max_speed 
        self.mileage = mileage
    def display(self):
        print(self.name)
        print(self.max_speed)
        print(self.mileage)
class Bus(Vehicles):
    def __init__(self, color, name, max_speed, mileage):
        self.color = color
        Vehicles.__init__(self, name, max_speed, mileage)
school_bus = Bus("Yellow", "School Volvo", 100, 20)
school_bus.display()