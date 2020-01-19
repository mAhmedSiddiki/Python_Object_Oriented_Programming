#Object Oriented Programming(OOP)
#Polimorphism -> many forms
#Polimorphism with class method

class Man:
    def leg(self):
        print("has 2 legs")

class Animal:
    def leg(self):
        print("has 4 legs")

a = Man()
b = Animal()

for obj in (a,b):
    obj.leg()