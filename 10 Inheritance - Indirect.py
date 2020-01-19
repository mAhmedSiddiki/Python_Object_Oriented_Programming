#Inheritance - indirect

class A:
    def first(self):
        print("method - A")

class B(A):
    def second(self):
        print("method - B")

class C(B):
    def third(self):
        print("method - C")

D = C()
D.first()
D.second()
D.third()
