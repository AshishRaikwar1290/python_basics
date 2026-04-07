class Employee:
    name = "Harry"
    def __len__(self):
        i = 0
        for c in self.name:
            i = i + 1
        return i
    
    def __str__(self):
        return f"The name of the employee is {self.name} str"
    
    def __repr__(self):
        pass

    def __call__(self, *args, **kwds):
        print("Hey I am good")


e = Employee()
print(e)
print(len(e)) 