#Object Oriented Programming(oop)
#Constractor
#attribute - > 1)propertise
              #2)method

class Vehicle:
    def __init__(self,name,wheel,driver):
        self.v_name = name
        self.v_wheel = wheel
        self.v_driver = driver

    def show(self):#self = car,truck
        print(self.v_name,self.v_driver)

car = Vehicle("Toyota",4,"Solimoddiin")
car.show()
#Vehicle.show(car)

truck = Vehicle("Tata",8,"Kolimoddin")
truck.show()