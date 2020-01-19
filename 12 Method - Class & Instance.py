#Object Oriented Programming(OOP)
#Method -->  1)Class Method
#            2)Instance Method
#            3)Static Method

class Vehicle:
    hey = "Hello World"
    def __init__(self,name,wheel,driver):  #instance method
        self.v_name = name
        self.v_wheel = wheel
        self.v_driver = driver

    def show(self):    #instance method
        print(self.v_name,self.v_driver,self.hey)

    @classmethod #decorator
    def seen(cls):
        print(cls.hey)


car = Vehicle("Toyota",4,"Solimoddiin")
car.show()
car.seen()

truck = Vehicle("Tata",8,"Kolimoddin")
truck.show()