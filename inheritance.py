class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id
    
    def show_details(self):
        print(f'The name of Employee: {self.id} is {self.name}')

class Programmer(Employee):
    def showLanguage(self):
        print("default lang is python")
        

e1 = Employee("Rohan Das", 400)
e1.show_details()

e2 = Programmer("Harry", 4001)
e2.show_details()
e2.showLanguage()
