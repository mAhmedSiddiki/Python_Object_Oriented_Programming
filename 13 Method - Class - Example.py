#Object Oriented Programming(OOP)
#Method --> Class Method

class Ractangle:
    def __init__(self,width,height):
        self.width = width
        self.height = height

    def cal_area(self):
        print(self.width * self.height)

    @classmethod
    def square(cls,no):
        return cls(no,no)


a = Ractangle(4,5)
a.cal_area()
a = Ractangle.square(3)
a.cal_area()

b = Ractangle.square(4)
b.cal_area()