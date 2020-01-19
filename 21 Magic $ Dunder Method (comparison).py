#                               Object Oriented Programming(OOP)
#                                Magic Method || Dunder Method
#                                   Comparison magic methods
#                                     ==, !=, <, >, <=, >=


class Vehicle:
    def __init__(self,name,price):
        self.name = name
        self.price = price

    def __eq__(self, other, oth2):
        print(self.name == other.name == oth2.name, self.price == other.price == oth2.price)


a = Vehicle("Toyota",200)
b = Vehicle("Toyota",200)
c = Vehicle("Toyota",300)

a.__eq__(b,c,)

