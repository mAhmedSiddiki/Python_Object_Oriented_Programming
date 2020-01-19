#Object Oriented Programming(oop)
#Class
#attribute - > 1)propertise

'''              #2)method
str = "codinglaugh"
str.__len__()
len(str)
'''

class Vehicle:
    def set_value(self,name,wheel,driver):
        self.v_name = name
        self.v_wheel = wheel
        self.v_driver = driver

    def show(self):#self = car,truck
        print(self.v_name,self.v_driver)

car = Vehicle()
car.set_value("Toyota",4,"Solimoddiin")
car.show()
#Vehicle.show(car)

truck = Vehicle()
truck.set_value("Taka",8,"Kolimoddin")
truck.show()