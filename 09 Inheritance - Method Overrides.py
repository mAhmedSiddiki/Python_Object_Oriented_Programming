#Inheritance - Method Overrides

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


C = B("Selim","Red")
C.nameshow()
C.info()