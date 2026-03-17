class Employee:
    company_name = 'Apple'
    def __init__(self, name):
        self.name = name

    def showDetails(self):
        print(f'the name of the employee is {self.name} {self.company_name}')

emp1 = Employee("Harry")
emp1.company_name = "Apple harry"
emp2 = Employee("Ashish")
Employee.showDetails(emp1)
Employee.showDetails(emp2)

# if instance is present otherwise class variable