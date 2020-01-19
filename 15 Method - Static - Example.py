#Object Oriented Programming(OOP)
#Method -->  Static Method
from datetime import date

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    @classmethod
    def birthdate(cls,name,year):
        return cls(name,date.today().year - year)

    @staticmethod
    def adult(age):
        return age>18


a = Person("Solimoddin",21)
b = Person.birthdate("Kolimoddin",1996)
print(a.name," : ",a.age," : adult -> ",Person.adult(a.age))
print(b.name," : ",b.age," : adult -> ",Person.adult(12))