#Inheritance - super()

class A:
    def first(self):
        print("method - A")

class B:
    def second(self):
        print("method - B")

class C(A,B):
    def third(self):
        print("method - C")
        super().first()
        super().second()

D = C()
D.third()