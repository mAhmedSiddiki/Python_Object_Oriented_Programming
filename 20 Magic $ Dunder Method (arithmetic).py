#                               Object Oriented Programming(OOP)
#                                Magic Method || Dunder Method
#                                 Normal Arithmetic Operators
#                                 +, -, *, /, %, &, ||, ^, **


class Vehicle:
    def __init__(self,name,price):
        self.name = name
        self.price = price

    def __add__(self, hey1, hey2):
        print("Total Price: ", self.price + hey1.price + hey2.price)

    def __sub__(self, other):
        print(self.price - other.price)

    def total_price(self,obj2):
        print(self.price+obj2.price)


a = Vehicle("Toyota",200)
b = Vehicle("Tata",300)
c = Vehicle("Tata",300)

Vehicle.__add__(a,b,c)
a.__add__(b,c)
#Vehicle(a+b+c)

b.__sub__(a)

c = "Marjuk"
d = "Ahmed"
print(c.__add__(d))

a.total_price(b)