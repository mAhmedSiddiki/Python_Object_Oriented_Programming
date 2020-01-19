#Multiple inheritance
#is a relationship
#Car is a vehicle
#Truck is a vehicle

class Vehicle():
    def __init__(self,name):
        self.vehicle_name = name

    def cname(self):
        print(self.vehicle_name)

class Driver():
    def __init__(self,name):
        self.driver_name = name

    def dname(self):
        print(self.driver_name)

class Car(Vehicle, Driver):
    def __init__(self,cname,dname):
        Vehicle.__init__(self,cname)
        Driver.__init__(self,dname)

    def drive(self):
        print(self.vehicle_name," is drive")

class Truck(Vehicle):
    def wheel(self):
        print(self.vehicle_name,"--> has 8 wheel")


a = Car("Toyota","Rahim Islam")
a.cname() #parent class - Vehicle
a.drive() #child class
a.dname() #parent class - Driver

b = Truck("tata")
b.cname()
b.wheel()