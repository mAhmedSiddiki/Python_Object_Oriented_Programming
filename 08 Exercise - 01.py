#Exercise - 01

class Student:
    versity = "Daffodil International University"
    def __init__(self,name ,subject,section):
        self.name = name
        self.subject = subject
        self.section = section

    def show(self):
        print("\nName: ",self.name,"\nSubject: ",self.subject,"\nSection: ",self.section,"\nVersity: ",self.versity)


first = Student(input("Enter your name: "),input("Subject: "),input("Sectiton: "))
second = Student(input("Enter your name: "),input("Subject: "),input("Sectiton: "))
third = Student(input("Enter your name: "),input("Subject: "),input("Sectiton: "))

first.show()
second.show()
third.show()
