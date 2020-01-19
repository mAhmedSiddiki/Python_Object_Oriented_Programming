#Object Oriented Programming(OOP)
#Abstraction --> Class
#                Method
from abc import ABC,abstractmethod


class Father(ABC):
    @abstractmethod
    def do_study(self):
        pass


class Son(Father):
    def __init__(self,name):
        self.name = name

    def show(self):
        print(self.name)

    def do_study(self):
       print("Yes. Father")

a = Son("Solimuddin")
a.show()
a.do_study()