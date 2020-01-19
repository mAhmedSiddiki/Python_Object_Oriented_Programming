#Object Oriented Programming(OOP)
#Encapsulation  -->  1) Pablic
#                    2) Protected
#                    3) Private

class Vehical:
    def __init__(self,name):
        self.name = name #public
        self._name = name #protected - single undersccore
        self.__name = name #private - double undersccore


a = Vehical("Solimoddin")
print("public: ",a.name)
print("Protected: ",a._name)
print("Private: ",a._Vehical__name)