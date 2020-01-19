#Object Oriented Programming(OOP)
#Polimorphism -> Example
#1. Polymorphism with Inheritance
#2. Polymorphism with Function and Objects
#3. Polymorphic functions

#1. Polymorphism with Inheritance
class A:
    def __init__(self,name,color):
        self.name = name
        self.color = color

    def nameshow(self):
        print(self.name)

    def info(self):
        print("good")


class B(A):
    def info(self):
        print("BAD")


C = A("Selim","Red")
C.nameshow()
C.info()

D = B("Salam","Red")
D.nameshow()
D.info()



#2. Polymorphism with Function and Objects
class Man:
    def leg(self):
        print("has 2 legs")

class Animal:
    def leg(self):
        print("has 4 legs")

def func(obj):
    obj.leg()

a = Man()
b = Animal()
func(a)
func(b)



#3. Polymorphic functions
def add(x,y,z=0):
    print(x+y+z)

add(1,2,3)
add(1,2)


#4. Builtin Polymorphism
len("codinglaugh")
len([1,2,3,4,5])
len((1,1,1,1,1))