#Object Oriented Programming(OOP)
#Variable -->1)Class Variable
#            2)Instance Variable

class Vehicle:
    hey = "Hello World"     #class vaiable
    def __init__(self,name,wheel,driver):
        self.v_name = name       #instance variable
        self.v_wheel = wheel     #instance variable
        self.v_driver = driver    #instance variable

    def show(self):#self = car,truck
        print(self.v_name,self.v_driver,self.hey)

car = Vehicle("Toyota",4,"Solimoddiin")
car.show()
print(Vehicle.hey)

truck = Vehicle("Tata",8,"Kolimoddin")
truck.show()