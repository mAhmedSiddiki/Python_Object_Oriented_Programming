#                               Object Oriented Programming(OOP)
#                                Magic Method || Dunder Method
#                                         repr and str
#                               __repr__()      &      __str__()


class Vehicle:
    def __init__(self,name,price):
        self.name = name
        self.price = price

    def __repr__(self):
        return self.name,self.price

    def __str__(self):
        return self.name


a = Vehicle("Toyota",200)
b = Vehicle("Toyota",200)
c = Vehicle("Toyota",300)

print(a.__str__())
print(a.__repr__())


